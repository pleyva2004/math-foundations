"""Derivatives (Univariate) -- concept 12-derivatives.

Numerically demonstrates two facts:

  1. The difference quotient (f(c+h) - f(c)) / h converges to f'(c) as h -> 0.
     We compute it for f(x) = x^2 at c = 2 with h = 1e-1, 1e-2, ..., 1e-10
     and watch the value approach 4.

  2. The chain rule: d/dx sin(x^2) at x = 1 equals 2 cos(1).

Stdlib only (math).
"""

import math


def diff_quotient(f, c, h):
    """Forward difference quotient (f(c + h) - f(c)) / h."""
    return (f(c + h) - f(c)) / h


def main():
    print("Derivatives (Univariate) -- concept 12")
    print("=" * 60)

    # -----------------------------------------------------------------
    # Part 1: derivative of f(x) = x^2 at c = 2, true value f'(2) = 4
    # -----------------------------------------------------------------
    f = lambda x: x * x
    c = 2.0
    true = 2 * c  # = 4.0

    print()
    print("Part 1: f(x) = x^2,  c = 2,  true f'(c) = 4")
    print("-" * 60)
    print(f"{'h':>10}  {'(f(c+h)-f(c))/h':>22}  {'|error|':>14}")
    for k in range(1, 11):
        h = 10.0 ** (-k)
        approx = diff_quotient(f, c, h)
        err = abs(approx - true)
        print(f"{h:>10.1e}  {approx:>22.15f}  {err:>14.2e}")
    print()
    print("Note: error shrinks as h decreases, then floating-point")
    print("cancellation begins to dominate near h ~ 1e-8.")

    # -----------------------------------------------------------------
    # Part 2: chain rule for g(x) = sin(x^2) at x = 1
    #   g'(x) = cos(x^2) * 2x   =>   g'(1) = 2 cos(1)
    # -----------------------------------------------------------------
    g = lambda x: math.sin(x * x)
    x0 = 1.0
    analytic = 2.0 * x0 * math.cos(x0 * x0)  # = 2 cos(1)

    print()
    print("Part 2: chain rule for g(x) = sin(x^2) at x = 1")
    print("-" * 60)
    print(f"Analytic g'(1) = 2 cos(1) = {analytic:.15f}")

    # Central difference is more accurate than forward for verification.
    h = 1e-6
    central = (g(x0 + h) - g(x0 - h)) / (2 * h)
    print(f"Central difference (h = {h:g}): {central:.15f}")
    print(f"|error| = {abs(central - analytic):.2e}")

    assert abs(central - analytic) < 1e-8, "chain-rule verification failed"
    print()
    print("Chain rule verified numerically.")


if __name__ == "__main__":
    main()
