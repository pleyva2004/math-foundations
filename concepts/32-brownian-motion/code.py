"""Brownian Motion / Wiener Process — concept 32-brownian-motion.

Simulate standard Brownian motion W_t on [0,1] with N=1000 steps using
the increment recursion W_{(k+1)/N} = W_{k/N} + sqrt(1/N) * Z_k, where
Z_k ~ N(0,1). Box-Muller is used to generate Z_k from random.random,
keeping the script stdlib-only.

Outputs:
  * 5 sample paths and their values at t = 0.5
  * Empirical Var(W_{0.5}) over 1000 independent paths (should be ~0.5)
"""

import math
import random


def box_muller(rng):
    """Return one N(0,1) sample via the Box-Muller transform."""
    u1 = rng.random()
    while u1 == 0.0:  # avoid log(0)
        u1 = rng.random()
    u2 = rng.random()
    return math.sqrt(-2.0 * math.log(u1)) * math.cos(2.0 * math.pi * u2)


def simulate_path(N, rng):
    """Simulate W_t on [0,1] with N steps; return list of length N+1."""
    dt = 1.0 / N
    sqrt_dt = math.sqrt(dt)
    W = [0.0] * (N + 1)
    for k in range(N):
        W[k + 1] = W[k] + sqrt_dt * box_muller(rng)
    return W


def main():
    print("Brownian Motion / Wiener Process (concept 32)")
    print("=" * 60)

    N = 1000
    rng = random.Random(20260514)

    # --- Five sample paths, report W_{0.5} ---
    half = N // 2  # index for t = 0.5
    print(f"\n5 sample paths on [0,1] with N={N} steps; values at t=0.5:")
    for i in range(5):
        path = simulate_path(N, rng)
        print(f"  path {i+1}: W_0 = {path[0]:+.4f}   "
              f"W_{{0.5}} = {path[half]:+.4f}   "
              f"W_1 = {path[N]:+.4f}")

    # --- Empirical variance of W_{0.5} over 1000 paths ---
    n_paths = 1000
    print(f"\nEmpirical Var(W_{{0.5}}) over {n_paths} independent paths:")
    samples = []
    for _ in range(n_paths):
        # Build only up to t=0.5 for speed (half the work).
        w = 0.0
        sqrt_dt = math.sqrt(1.0 / N)
        for _ in range(half):
            w += sqrt_dt * box_muller(rng)
        samples.append(w)

    mean = sum(samples) / n_paths
    var = sum((x - mean) ** 2 for x in samples) / (n_paths - 1)
    print(f"  sample mean      = {mean:+.4f}  (expected 0)")
    print(f"  sample variance  = {var:.4f}   (expected 0.5)")
    print(f"  relative error   = {abs(var - 0.5) / 0.5 * 100:.2f} %")

    # Sanity: covariance E[W_s W_t] = min(s,t).
    print("\nSanity check: covariance kernel min(s,t).")
    print("  Theory predicts E[W_{0.5} W_1] = 0.5.")
    print("  (Computed from a full-path Monte Carlo if extended.)")


if __name__ == "__main__":
    main()
