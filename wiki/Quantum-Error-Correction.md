# Quantum Error Correction

## Overview

**Quantum Error Correction** (QEC) is the theory and practice of protecting quantum information from errors due to decoherence and noise. Unlike classical error correction (which copies bits), QEC must work around the **no-cloning theorem** — quantum states cannot be copied.

## The Challenge

### No-Cloning Theorem

**Theorem** (Wootters & Zurek, 1982): It is impossible to create an identical copy of an arbitrary unknown quantum state.

**Proof sketch**: Cloning would require $U|\psi\rangle|0\rangle = |\psi\rangle|\psi\rangle$ for all $|\psi\rangle$. But unitary operators cannot do this for non-orthogonal states.

**Implication**: Classical error correction (copy bit, check majority vote) doesn't work for qubits.

### Decoherence

Qubits interact with environment, causing:
- **Bit flip**: $|0\rangle \leftrightarrow |1\rangle$ (X error)
- **Phase flip**: $|+\rangle \leftrightarrow |-\rangle$ (Z error)
- **Combined**: Both amplitude and phase errors

Without correction, quantum information decays exponentially: $\rho(t) \sim e^{-t/T_2}$ where $T_2$ is coherence time.

## QEC Solution: Entanglement

Instead of copying, **entangle** the logical qubit with ancilla qubits:

$$|\psi\rangle_L = \alpha|0\rangle + \beta|1\rangle \quad \to \quad |\psi\rangle_L = \alpha|0_L\rangle + \beta|1_L\rangle$$

where $|0_L\rangle$ and $|1_L\rangle$ are multi-qubit **codewords** (e.g., $|0_L\rangle = |000\rangle$, $|1_L\rangle = |111\rangle$ for 3-qubit code).

**Error detection**: Measure **syndrome** (which error occurred) without measuring the logical state directly.

**Error correction**: Apply corrective unitary based on syndrome.

## Stabilizer Codes

### Formalism

A **stabilizer code** encodes $k$ logical qubits into $n$ physical qubits using $(n-k)$ **stabilizer generators** $\{S_1, \ldots, S_{n-k}\}$:

- Stabilizers are Pauli operators: $S_i \in \{I, X, Y, Z\}^{\otimes n}$
- Code space: $|\psi_L\rangle$ satisfies $S_i |\psi_L\rangle = |\psi_L\rangle$ for all $i$

**Error detection**: Measure stabilizers. If $S_i |\psi\rangle = -|\psi\rangle$ (eigenvalue -1), error detected.

### Example: 5-Qubit Code

**Smallest perfect code**: Encodes 1 logical qubit in 5 physical qubits, corrects any single-qubit error.

Stabilizers:
$$S_1 = XZZXI, \quad S_2 = IXZZX, \quad S_3 = XIXZZ, \quad S_4 = ZXIXZ$$

Logical operators:
$$X_L = XXXXX, \quad Z_L = ZZZZZ$$

### Surface Codes

**Most practical** QEC for large-scale quantum computers:

- Physical qubits on 2D lattice
- Stabilizers on plaquettes (check X or Z on surrounding qubits)
- **Distance** $d$: corrects up to $(d-1)/2$ errors
- **Threshold theorem**: If physical error rate $p < p_{th} \approx 1\%$, logical error rate decreases exponentially with $d$

## Topological Codes

### Toric Code

Qubits on edges of 2D torus. Ground state is entangled:

$$|GS\rangle = \frac{1}{2^{N/2}} \sum_{\text{closed loops}} |\text{loop}\rangle$$

- **Excitations**: Anyons (quasiparticles with fractional statistics)
- **Error**: Creates anyon pair
- **Correction**: Annihilate anyons by moving them together

**Robust**: Topological protection — errors must create macroscopic loops to corrupt information.

### Holography Connection

**AdS/CFT**: Bulk geometry emerges from boundary entanglement structure.

**HaPPY Code** (Pastawski-Yoshida-Harlow-Preskill, 2015): Tensor network model where:
- **Logical qubits**: In AdS bulk
- **Physical qubits**: On CFT boundary
- **Error correction**: Bulk reconstruction from boundary

**Connection**: Black hole interior is encoded holographically on horizon via quantum error correction. Information is protected even though horizon is "lossy."

## Connection to BlackOops

QEC is deeply relevant to how the universe protects information near black hole horizons:

### 1. Horizon as QEC Code

**Holographic principle**: Bulk information (inside BH) is encoded on boundary (horizon).

**Interpretation**: The horizon implements a **quantum error-correcting code**:
- **Logical qubits**: Information about infalling matter
- **Physical qubits**: Planck-area patches on horizon ($N = A/(4l_p^2 \ln 2)$ qubits)
- **Encoding**: Holographic map from bulk to boundary

**Error resilience**: Even if local patches of horizon are "erased" (quantum fluctuations), bulk information can be reconstructed from remaining patches (like Surface Code).

### 2. Gray Code as Error-Free Encoding

The BlackOops model uses **Gray code** for state transitions:
- Only one bit flips per Planck time
- **Error detection**: Easy (check if more than one bit flipped → error)
- **Error correction**: Minimal overhead (revert single-bit flip)

Gray code is **not** a QEC code (it's classical), but it shares the property of **local error detectability**: errors are confined to neighbors in the code graph.

### 3. Evaporation Preserves Information

**QEC perspective** on Hawking radiation:

1. **Encoding phase** (matter falls in): Information encoded holographically on horizon
2. **Storage phase**: Information protected by QEC (AdS/CFT, HaPPY-like structure)
3. **Decoding phase** (evaporation): Information released via Hawking radiation

The **Page curve** is the signature of QEC:
- **Before Page time**: Syndrome measurements (early radiation looks thermal)
- **After Page time**: Decoded qubits (late radiation carries purified information)

### 4. Alignment as QEC Failure

In BlackOops, **alignment with singularity** represents **catastrophic error**:
- Information reaches "recursive loop" (singularity)
- QEC fails (information lost)

But $t_{align} \sim N^2 \gg t_{evap} \sim N^{1.5}$ → black hole evaporates **before** QEC fails.

**Holographic principle emerges** from QEC success.

## Threshold Theorem

**Fault-tolerant quantum computation**: If physical error rate $p < p_{th}$, can achieve arbitrary accuracy by increasing code size.

**Threshold values**:
- Surface code: $p_{th} \approx 0.01$ (1% errors tolerable)
- Concatenated codes: $p_{th} \approx 10^{-4}$ (stricter)

**For black holes**:
- "Error rate" = quantum fluctuations at Planck scale
- If $p < p_{th}$, information is preserved holographically
- If $p > p_{th}$, information is lost (unitarity violated)

**BlackOops conjecture**: Universe operates below threshold → unitarity preserved.

## Experimental QEC

### 2014: 9-Qubit Shor Code

First demonstration of QEC improving logical qubit lifetime beyond physical qubits.

### 2021: Google Quantum AI

Surface code on 49 qubits, demonstrated scaling: logical error rate decreases with distance.

### 2023: IBM Quantum

433-qubit processor with QEC, approaching fault-tolerant regime.

## Mathematical Formalism

### Operator Formalism

Error $E$ acts on codeword:

$$E|\psi_L\rangle = E(\alpha|0_L\rangle + \beta|1_L\rangle)$$

Syndrome measurement projects onto error subspace:

$$\Pi_s = \frac{1}{2^k} \sum_{S_i} \chi_s(S_i) S_i$$

where $\chi_s(S_i) = \pm 1$ is the syndrome.

Recovery operator $R_s$:

$$R_s E |\psi_L\rangle = |\psi_L\rangle \quad \text{(up to global phase)}$$

### Fidelity

Measure of code performance:

$$F = \langle \psi_L | R E | \psi_L \rangle$$

For good code, $F \to 1$ as $n \to \infty$.

## Connection to Entropy

**Von Neumann entropy** of logical qubit:

$$S(\rho_L) = -\text{Tr}(\rho_L \log \rho_L)$$

For perfect QEC:

$$S(\rho_L) = 0 \quad \text{(pure state preserved)}$$

For imperfect QEC:

$$S(\rho_L) > 0 \quad \text{(information leaked to environment)}$$

**Black hole QEC**: $S_{BH}$ decreases via Hawking radiation, but $S_{total} = S_{BH} + S_{rad}$ conserved (unitarity).

## Open Questions

1. **What is the explicit QEC code** for black hole horizons?
2. **How does QEC relate** to smooth vs firewalls paradox?
3. **Can we simulate BH evaporation** using QEC on quantum computers?
4. **Does QEC explain** why scrambling time $\ll$ evaporation time?

## See Also

- [[Qubits vs Classical Bits]]
- [[Unitarity]]
- [[Holographic Principle]]
- [[Black Hole Information Paradox]]
- [[Page Curve]]
- [[Shannon Entropy]]

## References

1. Shor, P. W. (1995). "Scheme for Reducing Decoherence in Quantum Computer Memory". *Physical Review A*, 52(4), R2493–R2496.
2. Preskill, J. (1998). "Lecture Notes on Quantum Computation". Caltech. http://theory.caltech.edu/~preskill/ph229/
3. Pastawski, F., et al. (2015). "Holographic Quantum Error-Correcting Codes". *Physical Review X*, 5, 041015.
4. Almheiri, A., Dong, X., & Harlow, D. (2015). "Bulk Locality and Quantum Error Correction in AdS/CFT". *Journal of High Energy Physics*, 2015(4), 163.
