"""Integration (Riemann) — concept 15-integration of the math-foundations map.

Compute Riemann sums (left, right, midpoint) for f(x) = x^2 on [0, 1] with
n = 10, 100, 1000 subintervals and show convergence to the exact value 1/3.
Verify FTC2: F(x) = x^3 / 3 gives F(1) - F(0) = 1/3.

Stdlib only. Runs in <1 s on CPU.
"""


def f(x: float) -> float:
    return x * x


def F(x: float) -> float:  # antiderivative
    return x * x * x / 3.0


def riemann_sum(g, a: float, b: float, n: int, rule: str = "midpoint") -> float:
    h = (b - a) / n
    total = 0.0
    for i in range(n):
        if rule == "left":
            x = a + i * h
        elif rule == "right":
            x = a + (i + 1) * h
        elif rule == "midpoint":
            x = a + (i + 0.5) * h
        else:
            raise ValueError(f"unknown rule: {rule}")
        total += g(x) * h
    return total


def main() -> None:
    print("Integration (Riemann) — concept 15")
    print("=" * 60)
    print("Approximating  integral_0^1 x^2 dx  (exact value = 1/3)")
    print()

    exact = 1.0 / 3.0
    header = f"{'n':>6} | {'left':>14} | {'right':>14} | {'midpoint':>14}"
    print(header)
    print("-" * len(header))

    for n in (10, 100, 1000):
        L = riemann_sum(f, 0.0, 1.0, n, "left")
        R = riemann_sum(f, 0.0, 1.0, n, "right")
        M = riemann_sum(f, 0.0, 1.0, n, "midpoint")
        print(f"{n:>6} | {L:>14.10f} | {R:>14.10f} | {M:>14.10f}")

    print()
    print(f"exact = {exact:.10f}")
    print()

    # Show errors decay
    print("Errors (|approx - 1/3|):")
    for n in (10, 100, 1000):
        M = riemann_sum(f, 0.0, 1.0, n, "midpoint")
        print(f"  n={n:>5}  midpoint error = {abs(M - exact):.3e}")

    print()
    print("FTC2 verification:")
    print(f"  F(1) - F(0) = {F(1.0) - F(0.0):.10f}")
    print(f"  matches exact 1/3 = {F(1.0) - F(0.0) == exact}")

    print()
    print("Conclusion: midpoint rule converges as O(1/n^2);")
    print("left/right as O(1/n). Both approach 1/3, confirming")
    print("Riemann integrability of f(x) = x^2 and the FTC.")


if __name__ == "__main__":
    main()
