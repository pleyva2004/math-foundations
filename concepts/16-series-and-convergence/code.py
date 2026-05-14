"""Series and Convergence — concept 16-series-and-convergence.

Stdlib-only demo of partial sums and Taylor expansion.
"""

import math


def partial_sums(term, n_terms):
    """Yield successive partial sums s_n = sum_{k=1}^{n} term(k)."""
    s = 0.0
    for k in range(1, n_terms + 1):
        s += term(k)
        yield k, s


def basel():
    """sum 1/n^2 -> pi^2 / 6."""
    target = math.pi ** 2 / 6
    for k, s in partial_sums(lambda n: 1.0 / n ** 2, 100_000):
        if k in (10, 100, 1_000, 10_000, 100_000):
            print(f"  n={k:>7d}  s_n = {s:.10f}   error = {abs(s - target):.2e}")
    print(f"  target  pi^2/6 = {target:.10f}")


def harmonic():
    """sum 1/n diverges (grows like ln n + gamma)."""
    for k, s in partial_sums(lambda n: 1.0 / n, 100_000):
        if k in (10, 100, 1_000, 10_000, 100_000):
            print(f"  n={k:>7d}  s_n = {s:.6f}   ln(n) = {math.log(k):.6f}")


def alternating_harmonic():
    """sum (-1)^n / n  (n >= 1)  =  -ln 2  (conditional)."""
    target = -math.log(2)
    for k, s in partial_sums(lambda n: (-1) ** n / n, 100_000):
        if k in (10, 100, 1_000, 10_000, 100_000):
            print(f"  n={k:>7d}  s_n = {s:.8f}   error = {abs(s - target):.2e}")
    print(f"  target  -ln 2 = {target:.10f}")


def taylor_exp(x, N):
    """Partial Taylor sum exp(x) ~ sum_{k=0}^{N} x^k / k!."""
    s = 0.0
    term = 1.0  # x^0 / 0!
    for k in range(N + 1):
        s += term
        term *= x / (k + 1)
    return s


def demo_taylor():
    """Show Taylor convergence of e^x at x = 1."""
    target = math.e
    for N in (0, 1, 2, 3, 5, 10, 15, 20):
        approx = taylor_exp(1.0, N)
        print(f"  N={N:>3d}  sum = {approx:.12f}   error = {abs(approx - target):.2e}")
    print(f"  target  e = {target:.12f}")


def main():
    print("Series and Convergence (concept 16-series-and-convergence)")
    print("=" * 60)

    print("\n[1] Basel:  sum 1/n^2  ->  pi^2/6")
    basel()

    print("\n[2] Harmonic:  sum 1/n  diverges like ln(n)")
    harmonic()

    print("\n[3] Alternating harmonic:  sum (-1)^n / n  =  -ln 2  (conditional)")
    alternating_harmonic()

    print("\n[4] Taylor:  e^x at x = 1, partial sums sum_{k=0}^{N} 1/k!")
    demo_taylor()


if __name__ == "__main__":
    main()
