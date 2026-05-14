"""Sample Spaces — concept 17-sample-spaces of the math-foundations learning map.

Build finite sample spaces, enumerate their event families (power sets),
verify |2^Omega| = 2^|Omega|, and simulate draws to show empirical
frequencies approach uniform.
"""

import random
from itertools import chain, combinations, product


def power_set(omega):
    """Return the list of all subsets of omega (as frozensets)."""
    items = list(omega)
    return [
        frozenset(c)
        for r in range(len(items) + 1)
        for c in combinations(items, r)
    ]


def verify_cardinality(omega, name):
    n = len(omega)
    events = power_set(omega)
    assert len(events) == 2 ** n, f"{name}: |2^Omega| mismatch"
    print(f"  {name}: |Omega|={n}, |2^Omega|={len(events)} = 2^{n}")
    return events


def simulate_uniform(omega, trials, seed=0):
    """Draw `trials` outcomes uniformly from omega and return frequency dict."""
    rng = random.Random(seed)
    counts = {w: 0 for w in omega}
    for _ in range(trials):
        counts[rng.choice(list(omega))] += 1
    return {w: c / trials for w, c in counts.items()}


def main():
    print("Sample Spaces (concept 17-sample-spaces)")
    print("=" * 60)

    coin = ("H", "T")
    die = (1, 2, 3, 4, 5, 6)
    two_dice = tuple(product(die, repeat=2))

    print("\nPower-set cardinalities (Theorem: |2^Omega| = 2^|Omega|):")
    coin_events = verify_cardinality(coin, "coin")
    die_events = verify_cardinality(die, "die")
    # 2 dice has 2^36 events — too many to enumerate; just check |Omega|.
    assert len(two_dice) == 36
    print(f"  two-dice: |Omega|=36 (2^36 events not enumerated)")

    print("\nSample events:")
    print(f"  coin events: {sorted(map(sorted, coin_events))}")
    even = frozenset(w for w in die if w % 2 == 0)
    print(f"  die 'even'  = {sorted(even)}")
    sum7 = frozenset(p for p in two_dice if sum(p) == 7)
    print(f"  two-dice 'sum=7' = {sorted(sum7)}  (|.|={len(sum7)})")

    print("\nEmpirical frequencies approach uniform (Law of Large Numbers):")
    for trials in (100, 10_000, 1_000_000):
        freqs = simulate_uniform(die, trials, seed=42)
        max_dev = max(abs(p - 1 / 6) for p in freqs.values())
        print(f"  die, {trials:>8d} trials: max |freq - 1/6| = {max_dev:.5f}")

    print("\nProbability of event 'sum=7' over two dice:")
    rng = random.Random(7)
    hits = sum(1 for _ in range(100_000)
               if (rng.randint(1, 6) + rng.randint(1, 6)) == 7)
    print(f"  empirical: {hits / 100_000:.4f}    theoretical: {6/36:.4f}")

    print("\nAll assertions passed. See README.md for the math.")


if __name__ == "__main__":
    main()
