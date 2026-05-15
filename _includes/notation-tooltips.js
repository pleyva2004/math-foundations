/*
 * notation-tooltips.js
 *
 * Walks the DOM after page load and wraps each known mathematical notation
 * in a <span class="notation-tip" data-meaning="..."> so the matching CSS
 * can render a hover bubble.
 *
 * Data source: /math-foundations/notation.json (157 entries with fields
 * { id, symbol, latex, category, read_as, plain_english, ... }).
 *
 * No jQuery, no build step, no CDN. Pure DOM APIs.
 */
(function () {
  "use strict";

  // ---------------------------------------------------------------------------
  // Configuration
  // ---------------------------------------------------------------------------

  // Try a couple of likely URLs so the script works both on the repo's Pages
  // root (`/math-foundations/notation.json`) and on a custom domain (`/notation.json`).
  var CANDIDATE_URLS = [
    "/math-foundations/notation.json",
    "notation.json",
    "/notation.json"
  ];

  // Cap how many text-node wraps we perform per page to stay inside the
  // <50 ms budget on a 100-symbol page.
  var MAX_TEXT_WRAPS = 2000;

  // Elements whose text content we should NOT scan for symbol replacements
  // (would break code highlighting or already-tooltipped content).
  var SKIP_TAGS = {
    SCRIPT: 1, STYLE: 1, NOSCRIPT: 1, TEXTAREA: 1, INPUT: 1,
    PRE: 1, CODE: 1, KBD: 1, SAMP: 1, VAR: 1
  };

  // ---------------------------------------------------------------------------
  // Lookup tables (built once, after fetch)
  // ---------------------------------------------------------------------------

  var byLatex = Object.create(null);   // "\\forall"   -> meaning string
  var bySymbol = Object.create(null);  // "∀"          -> meaning string
  var byReadAs = Object.create(null);  // "for all"    -> meaning string

  // Pre-built regex matching any single notation symbol, used for text-node scanning.
  var symbolRegex = null;

  function buildLookups(entries) {
    var symbols = [];
    for (var i = 0; i < entries.length; i++) {
      var e = entries[i];
      if (!e || !e.plain_english) continue;
      var meaning = formatMeaning(e);

      if (e.latex) {
        // Store both with and without the leading backslash so we can match
        // either variant easily.
        byLatex[e.latex] = meaning;
        byLatex[stripLeadingBackslash(e.latex)] = meaning;
      }
      if (e.symbol) {
        bySymbol[e.symbol] = meaning;
        symbols.push(e.symbol);
      }
      if (e.read_as) {
        byReadAs[e.read_as.toLowerCase()] = meaning;
      }
    }

    // Build symbol regex: longest first to ensure greedy multi-char matches
    // (e.g. "∃!" before "∃").
    symbols.sort(function (a, b) { return b.length - a.length; });
    var escaped = symbols.map(escapeRegExp);
    if (escaped.length > 0) {
      symbolRegex = new RegExp("(" + escaped.join("|") + ")", "g");
    }
  }

  function formatMeaning(entry) {
    // Combine "read_as" + "plain_english" into the bubble text.
    var read = entry.read_as ? '"' + entry.read_as + '" — ' : "";
    return read + entry.plain_english;
  }

  function stripLeadingBackslash(s) {
    return s.charAt(0) === "\\" ? s.slice(1) : s;
  }

  function escapeRegExp(s) {
    return s.replace(/[.*+?^${}()|[\]\\]/g, "\\$&");
  }

  // ---------------------------------------------------------------------------
  // Fetch loop
  // ---------------------------------------------------------------------------

  function fetchNotation() {
    // Try candidate URLs in order; resolve with the first one that works.
    var i = 0;
    function tryNext() {
      if (i >= CANDIDATE_URLS.length) {
        return Promise.reject(new Error("notation.json not reachable"));
      }
      var url = CANDIDATE_URLS[i++];
      return fetch(url, { credentials: "same-origin" })
        .then(function (r) {
          if (!r.ok) throw new Error("HTTP " + r.status);
          return r.json();
        })
        .catch(function () { return tryNext(); });
    }
    return tryNext();
  }

  // ---------------------------------------------------------------------------
  // DOM traversal: wrap math elements
  // ---------------------------------------------------------------------------

  function wrapMathElements(root) {
    // GitHub renders display & inline math as <math> (MathML) or as
    // <span class="MathJax">/.MathJax_Display containers.
    // We also inspect <code> elements that look like raw LaTeX fragments
    // (e.g. inline "`\forall`" markdown the author wrote without rendering).
    var selectors = [
      "math",
      "span.MathJax",
      "span.MathJax_Display",
      "[data-latex]",
      "code"
    ];
    var nodes = root.querySelectorAll(selectors.join(","));
    for (var i = 0; i < nodes.length; i++) {
      var node = nodes[i];
      if (node.closest(".notation-tip")) continue;

      // Prefer an explicit data-latex attribute when GitHub provides it.
      var raw = (node.getAttribute && node.getAttribute("data-latex")) ||
                node.textContent || "";
      raw = raw.trim();
      if (!raw) continue;

      var meaning = matchMeaning(raw);
      if (meaning) {
        wrapElement(node, meaning);
      }
    }
  }

  function matchMeaning(raw) {
    if (byLatex[raw]) return byLatex[raw];
    if (bySymbol[raw]) return bySymbol[raw];
    if (byReadAs[raw.toLowerCase()]) return byReadAs[raw.toLowerCase()];

    // Try stripping leading "\" — GitHub's data-latex sometimes drops/keeps it.
    var noSlash = stripLeadingBackslash(raw);
    if (byLatex[noSlash]) return byLatex[noSlash];

    return null;
  }

  function wrapElement(el, meaning) {
    // If already wrapped, just update meaning.
    if (el.classList && el.classList.contains("notation-tip")) {
      el.setAttribute("data-meaning", meaning);
      return;
    }
    var wrapper = document.createElement("span");
    wrapper.className = "notation-tip";
    wrapper.setAttribute("data-meaning", meaning);
    wrapper.setAttribute("tabindex", "0"); // keyboard-accessible

    var parent = el.parentNode;
    if (!parent) return;
    parent.insertBefore(wrapper, el);
    wrapper.appendChild(el);
  }

  // ---------------------------------------------------------------------------
  // DOM traversal: scan plain-text nodes for symbol characters
  // ---------------------------------------------------------------------------

  function wrapSymbolsInText(root) {
    if (!symbolRegex) return;

    // Collect candidate text nodes via a TreeWalker so we don't mutate the
    // DOM mid-iteration.
    var walker = document.createTreeWalker(
      root,
      NodeFilter.SHOW_TEXT,
      {
        acceptNode: function (node) {
          if (!node.nodeValue || !node.nodeValue.trim()) return NodeFilter.FILTER_REJECT;
          var p = node.parentNode;
          while (p && p !== root) {
            if (SKIP_TAGS[p.nodeName]) return NodeFilter.FILTER_REJECT;
            if (p.classList && p.classList.contains("notation-tip")) {
              return NodeFilter.FILTER_REJECT;
            }
            p = p.parentNode;
          }
          // Quick early-out: only bother if the text contains a non-ASCII char.
          // Notation symbols are Unicode (∀, ∃, ∈, ℝ, etc.).
          if (!/[^\x00-\x7F]/.test(node.nodeValue)) return NodeFilter.FILTER_REJECT;
          return NodeFilter.FILTER_ACCEPT;
        }
      }
    );

    var batch = [];
    var node;
    while ((node = walker.nextNode())) {
      batch.push(node);
      if (batch.length >= MAX_TEXT_WRAPS) break;
    }

    for (var i = 0; i < batch.length; i++) {
      replaceSymbolsInTextNode(batch[i]);
    }
  }

  function replaceSymbolsInTextNode(textNode) {
    var text = textNode.nodeValue;
    symbolRegex.lastIndex = 0;
    if (!symbolRegex.test(text)) return;
    symbolRegex.lastIndex = 0;

    var frag = document.createDocumentFragment();
    var lastIdx = 0;
    var m;
    while ((m = symbolRegex.exec(text)) !== null) {
      var sym = m[1];
      var start = m.index;
      if (start > lastIdx) {
        frag.appendChild(document.createTextNode(text.slice(lastIdx, start)));
      }
      var meaning = bySymbol[sym];
      if (meaning) {
        var span = document.createElement("span");
        span.className = "notation-tip";
        span.setAttribute("data-meaning", meaning);
        span.setAttribute("tabindex", "0");
        span.textContent = sym;
        frag.appendChild(span);
      } else {
        frag.appendChild(document.createTextNode(sym));
      }
      lastIdx = start + sym.length;
    }
    if (lastIdx < text.length) {
      frag.appendChild(document.createTextNode(text.slice(lastIdx)));
    }
    textNode.parentNode.replaceChild(frag, textNode);
  }

  // ---------------------------------------------------------------------------
  // Boot
  // ---------------------------------------------------------------------------

  function boot() {
    var t0 = (performance && performance.now) ? performance.now() : Date.now();
    fetchNotation()
      .then(function (entries) {
        if (!Array.isArray(entries)) return;
        buildLookups(entries);

        var scope = document.querySelector("main") || document.body;
        if (!scope) return;

        wrapMathElements(scope);
        wrapSymbolsInText(scope);

        var t1 = (performance && performance.now) ? performance.now() : Date.now();
        if (window.console && console.debug) {
          console.debug("[notation-tooltips] ready in " + (t1 - t0).toFixed(1) + " ms");
        }
      })
      .catch(function (err) {
        if (window.console && console.warn) {
          console.warn("[notation-tooltips] disabled:", err && err.message);
        }
      });
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", boot);
  } else {
    boot();
  }
})();
