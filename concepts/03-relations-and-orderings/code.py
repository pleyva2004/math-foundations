"""Concept 03 -- Relations and Orderings.

Numerical witnesses for:
  (1) congruence mod 5 on {0,...,19} as an equivalence relation,
  (2) its equivalence classes forming a partition,
  (3) divisibility on {1,...,12} as a partial order with antisymmetry
      but not symmetry.
"""

from itertools import product


def is_reflexive(R, A):
    return all((a, a) in R for a in A)


def is_symmetric(R):
    return all((b, a) in R for (a, b) in R)


def is_transitive(R):
    pairs = {(a, b) for (a, b) in R}
    for (a, b) in pairs:
        for (c, d) in pairs:
            if b == c and (a, d) not in pairs:
                return False
    return True


def is_antisymmetric(R):
    for (a, b) in R:
        if a != b and (b, a) in R:
            return False
    return True


def equivalence_classes(R, A):
    classes = []
    seen = set()
    for a in A:
        if a in seen:
            continue
        cls = frozenset(b for b in A if (a, b) in R)
        classes.append(cls)
        seen |= cls
    return classes


def is_partition(blocks, A):
    union = set().union(*blocks)
    if union != set(A):
        return False
    for B1, B2 in product(blocks, blocks):
        if B1 is not B2 and B1 & B2:
            return False
    return all(len(B) > 0 for B in blocks)


def main():
    print("Concept 03: Relations and Orderings")
    print("=" * 50)

    # (1) Equivalence relation: x = y (mod 5) on {0,...,19}
    A = list(range(20))
    mod5 = {(x, y) for x in A for y in A if (x - y) % 5 == 0}
    print(f"Relation: x = y (mod 5) on {{0,...,19}} -- |R| = {len(mod5)}")
    print(f"  reflexive   : {is_reflexive(mod5, A)}")
    print(f"  symmetric   : {is_symmetric(mod5)}")
    print(f"  transitive  : {is_transitive(mod5)}")
    assert is_reflexive(mod5, A) and is_symmetric(mod5) and is_transitive(mod5)

    # (2) Equivalence classes partition A.
    classes = equivalence_classes(mod5, A)
    print(f"  #classes    : {len(classes)}")
    for c in sorted(classes, key=min):
        print(f"    {sorted(c)}")
    assert is_partition(classes, A)
    print("  partition?  : True\n")

    # (3) Partial order: divisibility on {1,...,12}
    B = list(range(1, 13))
    div = {(a, b) for a in B for b in B if b % a == 0}
    print(f"Relation: a | b on {{1,...,12}} -- |R| = {len(div)}")
    print(f"  reflexive     : {is_reflexive(div, B)}")
    print(f"  antisymmetric : {is_antisymmetric(div)}")
    print(f"  transitive    : {is_transitive(div)}")
    print(f"  symmetric     : {is_symmetric(div)}  (expected False)")
    assert is_reflexive(div, B) and is_antisymmetric(div) and is_transitive(div)
    assert not is_symmetric(div)
    incomp = [(a, b) for a in B for b in B if a < b and (a, b) not in div and (b, a) not in div]
    print(f"  e.g. incomparable pair: {incomp[0]} (not total)")


if __name__ == "__main__":
    main()
