"""Existence and Uniqueness (Picard-Lindelöf) -- concept 30.

(1) Picard iteration for y' = y, y(0) = 1 converges to e^t; the k-th
    iterate is the k-th Taylor polynomial of e^t.
(2) y' = y^{2/3}, y(0) = 0 has multiple solutions because f(t,y) =
    y^{2/3} is NOT Lipschitz at y=0. Two are: y == 0 and y = (t/3)^3.

Stdlib only. CPU-runnable in <1 s.
"""
from math import factorial


def picard(n_steps):
    """Return Picard iterates for y'=y, y(0)=1 as coefficient lists."""
    poly = [1.0]
    hist = [list(poly)]
    for _ in range(n_steps):
        integ = [0.0] + [poly[j] / (j + 1) for j in range(len(poly))]
        integ[0] += 1.0  # add the y_0 = 1 constant.
        poly = integ
        hist.append(list(poly))
    return hist


def evalp(p, t):
    return sum(c * (t ** j) for j, c in enumerate(p))


def exp_taylor(t, k):
    return sum((t ** j) / factorial(j) for j in range(k + 1))


def main():
    print("Existence and Uniqueness (Picard-Lindelof) -- concept 30")
    print("=" * 60)

    # Part 1: Picard iteration for y' = y, y(0) = 1.
    print("\n[1] Picard iterates for y' = y, y(0) = 1:")
    polys = picard(5)
    for k, p in enumerate(polys):
        coeffs = ", ".join(f"{c:.6f}" for c in p)
        print(f"  y_{k}(t) coefs = [{coeffs}]")
    print("\n  Compare y_k(1) to k-th Taylor partial sum of e^1:")
    for k, p in enumerate(polys):
        print(f"    y_{k}(1) = {evalp(p,1.0):.8f}    "
              f"taylor_{k}(1) = {exp_taylor(1.0,k):.8f}")
    print("  -> Picard iterates ARE the Taylor polynomials of e^t.")

    # Part 2: Non-uniqueness when Lipschitz fails.
    print("\n[2] y' = y^{2/3}, y(0) = 0 has multiple solutions:")
    for t in [0.0, 0.5, 1.0, 2.0]:
        y_a, y_b = 0.0, (t / 3.0) ** 3
        print(f"  t={t}:  y_a={y_a:.6f}   y_b=(t/3)^3={y_b:.6f}")
    print("  Both satisfy the IVP. Reason: f(t,y) = y^{2/3} is NOT")
    print("  Lipschitz at y=0; (2/3) y^{-1/3} blows up there.")
    eps = 1e-7
    yp = (((1.0 + eps) / 3.0) ** 3 - ((1.0 - eps) / 3.0) ** 3) / (2 * eps)
    rhs = ((1.0 / 3.0) ** 3) ** (2 / 3)
    print(f"  check t=1: y'(t)={yp:.6f}  vs  y^(2/3)={rhs:.6f}")


if __name__ == "__main__":
    main()
