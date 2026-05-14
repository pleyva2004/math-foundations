"""Probability Distributions -- concept 23-distributions.

Demos:
  1. Binomial(5, 0.3): analytic PMF vs. empirical PMF from 10000 samples.
  2. Uniform(0,1): empirical CDF, plotted in text mode.

Stdlib only -- uses `random`, `math`.
"""

import math
import random


def binom_pmf(n, p, k):
    """Analytic Binomial(n, p) PMF at k."""
    return math.comb(n, k) * (p ** k) * ((1 - p) ** (n - k))


def sample_binomial(n, p):
    """One draw from Binomial(n, p) via n Bernoulli(p) trials."""
    return sum(1 for _ in range(n) if random.random() < p)


def demo_binomial():
    random.seed(0)
    n, p, N = 5, 0.3, 10000
    samples = [sample_binomial(n, p) for _ in range(N)]
    print(f"Binomial({n}, {p}) -- analytic vs. empirical PMF (N = {N})")
    print(f"  {'k':>3} {'analytic':>10} {'empirical':>11} {'|diff|':>8}")
    total_a, total_e = 0.0, 0.0
    for k in range(n + 1):
        analytic = binom_pmf(n, p, k)
        empirical = samples.count(k) / N
        total_a += analytic
        total_e += empirical
        print(f"  {k:>3} {analytic:>10.5f} {empirical:>11.5f} "
              f"{abs(analytic - empirical):>8.5f}")
    print(f"  sums: analytic = {total_a:.5f}, empirical = {total_e:.5f}")
    print()


def demo_uniform_cdf():
    random.seed(1)
    N = 2000
    samples = sorted(random.random() for _ in range(N))

    def ecdf(x):
        # binary search for count of samples <= x
        lo, hi = 0, N
        while lo < hi:
            mid = (lo + hi) // 2
            if samples[mid] <= x:
                lo = mid + 1
            else:
                hi = mid
        return lo / N

    print("Uniform(0,1): empirical CDF (dots) vs. true CDF F(x)=x (line)")
    width = 50
    for i in range(21):
        x = i / 20.0
        e = ecdf(x)
        line = [" "] * (width + 1)
        line[int(round(x * width))] = "|"
        line[int(round(e * width))] = "*"
        row = "".join(line)
        print(f"  x={x:0.2f}  F_emp={e:0.3f}  {row}")
    print()
    print("  Legend: | true CDF position,  * empirical CDF position.")


def main():
    print("Probability Distributions (concept 23-distributions)")
    print("=" * 60)
    demo_binomial()
    demo_uniform_cdf()


if __name__ == "__main__":
    main()
