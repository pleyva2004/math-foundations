"""Logic and Proof — concept 01-logic-and-proof of the math-foundations learning map.

Brute-force truth tables for the basic connectives, verification of two
tautologies, and a numerical check of the induction identity
    sum_{k=1}^n k = n(n+1)/2
for n = 1, ..., 20.
"""

from itertools import product


def NEG(p): return not p
def AND(p, q): return p and q
def OR(p, q): return p or q
def IMP(p, q): return (not p) or q
def IFF(p, q): return p == q


def truth_table_binary(name, op):
    print(f"  {name}\n    p     q     result")
    for p, q in product([False, True], repeat=2):
        print(f"    {str(p):5} {str(q):5} {op(p, q)}")
    print()


def verify_tautology(name, pred, n_vars):
    """Return True iff `pred(*assignment)` is True for every assignment."""
    for asg in product([False, True], repeat=n_vars):
        if not pred(*asg):
            print(f"  [FAIL] {name}; counterexample {asg}")
            return False
    print(f"  [OK]  {name} (verified over {2**n_vars} assignments)")
    return True


def induction_check(n_max=20):
    """Compare explicit sum 1+...+n vs closed form n(n+1)/2."""
    print("  n  | explicit | closed   | equal?")
    all_ok = True
    for n in range(1, n_max + 1):
        explicit = sum(range(1, n + 1))
        closed = n * (n + 1) // 2
        ok = (explicit == closed)
        all_ok = all_ok and ok
        print(f"  {n:3d}|  {explicit:7d} |  {closed:7d} | {ok}")
    return all_ok


def main():
    print("Logic and Proof (concept 01-logic-and-proof)")
    print("=" * 60)
    print("\n[1] Truth tables for the binary connectives")
    for nm, op in [("AND (p and q)", AND), ("OR  (p or q)", OR),
                   ("IMP (p => q)", IMP), ("IFF (p <=> q)", IFF)]:
        truth_table_binary(nm, op)

    print("[2] Tautology verification")
    verify_tautology("p OR NOT p", lambda p: OR(p, NEG(p)), 1)
    verify_tautology("(p => q) <=> (NOT q => NOT p)",
                     lambda p, q: IFF(IMP(p, q), IMP(NEG(q), NEG(p))), 2)
    verify_tautology("NOT(p AND q) <=> (NOT p) OR (NOT q)",
                     lambda p, q: IFF(NEG(AND(p, q)), OR(NEG(p), NEG(q))), 2)

    print("\n[3] Numerical check: sum_{k=1}^n k = n(n+1)/2 for n=1..20")
    ok = induction_check(20)
    print(f"\n  Identity verified for n=1..20: {ok}")
    print("  (Full proof for all n in N is in lesson.tex, by induction.)")


if __name__ == "__main__":
    main()
