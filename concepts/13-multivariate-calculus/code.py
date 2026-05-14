"""Multivariate Calculus -- concept 13-multivariate-calculus.

Numerical partial derivatives via centred differences for
    f(x, y) = x^2 * y + sin(x * y),
compared against analytic answers at (1, 2), plus a directional-derivative
check D_v f = grad f . v for v = (1, 1) / sqrt(2). Stdlib only.
"""

import math


def f(x, y):
    return x * x * y + math.sin(x * y)


def grad_analytic(x, y):
    """Analytic gradient of f."""
    df_dx = 2.0 * x * y + y * math.cos(x * y)
    df_dy = x * x + x * math.cos(x * y)
    return (df_dx, df_dy)


def partial_central(g, x, y, axis, h=1e-5):
    """Centred-difference partial derivative of a scalar function g(x, y)."""
    if axis == 0:
        return (g(x + h, y) - g(x - h, y)) / (2.0 * h)
    if axis == 1:
        return (g(x, y + h) - g(x, y - h)) / (2.0 * h)
    raise ValueError("axis must be 0 or 1")


def directional_derivative_numeric(g, x, y, v, h=1e-5):
    """Numerical D_v g via the limit (g(p + h v) - g(p - h v)) / (2 h)."""
    vx, vy = v
    return (g(x + h * vx, y + h * vy) - g(x - h * vx, y - h * vy)) / (2.0 * h)


def main():
    x0, y0 = 1.0, 2.0
    print("Multivariate Calculus -- node 13")
    print("=" * 56)
    print(f"f(x, y) = x^2 y + sin(xy); evaluating at (x, y) = ({x0}, {y0})")
    print(f"f({x0}, {y0}) = {f(x0, y0):.10f}")
    print()

    # Partials.
    dfdx_a, dfdy_a = grad_analytic(x0, y0)
    dfdx_n = partial_central(f, x0, y0, axis=0)
    dfdy_n = partial_central(f, x0, y0, axis=1)
    print("Partial derivatives at (1, 2):")
    print(f"  df/dx  analytic = {dfdx_a:.10f}")
    print(f"  df/dx  numeric  = {dfdx_n:.10f}   |err|={abs(dfdx_a - dfdx_n):.2e}")
    print(f"  df/dy  analytic = {dfdy_a:.10f}")
    print(f"  df/dy  numeric  = {dfdy_n:.10f}   |err|={abs(dfdy_a - dfdy_n):.2e}")
    print()

    # Directional derivative.
    inv_sqrt2 = 1.0 / math.sqrt(2.0)
    v = (inv_sqrt2, inv_sqrt2)
    dv_formula = dfdx_a * v[0] + dfdy_a * v[1]          # grad f . v
    dv_numeric = directional_derivative_numeric(f, x0, y0, v)
    print(f"Unit vector v = (1/sqrt(2), 1/sqrt(2)) ~= ({v[0]:.6f}, {v[1]:.6f})")
    print(f"  D_v f  formula  (grad f . v) = {dv_formula:.10f}")
    print(f"  D_v f  numeric               = {dv_numeric:.10f}")
    print(f"  |err| = {abs(dv_formula - dv_numeric):.2e}")
    print()

    # Sanity: derivative along an axis equals the partial.
    e1_check = directional_derivative_numeric(f, x0, y0, (1.0, 0.0))
    print(f"Axis check: D_{{e1}} f numeric = {e1_check:.10f}  (should match df/dx)")

    tol = 1e-6
    assert abs(dfdx_a - dfdx_n) < tol
    assert abs(dfdy_a - dfdy_n) < tol
    assert abs(dv_formula - dv_numeric) < tol
    assert abs(e1_check - dfdx_a) < tol
    print("\nAll checks passed.")


if __name__ == "__main__":
    main()
