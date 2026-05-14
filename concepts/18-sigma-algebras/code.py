"""Events and Sigma-Algebras -- concept 18-sigma-algebras.

Finite witnesses:
  (1) the power set of {1,2,3,4} is a sigma-algebra (verified by exhaustion);
  (2) sigma({A}) for A = {1,2} equals {empty, A, A^c, Omega}.
Stdlib only.
"""

from itertools import combinations


def powerset(s):
    items = list(s)
    return frozenset(
        frozenset(c) for r in range(len(items) + 1) for c in combinations(items, r)
    )


def is_sigma_algebra(F, omega):
    """Check the three sigma-algebra axioms on a finite family F over omega.
    On a finite carrier, countable union collapses to finite union."""
    F = set(F)
    omega = frozenset(omega)
    if omega not in F:
        return False, "Omega not in F"
    for A in F:
        if (omega - A) not in F:
            return False, f"complement of {set(A)} not in F"
    for A in F:
        for B in F:
            if (A | B) not in F:
                return False, f"union of {set(A)} and {set(B)} not in F"
    return True, "OK"


def generated_sigma_algebra(generators, omega):
    """Brute-force sigma(C): close under complement and pairwise union."""
    omega = frozenset(omega)
    F = {frozenset(), omega} | {frozenset(g) for g in generators}
    while True:
        new = set(F)
        for A in F:
            new.add(omega - A)
        for A in F:
            for B in F:
                new.add(A | B)
        if new == F:
            return F
        F = new


def fmt(F):
    parts = []
    for A in sorted(F, key=lambda s: (len(s), sorted(s))):
        parts.append("{" + ",".join(map(str, sorted(A))) + "}" if A else "{}")
    return "{ " + ", ".join(parts) + " }"


def main():
    omega = {1, 2, 3, 4}

    P = powerset(omega)
    print(f"|2^Omega| = {len(P)} (expected 16)")
    print(f"power-set is sigma-algebra? {is_sigma_algebra(P, omega)}")

    G = generated_sigma_algebra([{1, 2}], omega)
    print(f"sigma({{1,2}}) has {len(G)} elements: {fmt(G)}")
    print(f"is sigma-algebra? {is_sigma_algebra(G, omega)}")

    expected = {frozenset(), frozenset({1, 2}), frozenset({3, 4}), frozenset(omega)}
    print(f"matches expected 4-element sigma-algebra? {G == expected}")


if __name__ == "__main__":
    main()
