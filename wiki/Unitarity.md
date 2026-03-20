# Unitarity

## Definition

In quantum mechanics, **unitarity** is the principle that quantum evolution preserves probability and is reversible. A quantum system evolving from state $|\psi(t_1)\rangle$ to $|\psi(t_2)\rangle$ does so via a **unitary operator** $U$:

$$|\psi(t_2)\rangle = U |\psi(t_1)\rangle$$

where $U$ satisfies:

$$U^\dagger U = U U^\dagger = I$$

($U^\dagger$ is the Hermitian conjugate, $I$ is the identity operator)

## Key Properties

### 1. Norm Preservation

$$\langle \psi(t) | \psi(t) \rangle = 1 \quad \text{for all } t$$

Probabilities always sum to 1. No information is created or destroyed.

### 2. Reversibility

If $|\psi_f\rangle = U|\psi_i\rangle$, then:

$$|\psi_i\rangle = U^\dagger |\psi_f\rangle$$

The inverse operation exists. Time evolution can be run backward.

### 3. Linearity

$$U(a|\psi_1\rangle + b|\psi_2\rangle) = a U|\psi_1\rangle + b U|\psi_2\rangle$$

Superposition is preserved. Quantum interference effects persist.

## Schrödinger Equation and Unitarity

The Schrödinger equation:

$$i\hbar \frac{\partial}{\partial t}|\psi(t)\rangle = H |\psi(t)\rangle$$

has formal solution:

$$|\psi(t)\rangle = e^{-iHt/\hbar} |\psi(0)\rangle = U(t) |\psi(0)\rangle$$

where $U(t) = e^{-iHt/\hbar}$ is the **time evolution operator**.

**Proof of unitarity**: If $H$ is Hermitian ($H^\dagger = H$), then:

$$U^\dagger(t) = e^{iHt/\hbar} = U(-t) = U^{-1}(t)$$

Thus $U$ is unitary. Hermiticity of the Hamiltonian **guarantees** unitarity.

## Why Unitarity Matters

Unitarity is **not optional** in quantum mechanics. If violated:

1. **Probabilities don't sum to 1**: System could disappear or spawn copies
2. **Information is lost**: Cannot reconstruct initial state from final state
3. **CPT theorem breaks**: Fundamental symmetries of physics fail
4. **Quantum mechanics fails**: Predictions become inconsistent

## Unitarity and Entropy

**Pure states** evolve into pure states under unitary evolution:
$$S(\rho) = -\text{Tr}(\rho \log \rho) = 0$$
for $\rho = |\psi\rangle\langle\psi|$ (pure state density matrix).

Entropy **cannot increase** under unitary evolution of a closed system. This contrasts with thermodynamics (second law: entropy increases). Resolution:

- **Thermodynamic entropy increase** = **coarse-graining** (ignoring microscopic details)
- **Von Neumann entropy of pure state** = 0 (always)
- **Entanglement entropy** can increase (subsystem appears mixed even if total system is pure)

## Connection to BlackOops: Gray Code Constraint

The BlackOops framework interprets unitarity as the **physical justification** for the Gray code constraint:

**Unitary evolution is continuous**:
$$U(t + dt) = U(t) \cdot U(dt) \approx U(t) \cdot (I - iH dt / \hbar)$$

Infinitesimal evolution $U(dt)$ is **close to identity** — it changes the state **minimally**.

**Gray code analogy**:
- Standard binary: 7 = `0111` → 8 = `1000` (three bits flip simultaneously — discontinuous jump)
- Gray code: 7 = `0100` → 8 = `1100` (one bit flips — continuous transition)

**Claim**: The universe uses Gray code because unitary evolution forbids discontinuous jumps in state space. Adjacent quantum states must differ minimally.

### Locality Enforces Gray Code

In quantum field theory:
- Observables at spacelike-separated points **commute**: $[O(x), O(y)] = 0$ for $(x-y)^2 < 0$
- Information propagates at $c$: causal influences are local
- State changes must propagate continuously through space

A "multi-bit flip" (standard binary increment) would require **faster-than-light coordination** across distant bits. Locality forbids this.

Gray code (single-bit flips) is **locally implementable** — only one Planck-area patch of horizon changes per Planck time.

## The Black Hole Information Paradox

Hawking's 1975 calculation suggested black hole evaporation is **non-unitary**:

1. Throw a pure state (e.g., $|0\rangle$) into a black hole
2. Black hole radiates thermally (mixed state $\rho_{thermal}$)
3. Final radiation has $S > 0$ even though initial state had $S = 0$

**Contradiction**: Unitary evolution maps pure → pure, but Hawking radiation is pure → mixed.

### Proposed Resolutions

1. **Information is in subtle correlations** (Page curve, island formula): The radiation appears thermal locally but is actually a pure state globally. Entanglement between early and late radiation carries information.

2. **Complementarity** (Susskind): Infalling observer sees information cross horizon; external observer sees it encoded in radiation. Both perspectives valid, never in conflict.

3. **ER=EPR** (Maldacena-Susskind): Entangled particles are connected by wormholes. Black hole interior is entangled with radiation → information preserved via wormhole geometry.

4. **Firewall** (AMPS 2012): Information preservation requires destroying the smooth horizon (infalling observer hits a "firewall" of high-energy particles).

**Current consensus** (2020s): Unitarity is preserved. The Page curve (entropy of radiation first rises, then falls) has been derived from quantum gravity (island formula). Information is never lost.

## BlackOops and Unitarity

The encoder model **enforces unitarity by construction**:

- Each black hole state = one of $N = 2^S$ encoder positions
- Hawking radiation = unwinding the Gray code sequence
- One bit released per step → total information = $N$ bits out
- **Information conservation**: Sum of (bits in BH) + (bits in radiation) = constant

From `test_alignment.py` Simulation 4:
```
N=1000 bit encoder:
  Initial: 1000 bits in BH, 0 in radiation
  Final:   0 bits in BH, 1000 in radiation
  Total conserved at all intermediate steps
```

### Alignment and Unitarity

The **alignment probability** $P \sim 1/N$ per Planck time suggests:

- Information trying to "reach" the singularity must align with the recursive loop
- Random walk on $\mathbb{Z}_N$ (cyclic group): hitting time $\sim N^2$ steps
- Evaporation time: $\sim N^{1.5}$ steps
- **Result**: Information never reaches the singularity before the BH evaporates

This is the holographic principle: information **stays on the horizon** (where unitarity is manifest) rather than disappearing into the singularity (where unitarity would be lost).

## Mathematical Formalism

A unitary operator on a Hilbert space $\mathcal{H}$ satisfies:

$$\langle U\psi | U\phi \rangle = \langle \psi | \phi \rangle$$

for all $|\psi\rangle, |\phi\rangle \in \mathcal{H}$.

**Matrix representation**: If $U$ is an $n \times n$ matrix,

$$U^\dagger U = I_n$$

Columns of $U$ form an orthonormal basis.

**Example** (2-qubit unitary):

$$U = \frac{1}{\sqrt{2}} \begin{pmatrix} 1 & 1 \\ 1 & -1 \end{pmatrix} \quad \text{(Hadamard gate)}$$

$$U^\dagger = U, \quad U^2 = I$$

This maps $|0\rangle \to (|0\rangle + |1\rangle)/\sqrt{2}$, creating superposition.

## CPT Theorem

Unitarity is closely related to the **CPT theorem** (charge conjugation, parity, time reversal):

**Theorem**: Any local quantum field theory that is Lorentz-invariant and unitary must be invariant under the combined transformation CPT.

**Consequence**: If unitarity is violated, CPT symmetry breaks, implying:
- Antimatter doesn't behave as mirror image of matter
- Fundamental asymmetry between past and future
- Possible breakdown of causality

No CPT violations have been observed (tested to $10^{-18}$ precision in kaon systems).

## Effective Non-Unitarity

While fundamental evolution is unitary, **measurements** appear non-unitary:

$$|\psi\rangle = a|0\rangle + b|1\rangle \xrightarrow{\text{measure}} \begin{cases} |0\rangle & \text{prob } |a|^2 \\ |1\rangle & \text{prob } |b|^2 \end{cases}$$

This is **not** unitary (norm of superposition is lost). Resolution:

- **Copenhagen interpretation**: Measurement is a separate process (wavefunction collapse)
- **Many-worlds**: Measurement is unitary evolution of system + environment; observer branches
- **Decoherence**: Environment entanglement makes superposition invisible locally (but preserves unitarity globally)

## See Also

- [[Quantum State Evolution]]
- [[Black Hole Information Paradox]]
- [[Hawking Radiation]]
- [[Shannon Entropy]]
- [[Entropy and the Arrow of Time]]
- [[Quantum Error Correction]]

## References

1. Nielsen, M. A., & Chuang, I. L. (2010). *Quantum Computation and Quantum Information*. Cambridge University Press. (Chapter 2: Quantum Mechanics)
2. Preskill, J. (1998). "Lecture Notes on Quantum Computation". Caltech. http://theory.caltech.edu/~preskill/ph229/
3. Almheiri, A., et al. (2020). "The Page Curve of Hawking Radiation from Semiclassical Geometry". *arXiv:1908.10996*.
4. Susskind, L. (1995). "The World as a Hologram". *Journal of Mathematical Physics*, 36(11), 6377–6396.
