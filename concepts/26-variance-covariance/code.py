"""Variance and Covariance — concept 26-variance-covariance.

Empirical demonstration of variance, covariance, and the variance-of-sum
identity Var(X+Y) = Var(X) + Var(Y) + 2*Cov(X, Y). Stdlib only.
"""

import math
import random


def mean(xs):
    return sum(xs) / len(xs)


def variance(xs):
    mu = mean(xs)
    return sum((x - mu) ** 2 for x in xs) / len(xs)


def covariance(xs, ys):
    mx, my = mean(xs), mean(ys)
    return sum((x - mx) * (y - my) for x, y in zip(xs, ys)) / len(xs)


def box_muller(n, rng):
    """Generate n standard-normal samples via the Box-Muller transform."""
    out = []
    while len(out) < n:
        u1 = rng.random() or 1e-12
        u2 = rng.random()
        r = math.sqrt(-2.0 * math.log(u1))
        out.append(r * math.cos(2 * math.pi * u2))
        if len(out) < n:
            out.append(r * math.sin(2 * math.pi * u2))
    return out


def main():
    random.seed(0)
    N = 200_000
    # 1) Bernoulli(p): theory Var = p(1-p).
    p = 0.3
    bern = [1 if random.random() < p else 0 for _ in range(N)]
    print(f"Bernoulli(p={p}):  Var_emp={variance(bern):.5f}   theory={p*(1-p):.5f}")

    # 2) Uniform[0,1]: theory Var = 1/12.
    uni = [random.random() for _ in range(N)]
    print(f"Uniform[0,1]:     Var_emp={variance(uni):.5f}   theory={1/12:.5f}")

    # 3) Correlated Gaussians via Box-Muller. Let Z1, Z2 ~ N(0,1) indep.
    #    Set X = Z1 and Y = rho*Z1 + sqrt(1-rho^2)*Z2  ⇒  Cov(X,Y) = rho.
    rho = 0.6
    z1 = box_muller(N, random)
    z2 = box_muller(N, random)
    X = z1
    Y = [rho * a + math.sqrt(1 - rho * rho) * b for a, b in zip(z1, z2)]

    vX, vY = variance(X), variance(Y)
    cXY = covariance(X, Y)
    corr = cXY / math.sqrt(vX * vY)
    print(f"Gaussians:  Var(X)={vX:.4f}  Var(Y)={vY:.4f}  "
          f"Cov(X,Y)={cXY:.4f}  rho_emp={corr:.4f}  (target rho={rho})")

    # 4) Variance-of-sum identity:
    #    Var(X+Y) == Var(X) + Var(Y) + 2*Cov(X, Y).
    S = [x + y for x, y in zip(X, Y)]
    vS_direct = variance(S)
    vS_identity = vX + vY + 2 * cXY
    print(f"Var(X+Y) direct  = {vS_direct:.5f}")
    print(f"Var(X+Y) formula = {vS_identity:.5f}")
    print(f"abs diff = {abs(vS_direct - vS_identity):.2e}")

    # 5) Independence sanity check: shuffle Y to destroy correlation.
    Y_shuf = Y[:]
    random.shuffle(Y_shuf)
    print(f"After shuffle:  Cov(X, Y_shuf) ≈ {covariance(X, Y_shuf):.4f}  (≈0)")


if __name__ == "__main__":
    main()
