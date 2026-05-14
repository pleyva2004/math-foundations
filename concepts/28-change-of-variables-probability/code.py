"""Change of Variables (Probability) -- concept 28.

Verify: if X ~ Uniform[0,1] and Y = -log X, then Y ~ Exp(1).
Stdlib only (random, math). CPU-runnable in <1 s.
"""

import math
import random


def empirical_pdf(samples, lo, hi, n_bins):
    """Histogram-based PDF estimate over [lo, hi]."""
    width = (hi - lo) / n_bins
    counts = [0] * n_bins
    for s in samples:
        if lo <= s < hi:
            counts[int((s - lo) / width)] += 1
    n = len(samples)
    centers = [lo + (k + 0.5) * width for k in range(n_bins)]
    densities = [c / (n * width) for c in counts]
    return centers, densities


def main():
    random.seed(20260514)
    n = 10_000
    xs = [random.random() for _ in range(n)]      # X ~ Uniform[0,1]
    ys = [-math.log(x) for x in xs if x > 0.0]    # Y = g(X) = -log X

    print("Change of Variables: X ~ U[0,1], Y = -log X  ==> Y ~ Exp(1)")
    print("=" * 64)
    print(f"N samples  = {len(ys)}")
    print(f"mean(Y)    = {sum(ys)/len(ys):.4f}   (analytic Exp(1) mean = 1.0000)")
    var = sum((y - 1.0) ** 2 for y in ys) / len(ys)
    print(f"var(Y)     = {var:.4f}   (analytic Exp(1) var  = 1.0000)")

    # --- Empirical PDF vs analytic Exp(1) PDF f_Y(y) = e^{-y} ---
    print("\nEmpirical f_Y(y) vs analytic e^{-y}:")
    print(f"  {'y':>6} | {'empirical':>10} | {'analytic':>10} | {'abs.err':>8}")
    centers, dens = empirical_pdf(ys, lo=0.0, hi=6.0, n_bins=60)
    max_err = 0.0
    for y, d in zip(centers, dens):
        analytic = math.exp(-y)
        err = abs(d - analytic)
        max_err = max(max_err, err)
        if abs(y - round(y * 2) / 2) < 1e-9 and y <= 4.5:  # print at y = 0.5, 1.0, ...
            print(f"  {y:>6.2f} | {d:>10.4f} | {analytic:>10.4f} | {err:>8.4f}")
    print(f"  max histogram error on [0,6]: {max_err:.4f}")

    # --- Pointwise verification of CoV formula ---
    # f_Y(y) = f_X(g^{-1}(y)) / |g'(g^{-1}(y))| with g(x) = -log x, |g'(x)| = 1/x.
    # f_X = 1 on (0,1); g^{-1}(y) = e^{-y}; so f_Y(y) = 1 / (1/e^{-y}) = e^{-y}.
    print("\nFormula check: f_Y(y) = f_X(g^{-1}(y)) / |g'(g^{-1}(y))|")
    print(f"  {'y':>6} | {'f_X(x)':>8} | {'|g_prime|':>10} | {'predicted':>10} | {'e^{-y}':>8}")
    f_X = 1.0  # uniform on (0,1)
    for y in [0.1, 0.5, 1.0, 2.0, 3.0]:
        x = math.exp(-y)            # g^{-1}(y)
        g_prime_abs = 1.0 / x       # |g'(x)| = 1/x
        predicted = f_X / g_prime_abs
        analytic = math.exp(-y)
        print(f"  {y:>6.2f} | {f_X:>8.4f} | {g_prime_abs:>10.4f} | "
              f"{predicted:>10.6f} | {analytic:>8.6f}")
        assert abs(predicted - analytic) < 1e-12, "CoV formula failed"

    print("\nOK: change-of-variables formula verified.")


if __name__ == "__main__":
    main()
