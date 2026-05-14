"""Vector Spaces - concept 05-vector-spaces.

Demonstrates: (1) building a basis of R^3, (2) checking linear
independence via the determinant, (3) expressing a vector as a linear
combination of basis elements (solving a 3x3 system), (4) the
dimension theorem (two bases of R^3 each have size 3).
"""

def det3(M):
    a, b, c = M[0]; d, e, f = M[1]; g, h, i = M[2]
    return a * (e * i - f * h) - b * (d * i - f * g) + c * (d * h - e * g)


def solve3(A, y):
    """Solve A x = y for a 3x3 system via Gaussian elimination."""
    M = [row[:] + [y[k]] for k, row in enumerate(A)]
    for i in range(3):
        p = max(range(i, 3), key=lambda r: abs(M[r][i]))
        M[i], M[p] = M[p], M[i]
        if abs(M[i][i]) < 1e-12:
            raise ValueError("singular: linearly dependent")
        for j in range(i + 1, 3):
            f = M[j][i] / M[i][i]
            for k in range(i, 4):
                M[j][k] -= f * M[i][k]
    x = [0.0, 0.0, 0.0]
    for i in (2, 1, 0):
        x[i] = (M[i][3] - sum(M[i][k] * x[k] for k in range(i + 1, 3))) / M[i][i]
    return x


def is_basis_R3(vs):
    return len(vs) == 3 and all(len(v) == 3 for v in vs) and abs(det3(vs)) > 1e-12


def coordinates(basis, v):
    """Return alpha with sum_i alpha_i * basis[i] == v (basis rows = vectors)."""
    BT = [[basis[i][k] for i in range(3)] for k in range(3)]
    return solve3(BT, v)


def combo(basis, a):
    return [sum(a[i] * basis[i][k] for i in range(len(basis))) for k in range(3)]


def main():
    print("Vector Spaces (concept 05-vector-spaces)")
    print("=" * 60)
    standard = [[1.0, 0, 0], [0, 1.0, 0], [0, 0, 1.0]]
    nonstd = [[1.0, 1, 0], [0, 1.0, 1], [1, 0, 1.0]]
    print(f"Standard det = {det3(standard):.4f}; basis? {is_basis_R3(standard)}")
    print(f"Non-std  det = {det3(nonstd):.4f}; basis? {is_basis_R3(nonstd)}")
    assert len(standard) == len(nonstd) == 3
    print("Dimension theorem: both bases have cardinality 3. [verified]")

    v = [2.0, 5.0, 7.0]
    a_std = coordinates(standard, v)
    a_non = coordinates(nonstd, v)
    print(f"\nv = {v}")
    print(f"  coords (standard):     {[round(x, 4) for x in a_std]}")
    print(f"  coords (non-standard): {[round(x, 4) for x in a_non]}")
    for a, B in [(a_std, standard), (a_non, nonstd)]:
        r = combo(B, a)
        assert all(abs(r[k] - v[k]) < 1e-9 for k in range(3))
    print("  Reconstructions match v. [verified]")

    dep = [[1.0, 0, 0], [2.0, 0, 0], [0, 1.0, 0]]
    assert not is_basis_R3(dep)
    print(f"Dependent set det = {det3(dep):.4f}; basis? {is_basis_R3(dep)}")
    print("All checks passed.")


if __name__ == "__main__":
    main()
