"""Sets and Functions -- concept 00. Demonstrates power sets, injectivity,
surjectivity, and the characteristic-function bijection. Stdlib only."""

from itertools import chain, combinations


def power_set(a):
    """Return the power set of iterable `a` as a list of frozensets."""
    elems = list(a)
    return [
        frozenset(c)
        for c in chain.from_iterable(
            combinations(elems, r) for r in range(len(elems) + 1)
        )
    ]


def is_injective(f, domain):
    """f is injective iff distinct inputs produce distinct outputs."""
    seen = {}
    for x in domain:
        y = f(x)
        if y in seen and seen[y] != x:
            return False
        seen[y] = x
    return True


def is_surjective(f, domain, codomain):
    """f is surjective iff every element of codomain is hit."""
    return set(codomain).issubset({f(x) for x in domain})


def fmt_set(s):
    """Format a (frozen)set as a readable string."""
    return "{" + ", ".join(str(x) for x in sorted(s)) + "}" if s else "{}"


def main():
    print("Sets and Functions (concept 00)")
    print("=" * 50)
    A = {0, 1, 2, 3}
    print(f"A = {fmt_set(A)}, |A| = {len(A)}")

    pA = power_set(A)
    status = "matches" if len(pA) == 2 ** len(A) else "MISMATCH"
    print(f"|P(A)| = {len(pA)}, 2^|A| = {2 ** len(A)}  -> {status}")

    print("\nFirst 5 subsets in P(A):")
    for s in pA[:5]:
        print(f"  {fmt_set(s)}")

    B = {0, 1}
    f = lambda x: x % 2
    print(f"\nf: A -> {fmt_set(B)} defined by f(x) = x % 2")
    print(f"  injective?  {is_injective(f, A)}")
    print(f"  surjective? {is_surjective(f, A, B)}")

    g = lambda x: (x + 1) % 4
    print("\ng: A -> A defined by g(x) = (x + 1) mod 4")
    inj, sur = is_injective(g, A), is_surjective(g, A, A)
    print(f"  injective?  {inj}\n  surjective? {sur}\n  bijective?  {inj and sur}")

    print("\nCharacteristic-function bijection P(A) <-> {0,1}^A:")
    for s in pA[:4]:
        bits = "".join("1" if x in s else "0" for x in sorted(A))
        print(f"  subset {fmt_set(s):>14}  <->  bits {bits}")

    print("\nAll checks complete.")


if __name__ == "__main__":
    main()
