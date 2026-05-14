"""Groups, Rings, Fields - concept 04 of the math-foundations learning map.

Implements the cyclic group Z/nZ under addition mod n, verifies the four
group axioms numerically, then shows that Z/5Z is a field while Z/6Z is not.
"""


class Zmod:
    """The cyclic additive group / commutative ring (Z/nZ, +, *)."""

    def __init__(self, n):
        self.n = n
        self.elements = list(range(n))

    def add(self, a, b):
        return (a + b) % self.n

    def mul(self, a, b):
        return (a * b) % self.n

    def neg(self, a):
        return (-a) % self.n


def verify_group_axioms(G):
    """Verify (Z/nZ, +) satisfies the four group axioms."""
    n = G.n
    # 1. Closure
    closure = all(G.add(a, b) in G.elements for a in G.elements for b in G.elements)
    # 2. Associativity
    associative = all(
        G.add(G.add(a, b), c) == G.add(a, G.add(b, c))
        for a in G.elements for b in G.elements for c in G.elements
    )
    # 3. Identity (e = 0)
    identity = all(G.add(0, a) == a and G.add(a, 0) == a for a in G.elements)
    # 4. Inverses
    inverses = all(G.add(a, G.neg(a)) == 0 and G.add(G.neg(a), a) == 0 for a in G.elements)
    return closure, associative, identity, inverses


def multiplicative_inverse(G, a):
    """Return b in Z/nZ with a*b = 1, or None if none exists."""
    for b in G.elements:
        if G.mul(a, b) == 1:
            return b
    return None


def is_field(G):
    """Z/nZ is a field iff every nonzero element has a multiplicative inverse."""
    bad = [a for a in G.elements if a != 0 and multiplicative_inverse(G, a) is None]
    return (len(bad) == 0), bad


def main():
    print("Groups, Rings, Fields - concept 04")
    print("=" * 50)

    for n in (5, 6):
        G = Zmod(n)
        c, a, i, inv = verify_group_axioms(G)
        print(f"\nZ/{n}Z under + :")
        print(f"  closure       = {c}")
        print(f"  associativity = {a}")
        print(f"  identity (0)  = {i}")
        print(f"  inverses      = {inv}")
        assert all((c, a, i, inv)), f"group axioms failed for n={n}"

    print("\n-- Field check on Z/nZ --")
    for n in (5, 6):
        G = Zmod(n)
        field, bad = is_field(G)
        if field:
            print(f"Z/{n}Z IS a field: every nonzero element has an inverse.")
            for x in G.elements:
                if x != 0:
                    print(f"  inverse of {x} mod {n} = {multiplicative_inverse(G, x)}")
        else:
            print(f"Z/{n}Z is NOT a field: nonzero elements without inverse: {bad}")
            x = bad[0]
            print(f"  e.g. {x} mod {n}: {x}*k mod {n} for k=0..{n-1} = "
                  f"{[G.mul(x, k) for k in G.elements]} (never 1)")

    print("\nAll group axioms verified; field structure correctly distinguished.")


if __name__ == "__main__":
    main()
