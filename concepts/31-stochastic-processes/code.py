"""Stochastic Processes — concept 31 of the math-foundations learning map.

Simulates the simple symmetric random walk S_n = X_1 + ... + X_n with
iid X_i in {-1, +1} (prob 1/2 each). Verifies E[S_n] = 0 and Var(S_n) = n.

Stdlib only.
"""

import random


def random_walk(n_steps, rng):
    """Return the full sample path [S_0, S_1, ..., S_n] of a SRW."""
    path = [0]
    s = 0
    for _ in range(n_steps):
        step = 1 if rng.random() < 0.5 else -1
        s += step
        path.append(s)
    return path


def main():
    print("Stochastic Processes (concept 31)")
    print("=" * 60)

    rng = random.Random(0)
    n_steps = 100

    # ---- Five sample paths --------------------------------------------------
    print(f"\nFive sample paths of the simple random walk (n = {n_steps}):")
    for k in range(5):
        path = random_walk(n_steps, rng)
        head = ", ".join(str(x) for x in path[:8])
        print(f"  path {k+1}: [{head}, ...]  S_{n_steps} = {path[-1]}")

    # ---- Empirical mean / variance over many walks --------------------------
    n_walks = 10_000
    total = 0
    sq_total = 0
    rng2 = random.Random(42)
    for _ in range(n_walks):
        s = 0
        for _ in range(n_steps):
            s += 1 if rng2.random() < 0.5 else -1
        total += s
        sq_total += s * s

    mean_emp = total / n_walks
    var_emp = sq_total / n_walks - mean_emp * mean_emp

    print(f"\nOver {n_walks} independent walks of length n = {n_steps}:")
    print(f"  empirical  E[S_n] = {mean_emp:+.4f}   (theory: 0)")
    print(f"  empirical Var(S_n) = {var_emp:.4f}   (theory: {n_steps})")
    print(f"  empirical SD(S_n)  = {var_emp ** 0.5:.4f}   "
          f"(theory: {n_steps ** 0.5:.4f})")

    # ---- Sanity bounds ------------------------------------------------------
    assert abs(mean_emp) < 1.0, "mean should be near 0"
    assert abs(var_emp - n_steps) < 0.15 * n_steps, "variance should be near n"
    print("\nAll empirical estimates match the theory within tolerance.")


if __name__ == "__main__":
    main()
