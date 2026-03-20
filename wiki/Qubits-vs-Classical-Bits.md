# Qubits vs Classical Bits

## Classical Bit

A **classical bit** is the fundamental unit of classical information. It can be in one of two states:

$$b \in \{0, 1\}$$

**Properties**:
- **Definite state**: Always in 0 or 1, never both
- **Copyable**: Can duplicate bits without restriction (e.g., $0 \to 00$)
- **Measurable**: Reading a bit doesn't change its value
- **Independent**: $N$ bits have $2^N$ possible states, all distinguishable

**Physical realizations**:
- Voltage levels (high/low)
- Magnetic domains (up/down)
- Optical intensity (bright/dark)
- Mechanical position (hole/no hole in punch card)

## Qubit (Quantum Bit)

A **qubit** is the fundamental unit of quantum information. Its state is a **superposition** of $|0\rangle$ and $|1\rangle$:

$$|\psi\rangle = \alpha |0\rangle + \beta |1\rangle$$

where $\alpha, \beta \in \mathbb{C}$ (complex amplitudes) and $|\alpha|^2 + |\beta|^2 = 1$ (normalization).

**Properties**:
- **Superposition**: Can be in both 0 and 1 simultaneously
- **Continuous state space**: Infinite possible states (parameterized by $\alpha, \beta$ on the Bloch sphere)
- **Non-copyable**: No-cloning theorem forbids $|\psi\rangle \to |\psi\rangle \otimes |\psi\rangle$
- **Measurement collapses**: Reading a qubit changes its state (to $|0\rangle$ or $|1\rangle$ with probabilities $|\alpha|^2$ and $|\beta|^2$)

**Physical realizations**:
- Spin of an electron (up/down)
- Polarization of a photon (horizontal/vertical)
- Energy levels of an atom (ground/excited)
- Superconducting circuits (current clockwise/counterclockwise)

## Superposition

### Classical Probability vs Quantum Superposition

**Classical bit with uncertainty**:
- 50% chance of 0, 50% chance of 1
- State: $(0.5, 0.5)$ (probability distribution)
- **Interpretation**: The bit is actually 0 or 1, we just don't know which (epistemic uncertainty)

**Quantum qubit in superposition**:
- State: $|\psi\rangle = \frac{1}{\sqrt{2}}(|0\rangle + |1\rangle)$
- **Interpretation**: The qubit is **genuinely in both states** until measured (ontological superposition)

**Key difference**: Quantum amplitudes $\alpha, \beta$ can **interfere** (add constructively/destructively). Classical probabilities cannot interfere.

### Interference Example

Consider two paths for a qubit:
- Path A: $|0\rangle \to |1\rangle$ (amplitude $a$)
- Path B: $|0\rangle \to |1\rangle$ (amplitude $b$)

**Classical**: Probabilities add: $P(1) = |a|^2 + |b|^2$

**Quantum**: Amplitudes add: $A(1) = a + b$, then $P(1) = |a + b|^2 = |a|^2 + |b|^2 + 2\text{Re}(a^*b)$

**Interference term** $2\text{Re}(a^*b)$ can be:
- Positive (constructive interference) → $P(1) > |a|^2 + |b|^2$
- Negative (destructive interference) → $P(1) < |a|^2 + |b|^2$

**Canonical example**: Double-slit experiment — interference fringes arise from quantum superposition of paths.

## Entanglement

### Definition

Two qubits are **entangled** if their joint state cannot be written as a product of individual states.

**Separable state** (not entangled):
$$|\psi\rangle = (a|0\rangle + b|1\rangle) \otimes (c|0\rangle + d|1\rangle) = ac|00\rangle + ad|01\rangle + bc|10\rangle + bd|11\rangle$$

**Entangled state** (Bell state):
$$|\Phi^+\rangle = \frac{1}{\sqrt{2}}(|00\rangle + |11\rangle)$$

**Cannot** be factored into $|\psi_A\rangle \otimes |\psi_B\rangle$.

### EPR Paradox and Non-Locality

Einstein, Podolsky, and Rosen (1935) argued that entanglement implies **spooky action at a distance**:

1. Prepare entangled pair: $|\Phi^+\rangle = \frac{1}{\sqrt{2}}(|00\rangle + |11\rangle)$
2. Send qubit A to Alice, qubit B to Bob (separated by light-years)
3. Alice measures qubit A → gets 0 or 1 (random, 50/50)
4. Bob measures qubit B → **always gets the same result as Alice**

**EPR's objection**: How does Bob's qubit "know" what Alice measured, faster than light?

**Resolution** (Bell's theorem, 1964): Quantum mechanics is **non-local** — correlations exist that cannot be explained by classical hidden variables. But **no faster-than-light signaling** is possible (Alice cannot send information to Bob via entanglement alone).

### Entanglement Entropy

For a bipartite system (A + B) in pure state $|\Psi\rangle_{AB}$, the **entanglement entropy** is:

$$S_A = -\text{Tr}(\hat{\rho}_A \log \hat{\rho}_A)$$

where $\hat{\rho}_A = \text{Tr}_B(|\Psi\rangle\langle\Psi|)$ is the **reduced density matrix** of subsystem A.

**For separable states**: $S_A = 0$ (no entanglement)

**For maximally entangled states**: $S_A = \log_2 d$ (where $d$ = dimension of A's Hilbert space)

**Example**: Bell state $|\Phi^+\rangle = \frac{1}{\sqrt{2}}(|00\rangle + |11\rangle)$

$$\hat{\rho}_A = \text{Tr}_B(|\Phi^+\rangle\langle\Phi^+|) = \frac{1}{2}(|0\rangle\langle 0| + |1\rangle\langle 1|) = \frac{1}{2}\hat{I}$$

$$S_A = -\frac{1}{2}\log_2(1/2) - \frac{1}{2}\log_2(1/2) = 1 \text{ bit}$$

**Maximal entanglement**: Each qubit carries 1 bit of entanglement entropy.

## No-Cloning Theorem

### Statement

**There is no quantum operation that can copy an arbitrary unknown quantum state**:

$$\text{No unitary } \hat{U} \text{ such that } \hat{U}(|\psi\rangle \otimes |0\rangle) = |\psi\rangle \otimes |\psi\rangle \text{ for all } |\psi\rangle$$

### Proof (Sketch)

Assume a cloning machine exists: $\hat{U}(|\psi\rangle \otimes |0\rangle) = |\psi\rangle \otimes |\psi\rangle$.

For two states $|\psi\rangle$ and $|\phi\rangle$:

$$\hat{U}(|\psi\rangle \otimes |0\rangle) = |\psi\rangle \otimes |\psi\rangle$$
$$\hat{U}(|\phi\rangle \otimes |0\rangle) = |\phi\rangle \otimes |\phi\rangle$$

Take inner product:

$$\langle\psi|\phi\rangle = \langle\psi \otimes 0 | \phi \otimes 0\rangle = \langle\psi \otimes \psi | \phi \otimes \phi\rangle = \langle\psi|\phi\rangle^2$$

This implies $\langle\psi|\phi\rangle = 0$ or $1$ — only orthogonal or identical states can be cloned. **Arbitrary unknown states cannot be cloned**.

### Consequences

1. **Quantum information is fragile**: Cannot make backup copies of an unknown qubit
2. **Measurement is destructive**: Reading a qubit changes it (no "peeking" at quantum state)
3. **Quantum cryptography**: Eavesdropper cannot copy quantum key without being detected (BB84 protocol)
4. **Black hole information paradox**: Cannot clone Hawking radiation and horizon state simultaneously (entanglement monogamy)

### Classical vs Quantum

**Classical bits**: Can copy freely ($b \to b \otimes b$)

**Qubits**: Cannot copy unknown states (no-cloning)

**BUT**: Can **teleport** a quantum state (transfer $|\psi\rangle$ from Alice to Bob via entanglement + classical communication).

## Quantum Information in Black Holes

### Horizon as Quantum Memory

In the BlackOops framework:
- Each Planck area $l_p^2$ is a **qubit** (can store 1 bit of quantum information)
- Total qubits on horizon: $N = A / (4 l_p^2 \ln 2) \approx 10^{77}$ (solar mass)
- State is a **superposition** over $2^N$ configurations

**Classical interpretation**: Horizon is in one of $2^N$ microstates (we don't know which)

**Quantum interpretation**: Horizon is in **superposition** of all $2^N$ microstates

$$|\Psi_{horizon}\rangle = \sum_{i=1}^{2^N} \alpha_i |i\rangle$$

with $\sum_i |\alpha_i|^2 = 1$.

### Entanglement Between Horizon and Radiation

As Hawking radiation is emitted:
- **Early radiation**: Entangled with late radiation (purification)
- **Horizon**: Entangled with external radiation (holographic encoding)

**Total state** (black hole + radiation) is **pure**:

$$|\Psi_{total}\rangle = \sum_{ij} c_{ij} |BH_i\rangle \otimes |rad_j\rangle$$

**Subsystem states** (black hole alone, radiation alone) are **mixed** (appear thermal).

**No-cloning constraint**: Cannot copy the entanglement (attempting to clone the radiation would violate no-cloning theorem).

### Information Paradox Resolution

Hawking's original argument (1975):
- Radiation is thermal (classical randomness) → entropy $S_{rad} \to \infty$ as black hole evaporates
- Initial state was pure (entropy $S_0 = 0$) → **information lost**

**Quantum resolution**:
- Radiation is **entangled** with itself and the black hole (quantum correlations)
- Entropy of radiation increases, then **decreases** (Page curve) → **information preserved**
- No-cloning ensures consistency: Cannot have independent copies of information in radiation and on horizon

**BlackOops model**: Encoder bits are released sequentially, maintaining entanglement. Total quantum state is pure throughout evaporation.

From `test_alignment.py` Sim 4: Total bit-count conserved → **unitarity preserved**.

## Quantum vs Classical: Summary Table

| Property | Classical Bit | Qubit |
|----------|--------------|-------|
| States | 0 or 1 (discrete) | $\alpha\|0\rangle + \beta\|1\rangle$ (continuous) |
| Superposition | No (probabilistic mixture) | Yes (coherent superposition) |
| Measurement | Non-destructive | Destructive (collapses state) |
| Cloning | Yes (copy freely) | No (no-cloning theorem) |
| Entanglement | No | Yes (non-local correlations) |
| $N$-bit state space | $2^N$ distinguishable states | $2^N$-dimensional Hilbert space |
| Information capacity | $N$ bits (can read all) | $N$ bits (measurement yields $N$ bits, but destroys superposition) |
| Evolution | Discrete updates (boolean logic) | Continuous (Schrödinger equation) |
| Reversibility | Generally irreversible (e.g., AND gate) | Always reversible (unitary) |

## Connection to BlackOops

### 1. Horizon Qubits

The encoder model treats each Planck area as a **classical bit** (0 or 1 state). But the full quantum description requires **qubits**:

$$|\psi_{area}\rangle = \alpha |0\rangle + \beta |1\rangle$$

**Bekenstein-Hawking entropy** counts the **information capacity** (number of classical bits after measurement), not the **Hilbert space dimension** ($2^N$ for $N$ qubits).

**Classical encoder**: $N$ positions (one position occupied at a time)

**Quantum encoder**: Superposition over all $N$ positions:

$$|\Psi\rangle = \sum_{n=1}^{N} c_n |n\rangle$$

### 2. Gray Code = Unitary Evolution

The single-bit-flip rule (Gray code) is the **discrete analog** of continuous unitary evolution (Schrödinger equation).

**Classical Gray code**: Flip 1 bit per step (deterministic)

**Quantum Gray code**: Evolve 1 qubit per Planck time (unitary), but state is **superposition** over multiple paths:

$$|\psi(t + t_p)\rangle = \hat{U}(t_p) |\psi(t)\rangle$$

where $\hat{U}(t_p) = e^{-i\hat{H}t_p/\hbar}$ flips (evolves) one qubit.

### 3. Entanglement and Holography

The horizon qubits are **entangled** with external radiation. This is the **holographic encoding** of information:

- **Bulk information**: Appears to fall into black hole
- **Boundary information**: Encoded on horizon via entanglement
- **Radiation information**: Released sequentially, entangled with horizon

**No-cloning** ensures: Cannot have independent information in bulk, on horizon, and in radiation — only one "copy" exists, distributed via entanglement.

### 4. Measurement and Decoherence

An external observer **measuring** the black hole collapses the superposition:

$$|\Psi\rangle = \sum_i c_i |i\rangle \xrightarrow{\text{measure}} |i_0\rangle$$

with probability $|c_{i_0}|^2$.

**Decoherence** (environment interaction) makes the horizon **appear classical** (one of $2^N$ microstates), even though the full quantum state is a superposition.

From `test_alignment.py` Sim 1: The alignment probability ($\sim 1/N^2$) is computed classically. The full quantum version would involve **amplitudes** (interference), not just probabilities.

### 5. Future Extension: Quantum Encoder Model

The current BlackOops framework is **classical** (encoder position is definite). A **quantum extension** would:
- Replace positions with qubits: $|n\rangle \to \alpha|n\rangle + \beta|n+1\rangle$
- Include superposition over multiple paths
- Track entanglement between horizon and radiation
- Compute quantum scrambling time (not just classical alignment time)

This would require **quantum simulation** (not just Monte Carlo), possibly on quantum computers (Google, IBM, IonQ).

## See Also

- [[Quantum State Evolution]]
- [[Unitarity]]
- [[Bekenstein-Hawking Entropy]]
- [[Shannon Entropy]]
- [[No-Cloning Theorem]]
- [[Quantum Entanglement]]
- [[Bell's Theorem]]

## References

1. Feynman, R. P. (1982). "Simulating Physics with Computers". *International Journal of Theoretical Physics*, 21(6/7), 467–488.
2. Nielsen, M. A., & Chuang, I. L. (2010). *Quantum Computation and Quantum Information* (10th Anniversary Edition). Cambridge University Press.
3. Wootters, W. K., & Zurek, W. H. (1982). "A Single Quantum Cannot be Cloned". *Nature*, 299(5886), 802–803.
4. Preskill, J. (2018). "Quantum Computing in the NISQ Era and Beyond". *Quantum*, 2, 79.
5. Almheiri, A., et al. (2013). "Black Holes: Complementarity or Firewalls?". *JHEP*, 2013(2), 062.
