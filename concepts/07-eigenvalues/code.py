"""Eigenvalues and Eigenvectors -- concept 07 of the math-foundations map.

Pure-stdlib demo on a 3x3 real symmetric A:
  1. Compute eigenpairs via Jacobi rotations.
  2. Verify A v = lambda v for each pair.
  3. Reconstruct A = Q Lambda Q^T (spectral theorem).
"""

from __future__ import annotations
import math


def matmul(A, B):
    return [[sum(A[i][k] * B[k][j] for k in range(len(B))) for j in range(len(B[0]))] for i in range(len(A))]


def jacobi_eigh(A, tol=1e-12, max_sweeps=80):
    """Symmetric eigendecomposition by Jacobi rotations. Returns (eigvals, Q)."""
    n = len(A)
    M = [row[:] for row in A]
    Q = [[float(i == j) for j in range(n)] for i in range(n)]
    for _ in range(max_sweeps):
        off = math.sqrt(sum(M[i][j] ** 2 for i in range(n) for j in range(n) if i != j))
        if off < tol: break
        for p in range(n - 1):
            for q in range(p + 1, n):
                if abs(M[p][q]) < 1e-15: continue
                theta = (M[q][q] - M[p][p]) / (2.0 * M[p][q])
                t = math.copysign(1.0, theta) / (abs(theta) + math.sqrt(1.0 + theta * theta))
                c = 1.0 / math.sqrt(1.0 + t * t); s = t * c; apq = M[p][q]
                M[p][p] -= t * apq; M[q][q] += t * apq; M[p][q] = M[q][p] = 0.0
                for i in range(n):
                    if i != p and i != q:
                        mip, miq = M[i][p], M[i][q]
                        M[i][p] = M[p][i] = c * mip - s * miq
                        M[i][q] = M[q][i] = s * mip + c * miq
                for i in range(n):
                    qip, qiq = Q[i][p], Q[i][q]
                    Q[i][p] = c * qip - s * qiq; Q[i][q] = s * qip + c * qiq
    return [M[i][i] for i in range(n)], Q


def main():
    A = [[4.0, 1.0, 2.0], [1.0, 3.0, 0.0], [2.0, 0.0, 5.0]]
    print("Matrix A (symmetric):")
    for row in A:
        print("  " + "  ".join(f"{x:+.4f}" for x in row))

    eigvals, Q = jacobi_eigh(A)
    order = sorted(range(3), key=lambda i: -eigvals[i])
    eigvals = [eigvals[i] for i in order]
    Q = [[Q[i][order[j]] for j in range(3)] for i in range(3)]

    print("\nEigenvalues:", [f"{l:+.6f}" for l in eigvals])
    print("Eigenvectors (columns of Q):")
    for row in Q:
        print("  " + "  ".join(f"{x:+.4f}" for x in row))

    print("\nVerification A v = lambda v:")
    for j, lam in enumerate(eigvals):
        v = [Q[i][j] for i in range(3)]
        Av = [sum(A[i][k] * v[k] for k in range(3)) for i in range(3)]
        residual = math.sqrt(sum((Av[i] - lam * v[i]) ** 2 for i in range(3)))
        print(f"  j={j}: lambda={lam:+.6f}  ||Av - lambda v|| = {residual:.2e}")

    L = [[eigvals[i] if i == j else 0.0 for j in range(3)] for i in range(3)]
    Qt = [[Q[j][i] for j in range(3)] for i in range(3)]
    A_rec = matmul(matmul(Q, L), Qt)
    err = math.sqrt(sum((A[i][j] - A_rec[i][j]) ** 2 for i in range(3) for j in range(3)))
    print("\nReconstruction Q Lambda Q^T:")
    for row in A_rec:
        print("  " + "  ".join(f"{x:+.4f}" for x in row))
    print(f"||A - Q Lambda Q^T||_F = {err:.2e}")
    QtQ = matmul(Qt, Q)
    ortho = math.sqrt(sum((QtQ[i][j] - float(i == j)) ** 2 for i in range(3) for j in range(3)))
    print(f"Orthogonality ||Q^T Q - I||_F = {ortho:.2e}")


if __name__ == "__main__":
    main()
