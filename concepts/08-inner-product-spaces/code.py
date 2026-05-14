"""Inner Product Spaces - concept 08-inner-product-spaces.

Demonstrates:
  1. The standard dot product in R^4.
  2. Numerical verification of the Cauchy-Schwarz inequality on random
     pairs.
  3. The Gram-Schmidt orthonormalisation procedure applied to three
     linearly independent vectors in R^3.

Pure-Python (numpy used if available, else a small fallback).
"""

from __future__ import annotations
import math
import random
from typing import List, Sequence

try:
    import numpy as _np  # type: ignore
    _HAVE_NUMPY = True
except ImportError:
    _HAVE_NUMPY = False


def inner(u: Sequence[float], v: Sequence[float]) -> float:
    return sum(a * b for a, b in zip(u, v))


def norm(u: Sequence[float]) -> float:
    return math.sqrt(inner(u, u))


def scale(alpha: float, u: Sequence[float]) -> List[float]:
    return [alpha * x for x in u]


def sub(u: Sequence[float], v: Sequence[float]) -> List[float]:
    return [a - b for a, b in zip(u, v)]


def gram_schmidt(vectors: Sequence[Sequence[float]]) -> List[List[float]]:
    """Return an orthonormal basis for span(vectors)."""
    basis: List[List[float]] = []
    for v in vectors:
        w = list(v)
        for e in basis:
            w = sub(w, scale(inner(w, e), e))
        n = norm(w)
        if n < 1e-12:
            raise ValueError("Input vectors are linearly dependent.")
        basis.append(scale(1.0 / n, w))
    return basis


def random_vector(n: int, rng: random.Random) -> List[float]:
    return [rng.gauss(0.0, 1.0) for _ in range(n)]


def main() -> None:
    print("Inner Product Spaces (concept 08-inner-product-spaces)")
    print("=" * 60)
    print(f"numpy available: {_HAVE_NUMPY}")

    # 1. Dot product in R^4.
    u = [1.0, 2.0, 2.0, 0.0]
    v = [2.0, 0.0, -1.0, 4.0]
    print("\n== Section 1: dot product in R^4 ==")
    print(f"u = {u}")
    print(f"v = {v}")
    print(f"<u, v> = {inner(u, v):.4f}    (expected 0; u and v are orthogonal)")
    print(f"||u|| = {norm(u):.4f},  ||v|| = {norm(v):.4f}")

    # 2. Cauchy-Schwarz.
    print("\n== Section 2: Cauchy-Schwarz on random pairs ==")
    rng = random.Random(0)
    max_ratio = 0.0
    trials = 2000
    for _ in range(trials):
        a = random_vector(7, rng)
        b = random_vector(7, rng)
        lhs = abs(inner(a, b))
        rhs = norm(a) * norm(b)
        assert lhs <= rhs + 1e-9, "Cauchy-Schwarz violated!"
        if rhs > 1e-12:
            max_ratio = max(max_ratio, lhs / rhs)
    print(f"All {trials} random pairs satisfy |<a,b>| <= ||a|| ||b||.")
    print(f"Largest observed ratio |<a,b>|/(||a|| ||b||) = {max_ratio:.4f}  (<= 1)")

    # 3. Gram-Schmidt.
    print("\n== Section 3: Gram-Schmidt in R^3 ==")
    v1 = [1.0, 1.0, 0.0]
    v2 = [1.0, 0.0, 1.0]
    v3 = [0.0, 1.0, 1.0]
    basis = gram_schmidt([v1, v2, v3])
    print("Orthonormal basis:")
    for i, e in enumerate(basis, 1):
        print(f"  e_{i} = {[round(x, 4) for x in e]}")

    # Verify orthonormality.
    err = 0.0
    for i in range(3):
        for j in range(3):
            target = 1.0 if i == j else 0.0
            err = max(err, abs(inner(basis[i], basis[j]) - target))
    print(f"Max deviation of Gram matrix from identity = {err:.2e}")
    assert err < 1e-10, "Gram-Schmidt output is not orthonormal."

    print("\nAll checks passed.")


if __name__ == "__main__":
    main()
