"""Gradient and Jacobian — concept 14-gradient-jacobian.

Demonstrates:
  1. Hand-coded analytic Jacobian of F(x,y) = (x^2 - y, e^{xy}).
  2. Centred-difference numerical Jacobian, compared to analytic.
  3. Jacobian determinant at (1, 0) — should equal 2.
  4. Numerical verification of the chain rule J_{F o G} = J_F(G) . J_G.
"""

import math


def F(p):
    x, y = p
    return [x * x - y, math.exp(x * y)]


def J_F_analytic(p):
    x, y = p
    e = math.exp(x * y)
    return [[2.0 * x, -1.0],
            [y * e, x * e]]


def G(t):
    # R^1 -> R^2
    return [math.cos(t[0]), math.sin(t[0])]


def J_G_analytic(t):
    return [[-math.sin(t[0])],
            [math.cos(t[0])]]


def numerical_jacobian(func, p, h=1e-6):
    """Centred-difference Jacobian of func: R^n -> R^m at p."""
    fp = func(p)
    m, n = len(fp), len(p)
    J = [[0.0] * n for _ in range(m)]
    for j in range(n):
        p_plus = list(p); p_plus[j] += h
        p_minus = list(p); p_minus[j] -= h
        f_plus = func(p_plus)
        f_minus = func(p_minus)
        for i in range(m):
            J[i][j] = (f_plus[i] - f_minus[i]) / (2.0 * h)
    return J


def matmul(A, B):
    m, k = len(A), len(A[0])
    k2, n = len(B), len(B[0])
    assert k == k2
    return [[sum(A[i][p] * B[p][j] for p in range(k)) for j in range(n)] for i in range(m)]


def max_abs_diff(A, B):
    return max(abs(A[i][j] - B[i][j]) for i in range(len(A)) for j in range(len(A[0])))


def det2(M):
    return M[0][0] * M[1][1] - M[0][1] * M[1][0]


def main():
    print("Gradient and Jacobian (concept 14)")
    print("=" * 60)

    p = [1.0, 0.0]
    Ja = J_F_analytic(p)
    Jn = numerical_jacobian(F, p)
    print(f"Analytic J_F(1,0) = {Ja}")
    print(f"Numeric  J_F(1,0) = {Jn}")
    print(f"Max abs diff      = {max_abs_diff(Ja, Jn):.2e}")
    print(f"det J_F(1,0)      = {det2(Ja):.6f}  (expected 2)")
    print()

    # Chain rule: H(t) = F(G(t)), G: R->R^2, F: R^2->R^2, so H: R->R^2.
    t0 = [0.7]
    JH_chain = matmul(J_F_analytic(G(t0)), J_G_analytic(t0))
    JH_num = numerical_jacobian(lambda t: F(G(t)), t0)
    print(f"Chain rule J_FoG(0.7) (analytic) = {JH_chain}")
    print(f"Direct numeric J_FoG(0.7)        = {JH_num}")
    print(f"Max abs diff                     = {max_abs_diff(JH_chain, JH_num):.2e}")


if __name__ == "__main__":
    main()
