"""KL Divergence — concept 38-kl-divergence of the math-foundations learning map.

Demonstrates:
  1. Discrete KL on several (p, q) pairs.
  2. Non-negativity (Gibbs).
  3. Asymmetry: D_KL(p||q) != D_KL(q||p).
  4. Triangle inequality fails.
  5. Closed-form Gaussian KL vs Monte Carlo agreement.

Stdlib only. CPU, <5 s.
"""

from math import log, pi, sqrt
import random


def kl_discrete(p, q):
    """KL(p || q) for finite distributions (lists summing to 1)."""
    total = 0.0
    for pi_, qi in zip(p, q):
        if pi_ == 0.0:
            continue
        if qi == 0.0:
            return float("inf")
        total += pi_ * log(pi_ / qi)
    return total


def kl_gaussian_closed(mu1, s1, mu2, s2):
    """Closed-form D_KL(N(mu1,s1^2) || N(mu2,s2^2))."""
    v1, v2 = s1 * s1, s2 * s2
    return 0.5 * (v1 / v2 - 1.0 - log(v1 / v2) + (mu1 - mu2) ** 2 / v2)


def log_normal_pdf(x, mu, s):
    return -0.5 * log(2.0 * pi * s * s) - (x - mu) ** 2 / (2.0 * s * s)


def kl_gaussian_mc(mu1, s1, mu2, s2, n=200_000, seed=0):
    """Monte-Carlo estimate of D_KL via samples from p = N(mu1, s1^2)."""
    rng = random.Random(seed)
    acc = 0.0
    for _ in range(n):
        x = rng.gauss(mu1, s1)
        acc += log_normal_pdf(x, mu1, s1) - log_normal_pdf(x, mu2, s2)
    return acc / n


def main():
    print("KL Divergence (concept 38-kl-divergence)")
    print("=" * 60)

    # 1. Discrete examples.
    pairs = [
        ([0.5, 0.5], [0.5, 0.5]),       # identical
        ([0.9, 0.1], [0.5, 0.5]),       # peaked vs uniform
        ([0.1, 0.9], [0.5, 0.5]),       # mirror
        ([0.25, 0.25, 0.25, 0.25], [0.7, 0.1, 0.1, 0.1]),
    ]
    print("\n[1] Discrete KL values (nats):")
    for p, q in pairs:
        print(f"  D_KL(p||q)={kl_discrete(p, q):.4f}  p={p}  q={q}")

    # 2. Non-negativity.
    print("\n[2] Non-negativity (Gibbs): all KLs >= 0?",
          all(kl_discrete(p, q) >= -1e-12 for p, q in pairs))

    # 3. Asymmetry.
    p, q = [0.1, 0.9], [0.5, 0.5]
    print(f"\n[3] Asymmetry: D_KL(p||q)={kl_discrete(p,q):.4f}  "
          f"D_KL(q||p)={kl_discrete(q,p):.4f}")

    # 4. Triangle inequality fails.
    p = [0.99, 0.01]
    qd = [0.50, 0.50]
    r = [0.01, 0.99]
    lhs = kl_discrete(p, r)
    rhs = kl_discrete(p, qd) + kl_discrete(qd, r)
    print(f"\n[4] Triangle inequality? D_KL(p||r)={lhs:.4f}  "
          f"D_KL(p||q)+D_KL(q||r)={rhs:.4f}  violated={lhs > rhs}")

    # 5. Gaussian closed form vs Monte Carlo.
    mu1, s1, mu2, s2 = 0.3, 1.2, -0.5, 2.0
    closed = kl_gaussian_closed(mu1, s1, mu2, s2)
    mc = kl_gaussian_mc(mu1, s1, mu2, s2, n=200_000, seed=42)
    print(f"\n[5] Gaussian KL  closed={closed:.4f}  MC={mc:.4f}  "
          f"|diff|={abs(closed - mc):.4f}")


if __name__ == "__main__":
    main()
