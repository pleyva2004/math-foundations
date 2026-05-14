"""Stochastic Differential Equations — concept 33-sde.

Euler-Maruyama simulation of the Ornstein-Uhlenbeck SDE
    dX_t = -theta * X_t dt + sigma dW_t,  X_0 = 2,
with theta = 1, sigma = 0.5 on [0, 5].

(1) Plots-free: prints three sample paths (subsampled).
(2) Verifies stationary variance Var(X_inf) = sigma^2 / (2*theta) = 0.125
    by averaging X_T^2 over many independent paths at large T.

Stdlib only.
"""
import math
import random


def euler_maruyama_ou(theta, sigma, x0, T, n_steps, rng):
    """One EM-discretized OU path. Returns list of length n_steps+1."""
    dt = T / n_steps
    sqrt_dt = math.sqrt(dt)
    x = x0
    path = [x]
    for _ in range(n_steps):
        z = rng.gauss(0.0, 1.0)
        x = x + (-theta * x) * dt + sigma * sqrt_dt * z
        path.append(x)
    return path


def main():
    theta, sigma, x0 = 1.0, 0.5, 2.0
    T, n_steps = 5.0, 1000
    rng = random.Random(0)

    print("Stochastic Differential Equations  (concept 33-sde)")
    print("=" * 60)
    print(f"OU SDE: dX = -{theta}*X dt + {sigma} dW, X_0={x0}, T={T}")
    print(f"Euler-Maruyama with dt = {T/n_steps:.4g}")
    print()

    # (1) Three sample paths, subsampled at 6 time points.
    print("Three sample paths (X_t at t = 0, 1, 2, 3, 4, 5):")
    sample_idx = [int(k * n_steps / 5) for k in range(6)]
    for i in range(3):
        path = euler_maruyama_ou(theta, sigma, x0, T, n_steps, rng)
        vals = [path[k] for k in sample_idx]
        print("  path {0}: ".format(i + 1)
              + "  ".join("{0:+.3f}".format(v) for v in vals))
    print()

    # (2) Empirical stationary variance: many paths to large T.
    T_long, n_long = 20.0, 4000  # 20 >> 1/theta; well into stationary regime.
    n_paths = 20000
    rng2 = random.Random(1)
    s1 = 0.0
    s2 = 0.0
    for _ in range(n_paths):
        path = euler_maruyama_ou(theta, sigma, x0, T_long, n_long, rng2)
        x_end = path[-1]
        s1 += x_end
        s2 += x_end * x_end
    mean_emp = s1 / n_paths
    var_emp = s2 / n_paths - mean_emp * mean_emp
    var_theory = sigma * sigma / (2.0 * theta)

    print(f"Stationary check at T = {T_long} over {n_paths} paths:")
    print(f"  empirical  E[X_T]    = {mean_emp:+.4f}   (theory: 0.0000)")
    print(f"  empirical  Var(X_T)  = {var_emp:.4f}")
    print(f"  theory     sigma^2/(2 theta) = {var_theory:.4f}")
    rel_err = abs(var_emp - var_theory) / var_theory
    print(f"  relative error       = {100*rel_err:.2f}%")
    assert rel_err < 0.05, "stationary variance off by >5%"
    print("\nPASS: Euler-Maruyama recovers OU stationary variance.")


if __name__ == "__main__":
    main()
