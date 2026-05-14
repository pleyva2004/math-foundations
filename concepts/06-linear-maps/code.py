"""Linear Maps and Matrices — concept 06-linear-maps.

Pure-stdlib demonstration of:
  * a 3x3 matrix as a linear map R^3 -> R^3,
  * its kernel (null space) and rank via Gaussian elimination,
  * the rank-nullity identity rank(A) + dim(null(A)) == 3,
  * composition of linear maps as matrix multiplication.
"""

from fractions import Fraction


def matmul(A, B):
    m, n = len(A), len(B[0])
    p = len(B)
    return [[sum(A[i][k] * B[k][j] for k in range(p)) for j in range(n)] for i in range(m)]


def matvec(A, v):
    return [sum(A[i][k] * v[k] for k in range(len(v))) for i in range(len(A))]


def rref_with_rank(M):
    """Reduced row-echelon form via Gaussian elimination, plus rank."""
    A = [row[:] for row in M]
    rows, cols = len(A), len(A[0])
    r = 0
    pivots = []
    for c in range(cols):
        pivot = None
        for i in range(r, rows):
            if A[i][c] != 0:
                pivot = i
                break
        if pivot is None:
            continue
        A[r], A[pivot] = A[pivot], A[r]
        lead = A[r][c]
        A[r] = [x / lead for x in A[r]]
        for i in range(rows):
            if i != r and A[i][c] != 0:
                factor = A[i][c]
                A[i] = [a - factor * b for a, b in zip(A[i], A[r])]
        pivots.append(c)
        r += 1
    return A, pivots


def null_space_basis(M):
    """Basis vectors for ker(M) (columns) via RREF + free variables."""
    rref, pivots = rref_with_rank(M)
    n = len(M[0])
    free = [c for c in range(n) if c not in pivots]
    basis = []
    for f in free:
        v = [Fraction(0)] * n
        v[f] = Fraction(1)
        for r, p in enumerate(pivots):
            v[p] = -rref[r][f]
        basis.append(v)
    return basis


def main():
    print("Linear Maps and Matrices (concept 06-linear-maps)")
    print("=" * 60)

    A = [[Fraction(1), Fraction(2), Fraction(3)],
         [Fraction(1), Fraction(2), Fraction(3)],
         [Fraction(4), Fraction(5), Fraction(6)]]
    print("A = [[1,2,3], [1,2,3], [4,5,6]]")

    _, pivots = rref_with_rank(A)
    rank = len(pivots)
    K = null_space_basis(A)
    nullity = len(K)
    print(f"rank(A)    = {rank}")
    print(f"nullity    = {nullity}")
    print(f"kernel basis: {[[float(x) for x in v] for v in K]}")

    assert rank + nullity == 3, "rank-nullity failed"
    print(f"rank + nullity = {rank} + {nullity} = 3 = dim(domain). OK")

    # A @ k must be zero for every kernel basis vector.
    for v in K:
        Av = matvec(A, v)
        assert all(x == 0 for x in Av), f"A @ kernel vector should be 0, got {Av}"
    print("A annihilates every kernel basis vector. OK")

    # Composition: (T o S)(x) == (T @ S) @ x.
    S = [[Fraction(2), Fraction(0), Fraction(1)],
         [Fraction(0), Fraction(1), Fraction(-1)],
         [Fraction(1), Fraction(1), Fraction(0)]]
    T = [[Fraction(1), Fraction(2), Fraction(0)],
         [Fraction(-1), Fraction(0), Fraction(1)],
         [Fraction(0), Fraction(1), Fraction(2)]]
    TS = matmul(T, S)
    x = [Fraction(3), Fraction(-1), Fraction(2)]
    lhs = matvec(T, matvec(S, x))
    rhs = matvec(TS, x)
    assert lhs == rhs, f"composition mismatch: {lhs} vs {rhs}"
    print(f"T(S(x)) = (T@S)(x) = {[int(v) for v in rhs]}. OK")
    print("Composition of linear maps matches matrix multiplication.")


if __name__ == "__main__":
    main()
