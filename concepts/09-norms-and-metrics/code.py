"""Norms and Metrics -- concept 09-norms-and-metrics.

Demonstrates:
  * l^1, l^2, l^infty norms on R^n (stdlib `math` only).
  * Numerical verification of the triangle inequality on random pairs.
  * The discrete metric, and why it cannot come from a norm
    (it violates absolute homogeneity).
"""

import math
import random


def l1(x):
    return sum(abs(c) for c in x)


def l2(x):
    return math.sqrt(sum(c * c for c in x))


def linf(x):
    return max(abs(c) for c in x) if x else 0.0


def vadd(x, y):
    return [a + b for a, b in zip(x, y)]


def discrete(x, y):
    return 0 if x == y else 1


def check_triangle(norm, trials=200, dim=5, seed=0):
    rng = random.Random(seed)
    worst_slack = math.inf
    for _ in range(trials):
        x = [rng.uniform(-10, 10) for _ in range(dim)]
        y = [rng.uniform(-10, 10) for _ in range(dim)]
        lhs = norm(vadd(x, y))
        rhs = norm(x) + norm(y)
        slack = rhs - lhs
        if slack < worst_slack:
            worst_slack = slack
        assert lhs <= rhs + 1e-9, "triangle inequality violated"
    return worst_slack


def main():
    print("Norms and Metrics (concept 09)")
    print("=" * 60)

    v = [3.0, -4.0, 12.0]
    print(f"v = {v}")
    print(f"  ||v||_1   = {l1(v)}   (expected 19)")
    print(f"  ||v||_2   = {l2(v)}   (expected 13)")
    print(f"  ||v||_inf = {linf(v)} (expected 12)")
    print(f"  inequality ||v||_inf <= ||v||_2 <= ||v||_1 holds: "
          f"{linf(v) <= l2(v) <= l1(v)}")
    print()

    print("Triangle inequality, 200 random pairs in R^5:")
    for name, norm in [("l1", l1), ("l2", l2), ("linf", linf)]:
        slack = check_triangle(norm)
        print(f"  {name:5s}: passed; smallest slack = {slack:.4f}")
    print()

    print("Discrete metric on R^n:")
    x = [1.0, 2.0, 3.0]
    y = [1.0, 2.0, 3.0]
    z = [0.0, 0.0, 0.0]
    print(f"  d(x,x) = {discrete(tuple(x), tuple(y))}  (expect 0)")
    print(f"  d(x,z) = {discrete(tuple(x), tuple(z))}  (expect 1)")
    print()

    print("Can the discrete metric come from a norm?")
    print("  If d(x,y) = ||x-y||, homogeneity forces ||2x|| = 2 ||x||.")
    a = [1.0, 0.0, 0.0]
    two_a = [2.0, 0.0, 0.0]
    n_a = discrete(tuple(a), tuple(z))
    n_2a = discrete(tuple(two_a), tuple(z))
    print(f"  ||x||  := d(x,0)  = {n_a}")
    print(f"  ||2x|| := d(2x,0) = {n_2a}")
    print(f"  homogeneity requires {n_2a} == 2 * {n_a} = {2 * n_a}: "
          f"{n_2a == 2 * n_a}")
    print("  -> homogeneity FAILS, so the discrete metric is not "
          "induced by any norm.")


if __name__ == "__main__":
    main()
