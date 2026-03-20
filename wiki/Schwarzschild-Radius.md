# Schwarzschild Radius

## Definition

The **Schwarzschild radius** $r_s$ is the radius of the event horizon of a non-rotating (Schwarzschild) black hole. It defines the boundary beyond which nothing, not even light, can escape the black hole's gravitational pull.

$$r_s = \frac{2GM}{c^2}$$

where:
- $G = 6.674 \times 10^{-11}$ m³ kg⁻¹ s⁻² (gravitational constant)
- $M$ = mass of the black hole (kg)
- $c = 2.998 \times 10^{8}$ m/s (speed of light)

## Derivation: Escape Velocity Argument

### Classical (Newtonian) Intuition

For an object to escape a gravitational field, its kinetic energy must exceed the gravitational potential energy:

$$\frac{1}{2}mv^2 \geq \frac{GMm}{r}$$

Setting escape velocity $v = c$ (speed of light):

$$\frac{1}{2}mc^2 = \frac{GMm}{r}$$

Solving for $r$:

$$r = \frac{2GM}{c^2} = r_s$$

This is the **Schwarzschild radius**. Below this radius, even light cannot escape.

**Note**: This derivation is heuristic. The rigorous result comes from general relativity (Schwarzschild solution to Einstein's field equations, 1916).

### General Relativistic Derivation

The **Schwarzschild metric** (spherically symmetric, static spacetime) is:

$$ds^2 = -\left(1 - \frac{2GM}{c^2 r}\right)c^2 dt^2 + \left(1 - \frac{2GM}{c^2 r}\right)^{-1} dr^2 + r^2 d\Omega^2$$

At $r = r_s = 2GM/c^2$, the metric coefficient $g_{tt}$ vanishes and $g_{rr}$ diverges. This is a **coordinate singularity** (not a physical singularity — the curvature is finite). It marks the event horizon.

Outward-directed light rays at $r = r_s$ have zero radial velocity as measured by a distant observer — they're "frozen" at the horizon.

## Physical Meaning

The Schwarzschild radius is **not** a physical surface. It's a **one-way membrane** in spacetime:

- **Outside** ($r > r_s$): Timelike observers can escape to infinity
- **At** ($r = r_s$): Light cones tip over exactly 45° — outward light rays remain stationary (from external perspective)
- **Inside** ($r < r_s$): All future-directed paths lead toward $r = 0$ (the singularity). Escape is impossible — not due to insufficient velocity, but because "outward" is no longer a direction in spacetime.

An observer falling through the horizon experiences nothing special locally (no "surface"), but can never return or send signals outward.

## Numerical Values

| Object | Mass (kg) | Mass (M☉) | Schwarzschild Radius | Context |
|--------|-----------|-----------|---------------------|---------|
| **Earth** | $5.972 \times 10^{24}$ | $3.0 \times 10^{-6}$ | **8.87 mm** | Size of a marble |
| **Sun** | $1.989 \times 10^{30}$ | 1 | **2.95 km** | ~1.8 miles |
| **Sgr A*** | $7.96 \times 10^{36}$ | $4.0 \times 10^6$ | **12 million km** | ~17× Sun-Earth distance |
| **M87*** | $1.29 \times 10^{40}$ | $6.5 \times 10^9$ | **19.5 billion km** | ~130 AU (beyond Pluto) |
| **Planck mass** | $2.176 \times 10^{-8}$ | $1.1 \times 10^{-38}$ | **3.23 × 10⁻³⁵ m** | $2 l_p$ (Planck length) |

### Key Observations:

1. **$r_s \propto M$**: Schwarzschild radius scales linearly with mass.
2. **Earth as black hole**: Would fit in your pocket (9 mm radius).
3. **Planck mass**: At $M = m_p$, $r_s = 2l_p$ — the quantum gravity regime.

## Horizon Area and Entropy

The event horizon is a sphere of radius $r_s$:

$$A = 4\pi r_s^2 = 4\pi \left(\frac{2GM}{c^2}\right)^2 = \frac{16\pi G^2 M^2}{c^4}$$

**Bekenstein-Hawking entropy** is proportional to this area:

$$S = \frac{k_B A}{4 l_p^2} = \frac{k_B c^3 A}{4 \hbar G}$$

where $l_p = \sqrt{\hbar G / c^3} \approx 1.616 \times 10^{-35}$ m is the Planck length.

For a solar-mass black hole:
- $A = 1.097 \times 10^{14}$ m²
- $S \approx 1.53 \times 10^{77}$ k_B (nats) or $\approx 1.09 \times 10^{77}$ bits

This is an **enormous** entropy — the most entropic object in nature per unit mass.

## Time Dilation at the Horizon

Time dilation factor for a stationary observer at radius $r$:

$$\frac{dt_{far}}{dt_{local}} = \frac{1}{\sqrt{1 - r_s/r}}$$

As $r \to r_s$, time dilation $\to \infty$. An external observer sees infalling objects **freeze** at the horizon, taking infinite time to cross. The infalling observer crosses in finite proper time (~$10^{-5}$ s for solar-mass BH).

## Schwarzschild vs. Kerr

The Schwarzschild solution assumes:
- **Spherical symmetry** (non-rotating)
- **No charge** (electrically neutral)

Real astrophysical black holes rotate (angular momentum $J \neq 0$), described by the **Kerr metric**:

$$r_{\pm} = \frac{GM}{c^2} \pm \sqrt{\left(\frac{GM}{c^2}\right)^2 - \left(\frac{J}{Mc}\right)^2}$$

where $r_+$ is the outer horizon and $r_-$ is the inner (Cauchy) horizon. For $J = 0$, $r_+ = 2GM/c^2$ (Schwarzschild).

Maximal rotation (extremal Kerr): $J = GM^2/c$, giving $r_+ = GM/c^2 = r_s/2$. The ergosphere and frame-dragging effects are maximal.

## Connection to BlackOops

In the BlackOops encoder model:

- **$r_s$** is the **encoder radius** — the physical size of the "disk"
- **Horizon area** $A = 4\pi r_s^2$ determines **encoder positions** $N = A/(4l_p^2 \ln 2)$ (in bits)
- **Single-bit-flip constraint**: Each Planck area $l_p^2$ on the horizon is one encoder position. State transitions flip one bit per Planck time $t_p$.

For a solar-mass black hole:
- $r_s = 2.95$ km
- $A = 1.097 \times 10^{14}$ m²
- $N = 1.514 \times 10^{77}$ bits

The encoder has $10^{77}$ positions arranged on a sphere of radius 3 km, with angular resolution $4\pi / N \approx 8.3 \times 10^{-77}$ steradians per bit.

From `constants.py`:
```python
@property
def schwarzschild_radius(self) -> float:
    """Encoder physical radius [m]."""
    return 2 * G * self.mass_kg / c**2
```

## Observational Evidence

While we cannot directly "see" the Schwarzschild radius (it's a black void), the **photon sphere** at $r = 1.5 r_s$ and the **innermost stable circular orbit (ISCO)** at $r = 3 r_s$ (for Schwarzschild) produce observable signatures:

- **X-ray binaries**: Accretion disk emission peaks near ISCO
- **Gravitational waves**: LIGO detections show inspiral cutoff at ISCO before merger
- **Event Horizon Telescope**: M87* and Sgr A* shadow size is $\sim 2.6 r_s$ (photon sphere projected)

EHT measurements of M87* shadow diameter: $42 \pm 3$ microarcseconds, consistent with $r_s = 19.5$ billion km for $M = 6.5 \times 10^9 M_\odot$.

## Historical Context

- **1784**: John Michell proposes "dark stars" from which light cannot escape (Newtonian)
- **1796**: Pierre-Simon Laplace independently derives the same idea
- **1915**: Einstein publishes general relativity
- **1916**: Karl Schwarzschild derives exact solution for spherical black hole (while serving in WWI)
- **1958**: David Finkelstein shows $r_s$ is not a physical singularity, just a coordinate artifact
- **1964**: John Wheeler coins the term "black hole"
- **2015**: LIGO detects gravitational waves from black hole mergers
- **2019**: Event Horizon Telescope images M87* shadow

## See Also

- [[Bekenstein-Hawking Entropy]]
- [[Hawking Radiation]]
- [[Planck Units]]
- [[Kerr Black Holes]]
- [[Event Horizon Telescope Observations]]
- [[Holographic Principle]]

## References

1. Schwarzschild, K. (1916). "Über das Gravitationsfeld eines Massenpunktes nach der Einsteinschen Theorie". *Sitzungsberichte der Königlich Preussischen Akademie der Wissenschaften*, 189–196.
2. Misner, C. W., Thorne, K. S., & Wheeler, J. A. (1973). *Gravitation*. W. H. Freeman. (Chapter 31: Schwarzschild Geometry)
3. Wald, R. M. (1984). *General Relativity*. University of Chicago Press.
4. Carroll, S. M. (2004). *Spacetime and Geometry: An Introduction to General Relativity*. Addison-Wesley.
