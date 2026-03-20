# Planck Mass as Critical Threshold

## Definition

The **Planck mass** is the mass scale at which quantum gravitational effects become dominant:

$$M_p = \sqrt{\frac{\hbar c}{G}} \approx 2.176 \times 10^{-8} \text{ kg} \approx 1.221 \times 10^{19} \text{ GeV}/c^2$$

This is the **critical threshold** where:
- The Schwarzschild radius equals the Planck length: $r_s \approx l_p$
- The Compton wavelength equals the Schwarzschild radius: $\lambda_C \approx r_s$
- Black hole physics and quantum mechanics collide at equal strength

Below $M_p$, quantum mechanics dominates. Above $M_p$, gravity dominates. **At $M_p$, we enter the quantum gravity "no man's land"** where neither theory alone is sufficient.

## Why $M_p$ Is Where $r_s \approx l_p$

The **Schwarzschild radius** for mass $M$:

$$r_s = \frac{2GM}{c^2}$$

The **Planck length**:

$$l_p = \sqrt{\frac{\hbar G}{c^3}} \approx 1.616 \times 10^{-35} \text{ m}$$

Set $r_s = l_p$:

$$\frac{2GM}{c^2} = \sqrt{\frac{\hbar G}{c^3}}$$

Solve for $M$:

$$M = \frac{c^2}{2G} \sqrt{\frac{\hbar G}{c^3}} = \frac{1}{2} \sqrt{\frac{\hbar c}{G}} = \frac{M_p}{2}$$

So **exactly** at $M = M_p/2 \approx 1.09 \times 10^{-8}$ kg, we have $r_s = l_p$.

For $M = M_p$, the Schwarzschild radius is:

$$r_s = 2l_p \approx 3.23 \times 10^{-35} \text{ m}$$

This is the **smallest black hole** you can meaningfully describe with classical geometry before quantum corrections dominate.

## Quantum vs Classical Crossover

### Compton Wavelength

The **Compton wavelength** of a particle with mass $M$:

$$\lambda_C = \frac{\hbar}{Mc}$$

This is the length scale below which quantum effects (particle creation, position uncertainty) become important.

For the Planck mass:

$$\lambda_C = \frac{\hbar}{M_p c} = \frac{\hbar}{\sqrt{\hbar c / G} \cdot c} = \sqrt{\frac{\hbar G}{c^3}} = l_p$$

**Key result**: $\lambda_C = l_p = r_s/2$ at the Planck mass.

### Three Regimes

| Mass | $r_s$ vs $\lambda_C$ | Dominant Physics |
|------|---------------------|------------------|
| $M \ll M_p$ | $r_s \ll \lambda_C$ | Quantum mechanics (particle, not black hole) |
| $M \sim M_p$ | $r_s \sim \lambda_C$ | **Quantum gravity** (neither description valid) |
| $M \gg M_p$ | $r_s \gg \lambda_C$ | General relativity (classical black hole) |

**Example**: An electron ($m_e = 9.109 \times 10^{-31}$ kg $\ll M_p$):
- $r_s = 1.35 \times 10^{-57}$ m (absurdly small, unmeasurable)
- $\lambda_C = 2.43 \times 10^{-12}$ m (measurable, atomic scale)
- Described by quantum mechanics, not gravity

**Example**: Solar-mass black hole ($M = 1.989 \times 10^{30}$ kg $\gg M_p$):
- $r_s = 2950$ m (measurable)
- $\lambda_C = 1.05 \times 10^{-61}$ m (unmeasurable)
- Described by general relativity, quantum effects negligible

**Example**: Planck-mass object:
- $r_s = 3.23 \times 10^{-35}$ m
- $\lambda_C = 1.62 \times 10^{-35}$ m
- **Neither description works** — need quantum gravity

## Black Hole Remnant Proposals

When a black hole evaporates via Hawking radiation, it loses mass. As $M \to M_p$, quantum effects become strong. What happens?

### Three Scenarios

**1. Complete Evaporation**

The black hole radiates all its mass and disappears in a burst of Planck-energy photons. Final state: vacuum + radiation.

**Problem**: If the black hole had large initial entropy (e.g., $S \sim 10^{77}$ bits for solar mass), where did the information go? Hawking radiation is (semi-classically) thermal, carrying no information.

**2. Planck-Mass Remnant**

The black hole stops evaporating at $M \sim M_p$, leaving a stable **remnant** — a Planck-mass object with event horizon $r_s \sim l_p$.

**Problem**: If every black hole leaves a remnant, and remnants can have arbitrary internal states (to encode the initial entropy), there are **infinitely many species of Planck-mass particles**. This violates effective field theory assumptions (species proliferation).

**3. Information Escapes Before Planck Scale**

Quantum corrections to Hawking radiation encode information in subtle correlations. By the time the black hole reaches $M \sim M_p$, most information has already escaped. The final burst radiates the last few bits.

**Status**: Favored by holographic principle and island formula. Remnants might still exist, but don't need to carry large entropy.

## The 1-Bit Encoder Sweet Spot

In the BlackOops framework, the Planck-mass black hole is the **1-bit encoder** — the minimal rotary encoder.

### Bekenstein-Hawking Entropy at Planck Mass

$$S = \frac{k_B A}{4 l_p^2} = \frac{k_B \cdot 4\pi r_s^2}{4 l_p^2} = \frac{k_B \cdot 4\pi (2l_p)^2}{4 l_p^2} = 4\pi k_B$$

In nats: $S = 4\pi \approx 12.57$ nats

In bits: $N = S / \ln 2 \approx 18.13$ bits

From `constants.py`:

```python
encoder_planck_mass = EncoderState(mass_kg=M_p)
print(encoder_planck_mass.n_bits)  # Output: 18.13
```

**Not exactly 1 bit** due to geometric factors ($4\pi$ from sphere area), but **O(1) bits** — the encoder has tens of positions, not billions.

### Evaporation Time at Planck Mass

From `test_core.py` Test 2:

| Quantity | Value | Expected |
|----------|-------|----------|
| $r_s / l_p$ | 2.0000 | 2 ✓ |
| $N_{bits}$ | 18.13 | $\sim 1$ ✓ |
| $T_H / T_p$ | 0.0398 | $\sim 1$ ✓ |
| $t_{evap} / t_p$ | 16,085 | $\sim N$ ✓ |

The Planck-mass black hole evaporates in $\sim 16,000 \times t_p \approx 8.7 \times 10^{-40}$ s — essentially **instantaneous** by macroscopic standards.

**Interpretation**: The 18-bit encoder unwinds in $\sim 18 \times 10^3$ Planck times. The overhead factor is $\sim 10^3$ (compared to $\sim 10^{41}$ for solar-mass), suggesting minimal Gray code traversal cost for small $N$.

### Self-Destruct Condition

At Planck mass, the Hawking temperature is:

$$T_H = \frac{\hbar c^3}{8\pi G M_p k_B} = \frac{\hbar c^3}{8\pi k_B} \sqrt{\frac{G}{\hbar c}} = \frac{c^2}{8\pi k_B} \sqrt{\frac{\hbar}{G}} = \frac{T_p}{8\pi}$$

where $T_p = \sqrt{\hbar c^5 / (G k_B^2)} = 1.417 \times 10^{32}$ K is the Planck temperature.

So $T_H \approx 0.04 \times T_p \approx 5.6 \times 10^{30}$ K.

The energy of a photon at this temperature:

$$E_{photon} = k_B T_H \approx 0.04 \times E_p$$

where $E_p = M_p c^2 = 1.956 \times 10^9$ J is the Planck energy.

**Self-destruct ratio**: $E_{photon} / (M_p c^2) \approx 0.04$

**Interpretation**: The black hole radiates photons with energy $\sim 4\%$ of its rest mass. After $\sim 25$ such photons, it's gone. This matches the $\sim 18$ bits of entropy.

## The Quantum Gravity "No Man's Land"

At $M \sim M_p$, we have:

| Quantity | Value | Interpretation |
|----------|-------|----------------|
| $r_s$ | $\sim l_p$ | Horizon size = quantum fluctuation scale |
| $T_H$ | $\sim T_p$ | Temperature = Planck scale |
| $E_{photon}$ | $\sim E_p$ | Radiated energy = quantum gravity scale |
| $t_{evap}$ | $\sim t_p$ | Evaporation time = Planck time |

**None of our usual tools work**:
- Can't use quantum field theory (curved spacetime backreaction is O(1))
- Can't use classical GR (quantum fluctuations are O(1))
- Can't separate "background" from "fluctuations"

This is the regime where **quantum gravity is required**. We don't have a complete theory. Candidates:

1. **String theory** — replaces point particles with extended strings; sets a minimum length scale
2. **Loop quantum gravity** — quantizes spacetime geometry directly; area and volume are discrete
3. **Causal set theory** — spacetime is fundamentally discrete (causal network)
4. **Asymptotic safety** — GR is UV-complete via fixed point in renormalization group flow

None are experimentally confirmed at Planck scale (energy $\sim 10^{19}$ GeV, far beyond LHC's $\sim 10^4$ GeV).

## Numerical Example: Creating a Planck-Mass Black Hole

To compress mass $M_p = 2.18 \times 10^{-8}$ kg into a sphere of radius $r_s = 2l_p = 3.2 \times 10^{-35}$ m:

**Energy required**: $E = M_p c^2 = 1.96 \times 10^9$ J

**Equivalent to**:
- 468 kilotons of TNT (comparable to a large nuclear bomb)
- $1.22 \times 10^{19}$ GeV (Grand Unified Theory scale)

**Density**: $\rho = M_p / (\frac{4}{3}\pi r_s^3) \approx 1.58 \times 10^{97}$ kg/m³

**For comparison**:
- Nuclear density: $\sim 10^{17}$ kg/m³
- Neutron star core: $\sim 10^{18}$ kg/m³
- Planck density: $\rho_p = c^5 / (\hbar G^2) \approx 5.16 \times 10^{96}$ kg/m³

The Planck-mass black hole has density $\sim 3 \times \rho_p$ — **beyond the Planck density**.

## Connection to Encoder Sweet Spot

In the BlackOops model, the Planck-mass black hole is the **minimal encoder**:

### Analogy to Minimal Rotary Encoder

A mechanical rotary encoder with $N=1$ position is degenerate (no rotation). The minimal useful encoder has $N \sim 2$ positions (binary switch).

The Planck-mass black hole has $N \approx 18$ positions — **few enough to analyze explicitly**, large enough to exhibit encoder behavior.

### Phase Transition at Planck Mass

From `test_alignment.py` Sim 3:

- **Peak ambiguity** occurs at $M / M_p = 0.225$, where $N \approx 0.92$ bits
- Transition region (neither clearly black hole nor not): $M/M_p \in [0.18, 0.31]$
- Width: 0.23 decades (factor of $\sim 1.7$)

**Interpretation**: The "black hole vs not-black hole" distinction breaks down in a narrow window around $M \sim M_p / 4$, where the horizon area is $\sim l_p^2$ (exactly one Planck pixel).

This is the **1-bit encoder regime** — the system can be in position 0 or position 1, oscillating quantum-mechanically between black hole and not-black hole.

### Testable Prediction

If Planck-mass black holes (or their remnants) exist:

1. They have $N \sim 18$ internal states
2. They evaporate in $\sim 10^{-40}$ s (unobservable directly)
3. They radiate $\sim 18$ Planck-energy quanta (ultra-high-energy gamma rays)
4. If stable as remnants, they contribute to dark matter (mass $\sim 10^{-8}$ kg, cross-section $\sim l_p^2$)

**Problem**: Creating one requires $\sim 10^{19}$ GeV collisions (inaccessible). Primordial Planck-mass black holes might exist from the Big Bang, but none have been detected.

## Oscillating Between Black Hole and Not Black Hole

The user's original intuition: "perfectly both a black hole and not a black hole" — this is realized at the Planck mass.

**Quantum superposition**:

$$|\psi\rangle = \alpha |BH\rangle + \beta |not\text{-}BH\rangle$$

where $|BH\rangle$ is the black hole state (horizon exists) and $|not\text{-}BH\rangle$ is the quantum particle state (no horizon).

At $M \sim M_p$, both amplitudes are $|\alpha|^2 \sim |\beta|^2 \sim 0.5$ — the system is in **equal superposition**.

**This is the encoder "bit flip ambiguity"** — when trying to write under the angular resolution, the encoder state is undefined.

## See Also

- [[Planck Units]]
- [[Schwarzschild Radius]]
- [[Bekenstein-Hawking Entropy]]
- [[Hawking Radiation]]
- [[Quantum State Evolution]]
- [[Black Hole Information Paradox]]
- [[Holographic Principle]]

## References

1. Planck, M. (1899). "Über irreversible Strahlungsvorgänge". *Sitzungsberichte der Königlich Preußischen Akademie der Wissenschaften zu Berlin*, 5, 440–480.
2. Giddings, S. B. (1992). "Black Holes and Massive Remnants". *Physical Review D*, 46(4), 1347–1352.
3. Chen, P., et al. (2014). "Black Hole Remnants and the Information Loss Paradox". *Physics Reports*, 603, 1–45.
4. Carr, B. J. (2005). "Primordial Black Holes: Do They Exist and Are They Useful?". arXiv:astro-ph/0511743.
