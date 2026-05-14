"""Cross-Entropy — concept 37-cross-entropy.

H(p, q) = -E_p[log q]; the average code-length when using q to encode
samples drawn from p. Verifies Gibbs (H(p,q) >= H(p)) and the
decomposition H(p,q) = H(p) + KL(p||q). Stdlib only.
"""

from math import log2


def entropy(p):
    return -sum(pi * log2(pi) for pi in p if pi > 0.0)


def cross_entropy(p, q):
    t = 0.0
    for pi, qi in zip(p, q):
        if pi == 0.0:
            continue
        if qi == 0.0:
            return float("inf")
        t -= pi * log2(qi)
    return t


def kl_divergence(p, q):
    t = 0.0
    for pi, qi in zip(p, q):
        if pi == 0.0:
            continue
        if qi == 0.0:
            return float("inf")
        t += pi * log2(pi / qi)
    return t


def main():
    print("Cross-Entropy (concept 37-cross-entropy)")
    print("=" * 60)

    pairs = [
        ([0.5, 0.5], [0.5, 0.5]),       # q = p, equality case
        ([0.5, 0.5], [0.9, 0.1]),       # worked example from README
        ([0.7, 0.3], [0.3, 0.7]),       # asymmetric mismatch
        ([0.25, 0.25, 0.25, 0.25], [0.1, 0.2, 0.3, 0.4]),
        ([1.0, 0.0], [0.5, 0.5]),       # degenerate p
    ]
    print(f"\n{'p':<28}{'q':<28}{'H(p)':>8}{'H(p,q)':>10}{'KL':>10}")
    print("-" * 84)
    for p, q in pairs:
        Hp = entropy(p)
        Hpq = cross_entropy(p, q)
        Dkl = kl_divergence(p, q)
        gibbs_ok = Hpq + 1e-12 >= Hp
        decomp_ok = abs((Hpq - Hp) - Dkl) < 1e-9
        assert gibbs_ok, f"Gibbs violated for p={p}, q={q}"
        assert decomp_ok, f"Decomposition broken for p={p}, q={q}"
        print(f"{str(p):<28}{str(q):<28}{Hp:>8.4f}{Hpq:>10.4f}{Dkl:>10.4f}")
    print("\nAll Gibbs inequalities and decomposition identities verified.")

    print("\n--- 5-class softmax classification example ---")
    truth = [1.0, 0.0, 0.0, 0.0, 0.0]
    pred = [0.6, 0.1, 0.1, 0.1, 0.1]
    ce = cross_entropy(truth, pred)
    print(f"  ground truth p = {truth}")
    print(f"  prediction   q = {pred}")
    print(f"  H(p, q) = -log2(0.6) = {ce:.4f} bits")
    print(f"  (matches -log2(q[true_class]) = {-log2(pred[0]):.4f})")


if __name__ == "__main__":
    main()
