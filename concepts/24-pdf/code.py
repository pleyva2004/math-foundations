"""Probability Density Functions — concept 24-pdf.

Demonstrates:
  (1) Trapezoidal numerical integration of the standard Gaussian PDF over
      [-5, 5] confirms total mass approx 1.
  (2) Inverse-CDF (inverse-transform) sampling: U ~ Uniform(0,1) becomes
      X = -ln(1-U)/lambda ~ Exp(lambda). Empirical histogram bin counts
      are compared to lambda * exp(-lambda * x) at bin centers.

Stdlib only: math, random.
"""

import math
import random


def gauss_pdf(x):
    return math.exp(-0.5 * x * x) / math.sqrt(2.0 * math.pi)


def trapz(f, a, b, n):
    """Composite trapezoidal rule on [a, b] with n subintervals."""
    h = (b - a) / n
    total = 0.5 * (f(a) + f(b))
    for k in range(1, n):
        total += f(a + k * h)
    return h * total


def exp_pdf(x, lam):
    return lam * math.exp(-lam * x) if x >= 0 else 0.0


def main():
    print("Probability Density Functions (concept 24-pdf)")
    print("=" * 60)

    # (1) Gaussian normalization via trapezoidal rule.
    integral = trapz(gauss_pdf, -5.0, 5.0, 10_000)
    print(f"[1] trapz integral of phi(x) over [-5, 5] = {integral:.8f}")
    print(f"    error vs 1.0                          = {abs(1.0 - integral):.2e}")
    print(f"    (mass outside [-5,5] is ~ 5.7e-7, negligible)")

    # (2) Inverse-CDF sampling: F(x) = 1 - exp(-lam*x) for x>=0,
    # so F^{-1}(u) = -ln(1-u)/lam. Equivalently -ln(u)/lam.
    random.seed(42)
    lam = 1.5
    N = 200_000
    samples = [-math.log(1.0 - random.random()) / lam for _ in range(N)]

    # Histogram on [0, 5] with bin width 0.25.
    bin_w = 0.25
    n_bins = 20  # covers [0, 5]
    counts = [0] * n_bins
    for s in samples:
        if 0.0 <= s < n_bins * bin_w:
            counts[int(s / bin_w)] += 1

    print(f"\n[2] Inverse-CDF sampling of Exp(lambda={lam}), N={N}")
    print(f"    bin_center  empirical_density   pdf(center)   abs_diff")
    max_abs = 0.0
    for k in range(n_bins):
        center = (k + 0.5) * bin_w
        empirical = counts[k] / (N * bin_w)
        analytic = exp_pdf(center, lam)
        diff = abs(empirical - analytic)
        max_abs = max(max_abs, diff)
        if k < 8 or k == n_bins - 1:
            print(f"    {center:6.3f}      {empirical:10.5f}        "
                  f"{analytic:8.5f}     {diff:.4f}")
    print(f"    max |empirical - pdf| across all bins = {max_abs:.4f}")
    print("    (matches well; deviations are O(1/sqrt(N*bin_w)))")


if __name__ == "__main__":
    main()
