"""Shannon Entropy — concept 36-shannon-entropy of the math-foundations learning map.

H(X) = E[-log p(X)]; the average information content of a random variable.

Demonstrates:
  1. H(p) = -sum p_i log2 p_i (in bits).
  2. Bernoulli entropy curve over p in {0.05, 0.10, ..., 0.95}, text-mode plot.
  3. The bound H <= log2(n) on n=4 outcomes (uniform saturates it).
  4. Connection to Akgul: Shannon entropy of a softmax distribution over 5 tokens
     as a function of sampling temperature T.

Stdlib only. CPU-runnable, <1 s.
"""

from math import log2, exp


def H(probs):
    """Shannon entropy in bits. probs: iterable of nonnegative numbers summing to 1."""
    return -sum(p * log2(p) for p in probs if p > 0.0)


def softmax(logits, T):
    """Stable softmax with temperature T > 0."""
    scaled = [z / T for z in logits]
    m = max(scaled)
    exps = [exp(z - m) for z in scaled]
    Z = sum(exps)
    return [e / Z for e in exps]


def bar(value, vmax, width=40):
    n = int(round(width * value / vmax)) if vmax > 0 else 0
    return "#" * n


def main():
    print("Shannon Entropy (concept 36-shannon-entropy)")
    print("=" * 60)

    # ---- (1) Bernoulli entropy curve ------------------------------------
    print("\n[1] Bernoulli(p) entropy H(p) in bits — text plot")
    ps = [0.05 * k for k in range(1, 20)]  # 0.05, 0.10, ..., 0.95
    Hs = [H([p, 1 - p]) for p in ps]
    Hmax = max(Hs)
    for p, h in zip(ps, Hs):
        print(f"  p={p:0.2f}  H={h:0.4f}  |{bar(h, Hmax)}")
    pstar = ps[Hs.index(Hmax)]
    print(f"  argmax at p={pstar:0.2f} with H={Hmax:0.4f} bits (theory: p=0.5, H=1)")

    # ---- (2) Bound H <= log2(n) on n=4 ----------------------------------
    print("\n[2] Bound H(X) <= log2(n) for n=4 outcomes")
    log2n = log2(4)
    dists = {
        "uniform        ": [0.25, 0.25, 0.25, 0.25],
        "mildly skewed  ": [0.40, 0.30, 0.20, 0.10],
        "heavily skewed ": [0.85, 0.10, 0.04, 0.01],
        "deterministic  ": [1.00, 0.00, 0.00, 0.00],
    }
    for name, p in dists.items():
        h = H(p)
        ok = "OK" if h <= log2n + 1e-12 else "FAIL"
        print(f"  {name} H={h:0.4f}  <=  log2(4)={log2n:0.4f}  [{ok}]")

    # ---- (3) Akgul connection: temperature vs entropy --------------------
    print("\n[3] Akgul §3.1 Eq.1: H of softmax(logits/T) on 5 tokens vs T")
    logits = [3.0, 1.5, 0.5, 0.0, -1.0]
    print(f"  logits = {logits}")
    print(f"  T -> 0+  : H -> 0           (argmax dominates)")
    print(f"  T -> inf : H -> log2(5) = {log2(5):0.4f}  (uniform)")
    for T in [0.25, 0.5, 1.0, 2.0, 4.0, 16.0, 64.0]:
        p = softmax(logits, T)
        h = H(p)
        probs_str = "[" + ", ".join(f"{q:0.3f}" for q in p) + "]"
        print(f"  T={T:6.2f}  H={h:0.4f} bits  p={probs_str}")
    print("  H is monotone non-decreasing in T (exercise 3 in README).")


if __name__ == "__main__":
    main()
