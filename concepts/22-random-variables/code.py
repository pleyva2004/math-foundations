"""Random Variables (concept 22). Stdlib only; CPU-runnable in <1 s.

Demonstrates: (Omega, F, P) for a fair die; the RV X : Omega -> R;
empirical vs. true CDF; composition Y = g(X) with g Borel.
"""

import random
from collections import Counter


def make_die_rv():
    """Return X : Omega -> R for a fair six-sided die."""
    Omega = [1, 2, 3, 4, 5, 6]            # sample space
    P = {omega: 1 / 6 for omega in Omega}  # probability measure
    X = lambda omega: float(omega)         # the random variable
    return Omega, P, X


def true_cdf(x, Omega, P, X):
    """F_X(x) = P({omega : X(omega) <= x})."""
    return sum(p for omega, p in P.items() if X(omega) <= x)


def empirical_cdf(x, samples):
    """Empirical CDF from a list of samples."""
    return sum(1 for s in samples if s <= x) / len(samples)


def main():
    random.seed(0)
    Omega, P, X = make_die_rv()

    print("Random Variables (concept 22)")
    print("=" * 60)
    print(f"Sample space Omega = {Omega}")
    print(f"X(omega) = omega; image X(Omega) = {sorted({X(o) for o in Omega})}")

    # Sample N outcomes omega ~ P, then push through X.
    N = 20_000
    omegas = random.choices(Omega, weights=[P[o] for o in Omega], k=N)
    X_samples = [X(o) for o in omegas]

    print()
    print(f"Comparing empirical CDF to true CDF (N={N}):")
    print(f"{'x':>4} | {'F_X(x) true':>12} | {'F_X(x) emp.':>12} | {'|diff|':>8}")
    print("-" * 50)
    for x in [0.5, 1.0, 2.5, 3.0, 4.5, 6.0, 7.0]:
        t = true_cdf(x, Omega, P, X)
        e = empirical_cdf(x, X_samples)
        print(f"{x:>4} | {t:>12.4f} | {e:>12.4f} | {abs(t - e):>8.4f}")

    # Composition: Y = g(X) with g(x) = x**2.  Y is a random variable
    # because g is Borel (continuous => Borel).
    g = lambda x: x * x
    Y = lambda omega: g(X(omega))
    Y_samples = [Y(o) for o in omegas]

    print()
    print("Composition Y = X**2 (also a random variable):")
    print(f"Image Y(Omega) = {sorted({Y(o) for o in Omega})}")
    counts = Counter(Y_samples)
    print(f"{'y':>4} | {'p_Y(y) true':>12} | {'p_Y(y) emp.':>12}")
    print("-" * 40)
    for y in sorted(counts):
        true_p = 1 / 6   # bijection on this image
        emp_p = counts[y] / N
        print(f"{y:>4.0f} | {true_p:>12.4f} | {emp_p:>12.4f}")

    print()
    print("Takeaway: X is a function Omega -> R; pushing P through X^{-1}")
    print("gives the distribution of X.  Composing with any Borel g keeps")
    print("us inside the world of random variables.")


if __name__ == "__main__":
    main()
