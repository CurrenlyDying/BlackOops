# BlackOops — Gray Code Universe Wiki 🌀

Welcome to the comprehensive reference wiki for **BlackOops**, a computational framework testing the hypothesis that the universe encodes state transitions like a Gray code rotary encoder.

## Core Hypothesis (3 Sentences)

Physical state transitions follow the Gray code constraint — only one bit flips between adjacent states. When mapped onto black hole thermodynamics, this constraint reproduces Hawking radiation, the holographic principle, and the Bekenstein-Hawking entropy from combinatorial arguments alone. The Planck scale defines the "encoder's angular resolution," and singularities emerge as recursive bit loops that information can never quite reach.

## Quick Start

```bash
# Clone the repository
git clone https://github.com/CurrenlyDying/BlackOops.git
cd BlackOops

# Install dependencies (just NumPy)
pip install numpy

# Run all tests (~60 seconds)
python run_all.py

# Fast sanity check (~10 seconds)
python run_all.py --quick

# Full Monte Carlo (GPU/Colab recommended)
python run_all.py --heavy
```

## Navigation

### For Contributors & Developers
- [[constants.py Documentation]] — The `EncoderState` class and all physics computations
- [[test_core.py Documentation]] — Analytical test suite (5 tests)
- [[test_alignment.py Documentation]] — Monte Carlo simulation suite (4 sims)
- [[run_all.py Documentation]] — Master runner and CLI
- [[How to Contribute]] — Adding tests, running on Colab, submitting results
- [[Results Format]] — JSON output schema

### For Polymath Community
- [[The Gray Code Universe Hypothesis]] — Full theoretical framework
- [[Key Results Summary]] — The 5 main findings with tables and interpretation
- [[Open Questions and Future Work]] — What's unresolved and what to test next
- [[Glossary]] — Alphabetical list of all technical terms

### Foundational Concepts

**Information Theory:**
- [[Shannon Entropy]] — The bit as fundamental unit, connection to thermodynamics
- [[Boolean Algebra and Physical Circuits]] — Shannon's 1937 thesis, computation as substrate-independent
- [[Gray Code]] — Reflected binary, single-bit-flip property, traversal cost
- [[Rotary Encoders]] — Physical devices, angular resolution, glitch states
- [[Shannon's Theseus]] — 1950 maze-solving mouse, entropy reduction

**Black Hole Physics:**
- [[Schwarzschild Radius]] — Derivation, values for key objects
- [[Bekenstein-Hawking Entropy]] — $S = k_B A / 4 l_p^2$, interpretation as information
- [[Hawking Radiation]] — Temperature, luminosity, evaporation time
- [[Holographic Principle]] — Information on boundaries not volumes, AdS/CFT
- [[Black Hole Information Paradox]] — Hawking's 1975 argument, proposed resolutions
- [[Planck Units]] — Natural limits on measurement, quantum gravity scale
- [[Planck Mass as Critical Threshold]] — The 1-bit encoder sweet spot
- [[Kerr Black Holes]] — Rotating BHs, ring singularity, ergosphere
- [[Event Horizon Telescope Observations]] — M87* and Sgr A* images

**Thermodynamics & Statistical Mechanics:**
- [[Bekenstein Bound]] — Maximum entropy in bounded region
- [[Stefan-Boltzmann Law]] — Blackbody radiation, application to Hawking luminosity
- [[Unitarity]] — Information conservation in quantum mechanics
- [[Entropy and the Arrow of Time]] — Second law, Boltzmann's H-theorem

**Quantum Mechanics:**
- [[Quantum State Evolution]] — Schrödinger equation, continuous evolution = Gray code
- [[Qubits vs Classical Bits]] — Superposition, entanglement, no-cloning
- [[Quantum Error Correction]] — Stabilizer codes, connection to holography

**Mathematics:**
- [[Random Walks on Cyclic Groups]] — $Z_N$ random walk, return time O(N²)
- [[Power Law Scaling]] — Log-log fitting, identifying power laws in data
- [[Geometric Mean]] — Why Hawking rate being geometric mean is significant

**Computation:**
- [[Monte Carlo Simulation]] — Law of large numbers, variance reduction, GPU acceleration
- [[Reinforcement Learning]] — Connection to Theseus, state-action-reward

### Extended Topics [EXTENDED]

**Adjacent Physics:**
- [[Page Curve [EXTENDED]]] — Entanglement entropy evolution during evaporation
- [[Analog Gravity [EXTENDED]]] — Sonic black holes, laboratory tests
- [[Loop Quantum Gravity and Black Holes [EXTENDED]]] — Quantized area spectrum
- [[Causal Set Theory [EXTENDED]]] — Discrete spacetime structure
- [[Verlinde's Entropic Gravity [EXTENDED]]] — Information-theoretic derivation of gravity
- [[Jacobson's Thermodynamic Derivation of GR [EXTENDED]]] — Einstein equation from horizon entropy

**Information Theory Depth:**
- [[Landauer's Principle [EXTENDED]]] — Minimum energy to erase a bit
- [[Margolus-Levitin Theorem [EXTENDED]]] — Maximum computation rate
- [[Wheeler's It from Bit [EXTENDED]]] — Information-theoretic ontology
- [[Quantum Channel Capacity [EXTENDED]]] — Holevo bound
- [[Kolmogorov Complexity [EXTENDED]]] — Algorithmic information theory

**Mathematical Structures:**
- [[Cayley Graphs [EXTENDED]]] — Graph structure of cyclic groups
- [[Spectral Gap and Mixing Time [EXTENDED]]] — Formalizing alignment time
- [[Gray Code as Hamiltonian Path [EXTENDED]]] — Graph-theoretic perspective
- [[de Bruijn Sequences [EXTENDED]]] — Related combinatorial structures

**Data Sources:**
- [[EHT Data Products [EXTENDED]]] — How to access Event Horizon Telescope data
- [[LIGO Public Data [EXTENDED]]] — Gravitational wave strain data
- [[Planck CMB Data [EXTENDED]]] — Cosmic microwave background observations
- [[Known Black Hole Masses [EXTENDED]]] — Catalog with uncertainties

**Computational Extensions:**
- [[GPU Acceleration with Python [EXTENDED]]] — CuPy, JAX, Numba
- [[Google Colab Setup Guide [EXTENDED]]] — Running heavy parameter sweeps
- [[Visualization Approaches [EXTENDED]]] — matplotlib, plotly, dashboards

## Key Findings (Executive Summary)

1. **Suppression Factor = √N** — The Gray code overhead is exactly N^0.5, giving t_evap ∝ N^1.5 which matches Hawking's formula to 4 decimal places across 50 orders of magnitude.

2. **Alignment Harder Than Evaporation** — Random walk alignment scales as N^1.96 while evaporation scales as N^1.5. Information stays on the horizon rather than reaching the singularity — the holographic principle emerges from combinatorics.

3. **Planck Mass = 1-Bit Encoder** — At M = M_planck, the encoder has ~18 bits and self-destructs in ~16,000 Planck times. This is the "oscillates between black hole and not black hole" regime.

4. **Geometric Mean Structure** — Hawking radiation rate is the geometric mean between alignment probability (N^-1) and trivial rate. This structural relation is non-trivial.

5. **Phase Transition at M/M_p = 0.225** — Razor-sharp boundary (0.23 decades wide) where N ≈ 1 bit, separating black hole from non-black-hole regimes.

## What This Framework Does

✅ Reproduces Hawking evaporation time from combinatorial arguments
✅ Identifies Planck mass as special 1-bit case
✅ Derives holographic principle from random walk scaling
✅ Makes concrete predictions testable with Monte Carlo
✅ Provides computational framework for exploring parameter space

## What This Framework Doesn't (Yet) Do

- POV-dependent photon intensity predictions
- Kerr (rotating) black hole / ring singularity analysis
- Comparison to real EHT shadow data (M87*, Sgr A*)
- CMB or gravitational wave data integration
- Formal derivation of √N overhead from Gray code graph theory

## Project Status

**Not peer-reviewed.** This is playground physics with real math. The interesting question is whether the framework makes predictions distinguishable from standard semiclassical gravity. Community validation, falsification attempts, and extensions are welcomed.

## License

MIT — share freely, break things, run your own tests, tell us what you find.

## See Also

- [[The Gray Code Universe Hypothesis]] — Detailed theoretical framework
- [[Key Results Summary]] — Full data tables and analysis
- [[Open Questions and Future Work]] — Research directions
- [[How to Contribute]] — Get involved
- [[Glossary]] — Technical terms quick reference

## References

1. Shannon, C. E. (1948). "A Mathematical Theory of Communication." *Bell System Technical Journal*
2. Bekenstein, J. D. (1973). "Black Holes and Entropy." *Physical Review D*
3. Hawking, S. W. (1975). "Particle Creation by Black Holes." *Communications in Mathematical Physics*
4. 't Hooft, G. (1993). "Dimensional Reduction in Quantum Gravity." arXiv:gr-qc/9310026
5. Susskind, L. (1995). "The World as a Hologram." *Journal of Mathematical Physics*
