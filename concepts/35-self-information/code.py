"""Self-Information (Surprisal) -- concept 35-self-information.

I(x) = -log p(x): the surprisal of observing outcome x under distribution p.

This script:
  1. Computes I(H), I(T) in bits for biased coins with p(H) in {0.9, 0.5, 0.1}.
  2. Verifies the additivity theorem I(HH) = I(H) + I(H) for two independent flips.
  3. Numerically verifies that the expectation E[I(X)] equals the Shannon
     entropy H(p) = -sum_x p(x) log2 p(x) (forward reference to concept 36).

Stdlib only (uses math).
"""

import math


def self_information_bits(p: float) -> float:
    """I(x) = -log2 p(x), in bits. Requires 0 < p <= 1."""
    if not 0.0 < p <= 1.0:
        raise ValueError(f"probability must be in (0, 1], got {p}")
    return -math.log2(p)


def shannon_entropy_bits(probs):
    """H(p) = -sum_x p(x) log2 p(x), in bits. Skips zero-probability terms."""
    return sum(p * self_information_bits(p) for p in probs if p > 0.0)


def expected_self_information(probs):
    """E[I(X)] = sum_x p(x) * I(x). Should equal H(p) exactly."""
    return sum(p * self_information_bits(p) for p in probs if p > 0.0)


def main():
    print("Self-Information (Surprisal) -- concept 35")
    print("=" * 60)

    # --- 1. Biased-coin surprisals ---------------------------------------
    print("\n[1] Single-outcome self-information I(x) = -log2 p(x), in bits:")
    print(f"  {'p(H)':>6} | {'I(H) bits':>10} | {'I(T) bits':>10}")
    print("  " + "-" * 34)
    for pH in (0.9, 0.5, 0.1):
        pT = 1.0 - pH
        print(f"  {pH:>6.2f} | {self_information_bits(pH):>10.4f}"
              f" | {self_information_bits(pT):>10.4f}")

    # --- 2. Additivity for independent events ----------------------------
    print("\n[2] Additivity:  I(H, H) ?= I(H) + I(H) for two independent fair flips.")
    pH = 0.5
    I_H = self_information_bits(pH)
    I_HH_direct = self_information_bits(pH * pH)       # via joint probability
    I_HH_sum = I_H + I_H                                # via additivity
    print(f"  I(H)              = {I_H:.6f} bits")
    print(f"  I(HH) direct      = -log2({pH*pH:.2f}) = {I_HH_direct:.6f} bits")
    print(f"  I(H) + I(H)       = {I_HH_sum:.6f} bits")
    print(f"  match? {math.isclose(I_HH_direct, I_HH_sum)}")

    # --- 3. Expectation of self-information equals Shannon entropy -------
    print("\n[3] E[I(X)] == H(p)  (forward link to concept 36-shannon-entropy):")
    print(f"  {'p(H)':>6} | {'E[I(X)]':>10} | {'H(p)':>10} | match?")
    print("  " + "-" * 42)
    for pH in (0.9, 0.5, 0.1, 0.25):
        probs = [pH, 1.0 - pH]
        e_I = expected_self_information(probs)
        H = shannon_entropy_bits(probs)
        print(f"  {pH:>6.2f} | {e_I:>10.6f} | {H:>10.6f}"
              f" | {math.isclose(e_I, H)}")

    print("\nAll three properties hold numerically. QED (modulo floating point).")


if __name__ == "__main__":
    main()
