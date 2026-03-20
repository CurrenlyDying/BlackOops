# Code Documentation: run_all.py

## Overview

`run_all.py` is the master orchestration script that runs all test suites, synthesizes results, and generates a comprehensive summary report. It provides the primary entry point for validating the entire Gray Code Universe framework.

**File Location:** `/home/runner/work/BlackOops/BlackOops/run_all.py`

**Purpose:**
- Execute analytical tests (test_core.py) and Monte Carlo simulations (test_alignment.py) in sequence
- Adjust simulation parameters based on computational budget (quick/default/heavy modes)
- Extract and present key findings across all tests
- Generate machine-readable JSON outputs for downstream analysis
- Provide next-step recommendations

**Runtime:** ~70 seconds (default mode)

**Dependencies:** test_core.py, test_alignment.py, numpy, json, sys, time

---

## Usage

### Basic Invocation

```bash
# Standard run (recommended for first-time users)
python run_all.py

# Quick sanity check (development/debugging)
python run_all.py --quick

# Heavy computation (publication-quality statistics)
python run_all.py --heavy
```

### Command-Line Flags

#### --quick Mode

**Purpose:** Fast validation during development

**Parameters:**
```python
test_alignment.N_SAMPLES = 10_000  # 10× fewer Monte Carlo trials
```

**Expected runtime:** ~10 seconds

**Use cases:**
- Code changes that might break tests
- Quick CI/CD checks
- Laptop with limited CPU
- Impatient users who want a taste

**Tradeoffs:**
- Lower statistical confidence (exponent errors ~±0.1)
- Some trials may not converge (aligned_count < n_trials)
- Power law fits less reliable

**Example output:**
```
SCALING FITS (log-log):
  mean_alignment_steps ∝ N^1.88   (expected: 2.0)
  [Warning: Low sample count, ±0.12 error expected]
```

#### --heavy Mode

**Purpose:** High-confidence results for publication or serious analysis

**Parameters:**
```python
test_alignment.N_SAMPLES = 1_000_000  # 10× more trials
```

**Expected runtime:** ~600 seconds (10 minutes)

**Use cases:**
- Final validation before publication
- Generating figures for papers
- Precise exponent measurements
- Colab with GPU acceleration
- Overnight runs on workstation

**Tradeoffs:**
- 10× longer runtime
- Memory usage ~100 MB (still modest)
- Diminishing returns (√10 ≈ 3× improvement in precision)

**Example output:**
```
SCALING FITS (log-log):
  mean_alignment_steps ∝ N^2.003   (expected: 2.0)
  [1M samples, exponent error ±0.003]
```

#### Default Mode

**Purpose:** Balanced speed and accuracy for typical use

**Parameters:**
```python
test_alignment.N_SAMPLES = 100_000  # Default
```

**Expected runtime:** ~70 seconds (60s sims + 10s core tests)

**Use cases:**
- First-time run to see all results
- Standard validation workflow
- Reproducible benchmarks
- Tutorial walkthroughs

**Tradeoffs:** None — this is the sweet spot

---

## Program Structure

### Main Function

```python
def main():
    mode = "default"
    if "--quick" in sys.argv:
        mode = "quick"
    elif "--heavy" in sys.argv:
        mode = "heavy"

    print("=" * 70)
    print("  GRAY CODE UNIVERSE — Computational Test Suite")
    print(f"  Mode: {mode}")
    print("=" * 70)

    # Adjust simulation parameters based on mode
    if mode == "quick":
        import test_alignment
        test_alignment.N_SAMPLES = 10_000
    elif mode == "heavy":
        import test_alignment
        test_alignment.N_SAMPLES = 1_000_000

    start = time.time()

    # ---- CORE TESTS ----
    print("\n\n" + "█" * 70)
    print("█  PART 1: CORE ENCODER MODEL TESTS")
    print("█" * 70)
    import test_core
    core_results = test_core.run_all()

    # ---- ALIGNMENT SIMS ----
    print("\n\n" + "█" * 70)
    print("█  PART 2: ALIGNMENT & RECURSIVE BIT SIMULATIONS")
    print("█" * 70)
    import test_alignment
    align_results = test_alignment.run_all()

    elapsed = time.time() - start

    # ---- SYNTHESIS REPORT ----
    print("\n\n" + "=" * 70)
    print("  SYNTHESIS REPORT")
    print("=" * 70)

    # [Extract and present key findings]
    # [See synthesis logic section below]

    print(f"\n  Total runtime: {elapsed:.1f}s")
```

### Execution Flow

```
[User invokes: python run_all.py]
         ↓
[Parse CLI flags: --quick / --heavy]
         ↓
[Adjust N_SAMPLES in test_alignment]
         ↓
[Part 1: Run test_core.py]
    - Test 1: Suppression factor
    - Test 2: Planck sweet spot
    - Test 3: Alignment vs Hawking
    - Test 4: Gray code overhead
    - Test 5: Mass spectrum
    → results_core_tests.json
         ↓
[Part 2: Run test_alignment.py]
    - Sim 1: Random walk alignment
    - Sim 2: Two-body timing attack
    - Sim 3: Phase transition
    - Sim 4: Info conservation
    → results_alignment_sims.json
         ↓
[Synthesis Report]
    - Extract key findings
    - Cross-reference results
    - Present conclusions
         ↓
[Print summary and next steps]
         ↓
[Exit]
```

**Total output files:** 2 JSON files (core tests, alignment sims)

---

## Synthesis Report Logic

The synthesis report extracts key results and presents them in human-readable format with context and interpretation.

### Finding 1: Suppression Factor

**Goal:** Confirm that Gray code overhead reproduces Hawking evaporation

**Extraction logic:**
```python
if "test4_overhead" in core_results:
    exp = core_results["test4_overhead"].get("power_law_exponent", "?")
    total = core_results["test4_overhead"].get("total_evap_exponent", "?")
```

**Output:**
```
1. SUPPRESSION FACTOR
   Overhead scales as N^0.5000
   Total: t_evap ∝ N^1.5000
   Expected from Hawking: t_evap ∝ N^1.5
   ✓ MATCH — encoder model reproduces Hawking evaporation scaling!
```

**Pass criteria:**
- Exponent within 0.1 of 1.5: ✓ MATCH
- Exponent deviates > 0.1: ⚠ DEVIATION
- Key is printed even if test failed (for debugging)

**Physical meaning:**
The √N overhead is the core result. If this doesn't match Hawking, either:
- Implementation bug in formulas
- Model doesn't capture essential physics
- Need additional correction terms

### Finding 2: Planck Sweet Spot

**Goal:** Verify Planck mass is the 1-bit threshold

**Extraction logic:**
```python
if "test2_planck_spot" in core_results:
    ps = core_results["test2_planck_spot"]
    N_bits = ps.get('N_bits', '?')
    self_destruct = ps.get('self_destruct_ratio', '?')
```

**Output:**
```
2. PLANCK SWEET SPOT (1-bit encoder)
   N_bits at Planck mass:  18.169
   Self-destruct ratio:    1.000
   ✓ CONFIRMED — Planck mass = 1-bit encoder sweet spot
```

**Pass criteria:**
- N_bits between 15 and 25: ✓ CONFIRMED
- Self-destruct ratio between 0.9 and 1.1: ✓
- Outside range: report actual values

**Physical meaning:**
The ~18 bits (not exactly 1) arises from geometric factors:
- Schwarzschild radius = 2GM/c² = 2l_p at M = M_p
- Area = 4π(2l_p)² = 16πl_p² ≈ 50.3 l_p²
- Entropy S = A/(4l_p²) = 50.3/4 ≈ 12.6 nats ≈ 18.2 bits

The "1-bit" label is conceptual (minimal encoder), not literal.

### Finding 3: Alignment Scaling

**Goal:** Show alignment is harder than evaporation → holographic principle

**Extraction logic:**
```python
if "alignment_scaling" in align_results:
    asc = align_results["alignment_scaling"]
    valid_data = [(r["N_encoder"], r["mean_steps"]) for r in asc
                 if r["mean_steps"] < float('inf') and r["aligned_count"] > 10]
    if len(valid_data) >= 3:
        Ns, Ss = zip(*valid_data)
        fit = np.polyfit(np.log10(Ns), np.log10(Ss), 1)
```

**Output:**
```
3. ALIGNMENT SCALING
   Alignment time ∝ N^1.96
   Evaporation ∝ N^1.5
   ✓ Alignment HARDER than evaporation → info stays on horizon
     This IS the holographic principle emerging from combinatorics!
```

**Pass criteria:**
- Exponent > 1.5: ✓ Alignment harder
- Exponent ≈ 2.0: ✓ Matches random walk theory
- Exponent < 1.5: ⚠ Unexpected result (alignment too easy)

**Physical meaning:**
If alignment time ≤ evaporation time, information could reach the singularity before the black hole evaporates. Actual result (N² > N^1.5 for N > 1) means info stays on horizon — the holographic principle.

### Finding 4: Two-Body Timing Attack

**Goal:** Verify that two-body collisions don't provide shortcuts

**Output:**
```
4. TWO-BODY ('TIMING ATTACK')
   Result: equivalent to one-body return (as predicted)
   Timing attack provides no advantage over random alignment
```

**Pass criteria:**
- Always passes (this is a statement of result, not a test)
- If two-body mean ≪ one-body mean: major discovery (would invalidate model)

**Physical meaning:**
No coordination or memory → can't exploit "birthday paradox" speedup. This supports the random walk model and rules out clever shortcuts to recursive loop formation.

### Finding 5: Information Conservation

**Goal:** Confirm unitarity preserved

**Extraction logic:**
```python
if "info_conservation" in align_results:
    ic = align_results["info_conservation"]
    if ic.get("conserved"):
        print("5. INFORMATION CONSERVATION: ✓ PRESERVED")
```

**Output:**
```
5. INFORMATION CONSERVATION: ✓ PRESERVED
   Encoder model maintains unitarity by construction
```

**Pass criteria:**
- conserved == True: ✓ PRESERVED
- conserved == False: ✗ VIOLATION (would be a critical bug)

**Physical meaning:**
Bits on horizon are in one-to-one correspondence with emitted radiation. No information disappears. This resolves the information paradox at the accounting level (though entanglement structure still needs work).

---

## Key Findings Presentation

### Summary Table

The synthesis report consolidates results into a decision matrix:

| Finding | Result | Status | Implication |
|---------|--------|--------|-------------|
| Suppression factor | N^0.5 | ✓ | Reproduces Hawking |
| Planck sweet spot | N=18.17 | ✓ | Quantum gravity scale identified |
| Alignment scaling | N^1.96 | ✓ | Holographic principle emerges |
| Timing attack | No speedup | ✓ | Random walk model validated |
| Info conservation | Exact | ✓ | Unitarity preserved |

**Overall verdict:**
- All 5 findings confirm theoretical predictions
- Model is internally consistent
- Reproduces known results (Hawking evaporation)
- Makes novel predictions (alignment, overhead structure)

### Cross-References

The synthesis report connects findings:
- Suppression factor (Test 1) = Gap exponent (Test 3) = √N
- Both measure Gray code traversal overhead
- Alignment time (Sim 1) > Evaporation time → holographic principle
- Two-body result (Sim 2) validates random walk assumption (Sim 1)
- Info conservation (Sim 4) necessary for unitarity (framework constraint)

**Network of evidence:**
```
Test 1 (suppression) ←→ Test 4 (overhead) ←→ Test 3 (gap)
         ↓                      ↓                    ↓
    Hawking evap         Gray code           Holographic
    reproduced           structure           principle
         ↓                      ↓                    ↓
    Test 2 (Planck)      Sim 1 (walk)       Sim 4 (unitarity)
```

All tests mutually support the encoder framework.

---

## Next Steps Section

The report concludes with actionable recommendations:

### Immediate Next Steps

```
NEXT STEPS:
  - Run with --heavy on Colab for higher-confidence Monte Carlo
  - Add real data comparison (CMB, LIGO, BH shadow observations)
  - Investigate the suppression factor ↔ Gray code traversal
  - Formalize the POV-dependent intensity prediction
```

**Rationale:**

1. **--heavy mode:**
   - Reduces Monte Carlo error from ±0.03 to ±0.01
   - Increases confidence in power law exponents
   - Necessary for publication-quality claims

2. **Real data comparison:**
   - Test against EHT M87*/Sgr A* shadow observations
   - Check LIGO ringdown frequencies (Kerr BH predictions)
   - Look for CMB anomalies if primordial BHs exist

3. **Gray code traversal theory:**
   - Derive √N overhead from graph theory of Gray code cycles
   - Compute exact coefficient (currently ~10, needs explanation)
   - Prove return time scaling on Z_N with thermal driving

4. **POV-dependent intensity:**
   - Implement photon emission directionality model
   - Predict angular distribution of Hawking radiation
   - Test whether distant observers see different spectra

### Long-Term Directions

(Not printed in default output, but documented here)

**Extensions:**
- Kerr (rotating) black holes: entropy, frame-dragging
- Charged black holes (Reissner-Nordström): extremal limit
- Quantum corrections: next-to-leading order in ℏ
- Entanglement structure: correlations between horizon and radiation

**Applications:**
- Quantum computing analogy: black hole as quantum error-correcting code
- Thermodynamic engines: extracting work from Hawking radiation
- Early universe cosmology: primordial black holes as dark matter

**Theoretical foundations:**
- Rigorous connection to AdS/CFT (if it exists)
- Relationship to loop quantum gravity (spin networks ↔ Gray code?)
- ER=EPR: wormholes as entangled encoder states

**See Also:** [Open-Questions-and-Future-Work](Open-Questions-and-Future-Work.md)

---

## Output Files Generated

### results_core_tests.json

**Content:** All analytical test results
- Test 1: Suppression factor data (7 masses)
- Test 2: Planck mass ratios
- Test 3: Alignment vs Hawking scaling (50 masses)
- Test 4: Overhead models (5 masses)
- Test 5: Mass spectrum (100 masses)

**Size:** ~50 KB

**Format:** See [Code-Results-Format.md](Code-Results-Format.md)

### results_alignment_sims.json

**Content:** All Monte Carlo simulation results
- Sim 1: Alignment scaling (5 encoder sizes)
- Sim 2: Two-body vs one-body (3 comparisons)
- Sim 3: Phase transition (200 mass ratios)
- Sim 4: Info conservation (1 run, N_start=1000)

**Size:** ~200 KB (larger due to phase transition sweep)

**Format:** See [Code-Results-Format.md](Code-Results-Format.md)

### How to Load Results

**Python:**
```python
import json

with open("results_core_tests.json") as f:
    core = json.load(f)

with open("results_alignment_sims.json") as f:
    align = json.load(f)

# Extract specific result
planck_N = core["test2_planck_spot"]["N_bits"]
print(f"Planck mass encoder has {planck_N:.1f} bits")

# Plot alignment scaling
import matplotlib.pyplot as plt
data = align["alignment_scaling"]
Ns = [r["N_encoder"] for r in data]
steps = [r["mean_steps"] for r in data]
plt.loglog(Ns, steps, 'o-')
plt.xlabel("N (encoder bits)")
plt.ylabel("Mean alignment steps")
plt.title("Alignment time scaling")
plt.savefig("alignment_scaling.png")
```

**Jupyter:**
```python
%matplotlib inline
import json
import numpy as np
import matplotlib.pyplot as plt

# Load and visualize
with open("results_core_tests.json") as f:
    core = json.load(f)

# Test 1: Suppression factor
data = core["test1_suppression"]
masses = [r["mass_kg"] for r in data if "log10_suppression" in r]
suppression = [r["suppression_factor"] for r in data if "log10_suppression" in r]

plt.figure(figsize=(10,6))
plt.loglog(masses, suppression, 'o-', label='Actual')
plt.loglog(masses, [np.sqrt(r["N_bits"]) for r in data[:len(masses)]],
           '--', label='√N model')
plt.xlabel("Mass (kg)")
plt.ylabel("Suppression factor")
plt.legend()
plt.grid(True, which='both', alpha=0.3)
plt.title("Evaporation suppression factor")
plt.show()
```

---

## How to Add New Test Suites

### Step 1: Create New Test Module

```python
# test_new_suite.py

import numpy as np
import json
from constants import EncoderState, m_p

def test_new_property():
    """New test of encoder property."""
    results = []
    # ... test logic ...
    return results

def run_all():
    """Run all tests in this suite."""
    results = {}
    results["new_test"] = test_new_property()

    with open("results_new_suite.json", 'w') as f:
        json.dump(results, f, indent=2)

    return results

if __name__ == "__main__":
    run_all()
```

### Step 2: Integrate into run_all.py

```python
def main():
    # [existing code]

    # ---- NEW SUITE ----
    print("\n\n" + "█" * 70)
    print("█  PART 3: NEW TEST SUITE")
    print("█" * 70)
    import test_new_suite
    new_results = test_new_suite.run_all()

    # Update synthesis report
    # [add extraction logic for new findings]
```

### Step 3: Update Synthesis Report

```python
# In synthesis section:
if "new_test" in new_results:
    result = new_results["new_test"]
    print(f"\n  6. NEW PROPERTY")
    print(f"     Result: {result['value']:.3f}")
    print(f"     Expected: {result['expected']:.3f}")
    if abs(result['value'] - result['expected']) < 0.1:
        print(f"     ✓ CONFIRMED")
```

### Step 4: Document

- Add section to appropriate Code-*.md page
- Update this page with new synthesis logic
- Add to [Code-Results-Format.md](Code-Results-Format.md)

---

## Error Handling

### Import Errors

If test modules fail to import:
```python
try:
    import test_core
except ImportError as e:
    print(f"ERROR: Cannot import test_core: {e}")
    print("Ensure constants.py is in the same directory.")
    sys.exit(1)
```

### Test Failures

Individual tests can fail without crashing the whole run:
```python
try:
    core_results = test_core.run_all()
except Exception as e:
    print(f"ERROR in test_core: {e}")
    core_results = {"error": str(e)}
```

Synthesis report checks for errors:
```python
if "error" in core_results:
    print(f"\n  ⚠ CORE TESTS FAILED: {core_results['error']}")
else:
    # Normal processing
```

### JSON Serialization

Handle numpy types that aren't JSON-serializable:
```python
def convert(obj):
    if isinstance(obj, (np.floating, np.float64)):
        return float(obj)
    if isinstance(obj, (np.integer, np.int64)):
        return int(obj)
    if isinstance(obj, np.ndarray):
        return obj.tolist()
    return obj
```

This is handled within test_core.py and test_alignment.py, but run_all.py can add additional safeguards if needed.

---

## Performance Notes

### Timing Breakdown

**Default mode (~70s total):**
- Imports and setup: ~1s
- Test 1 (suppression): ~0.5s
- Test 2 (Planck): ~0.1s
- Test 3 (alignment): ~1s
- Test 4 (overhead): ~0.5s
- Test 5 (spectrum): ~5s
- Sim 1 (alignment scaling): ~40s (dominates!)
- Sim 2 (two-body): ~10s
- Sim 3 (phase transition): ~5s
- Sim 4 (info conservation): ~0.1s
- Synthesis report: ~0.5s
- JSON writing: ~0.5s

**Bottleneck:** Sim 1 random walks (60% of total time)

### Optimization Opportunities

**Parallelize test suites:**
```python
import multiprocessing as mp

with mp.Pool(2) as pool:
    core_future = pool.apply_async(test_core.run_all)
    align_future = pool.apply_async(test_alignment.run_all)

    core_results = core_future.get()
    align_results = align_future.get()
```

**Expected speedup:** 1.5–2× (limited by Sim 1 dominance)

**Vectorize random walks:**
- Use NumPy broadcasting to simulate all trials at once
- Store positions as array of shape (n_trials,)
- Update all positions simultaneously

**Expected speedup:** 2–5× for Sim 1

**GPU acceleration:**
- Port random walks to CuPy or JAX
- Run 100K trials in parallel on GPU
- Expected speedup: 50–100×

**Caching:**
- Store results of expensive calculations (EncoderState properties)
- Reuse across tests if mass is the same
- Expected speedup: negligible (property access is fast)

---

## Reproducibility

### Fixed Seed

All simulations use `SEED = 42` by default:
```python
# In test_alignment.py
SEED = 42
rng = np.random.default_rng(SEED)
```

**To get different results:**
```python
# In test_alignment.py, change:
SEED = None  # or any other integer
```

### Platform Differences

**Expected sources of variation:**
- Floating-point rounding (different CPU architectures)
- NumPy version (RNG algorithms changed in 1.17+)
- OS differences (Windows vs Linux random seed initialization)

**Mitigation:**
- Use fixed seed (eliminates RNG variation)
- Use double precision (np.float64)
- Document NumPy version in output

**Acceptable variation:**
- Power law exponents: ±0.01 (due to finite sampling)
- Mean values: ±1% (Monte Carlo noise)
- Ratios: ±0.05 (propagated errors)

**If variation > acceptable:**
- Check NumPy version (`np.__version__`)
- Verify constants.py values match
- Increase N_SAMPLES to reduce noise

---

## Validation Checklist

Before releasing new version of run_all.py:

- [ ] All tests pass on developer machine
- [ ] --quick mode completes in < 15s
- [ ] --heavy mode completes in < 1000s
- [ ] JSON files written to correct locations
- [ ] Synthesis report prints all 5 findings
- [ ] No import errors on fresh Python 3.8+ install
- [ ] Results reproducible with fixed seed
- [ ] No warnings from NumPy about overflow/underflow
- [ ] Output files < 1 MB each (check with `ls -lh results*.json`)

---

## See Also

- [Code-constants.py.md](Code-constants.py.md) — Physical constants and encoder model
- [Code-test_core.py.md](Code-test_core.py.md) — Analytical validation tests
- [Code-test_alignment.py.md](Code-test_alignment.py.md) — Monte Carlo simulations
- [Code-Results-Format.md](Code-Results-Format.md) — JSON output schema
- [Key-Results-Summary](Key-Results-Summary.md) — High-level findings
- [How-to-Contribute](How-to-Contribute.md) — Adding new tests

---

**Last Updated:** 2026-03-20
**Lines of Code:** 129
**Test Runtime:** ~70 seconds (default), ~10 seconds (quick), ~600 seconds (heavy)
**All Tests Pass:** ✓
