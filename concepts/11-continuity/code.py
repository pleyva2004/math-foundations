"""Continuity — concept 11-continuity of the math-foundations learning map.

Numerically verify the epsilon-delta definition for f(x) = x^2 at x = 2,
and exhibit the failure of sequential continuity for the Dirichlet
indicator of the rationals. Stdlib only.
"""

from fractions import Fraction
from math import sqrt


def delta_for_x_squared_at_2(epsilon):
    """Return a delta valid for f(x)=x^2 at c=2 with tolerance epsilon.

    Derivation: |x^2 - 4| = |x-2||x+2|. Restricting to |x-2|<1 gives
    |x+2|<5, so |x^2-4| < 5|x-2|. Choose delta = min(1, epsilon/5).
    """
    return min(1.0, epsilon / 5.0)


def verify_x_squared(epsilon, n_samples=200):
    delta = delta_for_x_squared_at_2(epsilon)
    worst = 0.0
    # sample x uniformly across (2-delta, 2+delta), endpoints excluded
    for k in range(1, n_samples):
        x = 2.0 - delta + 2.0 * delta * k / n_samples
        worst = max(worst, abs(x * x - 4.0))
    return delta, worst


def dirichlet(x):
    """Indicator of the rationals. Inputs are exact (Fraction or int)."""
    return 1 if isinstance(x, (int, Fraction)) else 0


def sequential_failure_at_sqrt2():
    """Build x_n -> sqrt(2): rational truncations of sqrt(2) decimal expansion.

    Each x_n is rational so dirichlet(x_n) = 1, but the limit sqrt(2) is
    irrational, so dirichlet(sqrt(2)) = 0. Sequential continuity fails.
    """
    s = sqrt(2.0)
    seq = []
    for n in range(1, 9):
        digits = int(s * 10 ** n)
        x_n = Fraction(digits, 10 ** n)
        seq.append((n, x_n, dirichlet(x_n)))
    return seq, dirichlet(s)  # second arg passed as float -> not rational


def main():
    print("Continuity (concept 11-continuity)")
    print("=" * 60)

    print("\n[1] epsilon-delta verification for f(x) = x^2 at x = 2")
    print("-" * 60)
    for eps in (1.0, 0.1, 0.01, 1e-4):
        delta, worst = verify_x_squared(eps)
        ok = worst < eps
        print(f"  eps = {eps:<8g}  delta = {delta:<10.6f}  "
              f"max|f(x)-f(2)| = {worst:.6g}  passes? {ok}")
    print("  Choosing delta = min(1, eps/5) certifies continuity at x = 2.")

    print("\n[2] Sequential failure of the Dirichlet indicator at sqrt(2)")
    print("-" * 60)
    seq, limit_value = sequential_failure_at_sqrt2()
    for n, x_n, val in seq:
        print(f"  n = {n}  x_n = {float(x_n):.8f} (rational)  1_Q(x_n) = {val}")
    print(f"  limit x_n -> sqrt(2) (irrational); 1_Q(sqrt(2)) = {limit_value}")
    print("  Hence 1_Q(x_n) = 1 for all n but 1_Q(lim) = 0:")
    print("  sequential characterisation fails => 1_Q is discontinuous at sqrt(2).")
    print("  By a parallel argument with irrational approximants, 1_Q is")
    print("  discontinuous at every real number.")


if __name__ == "__main__":
    main()
