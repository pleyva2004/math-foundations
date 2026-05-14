"""Conditional Probability — concept 20-conditional-probability.

Two demos:
  (1) Bayes' theorem on a medical test (prior 0.01, sensitivity 0.99,
      specificity 0.95) — analytic formula and Monte Carlo cross-check.
  (2) Monty Hall: 10,000 trials, switching wins ~2/3 of the time.

Stdlib only.
"""

import random


def bayes_medical(prior=0.01, sens=0.99, spec=0.95):
    """Analytic posterior P(disease | positive)."""
    p_pos = sens * prior + (1 - spec) * (1 - prior)
    return sens * prior / p_pos


def bayes_medical_mc(prior=0.01, sens=0.99, spec=0.95, n=200_000, seed=0):
    """Monte Carlo posterior."""
    rng = random.Random(seed)
    pos = 0
    pos_and_sick = 0
    for _ in range(n):
        sick = rng.random() < prior
        positive = rng.random() < (sens if sick else 1 - spec)
        if positive:
            pos += 1
            if sick:
                pos_and_sick += 1
    return pos_and_sick / pos if pos else float("nan")


def monty_hall(n_trials=10_000, seed=1):
    """Return (P(win | stay), P(win | switch))."""
    rng = random.Random(seed)
    stay_wins = 0
    switch_wins = 0
    for _ in range(n_trials):
        car = rng.randrange(3)
        pick = rng.randrange(3)
        # Host opens a goat door != pick, != car.
        candidates = [d for d in range(3) if d != pick and d != car]
        host_opens = rng.choice(candidates)
        switch_to = next(d for d in range(3) if d != pick and d != host_opens)
        if pick == car:
            stay_wins += 1
        if switch_to == car:
            switch_wins += 1
    return stay_wins / n_trials, switch_wins / n_trials


def main():
    print("Conditional Probability (concept 20)")
    print("=" * 56)
    analytic = bayes_medical()
    mc = bayes_medical_mc()
    print("\n[Bayes — medical test]")
    print(f"  P(sick | positive)  analytic = {analytic:.6f}")
    print(f"  P(sick | positive)  Monte Carlo = {mc:.6f}")
    print("  Intuition: prior 1% dominates 99% sensitivity ->")
    print("  the posterior is only ~16.7%. Most positives are false.")

    # (2) Monty Hall.
    p_stay, p_switch = monty_hall()
    print("\n[Monty Hall — 10,000 trials]")
    print(f"  P(win | stay)   = {p_stay:.4f}  (theory 1/3 ≈ 0.3333)")
    print(f"  P(win | switch) = {p_switch:.4f}  (theory 2/3 ≈ 0.6667)")

    # Theory check on Bayes.
    assert abs(analytic - 0.16666666) < 1e-3, "Bayes formula sanity"
    assert abs(mc - analytic) < 0.01, "Monte Carlo within tolerance"
    assert abs(p_switch - 2 / 3) < 0.02, "Monty Hall within tolerance"
    print("\nAll sanity checks passed.")


if __name__ == "__main__":
    main()
