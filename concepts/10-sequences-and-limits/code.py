"""Sequences and Limits -- concept 10 of the math-foundations learning map.

Two numerical demonstrations:
  (1) For x_n = 1/n, find the smallest N such that |x_n - 0| < eps for
      eps in {1e-2, 1e-3, 1e-4}. This is the epsilon-N definition in action.
  (2) For x_n = sum_{k=1}^n 1/k^2 (Basel sequence, limit pi^2/6), verify
      the Cauchy criterion numerically: |x_m - x_n| shrinks as m, n grow.

Stdlib only (math module).
"""

import math


def smallest_N_for_one_over_n(eps: float, n_max: int = 1000) -> int:
    """Smallest N in {1, ..., n_max} with 1/n < eps for all n >= N."""
    for N in range(1, n_max + 1):
        if 1.0 / N < eps:
            return N
    raise ValueError(f"no N <= {n_max} works for eps={eps}")


def basel_partial(n: int) -> float:
    """Partial sum sum_{k=1}^n 1/k^2."""
    s = 0.0
    for k in range(1, n + 1):
        s += 1.0 / (k * k)
    return s


def demo_one_over_n() -> None:
    print("Demo 1: x_n = 1/n -> 0 (epsilon-N witnesses)")
    print("-" * 60)
    print(f"{'epsilon':>12} {'smallest N':>14} {'1/N':>16} {'theory: ceil(1/eps)+1':>26}")
    for eps in (1e-2, 1e-3, 1e-4):
        N = smallest_N_for_one_over_n(eps, n_max=200000)
        theory = math.floor(1.0 / eps) + 1
        print(f"{eps:>12.6f} {N:>14d} {1.0/N:>16.8f} {theory:>26d}")
    print()


def demo_cauchy_basel() -> None:
    print("Demo 2: Cauchy criterion for x_n = sum_{k=1}^n 1/k^2")
    print("-" * 60)
    limit = math.pi ** 2 / 6.0
    print(f"True limit pi^2/6 = {limit:.10f}")
    print()
    print(f"{'n':>8} {'x_n':>16} {'|x_n - pi^2/6|':>20}")
    for n in (10, 100, 1000, 10000):
        xn = basel_partial(n)
        print(f"{n:>8d} {xn:>16.10f} {abs(xn - limit):>20.3e}")
    print()
    print("Pairwise differences |x_m - x_n| (Cauchy check):")
    print(f"{'m':>8} {'n':>8} {'|x_m - x_n|':>20}")
    pairs = [(100, 50), (1000, 500), (5000, 2500), (10000, 5000)]
    for m, n in pairs:
        diff = abs(basel_partial(m) - basel_partial(n))
        print(f"{m:>8d} {n:>8d} {diff:>20.3e}")
    print()
    print("As m, n -> infinity with m >= n, |x_m - x_n| -> 0, confirming")
    print("the Cauchy property numerically. Completeness of R then guarantees")
    print("the sequence has a limit -- which is pi^2/6.")


def main() -> None:
    print("Sequences and Limits (concept 10)")
    print("=" * 60)
    demo_one_over_n()
    demo_cauchy_basel()


if __name__ == "__main__":
    main()
