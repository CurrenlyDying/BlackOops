# How to Contribute

Welcome! The BlackOops framework is designed to be extended, validated, and stress-tested by the community. This page explains how to contribute effectively.

## Quick Start for Contributors

```bash
# 1. Fork the repository on GitHub
# 2. Clone your fork
git clone https://github.com/YOUR_USERNAME/BlackOops.git
cd BlackOops

# 3. Install dependencies (just NumPy)
pip install numpy

# 4. Run tests to verify setup
python run_all.py --quick

# 5. Make your changes (see sections below)

# 6. Run full test suite
python run_all.py

# 7. Submit a pull request with your results
```

## Types of Contributions

### 1. Adding New Analytical Tests

**Where:** `test_core.py`

**What to add:**
- New physical scenarios (charged black holes, cosmological constant)
- Alternative encoder models (non-Gray-code sequences)
- Consistency checks (energy conservation, information bounds)

**Template:**
```python
def test_your_new_idea():
    """
    Brief description of what this test checks.

    Expected result: [describe prediction]
    """
    separator("TEST N: Your Test Name")

    # Your computation here
    result = {}

    # Print results in table format
    print(f"{'Column 1':<20} {'Column 2':>15}")
    print("-" * 40)

    # Analysis and interpretation
    print("\n  INTERPRETATION:")
    print("  - Key finding 1")
    print("  - Key finding 2")

    return result

# Add to run_all() function:
results["testN_your_test"] = test_your_new_idea()
```

**Style Guide:**
- Use SI units exclusively
- Include docstrings with physics background
- Print results in human-readable tables (not just JSON)
- Add interpretation section explaining what the numbers mean

---

### 2. Adding New Monte Carlo Simulations

**Where:** `test_alignment.py`

**What to add:**
- Multi-particle alignment scenarios
- Non-uniform random walks (biased, constrained)
- Quantum random walks (unitary evolution)
- Phase space exploration (3D alignment, angular momentum)

**Template:**
```python
def sim_your_simulation():
    """
    Brief description of what this simulates.

    Parameters to tune: N_SAMPLES, max_steps, ...
    """
    separator("SIM N: Your Simulation Name")

    N_SAMPLES = 100_000  # Increase for heavy mode
    N_values = [10, 20, 50, 100, 200]

    results = []
    for N in N_values:
        samples = []
        for _ in range(N_SAMPLES):
            # Your simulation here
            outcome = your_random_walk(N)
            samples.append(outcome)

        mean_val = np.mean(samples)
        std_val = np.std(samples)
        results.append({"N": N, "mean": mean_val, "std": std_val})

    # Print table
    print(f"{'N':<10} {'Mean':>15} {'Std':>15}")
    print("-" * 45)
    for r in results:
        print(f"{r['N']:<10} {r['mean']:>15.3f} {r['std']:>15.3f}")

    # Fit scaling law
    N_arr = np.array([r["N"] for r in results])
    mean_arr = np.array([r["mean"] for r in results])
    fit = np.polyfit(np.log10(N_arr), np.log10(mean_arr), 1)
    print(f"\n  Scaling: outcome ∝ N^{fit[0]:.3f}")

    return results

# Add to run_all():
results["simN_your_sim"] = sim_your_simulation()
```

**Performance Tips:**
- Use NumPy vectorization where possible
- Avoid Python loops for inner-most operations
- Profile with `cProfile` if slow: `python -m cProfile -s cumtime test_alignment.py`

---

### 3. Running Heavy Parameter Sweeps

**For GPU Users:**

Install CuPy (NVIDIA CUDA required):
```bash
pip install cupy-cuda11x  # Replace 11x with your CUDA version
```

Modify `test_alignment.py`:
```python
# At top of file
try:
    import cupy as np  # Drop-in replacement for NumPy
    GPU_AVAILABLE = True
except ImportError:
    import numpy as np
    GPU_AVAILABLE = False

# In simulation functions, arrays automatically use GPU
```

**For Colab Users:**

1. Go to [colab.research.google.com](https://colab.research.google.com)
2. Runtime → Change runtime type → GPU (T4, or pay for A100)
3. Upload `constants.py`, `test_alignment.py`, `run_all.py`
4. Install NumPy: `!pip install numpy`
5. Run: `!python run_all.py --heavy`

**Recommended Heavy Parameters:**
```python
N_SAMPLES = 1_000_000  # 1M samples (was 100K)
N_values = [10, 20, 50, 100, 200, 500, 1000]  # Extend to N=1000
max_steps = 10_000_000  # 10M max steps (was 1M)
```

**Expected Runtimes:**
- CPU (single core): ~1-2 hours
- Colab GPU (T4): ~15-20 minutes
- Colab GPU (A100): ~5 minutes

---

### 4. Proposing New Encoder Models

**Current Model:** Gray code on cyclic group $\mathbb{Z}_N$

**Alternative Models to Try:**
1. **Kerr Encoder:** Ring singularity = multi-bit loop
2. **Charged Encoder:** Reissner-Nordström metric, inner/outer horizons
3. **de Sitter Encoder:** Cosmological constant, finite universe encoder
4. **Quantum Encoder:** Positions are qubits, superposition allowed
5. **Non-cyclic Graph:** Alignment on trees, lattices, hypercubes

**How to Implement:**

Create new file `my_encoder_model.py`:
```python
from constants import EncoderState, G, c, hbar, k_B

class KerrEncoderState(EncoderState):
    """Rotating black hole encoder."""

    def __init__(self, mass_kg, angular_momentum, label=""):
        super().__init__(mass_kg, label)
        self.J = angular_momentum  # kg·m²/s

    @property
    def n_bits(self):
        # Your formula for rotating BH entropy
        # (e.g., Kerr-Newman formula)
        pass

    @property
    def alignment_probability(self):
        # Does rotation make alignment easier?
        # (ring vs point target)
        pass
```

Add tests in new file `test_kerr.py` following same structure as `test_core.py`.

---

### 5. Real Data Comparisons

**EHT Shadow Data:**
- M87* shadow: 42 ± 3 microarcseconds
- Sgr A* shadow: 52 ± 2 microarcseconds
- Data products: eventhorizontelescope.org/for-astronomers/data

**LIGO Merger Data:**
- Public strain data: gwosc.org
- Python tutorial: `gwpy` library
- Example: GW150914 (36 M☉ + 29 M☉ → 62 M☉)

**Suggested Contribution:**
Create `validate_eht.py`:
```python
"""Compare encoder predictions to EHT shadow measurements."""

from constants import EncoderState, M_sun, c

def predict_shadow_size(mass_kg, spin):
    """
    Predict shadow size with encoder corrections.

    GR (Kerr metric): r_shadow ≈ 2.6 r_s
    Encoder model: r_shadow ≈ 2.6 r_s × (1 + correction(N, spin))
    """
    enc = EncoderState(mass_kg)
    r_s = enc.schwarzschild_radius
    N = enc.n_bits

    # Your quantum correction formula here
    correction = your_function(N, spin)

    return 2.6 * r_s * (1 + correction)

# M87* parameters
mass_M87 = 6.5e9 * M_sun
spin_M87 = 0.9  # dimensionless, from EHT
distance_M87 = 16.8e6 * 3.086e16  # 16.8 Mpc in meters

predicted_r = predict_shadow_size(mass_M87, spin_M87)
predicted_angle = predicted_r / distance_M87 * 206265e6  # microarcseconds

print(f"Predicted: {predicted_angle:.1f} μas")
print(f"Observed:  42 ± 3 μas")
print(f"Deviation: {abs(predicted_angle - 42) / 3:.1f} sigma")
```

---

### 6. Documentation and Wiki

**Adding Concept Pages:**

See [[Home]] for list of required and extended pages. If you're expert in one of the topics, consider:
- Expanding existing pages with more detail
- Adding worked examples or numerical values
- Connecting to BlackOops framework explicitly

**Style for Wiki Pages:**
- Use LaTeX for math: `$...$` inline, `$$...$$` display
- Include at least 2 references (papers, textbooks, or high-quality web sources)
- Add "Connection to BlackOops" section
- Link to related pages using `[[Page Title]]`
- Include numerical values and tables where applicable

**Missing Pages (Help Wanted):**
- [[Firewall Paradox]] — AMPS 2012 result, proposed resolutions
- [[ER=EPR Conjecture]] — Wormholes = entanglement
- [[Scrambling Time]] — Fast vs slow scramblers
- [[Penrose Diagrams]] — Causal structure visualization
- [[Tidal Forces]] — Why no firewall from equivalence principle?

---

### 7. Visualization and Interactive Tools

**Suggested Contributions:**
1. **Animation:** Encoder unwinding during evaporation (matplotlib FuncAnimation)
2. **Interactive Plot:** Dash or Streamlit app for parameter exploration
3. **3D Visualization:** Encoder surface with bit positions (Plotly)
4. **Log-log Plots:** Scaling relations with interactive zoom
5. **Phase Transition Video:** Q metric vs M/M_p, showing sharp boundary

**Example (Matplotlib Animation):**
```python
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from constants import EncoderState, M_sun

fig, ax = plt.subplots()

def update(frame):
    mass = M_sun * (1 - frame / 100)  # Evaporating from M_sun to 0
    enc = EncoderState(mass)
    ax.clear()
    ax.bar(['N bits', 'T_H [K]', 'L [W]'],
           [enc.n_bits, enc.hawking_temperature, enc.hawking_luminosity],
           log=True)
    ax.set_title(f"Evaporation: {frame}% complete")

ani = FuncAnimation(fig, update, frames=100, interval=50)
plt.show()
```

---

### 8. Code Quality and Testing

**Before Submitting PR:**
- [ ] Run `python run_all.py` successfully
- [ ] Add docstrings to new functions
- [ ] Follow existing code style (4-space indent, descriptive variable names)
- [ ] Include interpretation of results (don't just print numbers)
- [ ] Update README if adding major feature
- [ ] Add entry to CHANGELOG (if exists)

**Code Review Checklist:**
- Does it use SI units consistently?
- Are formulas correct (check against references)?
- Are variable names physically meaningful (not `x`, `y`, `z`)?
- Is the computational complexity reasonable (not O(N⁴) when O(N²) works)?
- Does it print useful diagnostics (not just silent computation)?

---

### 9. Reporting Issues

**Found a Bug?**

Open an issue on GitHub with:
- Python version: `python --version`
- NumPy version: `python -c "import numpy; print(numpy.__version__)"`
- OS: Windows / Linux / macOS
- Full error traceback
- What you were trying to do
- Minimal code to reproduce

**Incorrect Physics?**

If you think a formula is wrong:
- Cite the correct formula (textbook or paper reference)
- Explain the discrepancy
- Suggest a fix (bonus: submit PR with fix)

**Performance Problem?**

If a test is too slow:
- Profile with `cProfile`
- Identify bottleneck function
- Suggest optimization (vectorization, caching, algorithmic improvement)

---

### 10. Submitting Results to the Community

**If You Ran Heavy Sims:**

Format results as JSON:
```json
{
  "contributor": "Your Name",
  "date": "2026-03-20",
  "hardware": "Colab A100",
  "runtime_minutes": 5.2,
  "parameters": {
    "N_SAMPLES": 1000000,
    "N_values": [10, 20, 50, 100, 200, 500, 1000],
    "max_steps": 10000000
  },
  "results": {
    "power_law_exponent": 1.9985,
    "constant_208_value": 208.37,
    "largest_N_tested": 1000
  },
  "interpretation": "Scaling holds to N=1000 with exponent 1.9985 ± 0.003"
}
```

Submit as PR adding `results_community/your_name_YYYYMMDD.json`.

**If You Found a Discrepancy:**

Same format, but add:
```json
{
  "discrepancy": true,
  "expected": 1.96,
  "observed": 2.14,
  "sigma": 5.2,
  "possible_causes": ["Finite sampling", "Edge effects", "Bug in line 42"]
}
```

---

## Community Channels

**GitHub Discussions:**
- Use for general questions, brainstorming, showing results
- Tag with `question`, `idea`, `results`, `help-wanted`

**Polymath Discord:**
- *(If public Discord exists, add link here)*
- Channels: `#blackoops-general`, `#results`, `#theory`, `#code`

**Citation:**
If you use BlackOops in a paper, preprint, or blog post:
```bibtex
@software{blackoops2026,
  author = {Loputo and Claude (Anthropic)},
  title = {BlackOops: Gray Code Universe Framework},
  year = {2026},
  url = {https://github.com/CurrenlyDying/BlackOops}
}
```

---

## Advanced: Adding Concept Wiki Pages

**Required Format:**
1. Clear definition (smart non-specialist accessible)
2. Mathematical expressions (LaTeX)
3. Numerical values where applicable
4. "Connection to BlackOops" section
5. At least 2 references
6. "See Also" with links to related pages

**Example Structure:**
```markdown
# Your Topic Name

## Definition

[Clear explanation accessible to smart non-specialist]

## Mathematical Formulation

[Key equations in LaTeX]

$$E = mc^2$$

## Numerical Example

[Concrete calculation with numbers]

## Connection to BlackOops

[Explicit tie-in to encoder model, Gray code hypothesis, etc.]

## Applications

[Where this concept appears in physics/CS/math]

## See Also

- [[Related Page 1]]
- [[Related Page 2]]

## References

1. Author (Year). "Title." *Journal*
2. Author (Year). "Title." *Journal*
```

---

## Code of Conduct

- Be respectful and constructive in discussions
- Assume good faith; everyone is here to learn and explore
- Credit others' contributions appropriately
- Prioritize correctness over cleverness
- Document non-obvious choices
- Test before submitting

---

## Recognition

Contributors will be:
- Listed in `CONTRIBUTORS.md` (if exists)
- Credited in papers/preprints using the framework
- Acknowledged in README for major contributions

Top contributors may be invited to co-author papers if framework leads to publishable results.

---

## See Also

- [[Home]] — Project overview
- [[Open Questions and Future Work]] — What needs to be done
- [[constants.py Documentation]] — Understanding the codebase
- [[test_core.py Documentation]] — Analytical test structure
- [[test_alignment.py Documentation]] — Monte Carlo simulation structure
- [[Google Colab Setup Guide [EXTENDED]]] — Running on free GPUs

## References

1. Wilson, G. et al. (2014). "Best Practices for Scientific Computing." *PLOS Biology* 12(1): e1001745
2. Bryan, J. (2018). "Excuse me, do you have a moment to talk about version control?" *The American Statistician* 72(1): 20-27
