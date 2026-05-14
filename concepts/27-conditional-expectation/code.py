"""Conditional Expectation — concept 27 of the math-foundations learning map.

Empirical demo of E[X | Y] and the tower property using two fair dice.

  Y = first die, W = second die, X = Y + W.
  Analytic:  E[X | Y = y] = y + 3.5      and    E[X] = 7.

Stdlib only. Runs in well under 30 s.
"""

import random
from collections import defaultdict


def simulate(n_trials: int = 200_000, seed: int = 0):
    rng = random.Random(seed)
    sum_by_y: dict[int, float] = defaultdict(float)
    count_by_y: dict[int, int] = defaultdict(int)
    total_x = 0.0
    for _ in range(n_trials):
        y = rng.randint(1, 6)
        w = rng.randint(1, 6)
        x = y + w
        sum_by_y[y] += x
        count_by_y[y] += 1
        total_x += x
    cond_means = {y: sum_by_y[y] / count_by_y[y] for y in sorted(count_by_y)}
    marginal_p_y = {y: count_by_y[y] / n_trials for y in sorted(count_by_y)}
    return cond_means, marginal_p_y, total_x / n_trials


def main():
    print("Conditional Expectation (concept 27)")
    print("=" * 60)
    print("Setup: Y = first die, W = second die, X = Y + W.")
    print("Analytic claim: E[X | Y = y] = y + 3.5.\n")

    n = 200_000
    cond_means, p_y, ex_hat = simulate(n_trials=n)

    print(f"Empirical conditional means (n = {n:,}):")
    print(f"  {'y':>3} {'E[X|Y=y] (sim)':>16} {'y + 3.5':>10} {'abs err':>10}")
    for y, m in cond_means.items():
        analytic = y + 3.5
        print(f"  {y:>3} {m:>16.4f} {analytic:>10.4f} {abs(m - analytic):>10.4f}")

    # Tower property: E[E[X|Y]] = sum_y E[X|Y=y] * P(Y=y) should equal E[X].
    tower = sum(cond_means[y] * p_y[y] for y in cond_means)
    print()
    print("Tower property check:")
    print(f"  E[E[X|Y]] (from cond. means + P(Y)) = {tower:.4f}")
    print(f"  E[X]      (direct sample mean)      = {ex_hat:.4f}")
    print(f"  analytic  E[X]                      = 7.0000")
    print(f"  |tower - E[X]_hat|                  = {abs(tower - ex_hat):.6f}")

    max_err = max(abs(cond_means[y] - (y + 3.5)) for y in cond_means)
    assert max_err < 0.1, f"conditional means deviate too much: {max_err}"
    assert abs(tower - ex_hat) < 1e-9, "tower identity should hold exactly on the sample"
    print("\nAll checks passed.")


if __name__ == "__main__":
    main()
