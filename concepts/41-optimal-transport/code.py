"""Optimal Transport (Wasserstein) -- concept 41-optimal-transport.

Demo: compute W_1 between two empirical 1D distributions via the closed-form
quantile-difference formula (sort both samples, average absolute differences).

Verifies W_1(N(0,1), N(m,1)) ~ |m| for several m, and contrasts with KL
divergence -- which diverges as the two supports separate while W_1 stays
finite and grows linearly in |m|.

Stdlib only. Runs in <2s on CPU.
"""
import math
import random


def w1_empirical_1d(xs, ys):
    """W_1 between two equal-size samples via monotone (sorted) coupling."""
    assert len(xs) == len(ys), "equal sample sizes required"
    xs_s = sorted(xs)
    ys_s = sorted(ys)
    return sum(abs(a - b) for a, b in zip(xs_s, ys_s)) / len(xs_s)


def kl_gaussians(m1, s1, m2, s2):
    """Closed-form KL( N(m1, s1^2) || N(m2, s2^2) )."""
    return math.log(s2 / s1) + (s1 ** 2 + (m1 - m2) ** 2) / (2 * s2 ** 2) - 0.5


def kl_disjoint_uniforms(a_lo, a_hi, b_lo, b_hi):
    """KL between two uniform distributions on disjoint intervals = +inf."""
    return math.inf if (a_hi <= b_lo or b_hi <= a_lo) else 0.0


def w1_disjoint_uniforms(a_lo, a_hi, b_lo, b_hi, n=4000):
    """W_1 between Unif[a_lo,a_hi] and Unif[b_lo,b_hi] via Monte Carlo."""
    rng = random.Random(0)
    xs = [rng.uniform(a_lo, a_hi) for _ in range(n)]
    ys = [rng.uniform(b_lo, b_hi) for _ in range(n)]
    return w1_empirical_1d(xs, ys)


def gaussian_sample(mean, std, n, seed):
    rng = random.Random(seed)
    return [rng.gauss(mean, std) for _ in range(n)]


def main():
    print("Optimal Transport (Wasserstein) -- concept 41")
    print("=" * 60)

    n = 8000
    print(f"\nW_1(N(0,1), N(m,1)) for several m  (n={n}, sorted-coupling estimate)")
    print(f"  {'m':>6} {'W_1 estimate':>14} {'true |m|':>10}")
    base = gaussian_sample(0.0, 1.0, n, seed=1)
    for m in [0.0, 0.25, 0.5, 1.0, 2.0, 5.0]:
        shifted = gaussian_sample(m, 1.0, n, seed=2)
        w = w1_empirical_1d(base, shifted)
        print(f"  {m:>6.2f} {w:>14.4f} {abs(m):>10.2f}")

    print("\nW_1 vs KL as supports separate (Unif[0,1] vs Unif[s, s+1])")
    print(f"  {'shift s':>9} {'W_1':>10} {'KL':>14}")
    for s in [0.0, 0.5, 1.0, 2.0, 5.0]:
        w = w1_disjoint_uniforms(0.0, 1.0, s, s + 1.0)
        k = kl_disjoint_uniforms(0.0, 1.0, s, s + 1.0)
        k_str = "+inf" if math.isinf(k) else f"{k:.4f}"
        print(f"  {s:>9.2f} {w:>10.4f} {k_str:>14}")

    print("\nKL(N(0,1) || N(m,1)) for the same m (closed form: m^2/2)")
    print(f"  {'m':>6} {'KL':>10}")
    for m in [0.0, 0.25, 0.5, 1.0, 2.0, 5.0]:
        print(f"  {m:>6.2f} {kl_gaussians(0, 1, m, 1):>10.4f}")

    print("\nObservation:")
    print("  W_1 grows like |m| (linear, geometry-aware).")
    print("  KL grows like m^2/2 (Gaussians) and is +inf for disjoint supports.")


if __name__ == "__main__":
    main()
