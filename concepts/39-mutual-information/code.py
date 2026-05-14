"""Mutual Information — concept 39 of the math-foundations learning map.

Demonstrates I(X; Y) for two correlated Bernoulli variables (a binary
symmetric channel). Compares the empirical plug-in estimator against the
closed-form value, and verifies two limiting cases:
  (1) two independent fair coins  -> I(X; Y) = 0
  (2) Y = X (perfect dependence)  -> I(X; Y) = H(X) = 1 bit

Stdlib only. CPU-runnable in well under 5 s.
"""

import math
import random
from collections import Counter


def entropy_bits(probs):
    """Shannon entropy in bits of an iterable of probabilities."""
    return -sum(p * math.log2(p) for p in probs if p > 0.0)


def mutual_information_bits(samples):
    """Plug-in MI estimator in bits from an iterable of (x, y) samples."""
    n = 0
    joint = Counter()
    px = Counter()
    py = Counter()
    for x, y in samples:
        joint[(x, y)] += 1
        px[x] += 1
        py[y] += 1
        n += 1
    mi = 0.0
    for (x, y), nxy in joint.items():
        pxy = nxy / n
        denom = (px[x] / n) * (py[y] / n)
        mi += pxy * math.log2(pxy / denom)
    return mi


def binary_entropy(eps):
    """H_2(eps) in bits."""
    return entropy_bits([eps, 1.0 - eps])


def bsc_samples(n, eps, rng):
    """Sample n pairs (X, Y) where X ~ Bern(1/2) and Y = X XOR Bern(eps)."""
    out = []
    for _ in range(n):
        x = rng.randrange(2)
        flip = 1 if rng.random() < eps else 0
        out.append((x, x ^ flip))
    return out


def main():
    rng = random.Random(0)
    n = 200_000
    print("Mutual Information (concept 39)")
    print("=" * 60)

    print("\n(1) Independent fair coins -- expect I = 0")
    indep = [(rng.randrange(2), rng.randrange(2)) for _ in range(n)]
    print(f"    empirical I(X;Y) = {mutual_information_bits(indep):+.5f} bits")

    print("\n(2) Y = X exactly -- expect I = H(X) = 1 bit")
    eq = [(b, b) for b in (rng.randrange(2) for _ in range(n))]
    print(f"    empirical I(X;Y) = {mutual_information_bits(eq):+.5f} bits")

    print("\n(3) Binary symmetric channel: I = 1 - H_2(eps)")
    print(f"    {'eps':>6}  {'analytic':>10}  {'empirical':>10}  {'|diff|':>8}")
    for eps in [0.0, 0.05, 0.10, 0.25, 0.40, 0.50, 0.75, 0.90, 1.0]:
        analytic = 1.0 - binary_entropy(eps) if 0.0 < eps < 1.0 else 1.0
        emp = mutual_information_bits(bsc_samples(n, eps, rng))
        print(f"    {eps:>6.2f}  {analytic:>10.5f}  {emp:>10.5f}  {abs(analytic - emp):>8.4f}")


if __name__ == "__main__":
    main()
