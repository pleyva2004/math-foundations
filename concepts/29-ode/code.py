"""Ordinary Differential Equations — concept 29-ode of the math-foundations learning map.

Demonstration: Euler's method for the IVP

    y'(t) = -y(t),   y(0) = 1

over t in [0, 5], compared against the exact solution y(t) = exp(-t).
We run three step sizes h in {0.5, 0.1, 0.01} and report the max absolute
error on the time grid, then estimate the empirical order of convergence.
Stdlib only.
"""

import math


def euler(f, t0, y0, t_end, h):
    """Forward Euler. Returns parallel lists of (t_k, y_k)."""
    ts = [t0]
    ys = [y0]
    t, y = t0, y0
    n_steps = int(round((t_end - t0) / h))
    for _ in range(n_steps):
        y = y + h * f(t, y)
        t = t + h
        ts.append(t)
        ys.append(y)
    return ts, ys


def max_abs_error(ts, ys, exact):
    """Max |y_k - exact(t_k)| over the grid."""
    return max(abs(y - exact(t)) for t, y in zip(ts, ys))


def main():
    print("Ordinary Differential Equations (concept 29-ode)")
    print("=" * 60)
    print("IVP:    y'(t) = -y(t),  y(0) = 1")
    print("Exact:  y(t) = exp(-t)")
    print("Method: forward Euler on t in [0, 5]")
    print()

    f = lambda t, y: -y           # noqa: E731
    exact = lambda t: math.exp(-t)  # noqa: E731

    step_sizes = [0.5, 0.1, 0.01]
    errors = []

    print(f"{'h':>8} | {'steps':>6} | {'y_N (Euler)':>14} | "
          f"{'y(5) exact':>14} | {'max |err|':>12}")
    print("-" * 70)
    for h in step_sizes:
        ts, ys = euler(f, 0.0, 1.0, 5.0, h)
        err = max_abs_error(ts, ys, exact)
        errors.append(err)
        print(f"{h:>8.3f} | {len(ts) - 1:>6d} | {ys[-1]:>14.8f} | "
              f"{exact(5.0):>14.8f} | {err:>12.6e}")

    print()
    print("Empirical order of convergence (Euler is O(h), so ratio ~ step_ratio):")
    for i in range(1, len(step_sizes)):
        h_prev, h_curr = step_sizes[i - 1], step_sizes[i]
        e_prev, e_curr = errors[i - 1], errors[i]
        ratio_h = h_prev / h_curr
        ratio_e = e_prev / e_curr if e_curr > 0 else float("inf")
        order = math.log(ratio_e) / math.log(ratio_h)
        print(f"  h: {h_prev:.3f} -> {h_curr:.3f}  "
              f"error ratio = {ratio_e:8.3f}  order ~ {order:.3f}")

    print()
    print("Conclusion: error shrinks roughly linearly in h, matching Euler's "
          "O(h) global error.")


if __name__ == "__main__":
    main()
