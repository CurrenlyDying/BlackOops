"""
TEST SUITE 2: Alignment & Recursive Bit Simulations
=====================================================
Explores the "timing attack" and alignment conditions for
information merging with the recursive loop (singularity).

Key questions:
  1. Can two non-recursive bits align to create a recursive loop?
  2. What's the probability distribution of alignment attempts?
  3. Is there a critical mass/information density where alignment
     becomes inevitable vs impossible?
  4. Phase transition behavior at the Planck-mass boundary

Note: These are MONTE CARLO simulations — adjust N_SAMPLES for compute.
Default is conservative for fast runs. Crank up on Colab/H100.
"""

import numpy as np
import json
import time
from constants import (
    EncoderState, G, c, hbar, k_B, pi,
    l_p, t_p, m_p, E_p, T_p, A_p, M_sun,
    solar_mass_bh, planck_mass_bh, custom_bh
)

# =============================================================================
# SIMULATION PARAMETERS — tweak these for compute budget
# =============================================================================
N_SAMPLES = 100_000   # Monte Carlo samples (increase on Colab)
SEED = 42


# =========================================================================
# SIM 1: Random Walk Alignment Model
# =========================================================================
def sim_alignment_random_walk(N_encoder_bits, n_trials=N_SAMPLES, max_steps=None):
    """
    Model infalling information as a random walk on the Gray code cycle
    of the encoder (horizon). Information "aligns" with the recursive
    loop when it reaches position 0 (the singularity mapping).
    
    Gray code constraint: each step flips exactly 1 bit randomly.
    On an N-position encoder, this is a random walk on Z_N.
    
    Returns distribution of steps-to-alignment.
    
    Args:
        N_encoder_bits: Number of encoder positions (horizon bits)
        n_trials: Monte Carlo trials
        max_steps: Cutoff (default: 10*N for efficiency)
    """
    if max_steps is None:
        max_steps = min(int(10 * N_encoder_bits), 10_000_000)

    N = int(min(N_encoder_bits, 1e8))  # Cap for simulation
    rng = np.random.default_rng(SEED)

    steps_to_align = []
    aligned_count = 0

    for trial in range(n_trials):
        # Start at random position (infalling info enters at random phase)
        pos = rng.integers(1, max(N, 2))  # avoid starting at 0
        
        for step in range(max_steps):
            # Gray code step: flip one bit → move ±1 on the cycle
            # (In reflected Gray code, adjacent positions differ by 1 bit)
            direction = rng.choice([-1, 1])
            pos = (pos + direction) % N
            
            if pos == 0:
                steps_to_align.append(step + 1)
                aligned_count += 1
                break

    mean_steps = np.mean(steps_to_align) if steps_to_align else float('inf')
    median_steps = np.median(steps_to_align) if steps_to_align else float('inf')
    
    # Theoretical: 1D random walk return time on Z_N is N²/2
    theoretical_mean = N**2 / 2.0

    return {
        "N_encoder": N,
        "n_trials": n_trials,
        "max_steps": max_steps,
        "aligned_count": aligned_count,
        "alignment_rate": aligned_count / n_trials,
        "mean_steps": mean_steps,
        "median_steps": median_steps,
        "theoretical_mean_steps": theoretical_mean,
        "ratio_actual_over_theory": mean_steps / theoretical_mean if theoretical_mean > 0 else float('inf'),
        "std_steps": np.std(steps_to_align) if steps_to_align else float('inf'),
    }


def test_alignment_scaling():
    """
    Run alignment simulation for increasing encoder sizes.
    Check if mean alignment time scales as N² (random walk on cycle).
    
    THIS IS THE KEY TEST: if alignment time ∝ N², then
    t_align = N² × t_p, matching the evaporation scaling t_evap ∝ M³ ∝ N^1.5.
    
    Wait — that's N² vs N^1.5. The gap matters! It means alignment is HARDER
    than evaporation, consistent with info staying on the horizon.
    
    NOTE: For large N, random walk simulation is O(N²) per trial.
    We simulate up to N=500 and extrapolate via power law fit.
    Increase SIM_MAX_N for Colab/H100.
    """
    print("\n" + "#"*70)
    print("# SIM 1: Alignment Random Walk — Scaling Test")
    print("#"*70 + "\n")

    # Simulatable range (increase SIM_MAX_N on better hardware)
    SIM_MAX_N = 200
    N_values = [10, 20, 50, 100, 200]
    results = []

    print(f"{'N encoder':>12} {'Aligned':>10} {'Mean steps':>14} {'Theory N²/2':>14} {'Ratio':>10}")
    print("-" * 65)

    for N in N_values:
        if N > SIM_MAX_N:
            break
        trials = min(N_SAMPLES, max(500, 50_000 // max(N, 1)))
        max_steps = min(N * N * 5, 2_000_000)
        r = sim_alignment_random_walk(N, n_trials=trials, max_steps=max_steps)
        results.append(r)
        print(f"{N:>12} {r['aligned_count']:>10}/{trials} {r['mean_steps']:>14.1f} {r['theoretical_mean_steps']:>14.1f} {r['ratio_actual_over_theory']:>10.3f}")

    # Fit scaling: mean_steps ∝ N^α
    valid = [(r["N_encoder"], r["mean_steps"]) for r in results if r["mean_steps"] < float('inf') and r["aligned_count"] > 10]
    if len(valid) >= 3:
        Ns, Ss = zip(*valid)
        fit = np.polyfit(np.log10(Ns), np.log10(Ss), 1)
        print(f"\n  SCALING FIT: mean_alignment_steps ∝ N^{fit[0]:.3f}")
        print(f"  Expected for random walk on Z_N: N^2.0")
        print(f"  Compare to evaporation: t_evap ∝ N^1.5")
        if fit[0] > 1.5:
            print(f"  → Alignment is HARDER than evaporation by factor N^{fit[0]-1.5:.2f}")
            print(f"    This supports: info encodes on horizon, doesn't reach singularity")
    
    return results


# =========================================================================
# SIM 2: Two-Body Alignment ("Timing Attack")
# =========================================================================
def sim_two_body_alignment(N, n_trials=N_SAMPLES):
    """
    Two non-recursive bits trying to align with each other to form
    a recursive loop. Both are random-walking on Z_N.
    
    They "merge" when they occupy the same position.
    This is equivalent to ONE particle random-walking (relative motion),
    so the return time should still be ~N².
    
    The question: is two-body alignment easier or harder than
    single-body alignment with the fixed singularity?
    """
    rng = np.random.default_rng(SEED + 1)
    max_steps = min(N * N * 3, 500_000)
    
    steps_to_merge = []
    merged = 0

    for trial in range(n_trials):
        # Two particles at random positions
        pos_a = rng.integers(0, N)
        pos_b = rng.integers(0, N)
        while pos_a == pos_b:
            pos_b = rng.integers(0, N)

        for step in range(max_steps):
            # Both take Gray code steps independently
            pos_a = (pos_a + rng.choice([-1, 1])) % N
            pos_b = (pos_b + rng.choice([-1, 1])) % N

            if pos_a == pos_b:
                steps_to_merge.append(step + 1)
                merged += 1
                break

    mean_s = np.mean(steps_to_merge) if steps_to_merge else float('inf')

    return {
        "N": N,
        "n_trials": n_trials,
        "merged_count": merged,
        "merge_rate": merged / n_trials,
        "mean_steps": mean_s,
        "theoretical_mean": N**2 / 2.0,  # Same as single particle (relative coordinates)
        "ratio": mean_s / (N**2 / 2.0) if N > 0 else float('inf'),
    }


def test_two_body():
    """Test whether two-body collision is equivalent to one-body return."""
    print("\n" + "#"*70)
    print("# SIM 2: Two-Body Alignment ('Timing Attack')")
    print("#"*70 + "\n")

    N_values = [10, 20, 50]
    results_1body = []
    results_2body = []

    print(f"{'N':>8} {'1-body mean':>14} {'2-body mean':>14} {'Ratio 2/1':>12} {'Theory':>10}")
    print("-" * 62)

    for N in N_values:
        trials = min(N_SAMPLES, max(200, 10_000 // N))
        r1 = sim_alignment_random_walk(N, n_trials=trials, max_steps=min(N*N*3, 500_000))
        r2 = sim_two_body_alignment(N, n_trials=trials)
        results_1body.append(r1)
        results_2body.append(r2)
        
        ratio = r2["mean_steps"] / r1["mean_steps"] if r1["mean_steps"] > 0 else float('inf')
        print(f"{N:>8} {r1['mean_steps']:>14.1f} {r2['mean_steps']:>14.1f} {ratio:>12.3f} {'~1.0':>10}")

    print("\n  If ratio ≈ 1: two-body alignment is equivalent to one-body return")
    print("  (relative coordinate reduction works → your insight was correct!)")
    print("  The 'timing attack' doesn't help — it's the same random walk.")

    return {"one_body": results_1body, "two_body": results_2body}


# =========================================================================
# SIM 3: Phase Transition at Planck Mass
# =========================================================================
def test_phase_transition():
    """
    Sweep mass from sub-Planck to super-Planck and look for
    a phase transition in encoder behavior.
    
    Sub-Planck: N < 1 bit (meaningless encoder → not a black hole)
    Planck:     N ≈ 1 bit (the oscillation zone)
    Super-Planck: N >> 1 bit (stable black hole)
    
    We compute an "encoder quality" metric:
    Q = min(N, 1/N) which peaks at N=1 (maximum ambiguity).
    """
    print("\n" + "#"*70)
    print("# SIM 3: Phase Transition at Planck Mass")
    print("#"*70 + "\n")

    mass_ratios = np.logspace(-3, 6, 200)  # M/M_planck from 0.001 to 10^6
    
    results = []
    
    print(f"{'M/M_p':>10} {'N bits':>12} {'T_H/T_p':>12} {'t_evap/t_p':>12} {'Q (ambiguity)':>14}")
    print("-" * 65)

    for ratio in mass_ratios:
        mass = ratio * m_p
        enc = EncoderState(mass)
        N = max(enc.n_bits, 1e-100)
        
        # Ambiguity metric: peaks at N=1
        Q = min(N, 1.0/N) if N > 0 else 0
        
        T_ratio = enc.hawking_temperature / T_p if T_p > 0 else 0
        t_ratio = enc.evaporation_time / t_p if t_p > 0 else 0
        
        results.append({
            "mass_ratio": ratio,
            "N_bits": N,
            "T_ratio": T_ratio,
            "t_ratio": t_ratio,
            "ambiguity_Q": Q
        })

    # Print subset
    for r in results[::20]:
        print(f"{r['mass_ratio']:>10.3e} {r['N_bits']:>12.3e} {r['T_ratio']:>12.3e} {r['t_ratio']:>12.3e} {r['ambiguity_Q']:>14.3e}")

    # Find peak ambiguity
    Q_vals = [r["ambiguity_Q"] for r in results]
    peak_idx = np.argmax(Q_vals)
    peak = results[peak_idx]
    print(f"\n  PEAK AMBIGUITY at M/M_p = {peak['mass_ratio']:.3f}")
    print(f"  N_bits at peak = {peak['N_bits']:.3f}")
    print(f"  Q_max = {peak['ambiguity_Q']:.6f}")
    print(f"  → This IS the 'both black hole and not' sweet spot")
    
    # Check width of transition region (Q > 0.5)
    high_Q = [r for r in results if r["ambiguity_Q"] > 0.5]
    if high_Q:
        width_low = min(r["mass_ratio"] for r in high_Q)
        width_high = max(r["mass_ratio"] for r in high_Q)
        print(f"  Transition region (Q > 0.5): M/M_p ∈ [{width_low:.2f}, {width_high:.2f}]")
        print(f"  Width in decades: {np.log10(width_high/width_low):.2f}")

    return results


# =========================================================================
# SIM 4: Information Disappearance Audit
# =========================================================================
def test_info_conservation():
    """
    Track total information through a simulated evaporation process.
    
    Model: N-bit encoder releases bits one at a time.
    Each release involves:
      1. One bit escapes as Hawking radiation
      2. N decreases by 1
      3. Horizon shrinks
    
    Check: is total info (radiated + remaining) conserved?
    In the encoder model, it MUST be, or unitarity breaks.
    """
    print("\n" + "#"*70)
    print("# SIM 4: Information Conservation Audit")
    print("#"*70 + "\n")

    # Start with a moderate encoder
    N_start = 1000
    
    N = N_start
    bits_radiated = 0
    step = 0
    
    print(f"Starting encoder: N = {N_start} bits\n")
    print(f"{'Step':>8} {'N remaining':>14} {'Bits radiated':>14} {'Total':>10} {'Conserved?':>12}")
    print("-" * 62)

    conservation_ok = True
    log_interval = N_start // 10

    while N > 0:
        total = N + bits_radiated
        conserved = "✓" if total == N_start else "✗ VIOLATION"
        if total != N_start:
            conservation_ok = False
        
        if step % log_interval == 0 or N <= 5:
            print(f"{step:>8} {N:>14} {bits_radiated:>14} {total:>10} {conserved:>12}")
        
        # Release one bit (Hawking radiation event)
        N -= 1
        bits_radiated += 1
        step += 1

    total = N + bits_radiated
    conserved = "✓" if total == N_start else "✗ VIOLATION"
    print(f"{step:>8} {N:>14} {bits_radiated:>14} {total:>10} {conserved:>12}")
    
    print(f"\n  RESULT: Information {'CONSERVED' if conservation_ok else 'VIOLATED'}")
    print(f"  Total bits in = {N_start}, Total bits out = {bits_radiated}")
    
    if conservation_ok:
        print("  → The encoder model preserves unitarity by construction")
        print("  → Information never 'disappears' — it's released holographically")
    
    return {"conserved": conservation_ok, "N_start": N_start, "bits_out": bits_radiated}


# =========================================================================
# RUN ALL
# =========================================================================
def run_all():
    start = time.time()
    results = {}
    
    results["alignment_scaling"] = test_alignment_scaling()
    results["two_body"] = test_two_body()
    results["phase_transition"] = test_phase_transition()
    results["info_conservation"] = test_info_conservation()
    
    elapsed = time.time() - start
    print(f"\n{'='*70}")
    print(f"All simulations complete in {elapsed:.1f}s")
    print(f"{'='*70}")
    
    # Save
    def convert(obj):
        if isinstance(obj, (np.floating, np.float64)):
            return float(obj)
        if isinstance(obj, (np.integer, np.int64)):
            return int(obj)
        if isinstance(obj, np.ndarray):
            return obj.tolist()
        if isinstance(obj, dict):
            return {k: convert(v) for k, v in obj.items()}
        if isinstance(obj, list):
            return [convert(i) for i in obj]
        return obj
    
    with open("results_alignment_sims.json", 'w') as f:
        json.dump(convert(results), f, indent=2, default=str)
    
    print(f"Results saved to results_alignment_sims.json")
    return results


if __name__ == "__main__":
    run_all()
