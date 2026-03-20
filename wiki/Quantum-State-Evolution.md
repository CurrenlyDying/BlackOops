# Quantum State Evolution

## Definition

**Quantum state evolution** describes how quantum systems change over time according to the **Schrödinger equation**. For a system with state vector $|\psi(t)\rangle$ and Hamiltonian $\hat{H}$ (energy operator), the evolution is:

$$i\hbar \frac{\partial}{\partial t} |\psi(t)\rangle = \hat{H} |\psi(t)\rangle$$

The solution is:

$$|\psi(t)\rangle = \hat{U}(t, t_0) |\psi(t_0)\rangle$$

where $\hat{U}(t, t_0) = e^{-i\hat{H}(t-t_0)/\hbar}$ is the **unitary time evolution operator**.

## Key Properties

### 1. Unitarity

The evolution operator $\hat{U}$ is **unitary**: $\hat{U}^\dagger \hat{U} = \hat{I}$ (identity).

**Consequences**:
- **Norm preservation**: $\langle\psi(t)|\psi(t)\rangle = \langle\psi(t_0)|\psi(t_0)\rangle = 1$ (probability conserved)
- **Reversibility**: $\hat{U}^{-1} = \hat{U}^\dagger$ (time evolution can be reversed)
- **Information conservation**: No information is created or destroyed

**Physical meaning**: Quantum mechanics is **deterministic** (given initial state, final state is uniquely determined) and **reversible** (can run time backward).

### 2. Continuity

The state $|\psi(t)\rangle$ evolves **continuously** as a function of time. For small time steps $dt$:

$$|\psi(t + dt)\rangle = \left( \hat{I} - \frac{i}{\hbar} \hat{H} dt \right) |\psi(t)\rangle + O(dt^2)$$

**Key insight**: Adjacent states differ **infinitesimally** — the system cannot "jump" across state space. This is the quantum mechanical realization of the **Gray code constraint**: only minimal changes between successive states.

### 3. Linearity

If $|\psi_1\rangle$ and $|\psi_2\rangle$ are valid states, so is any **superposition** $\alpha|\psi_1\rangle + \beta|\psi_2\rangle$ (where $|\alpha|^2 + |\beta|^2 = 1$).

Evolution preserves superposition:

$$\hat{U}(\alpha|\psi_1\rangle + \beta|\psi_2\rangle) = \alpha \hat{U}|\psi_1\rangle + \beta \hat{U}|\psi_2\rangle$$

This is **linearity** — quantum mechanics is a linear theory.

## Time-Dependent vs Time-Independent Hamiltonian

### Time-Independent Hamiltonian

If $\hat{H}$ does not depend on time, the solution is straightforward:

$$|\psi(t)\rangle = e^{-i\hat{H}t/\hbar} |\psi(0)\rangle$$

For an energy eigenstate $\hat{H}|E_n\rangle = E_n |E_n\rangle$:

$$|\psi(t)\rangle = e^{-iE_n t/\hbar} |E_n\rangle$$

**Phase factor**: The state acquires a **phase** $e^{-iE_n t/\hbar}$ but the **probability density** $|\psi|^2$ remains constant. Energy eigenstates are **stationary** (no observable changes over time).

### Time-Dependent Hamiltonian

If $\hat{H}(t)$ changes with time, the evolution is more complex. The solution is formally:

$$|\psi(t)\rangle = \mathcal{T} \exp\left( -\frac{i}{\hbar} \int_{t_0}^{t} \hat{H}(t') dt' \right) |\psi(t_0)\rangle$$

where $\mathcal{T}$ is the **time-ordering operator** (ensures earlier times are applied first).

**Example**: Black hole evaporation — as mass $M(t)$ decreases, the Hamiltonian changes. The horizon's quantum state evolves non-trivially over time.

## Minimal Change Between Adjacent States

### Infinitesimal Evolution

For time step $dt \to 0$:

$$|\psi(t + dt)\rangle - |\psi(t)\rangle = -\frac{i}{\hbar} \hat{H} |\psi(t)\rangle dt$$

**Magnitude of change**:

$$\||\psi(t + dt)\rangle - |\psi(t)\rangle\| = \frac{1}{\hbar} \|\hat{H}|\psi(t)\rangle\| dt = \frac{\langle E \rangle}{\hbar} dt$$

where $\langle E \rangle = \langle\psi|\hat{H}|\psi\rangle$ is the expected energy.

**Interpretation**: The rate of state change is proportional to **energy**. High-energy states evolve faster; low-energy states evolve slower.

### Connection to Gray Code

In a discrete $N$-state system (e.g., $N$-bit encoder), Gray code requires adjacent states differ by **1 bit**.

In continuous quantum mechanics, adjacent times differ **infinitesimally**. The analog:

| Discrete (Gray code) | Continuous (Quantum) |
|---------------------|---------------------|
| State $n$ and $n+1$ differ by 1 bit | $\|\psi(t)\rangle$ and $\|\psi(t+dt)\rangle$ differ by $O(dt)$ |
| No multi-bit jumps | No discontinuous state jumps |
| Hamiltonian path on hypercube | Continuous path in Hilbert space |

**Physical constraint**: Locality — information propagates at finite speed ($\leq c$). A system cannot change non-locally (e.g., flip bits on opposite sides of a black hole horizon simultaneously) because that would require faster-than-light signaling.

### Numerical Example: Qubit Evolution

Consider a **qubit** (2-state system) with Hamiltonian:

$$\hat{H} = \frac{\hbar\omega}{2} \sigma_z = \frac{\hbar\omega}{2} \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}$$

Initial state: $|\psi(0)\rangle = |0\rangle = \begin{pmatrix} 1 \\ 0 \end{pmatrix}$

Evolution:

$$|\psi(t)\rangle = e^{-i\hat{H}t/\hbar} |0\rangle = e^{-i\omega t/2} |0\rangle$$

**State at $t = \pi/\omega$**:

$$|\psi(\pi/\omega)\rangle = e^{-i\pi/2} |0\rangle = -i |0\rangle$$

The state is **still $|0\rangle$** (same computational basis state), but with a **phase** $-i$. Observables ($|\psi|^2$) are unchanged.

**Adjacent state change**: For $dt = 10^{-10}$ s (nanosecond) and $\omega = 10^{10}$ rad/s (GHz qubit):

$$|\psi(t + dt)\rangle - |\psi(t)\rangle \approx -\frac{i\omega dt}{2} |0\rangle = -i \times 10^{-10} \times 10^{10} / 2 |0\rangle = -0.5i |0\rangle$$

**Magnitude**: $\|\Delta\psi\| \approx 0.5$ — significant change over nanosecond timescales at GHz frequencies.

## Decoherence

### Open vs Closed Systems

The Schrödinger equation applies to **closed** (isolated) systems. Real systems interact with an **environment**, leading to **decoherence** — loss of quantum coherence (superposition collapses to classical mixture).

**Evolution of open systems** (density matrix $\hat{\rho}$):

$$\frac{d\hat{\rho}}{dt} = -\frac{i}{\hbar} [\hat{H}, \hat{\rho}] + \mathcal{L}(\hat{\rho})$$

where $\mathcal{L}$ is the **Lindblad operator** (describes environment coupling).

**Decoherence time** $\tau_d$: Timescale over which off-diagonal elements of $\hat{\rho}$ (coherences) decay to zero.

### Example: Black Hole Horizon

The horizon's quantum state is entangled with the external environment (Hawking radiation). As bits are radiated:
- **Pure state** (black hole alone): $|\psi_{BH}\rangle$
- **Entangled state** (black hole + radiation): $|\Psi\rangle = \sum_i \alpha_i |BH_i\rangle \otimes |rad_i\rangle$
- **Reduced density matrix** (tracing out radiation): $\hat{\rho}_{BH} = \text{Tr}_{rad}(|\Psi\rangle\langle\Psi|)$

The black hole's state appears **mixed** (decohered) due to entanglement with radiation, even though the total state is pure.

**Decoherence time**: $\sim t_{scramble} \sim (r_s/c) \log N$ — information scrambles across horizon on this timescale.

For solar-mass black hole: $\tau_d \sim 10^{-4}$ s — much faster than evaporation ($\sim 10^{67}$ years).

## Connection to BlackOops

### 1. Gray Code as Unitary Evolution

The BlackOops encoder model maps:
- **Encoder state $n$** ↔ **Quantum state $|\psi_n\rangle$**
- **Single-bit flip** ↔ **Infinitesimal time step $dt$**
- **Gray code path** ↔ **Unitary trajectory in Hilbert space**

The constraint that adjacent encoder positions differ by 1 bit is the **discrete analog** of continuous quantum evolution.

From `constants.py`, the encoder has $N = A / (4 l_p^2 \ln 2)$ positions. Each position is a microstate of the horizon. Transitions between positions occur at **Planck time** intervals:

$$dt = t_p = \sqrt{\frac{\hbar G}{c^5}} \approx 5.39 \times 10^{-44} \text{ s}$$

### 2. Evaporation as State Unwinding

Hawking radiation is the **quantum evolution** of the horizon state from initial configuration (all bits on horizon) to final configuration (all bits radiated).

From `test_core.py` Test 1: evaporation time $t \propto N^{1.5}$ — this is the time for **unitary evolution** to traverse all $N$ encoder positions via Gray code.

**Continuous limit**: As $N \to \infty$, the discrete encoder approaches a continuous quantum state space (Hilbert space). The Gray code path becomes a smooth trajectory.

### 3. Locality and Planck-Time Ticks

The single-bit-flip rule enforces **locality** — only one Planck area ($l_p^2$) changes per Planck time ($t_p$).

**Speed of information propagation**:

$$v_{info} = \frac{l_p}{t_p} = \frac{l_p}{\sqrt{\hbar G / c^5}} = c$$

**The encoder updates at the speed of light** — consistent with causality.

**Example**: Solar-mass black hole has $N \sim 10^{77}$ positions. To update all positions sequentially:

$$t_{sequential} = N \times t_p \sim 10^{77} \times 5.4 \times 10^{-44} \sim 10^{33} \text{ s}$$

**Actual evaporation time**: $t_{evap} \sim 6.6 \times 10^{74}$ s — much longer.

**Interpretation**: The $\sqrt{N}$ overhead (from Test 1) represents a **diffusive** process — information spreads across the 2D horizon before escaping, requiring $\sim N^{1.5}$ steps instead of $N$.

### 4. Decoherence and Horizon Microstructure

The horizon's quantum state is **pure** (unitary evolution), but **appears mixed** to external observers due to entanglement with radiated bits.

From `test_alignment.py` Sim 4: total bit-count conserved ($N_{horizon} + N_{rad} = N_{initial}$). This is **unitarity** — the global state is pure even if subsystems are mixed.

**Decoherence interpretation**: An external observer measuring the black hole sees a thermal state (maximum entropy), but the full quantum state (black hole + radiation) is pure (zero entropy).

### 5. Continuous Evolution = No Firewalls

The continuity of quantum evolution implies **no discontinuities** at the horizon. The AMPS firewall paradox (2012) suggested the horizon might be a high-energy wall (discontinuous).

**BlackOops resolution**: The encoder evolves continuously (Gray code). No discontinuous energy injection at horizon. The horizon is **smooth** from the perspective of infalling observers (equivalence principle preserved).

## See Also

- [[Unitarity]]
- [[Gray Code]]
- [[Bekenstein-Hawking Entropy]]
- [[Hawking Radiation]]
- [[Quantum Error Correction]]
- [[Decoherence]]
- [[Schrödinger Equation]]

## References

1. Schrödinger, E. (1926). "Quantisierung als Eigenwertproblem". *Annalen der Physik*, 384(4), 361–376.
2. von Neumann, J. (1932). *Mathematical Foundations of Quantum Mechanics*. Princeton University Press.
3. Zurek, W. H. (2003). "Decoherence, Einselection, and the Quantum Origins of the Classical". *Reviews of Modern Physics*, 75(3), 715–775.
4. Hayden, P., & Preskill, J. (2007). "Black Holes as Mirrors: Quantum Information in Random Subsystems". *JHEP*, 2007(09), 120.
