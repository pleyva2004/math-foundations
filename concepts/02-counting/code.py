"""Counting and Combinatorics — concept 02-counting.

Demonstrations:
  (1) Enumerate permutations and combinations of a small set and compare
      counts to the formulae P(n,k) and C(n,k).
  (2) Verify the binomial theorem (1+x)^n = sum_k C(n,k) x^k at a chosen
      (x, n).
  (3) Demonstrate the pigeonhole principle: place 10 items into 7 bins
      and show some bin holds at least 2.
"""

from itertools import permutations, combinations
from math import comb, perm
from collections import Counter


def demo_perm_comb():
    S = ("a", "b", "c", "d", "e")
    n, k = len(S), 3

    perms = list(permutations(S, k))
    combs = list(combinations(S, k))

    print(f"Set S = {S},  n = {n},  k = {k}")
    print(f"  enumerated permutations: {len(perms)}   formula P(n,k) = {perm(n, k)}")
    print(f"  enumerated combinations: {len(combs)}   formula C(n,k) = {comb(n, k)}")
    print(f"  ratio perms / combs    = {len(perms) // len(combs)}   k! = {perm(k, k)}")
    assert len(perms) == perm(n, k)
    assert len(combs) == comb(n, k)
    assert len(perms) == len(combs) * perm(k, k)
    print("  [OK] enumeration agrees with formulae")


def demo_binomial_theorem():
    n = 6
    x = 2
    lhs = (1 + x) ** n
    rhs = sum(comb(n, k) * x**k for k in range(n + 1))
    print(f"Binomial theorem at n={n}, x={x}:")
    print(f"  (1+x)^n            = {lhs}")
    print(f"  sum_k C(n,k) x^k   = {rhs}")
    assert lhs == rhs
    expansion = " + ".join(f"C({n},{k})*{x}^{k}" for k in range(n + 1))
    print(f"  expansion: {expansion}")
    print("  [OK] both sides equal")


def demo_pigeonhole():
    items = list(range(10))  # 10 items
    bins = 7
    # Assign each item to a bin via i mod 7 (any assignment works).
    assignment = {item: item % bins for item in items}
    counts = Counter(assignment.values())
    print(f"Assigned {len(items)} items to {bins} bins (assignment by i mod {bins}):")
    for b in sorted(counts):
        print(f"  bin {b}: {counts[b]} item(s)")
    max_bin, max_count = max(counts.items(), key=lambda kv: kv[1])
    print(f"  fullest bin = {max_bin} with {max_count} items")
    assert max_count >= 2, "pigeonhole guarantees a bin of size >= 2"
    expected_min_max = -(-len(items) // bins)  # ceil division
    print(f"  pigeonhole guarantees some bin has >= ceil(10/7) = {expected_min_max}")
    print("  [OK] pigeonhole principle witnessed")


def main():
    print("Counting and Combinatorics (concept 02-counting)")
    print("=" * 60)
    demo_perm_comb()
    print("-" * 60)
    demo_binomial_theorem()
    print("-" * 60)
    demo_pigeonhole()
    print("=" * 60)
    print("All demonstrations passed.")


if __name__ == "__main__":
    main()
