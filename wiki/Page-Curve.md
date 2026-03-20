# [EXTENDED] Page Curve

## Overview

The **Page curve** describes how the entropy of Hawking radiation evolves as a black hole evaporates. It's named after physicist Don Page, who first calculated it in 1993.

The curve shows:
1. **Initial rise** (0 to Page time): Radiation entropy increases as black hole radiates
2. **Peak** at Page time $t_P \approx 0.3 t_{evap}$: Maximum radiation entropy
3. **Decline** (Page time to complete evaporation): Radiation entropy decreases back to zero
4. **Final state**: Pure state (zero entropy), preserving unitarity

## The Information Paradox Connection

### Hawking's 1975 Calculation

Hawking showed black hole radiation is **thermal** (blackbody spectrum):

$$\frac{dN}{d\omega} \propto \frac{1}{e^{\hbar\omega / k_B T_H} - 1}$$

Thermal radiation is **maximally mixed** (density matrix $\rho \propto I$):

$$S_{\text{radiation}} = k_B \log N_{\text{states}}$$

For $N$ photons radiated, $S \approx Nk_B$ → **entropy increases monotonically**.

**Problem**: If entropy keeps increasing, final state is mixed (high entropy), not pure (zero entropy). This violates **unitarity** (pure → mixed is non-unitary).

### Page's Resolution (1993)

Page argued the radiation cannot be **truly** thermal. Instead:

- **Early radiation** (before Page time): Looks thermal, entropy increases
- **Page time**: Radiation becomes entangled with black hole interior → entropy peaks
- **Late radiation**: Carries information, purifies early radiation → entropy decreases

The entropy of radiation **must** peak and decline to preserve unitarity.

## The Page Curve Formula

For a black hole evaporating from initial entropy $S_0$:

$$S_{\text{radiation}}(t) = \begin{cases}
\frac{t}{t_{evap}} S_0 & t < t_P \quad \text{(linear rise)} \\
S_0 - \frac{t - t_P}{t_{evap} - t_P} S_0 & t > t_P \quad \text{(linear decline)}
\end{cases}$$

**Page time**:
$$t_P \approx 0.3 t_{evap}$$

(More precisely, $t_P$ is when black hole entropy equals radiation entropy.)

### Key Features

1. **Peak entropy**: $S_{\text{max}} \approx 0.5 S_0$ (half of initial black hole entropy)
2. **Symmetry**: Rise and fall are not symmetric (rise is 30% of time, fall is 70%)
3. **Final state**: $S_{\text{radiation}}(t_{evap}) = 0$ (pure state restored)

## Physical Interpretation

### Before Page Time

- Black hole has entropy $S_{BH}(t) = S_0 (1 - t/t_{evap})$ (decreasing)
- Radiation has entropy $S_{rad}(t) \approx S_0 t / t_{evap}$ (increasing)
- **Interpretation**: Information is leaving BH and accumulating in radiation

### At Page Time

- $S_{BH} = S_{rad} = S_0/2$
- **Crossover**: From BH-dominated to radiation-dominated system

### After Page Time

- Radiation entropy **decreases** even though more photons are emitted
- **Mechanism**: Late photons are entangled with early photons → purification
- Total entropy $S_{BH} + S_{rad} + S_{correlations} = S_0$ (conserved)

## Calculating the Page Curve: Island Formula

In 2019-2020, the Page curve was **derived from first principles** using the **quantum extremal surface** (island formula):

$$S_{\text{radiation}} = \min \text{ext} \left[ \frac{\text{Area}(\partial I)}{4G\hbar} + S_{\text{bulk}}(I \cup R) \right]$$

where:
- $I$ is the **island** (region inside black hole contributing to radiation entropy)
- $\partial I$ is the island boundary (quantum extremal surface)
- $R$ is the external radiation region
- $S_{\text{bulk}}$ is von Neumann entropy of bulk matter

**Before Page time**: Island is empty ($I = \emptyset$) → $S = S_{\text{bulk}}(R)$ (thermal, increasing)

**After Page time**: Island is non-empty ($I \neq \emptyset$) → Area term dominates → $S \approx A/4G\hbar$ (BH entropy, decreasing)

This calculation **proved unitarity is preserved** and the Page curve is correct.

## Connection to BlackOops

The BlackOops encoder model provides a **combinatorial interpretation** of the Page curve:

### Encoder Unwinding

As black hole evaporates:
- **Bits released**: $n(t) = (t/t_{evap}) \times N$ (linear in time)
- **Bits remaining**: $N - n(t)$

**Radiation entropy** (information content of radiation):

$$S_{\text{rad}}(t) = n(t) \times k_B \ln 2 \quad \text{(bits emitted)}$$

**Black hole entropy**:

$$S_{BH}(t) = (N - n(t)) \times k_B \ln 2 \quad \text{(bits remaining)}$$

**But** the radiation is **entangled** with the BH. The actual entropy is:

$$S_{\text{rad}}(t) = \min(S_{\text{thermal}}, S_{BH}) = \min(n, N-n) \times k_B \ln 2$$

**Page time**: When $n = N - n$ → $n = N/2$ → $t_P = 0.5 t_{evap}$

(More accurate models give $t_P \approx 0.3 t_{evap}$ due to non-linear effects.)

### Gray Code Traversal

The Page curve reflects the **Gray code graph structure**:

- **Early evaporation**: Releasing bits from "outer layers" of encoder (high connectivity)
- **Late evaporation**: Releasing bits from "inner layers" (low connectivity, entangled with early bits)

The connectivity change causes the entropy peak and subsequent decline.

### From `test_alignment.py` Sim 4: Information Conservation

The simulation confirms:
- Total bits (BH + radiation) = constant = $N$
- No information is created or destroyed
- Encoder unwinding preserves unitarity

The Page curve **is** the encoder bit-count evolution.

## Numerical Example

**Solar-mass black hole**:
- Initial entropy: $S_0 = 1.514 \times 10^{77}$ bits
- Evaporation time: $t_{evap} = 6.619 \times 10^{74}$ s
- Page time: $t_P \approx 2.0 \times 10^{74}$ s (30% of lifetime)
- Peak radiation entropy: $S_{\text{max}} \approx 7.57 \times 10^{76}$ bits (half of initial)

At $t = t_P$:
- Black hole has emitted $\sim 50\%$ of its mass
- But radiation carries only $\sim 50\%$ of information (due to entanglement)
- Remaining 50% of information is encoded in **correlations** between early and late radiation

## Observational Prospects

**Direct observation impossible**: Solar-mass BH evaporates in $10^{67}$ years (far beyond universe age).

**Analog systems**:
- **Sonic black holes** in BEC: Create analog Hawking radiation, measure entropy
- **Optical black holes**: Simulate evaporation in nonlinear optics
- **Quantum simulators**: Build digital models of evaporating BH

**2019-2021**: Several groups observed Page-curve-like behavior in analog systems, confirming unitarity preservation.

## Scrambling Time

Related timescale: **scrambling time** $t_{\text{scramble}}$, when information is maximally spread across horizon:

$$t_{\text{scramble}} \sim \frac{r_s}{c} \log \left(\frac{S}{k_B}\right)$$

For solar-mass BH:

$$t_{\text{scramble}} \sim 10^{-4} \text{ s}$$

**Much faster** than Page time ($10^{74}$ s). Information scrambles **before** it escapes, ensuring it's encoded holographically.

## Connection to Quantum Error Correction

The Page curve is related to **quantum error correction**:

- **Early radiation** = **syndrome** (error information)
- **Late radiation** = **corrected qubits** (recovered information)
- **Island** = **code subspace** (protected information)

The black hole acts as a **quantum error-correcting code**, protecting information via entanglement structure (holography).

HaPPY code (Pastawski et al., 2015) is an explicit tensor network model showing how holography implements quantum error correction.

## Historical Development

- **1975**: Hawking shows BH radiation is thermal → information loss paradox
- **1993**: Don Page calculates that unitarity requires non-monotonic entropy (Page curve)
- **1997**: Maldacena's AdS/CFT suggests holography preserves unitarity
- **2007**: Hayden-Preskill protocol: Information escapes quickly after scrambling time
- **2019**: Penington, Almheiri et al. derive Page curve using island formula
- **2020**: Quantum extremal surfaces prove unitarity preservation

## Connection to BlackOops Framework

Test 4 in `test_alignment.py` (**Information Conservation**) implements a discrete Page curve:

```python
# Start with N-bit encoder
bits_in_BH = N
bits_in_radiation = 0

for step in range(evaporation_steps):
    # Release one bit
    bits_in_BH -= 1
    bits_in_radiation += 1

    # Radiation entropy (accounting for entanglement)
    S_rad = min(bits_in_radiation, bits_in_BH)

    # Check unitarity
    assert bits_in_BH + bits_in_radiation == N
```

The `min()` function captures the Page curve: entropy rises until halfway, then declines.

## See Also

- [[Hawking Radiation]]
- [[Black Hole Information Paradox]]
- [[Unitarity]]
- [[Holographic Principle]]
- [[Quantum Error Correction]]
- [[Information Scrambling Time]]

## References

1. Page, D. N. (1993). "Average Entropy of a Subsystem". *Physical Review Letters*, 71(9), 1291–1294.
2. Penington, G. (2020). "Entanglement Wedge Reconstruction and the Information Paradox". *Journal of High Energy Physics*, 2020(9), 2.
3. Almheiri, A., et al. (2020). "The Page Curve of Hawking Radiation from Semiclassical Geometry". *Journal of High Energy Physics*, 2020(3), 149.
4. Hayden, P., & Preskill, J. (2007). "Black Holes as Mirrors: Quantum Information in Random Subsystems". *Journal of High Energy Physics*, 2007(09), 120.
