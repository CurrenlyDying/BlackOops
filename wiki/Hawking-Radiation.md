# Hawking Radiation

## Overview

**Hawking radiation** is the thermal radiation predicted to be emitted by black holes due to quantum effects near the event horizon. Discovered by Stephen Hawking in 1974, it implies that black holes are not perfectly black — they glow with a faint thermal spectrum and gradually evaporate.

## Physical Mechanism

### Virtual Particle Pair Creation

In quantum field theory, the vacuum is not empty — it seethes with virtual particle-antiparticle pairs that spontaneously appear and annihilate on timescales $\Delta t \sim \hbar / E$ (Heisenberg uncertainty).

Near a black hole horizon:

1. A virtual pair is created just outside the horizon
2. Before the pair can recombine, one particle falls into the black hole (negative energy relative to infinity)
3. The other particle escapes to infinity (positive energy)
4. The black hole loses mass equal to the escaped particle's energy

From an external observer's perspective, the black hole has **radiated a particle**.

### Hawking Temperature

The radiation spectrum is **thermal** (Planckian blackbody) with temperature:

$$T_H = \frac{\hbar c^3}{8\pi G M k_B}$$

where:
- $M$ = black hole mass (kg)
- $k_B = 1.381 \times 10^{-23}$ J/K (Boltzmann constant)
- $\hbar = 1.055 \times 10^{-34}$ J·s (reduced Planck constant)
- $G = 6.674 \times 10^{-11}$ m³ kg⁻¹ s⁻² (gravitational constant)
- $c = 2.998 \times 10^8$ m/s (speed of light)

**Key feature**: $T_H \propto 1/M$ — smaller black holes are hotter.

## Numerical Values

| Object | Mass ($M_\odot$) | $T_H$ (K) | $T_H$ (eV) | Peak wavelength |
|--------|----------------|-----------|-----------|----------------|
| **Solar-mass BH** | 1 | $6.17 \times 10^{-8}$ K | $5.3 \times 10^{-12}$ eV | 47 km (radio) |
| **Earth-mass BH** | $3.0 \times 10^{-6}$ | $0.02$ K | $1.7 \times 10^{-6}$ eV | 140 m (radio) |
| **Mountain** ($10^{12}$ kg) | $5.0 \times 10^{-18}$ | $1.2 \times 10^{14}$ K | $10^{10}$ eV | 24 pm (gamma ray) |
| **Planck-mass BH** | $1.1 \times 10^{-38}$ | $1.42 \times 10^{32}$ K | $1.2 \times 10^{28}$ eV | $1.6 \times 10^{-35}$ m ($l_p$) |

### Astrophysical Black Holes Are Freezing

A solar-mass black hole radiates at $6 \times 10^{-8}$ K — **far colder than the cosmic microwave background** (CMB at 2.725 K). It **absorbs** more CMB photons than it emits, so it **grows** rather than evaporates in the current universe.

A black hole will only evaporate when the CMB cools below $T_H$, which requires the universe to expand by a factor of $\sim 10^7$ (age $\sim 10^{20}$ years).

### Primordial Black Holes Are Hot

Small black holes (mass $\lesssim 10^{12}$ kg) are hot enough to radiate gamma rays. If they exist, they could be detectable via:
- Gamma-ray bursts
- Antimatter annihilation signatures
- Distortion of dark matter distribution

No primordial black holes have been conclusively detected.

## Luminosity (Power Radiated)

Using the **Stefan-Boltzmann law** for a blackbody:

$$L = \sigma A T^4$$

where $\sigma = \pi^2 k_B^4 / (60 \hbar^3 c^2) = 5.67 \times 10^{-8}$ W m⁻² K⁻⁴ is the Stefan-Boltzmann constant (with quantum corrections for black hole spacetime).

For a black hole:
- Area: $A = 4\pi r_s^2 = 16\pi G^2 M^2 / c^4$
- Temperature: $T_H = \hbar c^3 / (8\pi G M k_B)$

Substituting and simplifying:

$$L = \frac{\hbar c^6}{15360 \pi G^2 M^2}$$

**Key scaling**: $L \propto 1/M^2$ — smaller black holes radiate vastly more power.

### Examples:

| Mass | Luminosity | Equivalent |
|------|-----------|-----------|
| $1 M_\odot$ | $9 \times 10^{-29}$ W | Single infrared photon per year |
| $10^{12}$ kg (mountain) | $3.6 \times 10^{11}$ W | ~360 MW (power plant) |
| $10^9$ kg | $3.6 \times 10^{17}$ W | ~10⁴ nuclear bombs per second |
| $m_p$ (Planck mass) | $3.6 \times 10^{52}$ W | ~Planck power |

## Evaporation Timescale

The black hole loses mass $dM/dt = -L/c^2$:

$$\frac{dM}{dt} = -\frac{\hbar c^4}{15360 \pi G^2 M^2}$$

Integrating from initial mass $M_0$ to zero:

$$t_{evap} = \frac{5120 \pi G^2 M_0^3}{\hbar c^4}$$

**Key scaling**: $t_{evap} \propto M^3$ — evaporation time increases cubically with mass.

### Examples:

| Initial Mass | Evaporation Time | Context |
|-------------|-----------------|---------|
| $1 M_\odot$ | $2.1 \times 10^{67}$ years | $10^{57} \times$ age of universe |
| $1 M_\oplus$ (Earth) | $5.7 \times 10^{50}$ years | Still impossibly long |
| $10^{12}$ kg | 2.6 billion years | Comparable to Earth's age |
| $10^9$ kg | 83 seconds | Observable in real-time |
| $m_p$ | $5.4 \times 10^{-44}$ s | One Planck time |

A Planck-mass black hole **radiates one Planck-energy photon and disappears in one Planck time**. This is the "one-bit encoder" regime.

## Spectrum and Particle Content

Hawking radiation is not monochromatic — it has a **thermal (blackbody) spectrum**:

$$\frac{dN}{d\omega} \propto \frac{1}{e^{\hbar\omega / k_B T_H} - 1}$$

for bosons (photons, gravitons). Fermions have a Fermi-Dirac spectrum.

Particle species radiated:
- **Photons** (massless): Always radiated
- **Gravitons** (massless): Always radiated (in principle, though not yet detected)
- **Neutrinos** (nearly massless): Radiated if $k_B T_H > m_\nu c^2$
- **Massive particles**: Radiated if $k_B T_H > mc^2$ (e.g., electrons, muons, quarks for hot black holes)

For solar-mass black holes, only photons and gravitons are radiated (temperature too low for massive particles). For Planck-mass black holes, all Standard Model particles are radiated.

## Information Paradox

Hawking's original 1975 calculation suggested the radiation is **purely thermal** — it contains no information about what fell into the black hole. If true, this would:

1. **Violate unitarity** (quantum evolution must be reversible)
2. **Lose information** (the $2^N$ microstates are indistinguishable in the radiation)
3. **Break quantum mechanics** fundamentally

This is the **black hole information paradox**.

**Current consensus** (post-2020): Information **is** encoded in the radiation via subtle quantum correlations. The resolution involves:
- **Island formula** (quantum extremal surfaces)
- **Page curve** (entropy of radiation first increases, then decreases)
- **Holographic principle** (information was never inside the black hole, always on the horizon)

The BlackOops model sides with information conservation: bits are released one at a time via Gray code unwinding, preserving unitarity.

## Connection to BlackOops

In the encoder model, Hawking radiation is the **release of encoder bits** at a rate constrained by Gray code overhead:

### Key Formulas from `constants.py`:

```python
@property
def hawking_temperature(self) -> float:
    """Hawking temperature [K]."""
    return hbar * c**3 / (8 * pi * G * self.mass_kg * k_B)

@property
def evaporation_time(self) -> float:
    """Total Hawking evaporation time [s]."""
    return 5120 * pi * G**2 * self.mass_kg**3 / (hbar * c**4)
```

### BlackOops Test Results:

From `test_core.py` Test 1:

| Mass | $N$ bits | $t_{evap}$ (Hawking) | Suppression $S$ |
|------|---------|---------------------|----------------|
| $1 M_\odot$ | $1.5 \times 10^{77}$ | $6.6 \times 10^{74}$ s | $N^{0.500} \times 208.4$ |
| $M_p$ | 18 | $8.7 \times 10^{-40}$ s | $N^{0.500} \times 208.4$ |

**Interpretation**:
- Naive expectation: 1 bit per Planck time → $t = N \times t_p$
- Actual: $t = N^{1.5} \times t_p / 208.4$
- Overhead factor: $\sqrt{N}$ (diffusive process on Gray code graph)

The $N^{1.5}$ scaling exactly reproduces Hawking's $M^3$ formula (since $N \propto M^2$).

### Gray Code Constraint

Each bit flip requires:
1. Quantum state to evolve continuously (unitary)
2. Only one Planck area changes per Planck time
3. Total $N$ bits must be released sequentially

The $\sqrt{N}$ overhead suggests **diffusive** spreading of information across the horizon before it can escape, analogous to a random walk with cover time $\sim N^{3/2}$ on a 2D surface.

## Page Time and Scrambling Time

Two important timescales:

1. **Page time** $t_{Page}$: When the black hole has evaporated half its entropy. For a black hole starting at mass $M_0$:

$$t_{Page} \approx 0.3 \times t_{evap}$$

Before $t_{Page}$, the radiation's entropy increases. After $t_{Page}$, it decreases (purification begins).

2. **Scrambling time** $t_{scramble}$: Time for information to spread across the horizon and become encoded in Hawking radiation:

$$t_{scramble} \sim r_s \log(S / k_B) / c$$

For a solar-mass BH: $t_{scramble} \sim 10^{-4}$ s. Much faster than evaporation.

## Experimental Prospects

Direct detection of Hawking radiation from astrophysical black holes is **impossible** with current technology (signal $\sim 10^{-29}$ W drowned by CMB).

Alternative approaches:
- **Analog gravity**: Simulate black hole horizons in BECs, water waves, optical systems (phonon/ripple Hawking radiation)
- **Primordial black holes**: Search for gamma-ray bursts from evaporating PBHs
- **Tabletop experiments**: Quantum simulators mimicking curved spacetime

**Analog Hawking radiation has been observed** in sonic black holes (2016, Steinhauer) and optical systems (2019, various groups).

## See Also

- [[Bekenstein-Hawking Entropy]]
- [[Black Hole Information Paradox]]
- [[Stefan-Boltzmann Law]]
- [[Unitarity]]
- [[Page Curve]]
- [[Analog Gravity Models]]
- [[Planck Units]]

## References

1. Hawking, S. W. (1974). "Black Hole Explosions?". *Nature*, 248(5443), 30–31.
2. Hawking, S. W. (1975). "Particle Creation by Black Holes". *Communications in Mathematical Physics*, 43(3), 199–220.
3. Page, D. N. (1976). "Particle Emission Rates from a Black Hole: Massless Particles from an Uncharged, Nonrotating Hole". *Physical Review D*, 13(2), 198–206.
4. Unruh, W. G. (1981). "Experimental Black-Hole Evaporation?". *Physical Review Letters*, 46(21), 1351–1353.
5. Almheiri, A., et al. (2020). "The Entropy of Hawking Radiation". *Reviews of Modern Physics*, 93, 035002.
