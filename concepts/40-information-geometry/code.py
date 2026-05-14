"""Information Geometry (Fisher Metric) -- concept 40.

Demonstrates two facts for the unit-variance Gaussian family
N(mu, 1) parameterized by mu in R:

  (a) Fisher information F(mu) = 1, computed analytically and numerically
      via a finite-difference Hessian of -log p_mu(x) averaged over draws
      x ~ N(mu, 1).
  (b) Local KL = 1/2 eps^2 F(mu): we verify
      D_KL(N(0,1) || N(eps,1)) = eps^2 / 2 for small eps.

Stdlib only -- uses random.gauss for sampling and math for log/exp.
"""

import math
import random


def log_p(x: float, mu: float) -> float:
    """Log-density of N(mu, 1) at x."""
    return -0.5 * math.log(2.0 * math.pi) - 0.5 * (x - mu) ** 2


def neg_log_p_at(mu0: float, x: float):
    """Return f(mu) = -log p_mu(x), useful for numerical Hessian in mu."""
    def f(mu: float) -> float:
        return -log_p(x, mu)
    return f


def numerical_second_derivative(f, mu: float, h: float = 1e-3) -> float:
    """Central finite-difference second derivative."""
    return (f(mu + h) - 2.0 * f(mu) + f(mu - h)) / (h * h)


def fisher_numerical(mu: float, n_samples: int, seed: int) -> float:
    """Estimate F(mu) = E_{x~p_mu}[-d^2/dmu^2 log p_mu(x)] by Monte Carlo."""
    rng = random.Random(seed)
    total = 0.0
    for _ in range(n_samples):
        x = rng.gauss(mu, 1.0)
        # We want E[-d^2/dmu^2 log p_mu(x)]. The negative sign is folded in
        # by computing the second derivative of f(mu) = -log p_mu(x).
        f = neg_log_p_at(mu, x)
        total += numerical_second_derivative(f, mu)
    return total / n_samples


def kl_gaussian_unit_var(mu_p: float, mu_q: float) -> float:
    """Closed-form KL(N(mu_p,1) || N(mu_q,1)) = (mu_p - mu_q)^2 / 2."""
    return 0.5 * (mu_p - mu_q) ** 2


def main():
    print("Information Geometry (Fisher Metric) -- concept 40")
    print("=" * 60)

    mu = 0.0
    print("\n(a) Fisher information for N(mu, 1) at mu = 0")
    print(f"    Analytical: F(mu) = 1.0")
    f_num = fisher_numerical(mu, n_samples=20_000, seed=0)
    print(f"    Numerical (MC, n=20000): F_hat = {f_num:.4f}")
    print(f"    |error| = {abs(f_num - 1.0):.4f}")

    print("\n(b) Second-order KL approximation: D_KL(N(0,1) || N(eps,1))")
    print(f"    Predicted by Fisher: 1/2 * eps^2 * F = eps^2 / 2")
    print(f"    {'eps':>10}  {'D_KL':>14}  {'eps^2/2':>14}  {'ratio':>10}")
    for eps in (1e-1, 1e-2, 1e-3, 1e-4):
        kl = kl_gaussian_unit_var(0.0, eps)
        approx = 0.5 * eps * eps
        ratio = kl / approx if approx > 0 else float("nan")
        print(f"    {eps:10.0e}  {kl:14.6e}  {approx:14.6e}  {ratio:10.6f}")

    print("\nFor N(mu, 1) the family is exactly quadratic in mu, so")
    print("the second-order Fisher approximation is exact (no higher-order terms).")


if __name__ == "__main__":
    main()
