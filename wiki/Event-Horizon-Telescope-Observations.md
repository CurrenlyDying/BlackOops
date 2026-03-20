# Event Horizon Telescope Observations

## Overview

The **Event Horizon Telescope (EHT)** is a planet-scale array of radio telescopes that uses **very long baseline interferometry (VLBI)** to achieve angular resolution comparable to the event horizon size of supermassive black holes.

**Key achievements**:
- **2019**: First image of a black hole shadow (M87*)
- **2022**: First image of Sagittarius A* (Sgr A*), the Milky Way's central black hole

These observations provide **direct visual evidence** of event horizons and serve as tests of general relativity in the strong-field regime.

## What Is a Black Hole Shadow?

Light rays passing near a black hole are deflected by gravity. Some rays:
- **Escape to infinity** (form the observed image)
- **Enter the event horizon** (disappear)
- **Orbit circularly** (photon sphere at $r = 3GM/c^2 = 1.5 r_s$ for Schwarzschild)

The **shadow** is the dark region in the sky corresponding to light rays captured by the black hole. Its boundary is formed by photons at the **photon sphere** — the innermost circular orbit for light.

### Shadow Size

For a **Schwarzschild black hole** viewed from infinity, the shadow radius is:

$$r_{shadow} = \sqrt{27} \frac{GM}{c^2} \approx 2.598 \, r_s$$

This is **larger** than the horizon radius $r_s = 2GM/c^2$ due to light bending (gravitational lensing amplifies the apparent size).

For a **Kerr black hole** (rotating), the shadow is:
- **Asymmetric** (offset due to frame dragging)
- **Dependent on spin** and viewing angle
- Size ranges from $\sim 2.5 r_s$ to $\sim 2.7 r_s$ depending on spin and inclination

## M87* Observation (2019)

### Target: Messier 87 Central Black Hole

**Properties**:
- Mass: $M = 6.5 \times 10^9 \, M_\odot = 1.3 \times 10^{40}$ kg
- Distance: $d = 16.8$ Mpc $= 5.5 \times 10^{25}$ m
- Schwarzschild radius: $r_s = 2GM/c^2 = 1.9 \times 10^{13}$ m $\approx 128$ AU $\approx 19.5$ billion km

**Angular size**:
$$\theta = \frac{r_{shadow}}{d} = \frac{2.6 r_s}{d} \approx \frac{2.6 \times 1.9 \times 10^{13}}{5.5 \times 10^{25}} \approx 42 \, \mu\text{as}$$

where $\mu$as = microarcsecond ($1 \mu$as = $1/3.6 \times 10^9$ degree).

**This is the angular size of a grapefruit on the Moon** as seen from Earth.

### Observation Details

- **Wavelength**: 1.3 mm (230 GHz radio)
- **Array**: 8 telescopes across 5 continents
- **Baseline**: Earth diameter $\sim 10,000$ km
- **Angular resolution**: $\sim 25 \, \mu$as (comparable to shadow size)
- **Data**: 5 petabytes (recorded April 2017, analyzed 2 years)

**Image features**:
- **Bright ring**: emission from hot accretion disk and photon sphere lensing
- **Dark shadow**: region where light is captured by event horizon
- **Asymmetry**: brighter on bottom (jet side), consistent with Doppler beaming and rotation

### Measured Shadow Size

$$\theta_{obs} = 42 \pm 3 \, \mu\text{as}$$

**Comparison to GR prediction**:
$$\theta_{GR} = 42 \, \mu\text{as}$$

**Agreement within $< 5\%$ uncertainty** — confirms general relativity in strong-field regime.

### Mass Estimate from Shadow

Inverting the relation $\theta = 2.6 r_s / d = 2.6 \times 2GM / (c^2 d)$:

$$M = \frac{\theta c^2 d}{5.2 G}$$

From shadow size: $M = (6.5 \pm 0.7) \times 10^9 \, M_\odot$

**Independent check**: Stellar dynamics in M87's core give $M \approx 6.6 \times 10^9 \, M_\odot$ — **consistent**.

### Bekenstein-Hawking Entropy

- Horizon area: $A = 4\pi r_s^2 = 4\pi (1.9 \times 10^{13})^2 \approx 4.5 \times 10^{27}$ m²
- Entropy: $S = A / (4 l_p^2) \approx 4.3 \times 10^{96}$ nats
- **Bit-count**: $N = S / \ln 2 \approx 6.4 \times 10^{96}$ bits

**This is the encoder's $N$** — the number of Planck-area positions on M87*'s horizon.

## Sgr A* Observation (2022)

### Target: Milky Way Central Black Hole

**Properties**:
- Mass: $M = 4.0 \times 10^6 \, M_\odot = 8.0 \times 10^{36}$ kg
- Distance: $d = 8.3$ kpc $= 2.6 \times 10^{20}$ m
- Schwarzschild radius: $r_s = 2GM/c^2 = 1.2 \times 10^{10}$ m $\approx 0.08$ AU $\approx 12$ million km

**Angular size**:
$$\theta = \frac{2.6 r_s}{d} \approx \frac{2.6 \times 1.2 \times 10^{10}}{2.6 \times 10^{20}} \approx 52 \, \mu\text{as}$$

**Larger angular size than M87*** (1600× closer, but 1600× less massive, so comparable apparent size).

### Observation Details

- **Wavelength**: 1.3 mm (same as M87*)
- **Array**: Enhanced to 11 telescopes
- **Data**: Observed April 2017 (same campaign as M87*), released May 2022
- **Challenge**: Sgr A* is **variable** on minute timescales (M87* is stable over days) due to shorter orbital period near horizon

### Image Features

- **Bright ring**: diameter $\sim 52 \, \mu$as
- **Dark shadow**: consistent with Schwarzschild prediction
- **Variability**: "hotspots" orbiting the black hole every $\sim 30$ minutes (orbital period at innermost stable circular orbit)

### Measured Shadow Size

$$\theta_{obs} = 51.8 \pm 2.3 \, \mu\text{as}$$

**GR prediction**: $\theta_{GR} = 52 \, \mu\text{as}$

**Agreement within $< 4\%$** — confirms GR at the Milky Way's center.

### Bekenstein-Hawking Entropy

- Horizon area: $A = 4\pi r_s^2 = 4\pi (1.2 \times 10^{10})^2 \approx 1.8 \times 10^{21}$ m²
- Entropy: $S = A / (4 l_p^2) \approx 1.7 \times 10^{90}$ nats
- **Bit-count**: $N = S / \ln 2 \approx 2.4 \times 10^{90}$ bits

### Spin Estimate

From the asymmetry and brightness distribution, Sgr A* has estimated spin:

$$\tilde{a} \sim 0.5 \text{ to } 0.9$$

(Moderate to high rotation). Schwarzschild ($\tilde{a} = 0$) is ruled out at high confidence.

## Comparison: M87* vs Sgr A*

| Property | M87* | Sgr A* | Ratio |
|----------|------|--------|-------|
| Mass ($M_\odot$) | $6.5 \times 10^9$ | $4.0 \times 10^6$ | 1625 |
| Distance (m) | $5.5 \times 10^{25}$ | $2.6 \times 10^{20}$ | 2115 |
| $r_s$ (m) | $1.9 \times 10^{13}$ | $1.2 \times 10^{10}$ | 1625 |
| Shadow angle ($\mu$as) | 42 | 52 | 0.81 |
| Entropy (bits) | $6.4 \times 10^{96}$ | $2.4 \times 10^{90}$ | $2.6 \times 10^6$ |
| Variability timescale | Days | Minutes | ~2000 |
| $T_H$ (K) | $1.5 \times 10^{-17}$ | $2.5 \times 10^{-14}$ | 1/1625 |
| $t_{evap}$ (years) | $\sim 10^{100}$ | $\sim 10^{91}$ | $\sim 10^9$ |

**Key insight**: Despite vastly different masses and distances, both have **comparable angular sizes** ($\sim 50 \, \mu$as) — this is why EHT targeted both.

## Tests of General Relativity

### 1. Shadow Size

**GR predicts**: $\theta = 2.6 r_s / d = 5.2 GM / (c^2 d)$

**Observed**: M87* and Sgr A* both match to $< 5\%$

**Alternative theories**:
- **Modified gravity** (e.g., scalar-tensor theories): Predict different shadow size
- **No horizon** (e.g., boson stars, gravastars): No shadow at all (emission from surface)
- **Naked singularity**: Shadow size depends on spin, could be much smaller

**Verdict**: GR confirmed. Alternatives constrained.

### 2. Photon Ring Structure

Higher-resolution future observations will resolve **photon ring substructure**:
- Primary ring (photons orbiting once)
- Secondary ring (photons orbiting twice)
- Tertiary ring (photons orbiting three times)
- ...

The ring spacing is **universal** (depends only on $GM/c^2$) — a **smoking gun** test of GR.

### 3. Spin and Frame Dragging

Asymmetry in shadow brightness probes:
- **Spin magnitude** $\tilde{a}$
- **Spin axis orientation**
- **Frame dragging** (Lense-Thirring effect near horizon)

M87*: $\tilde{a} \sim 0.9$ (high spin, aligned with jet)
Sgr A*: $\tilde{a} \sim 0.5$ to $0.9$ (moderate to high)

## Connection to BlackOops

The EHT observations provide **real data** for testing the encoder framework:

### 1. Bit-Count from Observed Mass

From $M = 6.5 \times 10^9 \, M_\odot$ (M87*):

$$N = \frac{4\pi (2GM/c^2)^2}{4 l_p^2 \ln 2} = \frac{4\pi G^2 M^2}{c^4 l_p^2 \ln 2}$$

**Calculation** (using `constants.py`):

```python
encoder_M87 = EncoderState(mass_kg=6.5e9 * M_sun)
print(encoder_M87.n_bits)  # Output: 6.4e96 bits
```

### 2. Evaporation Time

From `test_core.py`, the evaporation time for M87*:

$$t_{evap} = 5120 \pi G^2 M^3 / (\hbar c^4) \approx 1.8 \times 10^{104} \text{ s} \approx 5.7 \times 10^{96} \text{ years}$$

**Compare to age of universe**: $1.38 \times 10^{10}$ years

**Ratio**: $\sim 10^{86}$ — M87* will outlive the universe by a factor of $10^{86}$.

### 3. Angular Resolution as Encoder Resolution

The EHT resolves angles $\sim 25 \, \mu$as. The encoder's angular resolution is:

$$\Delta\theta_{encoder} = \frac{4\pi}{N} \text{ steradians}$$

For M87*:

$$\Delta\theta_{encoder} = \frac{4\pi}{6.4 \times 10^{96}} \approx 2 \times 10^{-96} \text{ sr}$$

**Linear angle**: $\sqrt{2 \times 10^{-96}} \approx 4 \times 10^{-49}$ radians $\approx 10^{-42} \, \mu$as

**EHT resolves $\sim 10^{42}$ encoder positions simultaneously** — vastly coarser than the Planck-scale structure.

**Implication**: We cannot directly observe single encoder bits. The EHT sees the horizon as a smooth continuum, not discrete pixels. Probing $l_p$-scale structure requires wavelengths $\sim l_p$ (Planck energy $\sim 10^{19}$ GeV), far beyond any technology.

### 4. Shadow Size as Test of Holographic Encoding

If the horizon encodes information holographically, the shadow size should be determined by the **area** (number of bits), not the volume.

**Prediction**: $\theta \propto r_s \propto M$ (area scaling)

**Observation**: M87* and Sgr A* both satisfy $\theta = 2.6 r_s / d$ to high precision.

**Alternative** (if information were volumetric): $\theta$ might depend on compactness $(r_s / r_{object})$ in non-trivial ways. Not observed.

### 5. Variability Timescale as Scrambling Time

Sgr A* varies on timescales $\sim 30$ minutes $\approx 1800$ s. This is the **orbital period** at the innermost stable circular orbit (ISCO):

$$t_{ISCO} = 2\pi \sqrt{r_{ISCO}^3 / (GM)}$$

For Schwarzschild, $r_{ISCO} = 6GM/c^2 = 3r_s$:

$$t_{ISCO} = 2\pi \sqrt{27 (GM/c^2)^3 / (GM)} = 2\pi \sqrt{27} \frac{GM}{c^3}$$

For Sgr A*:

$$t_{ISCO} \sim 2\pi \sqrt{27} \times \frac{6.67 \times 10^{-11} \times 8 \times 10^{36}}{(3 \times 10^8)^3} \approx 1800 \text{ s}$$

**Scrambling time** (information spreads across horizon):

$$t_{scramble} \sim \frac{r_s}{c} \log N \sim \frac{1.2 \times 10^{10}}{3 \times 10^8} \times \log(10^{90}) \sim 8000 \text{ s}$$

**Observed variability** ($\sim 1800$ s) is **faster than scrambling time** — suggests the variability is from matter orbiting, not information re-encoding on the horizon.

### 6. Future: Measuring Hawking Radiation?

M87* radiates at $T_H \sim 10^{-17}$ K (peak wavelength $\sim 10^{11}$ m, far radio). Luminosity:

$$L \sim 10^{-28} \text{ W}$$

**Flux at Earth**: $L / (4\pi d^2) \sim 10^{-79}$ W/m²

**Compare to CMB**: $\sim 10^{-6}$ W/m²

**Ratio**: $\sim 10^{-73}$ — Hawking radiation is **completely undetectable** for astrophysical black holes.

Only primordial black holes (mass $\lesssim 10^{12}$ kg) radiate detectable gamma rays.

## Future Improvements

### Next-Generation EHT (ngEHT)

- Add telescopes in Africa, South America → better coverage
- Extend to shorter wavelengths (0.87 mm) → higher resolution
- Space-based VLBI → baselines $> 10^5$ km

**Goals**:
- Resolve photon ring substructure
- Measure spin to $< 1\%$ precision
- Detect black hole "movies" (variability on minute timescales for Sgr A*)
- Test frame dragging quantitatively

### Gravitational Wave + EHT Synergy

If Sgr A* accretes a stellar-mass compact object:
- **LISA** (Laser Interferometer Space Antenna) detects gravitational waves
- **EHT** images the event horizon perturbation
- Combined: test GR in dynamical strong-field regime

## See Also

- [[Schwarzschild Radius]]
- [[Bekenstein-Hawking Entropy]]
- [[Kerr Black Holes]]
- [[Holographic Principle]]
- [[Frame Dragging]]
- [[Photon Sphere]]

## References

1. Event Horizon Telescope Collaboration (2019). "First M87 Event Horizon Telescope Results. I. The Shadow of the Supermassive Black Hole". *Astrophysical Journal Letters*, 875, L1.
2. Event Horizon Telescope Collaboration (2022). "First Sagittarius A* Event Horizon Telescope Results. I. The Shadow of the Supermassive Black Hole in the Center of the Milky Way". *Astrophysical Journal Letters*, 930, L12.
3. Akiyama, K., et al. (2019). "First M87 Event Horizon Telescope Results. VI. The Shadow and Mass of the Central Black Hole". *Astrophysical Journal Letters*, 875, L6.
4. Johannsen, T., et al. (2016). "Testing General Relativity with the Shadow Size of Sgr A*". *Physical Review Letters*, 116, 031101.
