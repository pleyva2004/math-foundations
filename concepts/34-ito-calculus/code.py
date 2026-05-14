"""Ito Calculus -- concept 34-ito-calculus of the math-foundations learning map.

Numerically computes the Ito integral I = int_0^1 W_s dW_s via the
LEFT-ENDPOINT Riemann-Stieltjes definition:

    I_N = sum_{i=0}^{N-1} W_{t_i} * (W_{t_{i+1}} - W_{t_i}),    t_i = i / N.

Theoretical results (consequences of Ito's lemma applied to f(x)=x^2,
which gives d(W_t^2) = 2 W_t dW_t + dt):

  * Path-by-path:  W_1^2 - 1 = 2 * I almost surely. Equivalently,
        I = (W_1^2 - 1) / 2.
  * The Ito correction lives in the "-1": the naive guess would be
    I = W_1^2 / 2; reality subtracts t/2 = 1/2.
  * E[I] = 0 (Ito integrals are martingales) and Var[I] = 1/2 (Ito
    isometry: Var = E int_0^1 W_s^2 ds = 1/2).
  * Mean of W_1^2 - 1 - 2*I = 0 path-by-path (Ito's lemma), so the
    empirical pathwise residual must approach 0.

Stdlib only. CPU-runnable, <30s.
"""

import math
import random


def simulate_ito_integral(N, seed):
    """Simulate one Brownian path on [0,1] with N steps and return
    (I_N, W_1) where I_N is the LEFT-endpoint Ito sum approximating
    int_0^1 W_s dW_s."""
    rng = random.Random(seed)
    dt = 1.0 / N
    sqrt_dt = math.sqrt(dt)
    W = 0.0
    I = 0.0
    for _ in range(N):
        dW = rng.gauss(0.0, 1.0) * sqrt_dt
        I += W * dW          # LEFT endpoint: W is W_{t_i} BEFORE update
        W += dW
    return I, W


def main():
    print("Ito Calculus (concept 34-ito-calculus)")
    print("=" * 60)
    print("Numerical verification of int_0^1 W_s dW_s = (W_1^2 - 1)/2")
    print()

    N = 1000          # time steps per path
    M = 1000          # number of sample paths

    # ----- Part 1: empirical mean of LEFT sums over M paths -----
    integrals = []
    pathwise_residuals = []
    for k in range(M):
        I, W1 = simulate_ito_integral(N, seed=12345 + k)
        integrals.append(I)
        # Path-by-path Ito identity: W_1^2 - 1 - 2*I should be ~0
        pathwise_residuals.append(W1 * W1 - 1.0 - 2.0 * I)

    mean_I = sum(integrals) / M
    var_I = sum((x - mean_I) ** 2 for x in integrals) / (M - 1)
    print(f"Steps per path: N = {N}")
    print(f"Sample paths:   M = {M}")
    print(f"Empirical mean of LEFT-endpoint sum I_N = {mean_I:+.4f}")
    print(f"  Theoretical:  E[int_0^1 W dW] = 0 (martingale)")
    print(f"Empirical Var(I_N) = {var_I:.4f}  (theoretical: 1/2 = 0.5000)")
    print(f"  Ito correction lives in: I = (W_1^2 - 1)/2  (the -1/2 vs naive W_1^2/2).")
    print()

    # ----- Part 2: single-path Ito identity W_1^2 - 1 = 2 * I -----
    I_single, W1_single = simulate_ito_integral(N, seed=42)
    lhs = W1_single * W1_single - 1.0
    rhs = 2.0 * I_single
    print("Single-path Ito identity check (seed=42):")
    print(f"  W_1 = {W1_single:+.4f}")
    print(f"  W_1^2 - 1   = {lhs:+.4f}  (LHS)")
    print(f"  2 * I_N     = {rhs:+.4f}  (RHS)")
    print(f"  |LHS - RHS| = {abs(lhs - rhs):.4e}  (O(1/sqrt(N)) Euler error)")
    print()

    # ----- Part 3: distribution of pathwise residuals -----
    mean_res = sum(pathwise_residuals) / M
    max_res = max(abs(r) for r in pathwise_residuals)
    print("Pathwise residuals W_1^2 - 1 - 2 I_N over all M paths:")
    print(f"  mean   = {mean_res:+.4e}    (-> 0 as N -> infinity)")
    print(f"  max|.| = {max_res:.4e}    (discretization error scale)")


if __name__ == "__main__":
    main()
