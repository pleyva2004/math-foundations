"""Expectation — concept 25-expectation of the math-foundations learning map.

Stdlib-only demonstration:
  1. E[X] for X ~ Binomial(10, 0.4): analytic (= np = 4.0) vs empirical.
  2. Linearity: E[X + Y] = E[X] + E[Y] (independent X, Y).
  3. Jensen's inequality (phi = x^2): E[X^2] >= (E[X])^2.
"""

import math
import random


def binomial_pmf(n, p, k):
    return math.comb(n, k) * (p ** k) * ((1 - p) ** (n - k))


def expectation_discrete(values, pmf):
    return sum(v * pmf(v) for v in values)


def sample_binomial(n, p):
    return sum(1 for _ in range(n) if random.random() < p)


def empirical_mean(samples):
    return sum(samples) / len(samples)


def main():
    random.seed(0)
    print("Expectation (concept 25-expectation)")
    print("=" * 60)

    # --- 1. Binomial(10, 0.4) ---
    n, p = 10, 0.4
    analytic = expectation_discrete(range(n + 1), lambda k: binomial_pmf(n, p, k))
    N = 10000
    samples = [sample_binomial(n, p) for _ in range(N)]
    empirical = empirical_mean(samples)
    print(f"\n[1] X ~ Binomial({n}, {p})")
    print(f"    E[X] = sum_k k * P(X=k)         = {analytic:.6f}")
    print(f"    E[X] = np                       = {n * p:.6f}")
    print(f"    Empirical mean ({N} samples)    = {empirical:.6f}")
    assert math.isclose(analytic, n * p, abs_tol=1e-9)
    assert abs(empirical - analytic) < 0.1

    # --- 2. Linearity: E[X+Y] = E[X] + E[Y] ---
    # X ~ Binomial(10, 0.4), Y ~ Bernoulli(0.7), independent
    pY = 0.7
    x_samples = [sample_binomial(n, p) for _ in range(N)]
    y_samples = [1 if random.random() < pY else 0 for _ in range(N)]
    EX = empirical_mean(x_samples)
    EY = empirical_mean(y_samples)
    EXY = empirical_mean([a + b for a, b in zip(x_samples, y_samples)])
    print("\n[2] Linearity (independent X ~ Bin(10,0.4), Y ~ Bern(0.7))")
    print(f"    E[X]               = {EX:.6f}")
    print(f"    E[Y]               = {EY:.6f}")
    print(f"    E[X] + E[Y]        = {EX + EY:.6f}")
    print(f"    E[X + Y] empirical = {EXY:.6f}")
    print(f"    |diff|             = {abs((EX + EY) - EXY):.2e}")
    assert math.isclose(EX + EY, EXY, abs_tol=1e-9)  # exact: same samples

    # --- 3. Jensen: phi(x) = x^2 is convex, so E[X^2] >= (E[X])^2 ---
    EX2 = empirical_mean([x * x for x in x_samples])
    print("\n[3] Jensen, phi(x) = x^2 (convex)")
    print(f"    E[X^2]            = {EX2:.6f}")
    print(f"    (E[X])^2          = {EX ** 2:.6f}")
    print(f"    Gap = Var(X)      = {EX2 - EX ** 2:.6f}  (>= 0)")
    assert EX2 >= EX ** 2 - 1e-9

    print("\nAll checks passed.")


if __name__ == "__main__":
    main()
