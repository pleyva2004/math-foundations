"""Probability Measures -- concept 19 of the math-foundations learning map.

Discrete probability measure on Omega = {1,...,6} with arbitrary non-negative
weights summing to 1. We verify the three Kolmogorov axioms numerically on the
full power-set sigma-algebra and check inclusion-exclusion on two events.
Stdlib only.
"""

from itertools import combinations
from fractions import Fraction


def power_set(omega):
    items = list(omega)
    return [frozenset(s) for r in range(len(items) + 1)
            for s in combinations(items, r)]


def make_measure(weights):
    if sum(weights.values()) != 1:
        raise ValueError("weights must sum to 1")
    if any(w < 0 for w in weights.values()):
        raise ValueError("weights must be non-negative")
    return lambda A: sum(weights[x] for x in A)


def verify_axioms(P, omega, sigma_algebra):
    k1 = all(P(A) >= 0 for A in sigma_algebra)
    k2 = (P(frozenset(omega)) == 1)
    k3 = True
    for A, B in combinations(sigma_algebra, 2):
        if A & B:
            continue
        if P(A | B) != P(A) + P(B):
            k3 = False
            break
    return k1, k2, k3


def main():
    omega = frozenset({1, 2, 3, 4, 5, 6})
    weights = {i: Fraction(1, 7) for i in range(1, 6)}
    weights[6] = Fraction(2, 7)  # loaded die: 6 is twice as likely as 1..5
    sigma_algebra = power_set(omega)
    P = make_measure(weights)

    print("Probability Measures -- discrete demo on Omega = {1,...,6}")
    print("=" * 60)
    print(f"|sigma-algebra| = 2^6 = {len(sigma_algebra)} events")
    print(f"weights = {{ {', '.join(f'{k}: {v}' for k, v in sorted(weights.items()))} }}")

    k1, k2, k3 = verify_axioms(P, omega, sigma_algebra)
    print("\nKolmogorov axiom check:")
    print(f"  (K1) non-negativity    : {k1}")
    print(f"  (K2) P(Omega) = 1      : {k2}")
    print(f"  (K3) finite additivity : {k3}")
    assert k1 and k2 and k3, "axioms failed"

    A = frozenset({1, 3, 5})  # odd
    B = frozenset({4, 5, 6})  # at least 4
    lhs = P(A | B)
    rhs = P(A) + P(B) - P(A & B)
    print("\nInclusion-exclusion check on A={1,3,5}, B={4,5,6}:")
    print(f"  P(A union B)               = {lhs}")
    print(f"  P(A) + P(B) - P(A inter B) = {rhs}")
    assert lhs == rhs, "inclusion-exclusion failed"
    print("  identity holds.")


if __name__ == "__main__":
    main()
