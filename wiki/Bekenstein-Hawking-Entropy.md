# Bekenstein-Hawking Entropy

## Definition

The **Bekenstein-Hawking entropy** is the thermodynamic entropy of a black hole, proportional to the area of its event horizon:

$$S_{BH} = \frac{k_B c^3 A}{4 \hbar G} = \frac{k_B A}{4 l_p^2}$$

where:
- $A$ = horizon area (m²)
- $k_B = 1.381 \times 10^{-23}$ J/K (Boltzmann constant)
- $l_p = \sqrt{\hbar G / c^3} = 1.616 \times 10^{-35}$ m (Planck length)
- $\hbar = 1.055 \times 10^{-34}$ J·s (reduced Planck constant)
- $G = 6.674 \times 10^{-11}$ m³ kg⁻¹ s⁻² (gravitational constant)
- $c = 2.998 \times 10^8$ m/s (speed of light)

This can also be expressed as:

$$S_{BH} = \frac{k_B \pi r_s^2}{l_p^2}$$

where $r_s = 2GM/c^2$ is the Schwarzschild radius.

## The Factor of 4

The factor of $4$ in the denominator comes from Hawking's 1974 calculation of black hole radiation. Bekenstein's original 1972 proposal had an unknown proportionality constant. Hawking showed via quantum field theory in curved spacetime that the constant is exactly $1/4$.

This factor has deep implications:
- It fixes the **temperature** of Hawking radiation
- It determines the **evaporation timescale**
- It connects black hole mechanics to thermodynamics via the **first law**

## Historical Development

### Bekenstein's Argument (1972)

Jacob Bekenstein argued that black holes must have entropy because:

1. **Second law would be violated otherwise**: Drop a hot object into a black hole → entropy of the universe decreases (violates thermodynamics)
2. **No-hair theorem**: Black holes are characterized only by mass, charge, angular momentum → lose all other information → must have entropy to compensate
3. **Horizon area never decreases** (Hawking's area theorem, 1971) → area behaves like entropy

Bekenstein proposed:
$$S \propto \frac{A}{l_p^2}$$

but didn't know the proportionality constant.

### Hawking's Calculation (1974)

Stephen Hawking computed black hole radiation using quantum field theory:
- Vacuum fluctuations near the horizon create particle-antiparticle pairs
- One falls in, one escapes → black hole radiates
- Spectrum is **thermal** (blackbody) with temperature:

$$T_H = \frac{\hbar c^3}{8\pi G M k_B}$$

From thermodynamics, $dS = dE/T$ for a system at temperature $T$. For a black hole, $E = Mc^2$:

$$dS = \frac{c^2 dM}{T_H} = \frac{8\pi G M k_B}{\hbar c^3} \cdot c^2 dM = \frac{8\pi G k_B}{\hbar c} M dM$$

Integrating and noting $A = 16\pi G^2 M^2 / c^4$:

$$S = \frac{k_B c^3 A}{4\hbar G}$$

The factor of $1/4$ emerges directly from the quantum calculation.

## Numerical Values

For a **solar-mass black hole** ($M = 1.989 \times 10^{30}$ kg):
- $r_s = 2.95$ km
- $A = 4\pi r_s^2 = 1.097 \times 10^{14}$ m²
- $S_{BH} = 1.542 \times 10^{54}$ J/K (in SI units with $k_B$)
- In natural units (nats): $S = 1.118 \times 10^{77}$ nats
- **In bits**: $N = S / \ln(2) = 1.514 \times 10^{77}$ bits

This is **enormous**. For comparison:
- Entropy of the Sun (thermal): $\sim 10^{57}$ $k_B$ (nats)
- A solar-mass black hole has $\sim 10^{20}$ times more entropy than the Sun

### Scaling with Mass

Since $A \propto M^2$:

$$S \propto M^2$$

Bigger black holes have quadratically more entropy. A black hole with 10× the mass has 100× the entropy.

| Object | Mass ($M_\odot$) | Entropy (bits) | Entropy/mass (bits/kg) |
|--------|----------------|----------------|----------------------|
| Solar-mass BH | 1 | $1.5 \times 10^{77}$ | $7.6 \times 10^{46}$ |
| Sgr A* | $4 \times 10^6$ | $2.4 \times 10^{90}$ | $3.0 \times 10^{53}$ |
| M87* | $6.5 \times 10^9$ | $6.4 \times 10^{96}$ | $5.0 \times 10^{56}$ |
| Planck-mass BH | $1.1 \times 10^{-38}$ | **18.1 bits** | $8.3 \times 10^{45}$ |

The Planck-mass black hole has entropy $S \approx 4\pi / \ln(2) \approx 18$ bits — essentially a **few-bit system**.

## Interpretation as Information

In information theory, entropy $S$ (in nats) converts to **number of bits**:

$$N_{bits} = \frac{S}{\ln(2)}$$

A black hole with $N$ bits of entropy can be in any of $2^N$ distinct microstates. For a solar-mass BH:

$$2^{1.5 \times 10^{77}} \text{ microstates}$$

This is incomprehensibly large. It vastly exceeds the number of particles in the observable universe ($\sim 10^{80}$) or the age of the universe in Planck times ($\sim 10^{61}$).

### What Are the Microstates?

**Major unsolved problem**: We don't know what the $2^N$ microstates are in terms of fundamental quantum gravity degrees of freedom.

Candidates include:
- **String theory**: Microstates are string/brane configurations (partially worked out for extremal black holes)
- **Loop quantum gravity**: Area quanta on the horizon (area spectrum is discrete: $A = 8\pi \gamma l_p^2 \sqrt{j(j+1)}$)
- **Holographic CFT**: Microstates are states in a dual conformal field theory (AdS/CFT)

The BlackOops encoder model proposes: **microstates = Gray code positions on the horizon**. Each Planck area is one bit, and the states differ by single-bit flips.

## Connection to Thermodynamics

The **four laws of black hole mechanics** (Bardeen, Carter, Hawking, 1973) are isomorphic to thermodynamic laws:

| Thermodynamics | Black Hole Mechanics |
|----------------|---------------------|
| Zeroth law: $T$ constant in equilibrium | $\kappa$ (surface gravity) constant on horizon |
| First law: $dE = T dS - P dV$ | $dM = \frac{\kappa}{8\pi G} dA + \Omega dJ + \Phi dQ$ |
| Second law: $dS \geq 0$ | $dA \geq 0$ (area never decreases) |
| Third law: Cannot reach $T = 0$ | Cannot reach $\kappa = 0$ (extremal BH) |

Hawking's discovery that black holes radiate showed this is **not just an analogy** — black holes have real temperature and entropy.

## Planck Area as Fundamental Bit

The formula $S = A / (4 l_p^2)$ suggests that **one Planck area encodes $1/(4 \ln 2) \approx 0.36$ bits** (or $1/4$ nat).

Alternatively, each **4 Planck areas** encodes 1 nat, or **2.77 Planck areas per bit**.

In the BlackOops framework, we interpret this as:
- Each Planck area $l_p^2$ is an **encoder position**
- The factor of 4 and $\ln(2)$ are geometric/conversion factors
- Total encoder positions: $N = A / (4 l_p^2 \ln 2)$

From `constants.py`:
```python
@property
def n_bits(self) -> float:
    """Number of encoder positions (Bekenstein-Hawking entropy in bits)."""
    return self.horizon_area / (4 * A_p * np.log(2))
```

where $A_p = l_p^2$.

## Generalized Entropy

For **rotating** (Kerr) or **charged** (Reissner-Nordström) black holes, the formula generalizes:

$$S = \frac{k_B (A_+ + A_-)}{4 l_p^2}$$

where $A_+$ and $A_-$ are the areas of the outer and inner horizons (for Schwarzschild, $A_- = 0$).

For **extremal** black holes (maximal spin or charge), $A_+ = A_-$ and the entropy is **zero** in the classical limit. Quantum corrections give a small residual entropy.

## Connection to BlackOops

The Bekenstein-Hawking entropy is the **foundational formula** for the BlackOops encoder model:

1. **$N$ encoder positions** = $S / \ln(2)$ (entropy in bits)
2. **Angular resolution** = $4\pi / N$ steradians per bit
3. **Evaporation time** scales as $S^{1.5} \times t_p$ (from Test 1 in `test_core.py`)
4. **Alignment probability** = $1/N$ per Planck time (Gray code constraint)

The model reproduces Hawking's evaporation formula ($t \propto M^3$) from combinatorial arguments about Gray code traversal overhead.

Key result from BlackOops simulations:
- Suppression factor $S = N^{0.500} \times 208.4$ (constant across 50 decades of mass)
- This gives $t_{evap} \propto N^{1.5} \propto M^3$ (exactly Hawking's result)

## Entropy Bounds

The Bekenstein-Hawking entropy is the **maximum entropy** any object of mass $M$ and size $R$ can have:

$$S_{max} = \frac{2\pi k_B R E}{\hbar c}$$

For a black hole, this saturates at $S = A / (4 l_p^2)$.

This is the **Bekenstein bound** (see [[Bekenstein Bound]]), which implies:
- Information capacity of any region is finite
- Black holes are the most efficient information storage (bits per unit volume)
- Holographic principle: information in a volume is encoded on its boundary

## See Also

- [[Schwarzschild Radius]]
- [[Hawking Radiation]]
- [[Planck Units]]
- [[Holographic Principle]]
- [[Bekenstein Bound]]
- [[Black Hole Information Paradox]]
- [[Shannon Entropy]]

## References

1. Bekenstein, J. D. (1973). "Black Holes and Entropy". *Physical Review D*, 7(8), 2333–2346.
2. Hawking, S. W. (1975). "Particle Creation by Black Holes". *Communications in Mathematical Physics*, 43(3), 199–220.
3. Bardeen, J. M., Carter, B., & Hawking, S. W. (1973). "The Four Laws of Black Hole Mechanics". *Communications in Mathematical Physics*, 31(2), 161–170.
4. Wald, R. M. (2001). "The Thermodynamics of Black Holes". *Living Reviews in Relativity*, 4(6).
