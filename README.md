# Gray Code Universe 🌀

**A computational framework testing the hypothesis that the universe encodes state transitions like a Gray code rotary encoder.**

## The Core Idea

What if physical state transitions follow the Gray code constraint — only one bit flips between adjacent states? This maps onto real physics:

- **Gray code constraint** → Unitarity (quantum evolution is continuous/reversible)
- **Encoder angular resolution** → Planck area (l_p²)
- **Encoder total positions** → Bekenstein-Hawking entropy (S = A/4l_p²)  
- **Recursive bit looping** → Black hole singularity
- **Info on horizon, never reaching center** → Holographic principle

## What's In Here

| File | What It Does |
|------|-------------|
| `constants.py` | Physical constants + `EncoderState` class mapping BH properties to encoder concepts |
| `test_core.py` | Analytical tests: evaporation scaling, Planck sweet spot, alignment vs Hawking rates |
| `test_alignment.py` | Monte Carlo sims: random walk alignment, two-body collision, phase transition |
| `run_all.py` | Master runner with `--quick` / `--heavy` modes |

## Quick Start

```bash
# Standard run (~60s)
python run_all.py

# Fast sanity check (~10s)  
python run_all.py --quick

# Full Monte Carlo (Colab/H100 recommended)
python run_all.py --heavy
```

## Key Results

### 1. Suppression Factor
The "Gray code overhead" — how much slower evaporation is than naive 1-bit-per-Planck-time — follows a power law that should reproduce Hawking's t_evap ∝ M³.

### 2. Planck Mass = 1-Bit Encoder
At M = M_planck, the encoder has exactly ~1 bit. It emits one Planck-energy photon and self-destructs in ~1 Planck time. This is the "oscillates between black hole and not-black-hole" regime.

### 3. Alignment Is Harder Than Evaporation
Random walk alignment time scales as N² while evaporation scales as N^1.5. The gap means information stays on the horizon rather than reaching the singularity — the holographic principle emerges from combinatorics alone.

### 4. Timing Attack Doesn't Help
Two-body alignment (the "timing attack") reduces to one-body return via relative coordinates. No shortcut to creating recursive loops.

## Parameters to Tweak

In `test_alignment.py`:
- `N_SAMPLES`: Monte Carlo trials (default 100K, crank to 10M on GPU)
- `N_values`: Encoder sizes to test (add larger values with more compute)

In `constants.py`:
- Use `custom_bh(mass_kg)` for any mass
- All SI units throughout

## What This Doesn't (Yet) Do

- [ ] Compare predictions to real BH shadow data (EHT M87*/Sgr A*)
- [ ] POV-dependent photon intensity prediction
- [ ] Kerr (spinning) black holes / ring singularities  
- [ ] CMB or gravitational wave data hooks
- [ ] Formal derivation of suppression factor from Gray code traversal graph theory

## Dependencies

Just NumPy. That's it.

```bash
pip install numpy
```

## License

MIT — share freely, break things, run your own tests, tell us what you find.

## Context

Developed as a thought experiment exploring information-theoretic foundations of black hole thermodynamics, mapping rotary encoder / Gray code concepts onto Bekenstein-Hawking entropy, Hawking radiation, and the holographic principle. Not peer-reviewed — this is playground physics with real math. The interesting question is whether the framework makes predictions distinguishable from standard semiclassical gravity.
