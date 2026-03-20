# Code Documentation: constants.py

## Overview

`constants.py` is the foundational module of the Gray Code Universe framework. It defines all physical constants in SI units, derives Planck-scale quantities, and implements the `EncoderState` class that maps black hole thermodynamics onto rotary encoder information theory.

**File Location:** `/home/runner/work/BlackOops/BlackOops/constants.py`

**Purpose:**
- Establish the encoder metaphor for black hole state spaces
- Map Bekenstein-Hawking entropy to encoder bit positions
- Compute all thermodynamic and geometric properties from mass alone
- Provide preset constructors for astrophysically relevant black holes

**Design Philosophy:** The entire framework uses SI units throughout for consistency and verifiability against published physics literature. Every derived quantity traces back to the five fundamental constants (G, c, ℏ, k_B, π).

---

## Physical Constants

All constants are defined in SI units following CODATA 2018 recommended values:

### Fundamental Constants

```python
G = 6.67430e-11       # Gravitational constant [m³ kg⁻¹ s⁻²]
c = 2.99792458e8      # Speed of light [m/s]
hbar = 1.054571817e-34 # Reduced Planck constant [J·s]
k_B = 1.380649e-23    # Boltzmann constant [J/K]
pi = np.pi            # Mathematical constant π
```

**Usage Notes:**
- `G`: Newton's gravitational constant; sets strength of gravitational interaction
- `c`: Defines spacetime causal structure; appears in Schwarzschild radius, Hawking temperature
- `hbar`: Quantum of action; sets Planck scale via ℏG/c³
- `k_B`: Converts between energy and temperature scales
- `pi`: Geometric factor appearing in horizon area, solid angles

---

## Planck Units

The Planck scale defines the fundamental "angular resolution" of the encoder — the minimum distinguishable state transition size.

### Derivation

Planck units arise from dimensional analysis of (G, c, ℏ):

```python
l_p = sqrt(ℏG/c³)          # Planck length  ~ 1.616×10⁻³⁵ m
t_p = sqrt(ℏG/c⁵)          # Planck time    ~ 5.391×10⁻⁴⁴ s
m_p = sqrt(ℏc/G)           # Planck mass    ~ 2.176×10⁻⁸ kg
E_p = sqrt(ℏc⁵/G)          # Planck energy  ~ 1.956×10⁹ J
T_p = sqrt(ℏc⁵/(Gk_B²))    # Planck temp    ~ 1.417×10³² K
A_p = l_p²                 # Planck area    ~ 2.612×10⁻⁷⁰ m²
```

**Physical Interpretation:**
- **l_p**: Quantum gravity scale; below this, spacetime geometry becomes uncertain
- **t_p**: Fundamental time tick; the encoder updates every Planck time
- **m_p**: Mass at which Schwarzschild radius ~ Compton wavelength ~ l_p
- **E_p**: Energy scale where quantum and gravitational effects equally important
- **T_p**: Temperature of a Planck-mass black hole
- **A_p**: Fundamental area quantum for horizon; Bekenstein-Hawking entropy S = A/(4A_p)

### The 1-Bit Sweet Spot

At M = M_planck:
- Schwarzschild radius r_s ≈ 2l_p
- Horizon area A ≈ 16πl_p² ≈ 50 A_p
- Number of encoder bits N ≈ 18 bits (from S = A/(4A_p ln(2)))
- Hawking temperature T_H ≈ T_p
- Evaporation time t_evap ≈ 10⁴ t_p

The encoder is minimally defined — emitting one Planck-energy photon removes significant mass. This is the "oscillates between black hole and not" regime.

---

## EncoderState Class

The `EncoderState` dataclass is the central object of the framework. Given only a black hole mass, it computes all thermodynamic, geometric, and information-theoretic properties.

### Initialization

```python
@dataclass
class EncoderState:
    mass_kg: float
    label: str = ""
```

**Parameters:**
- `mass_kg`: Black hole mass in kilograms (must be positive)
- `label`: Optional human-readable name for output formatting

**Example:**
```python
enc = EncoderState(M_sun, "Solar Mass Black Hole")
enc = EncoderState(1e12, "Primordial BH")
```

### Property: schwarzschild_radius

**Formula:**
```python
r_s = 2GM/c²
```

**Returns:** Schwarzschild radius in meters [m]

**Physical Meaning:** The event horizon radius. For non-rotating (Schwarzschild) black holes, this is the surface of no return. In the encoder model, r_s is the physical radius of the rotary encoder disk.

**Typical Values:**
- M_planck: r_s ~ 3.2×10⁻³⁵ m (2 Planck lengths)
- M_sun: r_s ~ 2,953 m (3 km)
- M87* (6.5×10⁹ M_sun): r_s ~ 1.9×10¹³ m (19 billion km, ~ 0.002 light-years)

**See Also:** [Schwarzschild-Radius](Schwarzschild-Radius.md)

---

### Property: horizon_area

**Formula:**
```python
A = 4πr_s²
```

**Returns:** Event horizon surface area in square meters [m²]

**Physical Meaning:** Total area of the spherical event horizon. This is the "encoder disk surface" — the substrate encoding all N bits as angular positions.

**Bekenstein-Hawking Connection:**
The horizon area directly determines entropy via S = A/(4l_p²) (in natural units, S/ln(2) for bits). Every 4 Planck areas corresponds to one nat of entropy.

**Scaling:**
- A ∝ r_s² ∝ M²
- Doubling mass quadruples area (and entropy)

**See Also:** [Bekenstein-Hawking-Entropy](Bekenstein-Hawking-Entropy.md), [Holographic-Principle](Holographic-Principle.md)

---

### Property: n_bits

**Formula:**
```python
N = A / (4 A_p ln(2))
```

**Returns:** Number of encoder bit positions (Bekenstein-Hawking entropy in bits)

**Derivation:**
1. Bekenstein-Hawking entropy: S = A/(4A_p) [nats]
2. Convert to bits: S_bits = S/ln(2)
3. In Gray code, N positions requires log₂(N) bits, but we interpret N directly as the total state space size

**Physical Meaning:**
The total number of distinguishable angular positions on the encoder. Each position corresponds to a unique microstate of the black hole. The Gray code constraint means adjacent positions differ by exactly 1 bit flip.

**Scaling:**
- N ∝ A ∝ M²
- Solar mass BH: N ~ 10⁷⁷ bits
- Sgr A* (4×10⁶ M_sun): N ~ 10⁹⁰ bits

**Information Density:**
The N bits are distributed holographically over the 2D horizon surface, not in the 3D interior volume. This gives surface density ~ 1 bit per 4A_p.

**See Also:** [Bekenstein-Bound](Bekenstein-Bound.md), [Shannon-Entropy](Shannon-Entropy.md)

---

### Property: n_nats

**Formula:**
```python
S = A / (4 A_p)
```

**Returns:** Bekenstein-Hawking entropy in nats (natural logarithm base e)

**Physical Meaning:** Entropy in natural units. Nats are the information-theoretic unit using ln instead of log₂. Conversion: 1 nat = 1/ln(2) ≈ 1.443 bits.

**Usage:** Useful when working with statistical mechanics formulas that use natural logarithms (S = k_B ln(Ω)).

---

### Property: angular_resolution_sr

**Formula:**
```python
Ω = 4π / N
```

**Returns:** Angular resolution per bit in steradians [sr]

**Physical Meaning:**
The solid angle subtended by one encoder position as viewed from the center. The full sphere (4π steradians) is divided into N equal patches, each representing one bit of information.

**Scaling:**
- Ω ∝ 1/N ∝ 1/M²
- Larger black holes have finer angular resolution

**Encoder Metaphor:**
If you imagine looking at the encoder from the singularity, each of the N positions occupies this solid angle. Gray code state transitions flip the bit corresponding to one patch.

**See Also:** [Rotary-Encoders](Rotary-Encoders.md)

---

### Property: hawking_temperature

**Formula:**
```python
T_H = ℏc³ / (8πGMk_B)
```

**Returns:** Hawking temperature in Kelvin [K]

**Derivation:**
From semiclassical quantum field theory in curved spacetime (Hawking 1975). The temperature arises from thermal radiation of the event horizon as seen by distant observers.

**Physical Meaning:**
The effective temperature of Hawking radiation. The black hole radiates as a black body with surface temperature T_H. In the encoder model, this is the thermal energy scale driving bit release.

**Scaling:**
- T_H ∝ 1/M
- Stellar-mass BH: T_H ~ 10⁻⁸ K (colder than CMB!)
- Planck-mass BH: T_H ~ 10³² K
- Smaller holes are hotter

**Observation Challenge:**
For astrophysical black holes, T_H ≪ T_CMB ≈ 2.7 K, making Hawking radiation undetectable with current technology.

**See Also:** [Hawking-Radiation](Hawking-Radiation.md), [Planck-Units](Planck-Units.md)

---

### Property: hawking_luminosity

**Formula:**
```python
L = σ A T⁴
where σ = π²k_B⁴ / (60ℏ³c²)
```

**Returns:** Hawking radiation power in Watts [W]

**Derivation:**
Stefan-Boltzmann law applied to horizon area with Hawking temperature. The prefactor σ is modified from the standard Stefan-Boltzmann constant due to relativistic quantum effects.

**Physical Meaning:**
Total power radiated across all frequencies and directions. This is the rate at which the black hole loses rest mass energy (E = Mc²).

**Scaling:**
- L ∝ A T⁴ ∝ M² (1/M)⁴ ∝ 1/M²
- Smaller holes radiate faster

**Energy Budget:**
- Solar mass: L ~ 10⁻²⁸ W (negligible)
- Planck mass: L ~ 10⁵² W (explosive!)

**Encoder Interpretation:**
Luminosity is the power output of the encoder unwinding. Each emitted photon carries one thermal bit of information (E_bit ~ k_B T_H).

**See Also:** [Hawking-Radiation](Hawking-Radiation.md)

---

### Property: evaporation_time

**Formula:**
```python
t_evap = 5120π G² M³ / (ℏc⁴)
```

**Returns:** Total evaporation lifetime in seconds [s]

**Derivation:**
Integrate dM/dt = -L/(c²) from initial mass M to zero:
```
t_evap = ∫₀^M (c²/L) dM' ∝ ∫₀^M M'² dM' = M³/3
```
The exact coefficient 5120π comes from the full integration with the Stefan-Boltzmann prefactor.

**Physical Meaning:**
Time for the black hole to completely evaporate via Hawking radiation (neglecting accretion).

**Scaling:**
- t_evap ∝ M³
- Doubling mass increases lifetime by factor of 8

**Timescales:**
- Planck mass: t_evap ~ 10⁻⁴⁰ s
- 10¹² kg (mountain): t_evap ~ 10¹⁰ years (comparable to age of universe)
- Solar mass: t_evap ~ 10⁶⁷ years (far longer than current age of universe)

**Encoder Model Prediction:**
If bits release at naive rate (1 bit per Planck time), evaporation would take:
```
t_naive = N × t_p
```
The suppression factor S = t_evap / t_naive encodes the Gray code traversal overhead.

**See Also:** [Hawking-Radiation](Hawking-Radiation.md), [The-Gray-Code-Universe-Hypothesis](The-Gray-Code-Universe-Hypothesis.md)

---

### Property: bits_per_planck_time

**Formula:**
```python
R = (L / E_bit) × t_p
where E_bit = k_B T_H
```

**Returns:** Hawking bit release rate in [bits per Planck time]

**Derivation:**
1. Energy per thermal bit: E_bit ~ k_B T_H
2. Photon emission rate: r = L / E_bit [photons/s]
3. Convert to Planck time scale: R = r × t_p

**Physical Meaning:**
The instantaneous rate at which the encoder releases information to the outside universe. This is the key observable linking thermodynamics to information theory.

**Scaling:**
- R ∝ L / T_H ∝ (1/M²) / (1/M) ∝ 1/M ∝ 1/√N
- Larger black holes release bits more slowly per Planck tick

**Comparison to Alignment:**
- Alignment probability: P_align ~ 1/N
- Bit release rate: R ~ 1/√N
- Gap: R/P ~ √N

The gap indicates Gray code traversal overhead — bits must "work their way out" through the cyclic structure.

**See Also:** [Shannon-Entropy](Shannon-Entropy.md), [Gray-Code](Gray-Code.md)

---

### Property: alignment_probability

**Formula:**
```python
P = 1 / N
```

**Returns:** Probability of infalling info aligning with recursive loop per Planck time

**Physical Meaning:**
In the encoder model, infalling information must "align" with the recursive loop (singularity) to merge and affect the internal state. If the N positions are equally likely, random alignment probability is 1/N per attempt.

**Scaling:**
- P ∝ 1/N ∝ 1/M²
- Larger holes are harder to align with

**Timing Attack Hypothesis:**
Could two infalling bits "time their approach" to align with each other before aligning with the singularity? Monte Carlo simulations (test_alignment.py) show this reduces to a random walk on relative coordinates — no speedup.

**Holographic Emergence:**
The fact that alignment time ∝ N² while evaporation time ∝ N^1.5 means information stays on the horizon rather than falling in. This is the holographic principle emerging from combinatorics alone.

**See Also:** [Random-Walks-on-Cyclic-Groups](Random-Walks-on-Cyclic-Groups.md), [Holographic-Principle](Holographic-Principle.md)

---

### Property: gray_code_traversal_depth

**Formula:**
```python
D = N
```

**Returns:** Number of Gray code flips to traverse all N positions

**Physical Meaning:**
In a reflected Gray code with N = 2^n positions, a complete cycle visits each position exactly once, requiring N steps (each step flips 1 bit). This is the minimal path through the state space.

**Encoder Unwinding:**
To release all information during evaporation, the encoder must traverse its full Gray code cycle. But the actual unwinding involves thermal fluctuations, backtracking, and overhead from the constraint that adjacent states differ by only 1 bit.

**Overhead Models:**
Testing shows the evaporation overhead scales as:
- Naive (no overhead): O(N) → t_evap ∝ N × t_p (too fast)
- Square root: O(√N) → t_evap ∝ N^1.5 × t_p (matches Hawking!)
- Linear: O(N) → t_evap ∝ N² × t_p (too slow)

The √N overhead arises from the combinatorial structure of Gray code traversal under thermal driving.

**See Also:** [Gray-Code](Gray-Code.md), [Test 4: Gray Code Overhead](Code-test_core.py.md#test-4-gray-code-traversal-overhead-hypothesis)

---

### Method: summary()

**Returns:** Multi-line string with human-readable encoder properties

**Example Output:**
```
============================================================
ENCODER STATE: Solar Mass Black Hole
============================================================
  Mass:                  1.989e+30 kg (1.00e+00 M☉)
  Schwarzschild radius:  2.953e+03 m
  Horizon area:          1.097e+08 m²
  Encoder bits (N):      1.545e+77
  Angular res/bit:       8.146e-77 sr
  Hawking temperature:   6.169e-08 K
  Hawking luminosity:    9.005e-29 W
  Evaporation time:      2.098e+67 s (6.649e+59 yr)
  Bits/Planck time:      3.289e-43
  Alignment prob/tick:   6.473e-78
============================================================
```

**Usage:**
```python
enc = solar_mass_bh()
print(enc.summary())
```

**Design Note:**
All values shown in scientific notation for readability across 100+ orders of magnitude. Solar mass values provided for astrophysical context.

---

## Preset Encoder Functions

Convenience constructors for physically relevant black holes:

### solar_mass_bh()
```python
def solar_mass_bh():
    return EncoderState(M_sun, "Solar Mass Black Hole")
```
**Mass:** 1.989×10³⁰ kg
**Schwarzschild radius:** 2,953 m (3 km)
**Bits:** ~10⁷⁷
**Temperature:** 6×10⁻⁸ K (below CMB)
**Evaporation time:** 10⁶⁷ years

---

### planck_mass_bh()
```python
def planck_mass_bh():
    return EncoderState(m_p, "Planck Mass (1-bit sweet spot)")
```
**Mass:** 2.176×10⁻⁸ kg
**Schwarzschild radius:** 3.2×10⁻³⁵ m (2 l_p)
**Bits:** ~18 bits
**Temperature:** 1.4×10³² K (Planck temperature)
**Evaporation time:** ~10⁴ Planck times (10⁻⁴⁰ s)

This is the critical threshold where quantum and gravitational effects balance. The "oscillator" regime.

---

### sgr_a_star()
```python
def sgr_a_star():
    return EncoderState(4.0e6 * M_sun, "Sgr A* (Milky Way center)")
```
**Mass:** 4×10⁶ M_sun
**Schwarzschild radius:** 1.2×10¹⁰ m (0.08 AU)
**Bits:** ~10⁹⁰
**Shadow size:** ~52 μas (microarcseconds) as seen from Earth

**See Also:** [Event-Horizon-Telescope-Observations](Event-Horizon-Telescope-Observations.md)

---

### m87_star()
```python
def m87_star():
    return EncoderState(6.5e9 * M_sun, "M87* (first imaged BH)")
```
**Mass:** 6.5×10⁹ M_sun
**Schwarzschild radius:** 1.9×10¹³ m (130 AU)
**Bits:** ~10⁹³
**Shadow size:** ~42 μas (first directly imaged in 2019)

**See Also:** [Event-Horizon-Telescope-Observations](Event-Horizon-Telescope-Observations.md)

---

### primordial_bh(mass_kg)
```python
def primordial_bh(mass_kg=1e12):
    return EncoderState(mass_kg, f"Primordial BH ({mass_kg:.0e} kg)")
```
**Default mass:** 10¹² kg (small mountain)
**Schwarzschild radius:** 1.5×10⁻¹⁵ m (subatomic)
**Evaporation time:** ~10¹⁰ years (comparable to age of universe)

Primordial black holes of this mass formed in the early universe would be evaporating today. Candidates for dark matter, though constraints are tight.

---

### custom_bh(mass_kg, label)
```python
def custom_bh(mass_kg, label="Custom"):
    return EncoderState(mass_kg, label)
```
**Usage:** Create black holes of arbitrary mass for parameter sweeps.

**Example:**
```python
# Sweep from Planck mass to supermassive
masses = np.logspace(np.log10(m_p), np.log10(1e10 * M_sun), 100)
encoders = [custom_bh(m, f"M={m:.2e}") for m in masses]
```

---

## Unit System

**All quantities use SI units throughout:**

| Quantity | SI Unit | Symbol |
|----------|---------|--------|
| Mass | kilogram | kg |
| Length | meter | m |
| Time | second | s |
| Energy | joule | J |
| Power | watt | W |
| Temperature | kelvin | K |
| Angle | steradian | sr |
| Information | bits or nats | bit / nat |

**Rationale:**
- Consistency: No unit conversions between modules
- Verifiability: Direct comparison to published values
- Transparency: No hidden factors of c, ℏ, or G set to 1

**Natural Units (Not Used Here):**
Many theoretical physics papers use units where c = ℏ = G = k_B = 1. We avoid this for clarity. To convert published formulas:
- Restore dimensions via dimensional analysis
- Check limiting cases (M → 0, M → ∞, M = M_planck)

---

## Design Choices

### Why SI Units?
- **Reproducibility:** Anyone can verify calculations against standard references (NIST, PDG)
- **Educational Value:** Students see the actual magnitudes, not dimensionless ratios
- **Error Detection:** Unit mismatches caught by dimensional analysis

### Why Dataclass?
- **Immutability:** Once created, encoder state doesn't change (black holes don't spontaneously gain mass in our model)
- **Properties:** Lazy evaluation — compute only what's requested
- **Composability:** Easy to store in lists, serialize to JSON

### Why Separate n_bits and n_nats?
- Different user communities: Information theorists use bits, physicists use nats
- Conversion factor ln(2) ≈ 0.693 is non-trivial; better to be explicit
- Prevents confusion about which entropy formula applies

### Why Include Luminosity?
- **Intermediate quantity:** Used to compute evaporation time and bit rate
- **Observable:** In principle detectable (though impractical for large BHs)
- **Pedagogical:** Shows Stefan-Boltzmann law extends to quantum gravity regime

---

## How to Extend

### Adding New Properties

To add a new encoder property (e.g., Kerr rotation parameter):

1. **Define property method:**
```python
@property
def kerr_spin(self) -> float:
    """Dimensionless spin parameter a/M."""
    # Requires additional parameter in __init__
    return self.angular_momentum / (self.mass_kg * c)
```

2. **Update docstring** with formula, units, physical meaning

3. **Add to summary()** if user-facing

4. **Write test** in test_core.py to validate against known limits

### Adding New Preset Encoders

```python
def ton618_bh():
    """TON 618 — one of the most massive known BHs."""
    return EncoderState(6.6e10 * M_sun, "TON 618")
```

### Extending to Rotating Black Holes

For Kerr black holes (angular momentum J ≠ 0):
- Add `angular_momentum: float = 0` to EncoderState
- Modify `schwarzschild_radius` → `outer_horizon_radius` (r₊)
- Account for ergosphere, superradiance
- Entropy formula changes: S = π(r₊² + a²) / A_p

**See Also:** [Kerr-Black-Holes](Kerr-Black-Holes.md)

### Adding Charge (Reissner-Nordström)

For charged black holes (Q ≠ 0):
- Add `charge_coulombs: float = 0`
- Account for electromagnetic stress-energy
- Entropy: S = π(r₊² + r₋²) / A_p
- Extremal limit: r₊ = r₋ (zero temperature, zero entropy rate)

---

## Validation Checklist

When modifying constants.py, verify:

- [ ] All formulas match published references (cite sources)
- [ ] Units are consistent (dimensional analysis)
- [ ] Planck mass gives N ≈ 18 bits (Test 2)
- [ ] Solar mass gives T_H ≈ 6×10⁻⁸ K
- [ ] Evaporation time scaling: t_evap ∝ M³ (Test 1, Test 4)
- [ ] Hawking temperature scaling: T_H ∝ 1/M
- [ ] Entropy scaling: N ∝ M² (Test 5)
- [ ] All property methods return finite values for M > 0

---

## References

1. Hawking, S. W. (1975). "Particle creation by black holes." *Commun. Math. Phys.* 43:199–220.
2. Bekenstein, J. D. (1973). "Black holes and entropy." *Phys. Rev. D* 7:2333–2346.
3. Wald, R. M. (1984). *General Relativity*. University of Chicago Press.
4. Thorne, K. S. (1994). *Black Holes and Time Warps*. W. W. Norton.

---

## See Also

- [Code-test_core.py.md](Code-test_core.py.md) — Analytical validation tests
- [Bekenstein-Hawking-Entropy](Bekenstein-Hawking-Entropy.md) — Entropy formula derivation
- [Hawking-Radiation](Hawking-Radiation.md) — Thermal emission mechanism
- [Planck-Units](Planck-Units.md) — Natural unit system
- [Gray-Code](Gray-Code.md) — Information-theoretic encoding
- [Rotary-Encoders](Rotary-Encoders.md) — Engineering analogy
- [The-Gray-Code-Universe-Hypothesis](The-Gray-Code-Universe-Hypothesis.md) — Theoretical framework

---

**Last Updated:** 2026-03-20
**Lines of Code:** 168
**Test Coverage:** 5/5 core tests pass (see test_core.py)
