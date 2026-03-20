"""
TEST SUITE 1: Core Encoder Model Validation
=============================================
Tests the fundamental predictions of the Gray Code Universe model
against known black hole thermodynamics.

Tests:
  1. Hawking evaporation as encoder unwinding → suppression factor
  2. Planck-mass sweet spot (1-bit encoder)
  3. Alignment probability vs Hawking radiation rate scaling
  4. Gray code traversal overhead hypothesis for suppression factor
  5. Mass spectrum sweep — how encoder properties scale
"""

import numpy as np
import json
import sys
from constants import (
    EncoderState, G, c, hbar, k_B, pi,
    l_p, t_p, m_p, E_p, T_p, A_p, M_sun,
    solar_mass_bh, planck_mass_bh, sgr_a_star, m87_star, custom_bh
)


def separator(title):
    print(f"\n{'#'*70}")
    print(f"# {title}")
    print(f"{'#'*70}\n")


# =========================================================================
# TEST 1: Hawking Evaporation as Encoder Unwinding
# =========================================================================
def test_evaporation_suppression():
    """
    If one encoder bit releases per Planck time, evaporation would take:
        t_naive = N * t_p
    Actual Hawking evaporation:
        t_evap = 5120π G² M³ / (ℏc⁴)
    
    Suppression factor S = t_evap / t_naive tells us how much "overhead"
    the Gray code constraint imposes on information release.
    """
    separator("TEST 1: Evaporation Suppression Factor")

    results = []
    test_masses = [
        ("Planck mass", m_p),
        ("Mountain (~10¹² kg)", 1e12),
        ("Moon mass", 7.342e22),
        ("Earth mass", 5.972e24),
        ("Solar mass", M_sun),
        ("Sgr A*", 4e6 * M_sun),
        ("M87*", 6.5e9 * M_sun),
    ]

    print(f"{'Label':<25} {'N bits':>12} {'t_naive [s]':>14} {'t_evap [s]':>14} {'Suppression':>14} {'log10(S)':>10}")
    print("-" * 95)

    for label, mass in test_masses:
        enc = EncoderState(mass, label)
        N = enc.n_bits
        t_naive = N * t_p
        t_evap = enc.evaporation_time

        if t_naive > 0:
            suppression = t_evap / t_naive
            log_s = np.log10(suppression) if suppression > 0 else float('nan')
        else:
            suppression = float('inf')
            log_s = float('inf')

        print(f"{label:<25} {N:>12.3e} {t_naive:>14.3e} {t_evap:>14.3e} {suppression:>14.3e} {log_s:>10.2f}")
        results.append({
            "label": label,
            "mass_kg": mass,
            "N_bits": N,
            "t_naive_s": t_naive,
            "t_evap_s": t_evap,
            "suppression_factor": suppression,
            "log10_suppression": log_s
        })

    # Check if suppression scales as a power law of N
    N_vals = np.array([r["N_bits"] for r in results if r["N_bits"] > 1])
    S_vals = np.array([r["suppression_factor"] for r in results if r["N_bits"] > 1])

    if len(N_vals) >= 2:
        # Fit log(S) = a * log(N) + b
        log_N = np.log10(N_vals)
        log_S = np.log10(S_vals)
        coeffs = np.polyfit(log_N, log_S, 1)
        print(f"\n  Power law fit: S ∝ N^{coeffs[0]:.4f}")
        print(f"  (If Gray code traversal: expect S ∝ N^1.0, i.e. t_evap ∝ N²)")
        print(f"  (If combinatorial overhead: expect S ∝ N^0.5, i.e. t_evap ∝ N^1.5)")
        results.append({
            "analysis": "power_law_fit",
            "exponent": coeffs[0],
            "intercept": coeffs[1]
        })

    return results


# =========================================================================
# TEST 2: Planck-Mass Sweet Spot
# =========================================================================
def test_planck_sweet_spot():
    """
    At M = M_planck:
      - Schwarzschild radius ~ l_p
      - Horizon area ~ l_p²
      - Encoder has ~1 bit
      - Hawking temperature ~ T_planck
      - Evaporation time ~ t_planck
      - One photon emitted → encoder self-destructs
    
    This is the "oscillates between black hole and not black hole" regime.
    """
    separator("TEST 2: Planck-Mass Sweet Spot")

    enc = planck_mass_bh()
    print(enc.summary())

    # Ratios to Planck units (should all be ~O(1))
    r_ratio = enc.schwarzschild_radius / l_p
    A_ratio = enc.horizon_area / A_p
    T_ratio = enc.hawking_temperature / T_p
    t_ratio = enc.evaporation_time / t_p

    print(f"  PLANCK UNIT RATIOS (should be ~O(1) for 1-bit encoder):")
    print(f"    r_s / l_p          = {r_ratio:.4f}")
    print(f"    A / l_p²           = {A_ratio:.4f}")
    print(f"    T_H / T_planck     = {T_ratio:.4f}")
    print(f"    t_evap / t_planck  = {t_ratio:.4f}")
    print(f"    N_bits             = {enc.n_bits:.4f}")

    # Energy of one Hawking photon at T_H
    E_photon = k_B * enc.hawking_temperature
    E_ratio = E_photon / E_p
    print(f"    E_photon / E_planck = {E_ratio:.4f}")

    # Key check: does the encoder self-destruct in ~1 tick?
    print(f"\n  SELF-DESTRUCTION CHECK:")
    print(f"    If 1-bit encoder emits 1 photon of energy E_p...")
    print(f"    Photon energy:  {E_photon:.3e} J")
    print(f"    BH rest energy: {enc.mass_kg * c**2:.3e} J")
    print(f"    Ratio (should be ~1): {E_photon / (enc.mass_kg * c**2):.4f}")

    return {
        "r_s_over_l_p": r_ratio,
        "A_over_A_p": A_ratio,
        "T_over_T_p": T_ratio,
        "t_evap_over_t_p": t_ratio,
        "N_bits": enc.n_bits,
        "E_photon_over_E_p": E_ratio,
        "self_destruct_ratio": E_photon / (enc.mass_kg * c**2)
    }


# =========================================================================
# TEST 3: Alignment Probability vs Hawking Rate Scaling
# =========================================================================
def test_alignment_vs_hawking():
    """
    Alignment probability:  P_align ~ 1/N  per Planck time
    Hawking bit rate:       R_H ∝ 1/M² ∝ 1/N  (since N ∝ M²)
    
    If these scale identically, the encoder model is thermodynamically
    consistent. The GAP between them reveals the Gray code overhead.
    """
    separator("TEST 3: Alignment vs Hawking Rate Scaling")

    masses = np.logspace(np.log10(m_p), np.log10(1e10 * M_sun), 50)
    
    print(f"{'Mass [kg]':>12} {'N bits':>12} {'P_align':>14} {'R_H [bit/t_p]':>14} {'Ratio R/P':>12} {'log10(R/P)':>12}")
    print("-" * 82)

    log_N_list = []
    log_P_list = []
    log_R_list = []
    ratio_list = []

    for mass in masses:
        enc = EncoderState(mass)
        N = enc.n_bits
        P = enc.alignment_probability
        R = enc.bits_per_planck_time

        if P > 0 and R > 0 and N > 1:
            ratio = R / P
            log_N_list.append(np.log10(N))
            log_P_list.append(np.log10(P))
            log_R_list.append(np.log10(R))
            ratio_list.append(np.log10(ratio))

    # Print a subset
    for i in range(0, len(masses), 10):
        enc = EncoderState(masses[i])
        N = enc.n_bits
        P = enc.alignment_probability
        R = enc.bits_per_planck_time
        if P > 0 and R > 0:
            ratio = R / P
            print(f"{masses[i]:>12.3e} {N:>12.3e} {P:>14.3e} {R:>14.3e} {ratio:>12.3e} {np.log10(ratio):>12.2f}")

    # Fit scaling relations
    log_N = np.array(log_N_list)
    log_P = np.array(log_P_list)
    log_R = np.array(log_R_list)
    log_ratio = np.array(ratio_list)

    if len(log_N) >= 3:
        fit_P = np.polyfit(log_N, log_P, 1)
        fit_R = np.polyfit(log_N, log_R, 1)
        fit_ratio = np.polyfit(log_N, log_ratio, 1)

        print(f"\n  SCALING FITS (log-log):")
        print(f"    P_align ∝ N^{fit_P[0]:.4f}   (expected: -1.0)")
        print(f"    R_hawking ∝ N^{fit_R[0]:.4f}   (expected: ~ -1.0 to -2.0)")
        print(f"    R/P ratio ∝ N^{fit_ratio[0]:.4f}")
        print(f"    → The gap exponent {fit_ratio[0]:.4f} encodes the Gray code overhead")

        return {
            "P_align_exponent": fit_P[0],
            "R_hawking_exponent": fit_R[0],
            "gap_exponent": fit_ratio[0],
            "data_points": len(log_N)
        }

    return {"error": "insufficient data points"}


# =========================================================================
# TEST 4: Gray Code Traversal Overhead Hypothesis
# =========================================================================
def test_gray_code_overhead():
    """
    HYPOTHESIS: The suppression factor comes from Gray code traversal cost.
    
    In reflected Gray code with n bits:
    - Full cycle = 2^n steps
    - To change bit k, you must cycle through all lower bits
    - Average flip cost for bit k: 2^(k-1) steps
    - Total cost to flip all n bits once each: 2^n - 1 ≈ N
    
    But to fully "unwind" the encoder (release all N bits of information),
    you might need to traverse the full Gray code cycle for each bit
    being released, giving:
        t_evap ~ N × (average_traversal_cost) × t_p
    
    We test several overhead models against the actual suppression factor.
    """
    separator("TEST 4: Gray Code Traversal Overhead Models")

    test_masses = [
        ("10¹² kg", 1e12),
        ("Earth", 5.972e24),
        ("Solar", M_sun),
        ("10 M☉", 10 * M_sun),
        ("Sgr A*", 4e6 * M_sun),
    ]

    print("Testing which overhead model O(N) matches: t_evap = N × O(N) × t_p\n")
    print(f"{'Label':<15} {'N bits':>12} {'O_actual':>12} {'√N':>12} {'N':>12} {'N·ln(N)':>12} {'N²':>12}")
    print("-" * 82)

    overhead_data = []

    for label, mass in test_masses:
        enc = EncoderState(mass, label)
        N = enc.n_bits
        t_evap = enc.evaporation_time
        
        # Actual overhead: t_evap = N * O * t_p → O = t_evap / (N * t_p)
        O_actual = t_evap / (N * t_p) if N > 0 else float('inf')
        
        # Model predictions
        O_sqrt_N = np.sqrt(N)
        O_N = N
        O_NlogN = N * np.log(N)
        O_N2 = N**2

        print(f"{label:<15} {N:>12.3e} {O_actual:>12.3e} {O_sqrt_N:>12.3e} {O_N:>12.3e} {O_NlogN:>12.3e} {O_N2:>12.3e}")
        
        overhead_data.append({
            "label": label, "N": N, "O_actual": O_actual,
            "ratio_sqrtN": O_actual / O_sqrt_N if O_sqrt_N > 0 else float('inf'),
            "ratio_N": O_actual / O_N if O_N > 0 else float('inf'),
            "ratio_NlogN": O_actual / O_NlogN if O_NlogN > 0 else float('inf'),
        })

    # Check which model gives constant ratio
    print(f"\n  RATIO ANALYSIS (constant ratio = model matches):")
    print(f"  {'Label':<15} {'O/√N':>14} {'O/N':>14} {'O/(N·lnN)':>14}")
    print(f"  {'-'*60}")
    for d in overhead_data:
        print(f"  {d['label']:<15} {d['ratio_sqrtN']:>14.3e} {d['ratio_N']:>14.3e} {d['ratio_NlogN']:>14.3e}")

    # Fit: log(O_actual) vs log(N)
    N_arr = np.array([d["N"] for d in overhead_data])
    O_arr = np.array([d["O_actual"] for d in overhead_data])
    fit = np.polyfit(np.log10(N_arr), np.log10(O_arr), 1)
    print(f"\n  POWER LAW FIT: O_actual ∝ N^{fit[0]:.4f}")
    print(f"  → t_evap ∝ N^{1 + fit[0]:.4f} × t_p")
    print(f"  (Compare: Hawking formula gives t_evap ∝ M³ ∝ N^1.5)")

    return {
        "overhead_data": overhead_data,
        "power_law_exponent": fit[0],
        "total_evap_exponent": 1 + fit[0]
    }


# =========================================================================
# TEST 5: Mass Spectrum Sweep
# =========================================================================
def test_mass_spectrum():
    """
    Sweep from Planck mass to supermassive BH.
    Compute all encoder properties and check internal consistency.
    """
    separator("TEST 5: Mass Spectrum — Encoder Properties")

    masses = np.logspace(np.log10(m_p), np.log10(1e10 * M_sun), 100)

    print(f"{'log10(M/M_p)':>14} {'log10(N)':>10} {'log10(T_H/T_p)':>16} {'log10(t/t_p)':>14} {'Bits/tick':>12}")
    print("-" * 70)

    spectrum_data = []
    for mass in masses[::10]:
        enc = EncoderState(mass)
        d = {
            "log_M": np.log10(mass / m_p),
            "log_N": np.log10(max(enc.n_bits, 1e-300)),
            "log_T": np.log10(max(enc.hawking_temperature / T_p, 1e-300)),
            "log_t": np.log10(max(enc.evaporation_time / t_p, 1e-300)),
            "bits_tick": enc.bits_per_planck_time
        }
        spectrum_data.append(d)
        print(f"{d['log_M']:>14.2f} {d['log_N']:>10.2f} {d['log_T']:>16.2f} {d['log_t']:>14.2f} {d['bits_tick']:>12.3e}")

    # Verify known scaling relations
    # N ∝ M² → log(N) = 2*log(M) + const
    log_M_all = np.array([np.log10(m / m_p) for m in masses])
    log_N_all = np.array([np.log10(max(EncoderState(m).n_bits, 1e-300)) for m in masses])

    valid = log_N_all > -100
    if np.sum(valid) >= 3:
        fit = np.polyfit(log_M_all[valid], log_N_all[valid], 1)
        print(f"\n  N vs M scaling: N ∝ M^{fit[0]:.4f} (expected: 2.0)")

    return spectrum_data


# =========================================================================
# RUN ALL TESTS
# =========================================================================
def run_all():
    results = {}

    results["test1_suppression"] = test_evaporation_suppression()
    results["test2_planck_spot"] = test_planck_sweet_spot()
    results["test3_alignment"] = test_alignment_vs_hawking()
    results["test4_overhead"] = test_gray_code_overhead()
    results["test5_spectrum"] = test_mass_spectrum()

    # Save results to JSON for downstream analysis
    output_path = "results_core_tests.json"

    # Convert numpy types for JSON serialization
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

    with open(output_path, 'w') as f:
        json.dump(convert(results), f, indent=2, default=str)

    print(f"\n{'='*70}")
    print(f"Results saved to {output_path}")
    print(f"{'='*70}")

    return results


if __name__ == "__main__":
    run_all()
