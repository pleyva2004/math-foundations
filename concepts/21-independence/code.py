"""Independence — concept 21 of the math-foundations learning map.

Two numerical demos (stdlib only):

  (1) Two independent fair coin flips: empirical frequencies converge to
      P(A and B) = P(A) P(B) = 0.25.

  (2) Canonical pairwise-but-not-mutually-independent triple on
      Omega = {1, 2, 3, 4} with uniform measure:
          A = {1, 2},  B = {1, 3},  C = {1, 4}.
      Every pair is independent; the triple is not.
"""

import random
from itertools import product


def empirical_two_coins(n_trials: int = 200_000, seed: int = 0) -> None:
    rng = random.Random(seed)
    nA = nB = nAB = 0
    for _ in range(n_trials):
        x1 = rng.random() < 0.5  # A = {X1 = H}
        x2 = rng.random() < 0.5  # B = {X2 = H}
        nA += x1
        nB += x2
        nAB += x1 and x2
    pA, pB, pAB = nA / n_trials, nB / n_trials, nAB / n_trials
    print("Demo 1: two independent fair coin flips")
    print(f"  P(A)        = {pA:.4f}  (theory 0.5000)")
    print(f"  P(B)        = {pB:.4f}  (theory 0.5000)")
    print(f"  P(A and B)  = {pAB:.4f}  (theory 0.2500)")
    print(f"  P(A) P(B)   = {pA * pB:.4f}")
    print(f"  |diff|      = {abs(pAB - pA * pB):.4f}  (->0 as n->inf)")
    print()


def prob(event: set, omega: set) -> float:
    """Uniform measure on a finite sample space."""
    return len(event) / len(omega)


def pairwise_not_mutual() -> None:
    omega = {1, 2, 3, 4}
    A = {1, 2}
    B = {1, 3}
    C = {1, 4}

    pA, pB, pC = prob(A, omega), prob(B, omega), prob(C, omega)
    pAB = prob(A & B, omega)
    pAC = prob(A & C, omega)
    pBC = prob(B & C, omega)
    pABC = prob(A & B & C, omega)

    print("Demo 2: pairwise-but-not-mutually-independent triple")
    print(f"  Omega = {sorted(omega)}, uniform")
    print(f"  A = {sorted(A)}, B = {sorted(B)}, C = {sorted(C)}")
    print(f"  P(A) = P(B) = P(C) = {pA}")
    print()
    print(f"  P(A and B) = {pAB}   vs  P(A) P(B) = {pA * pB}    "
          f"{'independent' if pAB == pA * pB else 'NOT independent'}")
    print(f"  P(A and C) = {pAC}   vs  P(A) P(C) = {pA * pC}    "
          f"{'independent' if pAC == pA * pC else 'NOT independent'}")
    print(f"  P(B and C) = {pBC}   vs  P(B) P(C) = {pB * pC}    "
          f"{'independent' if pBC == pB * pC else 'NOT independent'}")
    print()
    print(f"  P(A and B and C) = {pABC}")
    print(f"  P(A) P(B) P(C)   = {pA * pB * pC}")
    print(f"  --> {'MUTUALLY independent' if pABC == pA * pB * pC else 'pairwise only; NOT mutually independent'}")


def main() -> None:
    print("Independence (concept 21)")
    print("=" * 60)
    empirical_two_coins()
    pairwise_not_mutual()


if __name__ == "__main__":
    main()
