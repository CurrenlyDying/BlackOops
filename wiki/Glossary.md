# Glossary

Alphabetical reference of technical terms used in the BlackOops project.

---

## A

**AdS/CFT Correspondence** — Conjecture by Juan Maldacena (1997) stating that a gravitational theory in (d+1)-dimensional Anti-de Sitter space is mathematically equivalent to a conformal field theory on the d-dimensional boundary. A concrete realization of the holographic principle. See [[Holographic Principle]].

**Alignment** — In the encoder model, the process of infalling information "threading through" all $N$ positions on the horizon to reach the singularity (recursive loop). Expected time scales as $O(N^2)$ from random walk theory. See [[Random Walks on Cyclic Groups]].

**Alignment Probability** — Probability per Planck time that a piece of information aligns with the recursive loop. $P_{align} \sim 1/N$ where $N$ is number of encoder positions. See [[Key Results Summary]].

**Analog Gravity** — Laboratory systems (sonic black holes in BECs, water vortices, optical systems) that mimic gravitational phenomena. Used to test Hawking radiation predictions experimentally. See [[Analog Gravity [EXTENDED]]].

**Angular Resolution** — In rotary encoders, the smallest angular displacement that can be detected. In the encoder model: $\Delta\Omega = 4\pi/N$ steradians per bit. See [[Rotary Encoders]].

---

## B

**Bekenstein Bound** — Maximum entropy in a bounded region of space: $S \leq 2\pi R E / (\hbar c)$ where $R$ is radius and $E$ is energy. Derived by Jacob Bekenstein (1981) from thermodynamic arguments. See [[Bekenstein Bound]].

**Bekenstein-Hawking Entropy** — Entropy of a black hole: $S_{BH} = k_B A / (4 l_p^2)$ where $A$ is horizon area and $l_p$ is Planck length. In natural units ($k_B = 1$), $S = A/(4l_p^2)$. Proportional to area, not volume — a key hint toward the holographic principle. See [[Bekenstein-Hawking Entropy]].

**Black Hole** — Region of spacetime where gravity is so strong that nothing, not even light, can escape. Formed when mass $M$ is compressed within its Schwarzschild radius $r_s = 2GM/c^2$. See [[Schwarzschild Radius]].

**Boolean Algebra** — Mathematical structure with two values (0, 1) and operations (AND, OR, NOT). Claude Shannon showed in his 1937 thesis that Boolean logic maps onto physical relay circuits, establishing that computation is substrate-independent. See [[Boolean Algebra and Physical Circuits]].

**Bousso Bound** — Covariant formulation of the holographic principle: entropy flux through any light-sheet is bounded by its area in Planck units. Generalizes Bekenstein bound to arbitrary spacetimes.

---

## C

**Causal Set Theory** — Approach to quantum gravity where spacetime is fundamentally a discrete partially ordered set (poset) of events, with order relation = causal structure. Discrete at Planck scale. See [[Causal Set Theory [EXTENDED]]].

**Cayley Graph** — Graph representing a group with generators. For cyclic group $\mathbb{Z}_N$: nodes are integers 0 to N-1, edges connect $i \to (i±1) \mod N$. Random walk on this graph is used to model alignment dynamics. See [[Cayley Graphs [EXTENDED]]].

**Classical Bit** — Basic unit of information with two states: 0 or 1. Contrasts with quantum bit (qubit) which can be in superposition. See [[Qubits vs Classical Bits]].

**Cover Time** — In random walk theory, expected time to visit all $N$ nodes of a graph at least once. For cyclic graph: $\Theta(N^2)$. Related to alignment time in encoder model.

---

## D

**de Bruijn Sequence** — Cyclic sequence where every possible substring of length $n$ appears exactly once. Related to Gray code as minimal-change sequence. See [[de Bruijn Sequences [EXTENDED]]].

**Diffusive Process** — Process where spreading scales as $\sqrt{t}$, characteristic of random walks. The $\sqrt{N}$ overhead in encoder evaporation suggests diffusive dynamics.

---

## E

**Encoder Model** — Central framework of BlackOops mapping black hole properties onto rotary encoder concepts. Positions = Planck areas on horizon, angular resolution = $4\pi/N$ steradians, recursive loop = singularity. See [[The Gray Code Universe Hypothesis]].

**EncoderState** — Python dataclass in `constants.py` representing a black hole as a Gray code encoder. Properties include mass, Schwarzschild radius, number of bits $N$, Hawking temperature, evaporation time. See [[constants.py Documentation]].

**Entanglement** — Quantum correlation between particles where measuring one instantly determines the state of the other, regardless of distance. Key to understanding black hole information paradox. See [[Qubits vs Classical Bits]].

**Entropy** — Measure of disorder or missing information. In thermodynamics: $S = k_B \ln \Omega$ (Boltzmann). In information theory: $H = -\sum p_i \log_2 p_i$ (Shannon). For black holes: $S = k_B A/(4l_p^2)$ (Bekenstein-Hawking). See [[Shannon Entropy]], [[Bekenstein-Hawking Entropy]].

**Ergosphere** — Region outside a rotating (Kerr) black hole where spacetime is dragged faster than light. Objects cannot remain stationary. Extends from event horizon to outer boundary (ergosurface). See [[Kerr Black Holes]].

**Event Horizon** — Boundary of a black hole beyond which escape is impossible. For non-rotating (Schwarzschild) black hole, located at radius $r_s = 2GM/c^2$. In encoder model: 2D surface containing $N = A/(4l_p^2\ln 2)$ bits of information.

**Event Horizon Telescope (EHT)** — Global array of radio telescopes forming Earth-sized interferometer. First to image black hole shadows (M87* in 2019, Sgr A* in 2022). See [[Event Horizon Telescope Observations]].

**Evaporation Time** — Time for a black hole to completely evaporate via Hawking radiation: $t_{evap} = 5120\pi G^2 M^3 / (\hbar c^4) \propto M^3$. For solar mass: ~10⁶⁷ years. For Planck mass: ~10⁻⁴⁰ seconds. See [[Hawking Radiation]].

---

## F

**Firewall Paradox** — Paradox raised by Almheiri-Marolf-Polchinski-Sully (AMPS, 2012): if information is preserved in Hawking radiation (violating no-cloning), there must be a "firewall" of high-energy particles at the horizon, contradicting equivalence principle. No consensus resolution yet.

**Frame Dragging** — Effect where rotating massive object "drags" spacetime around it. Near rotating black hole, impossible to remain stationary — you're forced to orbit. See [[Kerr Black Holes]].

---

## G

**Geometric Mean** — For two numbers $a$ and $b$: $\sqrt{ab}$. In encoder model, Hawking radiation rate ($\propto N^{-0.5}$) is geometric mean of alignment probability ($N^{-1}$) and trivial rate ($N^0$). Structurally significant. See [[Geometric Mean]].

**Gray Code** — Binary encoding where consecutive values differ by exactly one bit. Prevents glitch states in rotary encoders. Reflected binary Gray code for $n$ bits has cycle length $2^n$. Central to BlackOops hypothesis. See [[Gray Code]].

**Gray Code Constraint** — Requirement that only one bit can flip between adjacent states. Maps onto unitarity in quantum mechanics (continuous evolution = minimal change). See [[The Gray Code Universe Hypothesis]].

---

## H

**Hamiltonian Path** — Path through a graph visiting each vertex exactly once. Gray code is a Hamiltonian cycle on the $n$-dimensional hypercube graph. See [[Gray Code as Hamiltonian Path [EXTENDED]]].

**Hawking Luminosity** — Power radiated by a black hole via Hawking radiation: $L = \sigma A T_H^4$ where $\sigma = \pi^2 k_B^4/(60\hbar^3 c^2)$ (Stefan-Boltzmann for quantum fields). For solar mass: ~10⁻²⁸ W. See [[Hawking Radiation]], [[Stefan-Boltzmann Law]].

**Hawking Radiation** — Thermal radiation emitted by black holes due to quantum effects near the horizon. Temperature: $T_H = \hbar c^3/(8\pi G M k_B) \propto 1/M$. Discovered by Stephen Hawking (1974). See [[Hawking Radiation]].

**Hawking Temperature** — Temperature of Hawking radiation: $T_H = \hbar c^3/(8\pi G M k_B)$. For solar mass: ~60 nanokelvin. For Planck mass: ~1.4×10³² K (Planck temperature). See [[Hawking Radiation]].

**Holevo Bound** — Maximum classical information extractable from $n$ qubits: $n$ bits. Shows quantum states carry more information than can be accessed classically. See [[Quantum Channel Capacity [EXTENDED]]].

**Holographic Principle** — Principle stating that information content of a volume is encoded on its boundary, with maximum $A/(4l_p^2)$ bits where $A$ is boundary area. Proposed by 't Hooft (1993) and Susskind (1995). In encoder model, emerges from $N^2$ alignment barrier. See [[Holographic Principle]].

**Horizon Area** — Surface area of black hole event horizon: $A = 4\pi r_s^2 = 16\pi G^2 M^2/c^4$ for Schwarzschild black hole. Proportional to entropy (Bekenstein-Hawking law).

---

## I

**Information Paradox** — Contradiction arising from Hawking's 1975 result that black holes destroy information (thermal radiation is featureless). Violates unitarity of quantum mechanics. Proposed resolutions: complementarity, firewalls, ER=EPR, island formula. See [[Black Hole Information Paradox]].

**Immirzi Parameter** — Dimensionless parameter $\gamma \approx 0.2375$ in loop quantum gravity that sets the scale for quantized area eigenvalues. Chosen to match Bekenstein-Hawking entropy. See [[Loop Quantum Gravity and Black Holes [EXTENDED]]].

**"It from Bit"** — Slogan by John Wheeler: physical reality ("it") emerges from information ("bit"). Ontological claim that information is more fundamental than matter or energy. See [[Wheeler's It from Bit [EXTENDED]]].

---

## K

**Kerr Black Hole** — Rotating black hole solution to Einstein's equations found by Roy Kerr (1963). Characterized by mass $M$ and angular momentum $J$. Has ring singularity and ergosphere. See [[Kerr Black Holes]].

**Kolmogorov Complexity** — Minimum length of a program that outputs a given string. Algorithmic measure of information content. See [[Kolmogorov Complexity [EXTENDED]]].

---

## L

**Landauer's Principle** — Minimum energy to erase one bit of information: $E = k_B T \ln 2$. Shows information has physical cost. Proposed by Rolf Landauer (1961). See [[Landauer's Principle [EXTENDED]]].

**LIGO** — Laser Interferometer Gravitational-Wave Observatory. First to directly detect gravitational waves (2015). Public data at gwosc.org. See [[LIGO Public Data [EXTENDED]]].

**Locality** — Principle that information propagates at finite speed (speed of light $c$). In encoder model: constraint on how fast bits can update — "angular resolution" of the encoder. See [[The Gray Code Universe Hypothesis]].

**Loop Quantum Gravity (LQG)** — Approach to quantum gravity based on quantized spacetime geometry. Predicts discrete area spectrum: $A_j = 8\pi\gamma l_p^2 \sqrt{j(j+1)}$. See [[Loop Quantum Gravity and Black Holes [EXTENDED]]].

---

## M

**M87*** — Supermassive black hole (6.5 billion solar masses) at center of galaxy M87. First black hole ever imaged (Event Horizon Telescope, 2019). Shadow diameter: 42 ± 3 microarcseconds. See [[Event Horizon Telescope Observations]].

**Margolus-Levitin Theorem** — Maximum rate of quantum state change (computation): $\Delta E \Delta t \geq \pi\hbar/2$ where $\Delta E$ is energy. Connects to Planck time as fundamental tick rate. See [[Margolus-Levitin Theorem [EXTENDED]]].

**Monte Carlo Simulation** — Computational method using repeated random sampling to estimate quantities. Used in `test_alignment.py` to measure alignment time scaling. See [[Monte Carlo Simulation]].

---

## N

**No-Cloning Theorem** — Quantum information cannot be copied: there's no unitary operation that takes $|\psi\rangle$ to $|\psi\rangle|\psi\rangle$. Central to understanding information paradox. See [[Qubits vs Classical Bits]].

---

## O

**Overhead Factor** — Ratio of actual evaporation time to naive estimate ($N \times t_p$): $O = t_{evap}/(N t_p)$. In encoder model: $O = 208.4 \sqrt{N}$, giving square-root barrier. See [[Key Results Summary]].

---

## P

**Page Curve** — Plot of entanglement entropy between Hawking radiation and black hole interior vs time. Initially increases (thermal radiation), then decreases (information recovery). "Page time" is halfway through evaporation. See [[Page Curve [EXTENDED]]].

**Page Time** — Time when entanglement entropy between radiated photons and black hole reaches maximum: $t_{Page} \sim t_{evap}/2$. After this, unitarity requires information to be recovered in radiation. See [[Page Curve [EXTENDED]]].

**Penrose Process** — Mechanism to extract rotational energy from a Kerr black hole by dropping object into ergosphere. Particle splits; one falls in with negative energy, other escapes with more energy than original. See [[Kerr Black Holes]].

**Phase Transition** — Encoder model predicts sharp transition from "black hole" to "not black hole" at $M/M_p \approx 0.225$ where $N \approx 1$ bit. Transition width: 0.23 decades. See [[Key Results Summary]].

**Planck Area** — Fundamental quantum of area: $A_p = l_p^2 \approx 2.6 \times 10^{-70}$ m². In encoder model: size of one "encoder position" on the horizon. See [[Planck Units]].

**Planck Energy** — $E_p = \sqrt{\hbar c^5/G} \approx 1.96 \times 10^9$ J ≈ 0.5 gigajoules. Energy of a photon with wavelength equal to Planck length. See [[Planck Units]].

**Planck Length** — $l_p = \sqrt{\hbar G/c^3} \approx 1.616 \times 10^{-35}$ m. Length scale where quantum gravity effects become important. See [[Planck Units]].

**Planck Mass** — $M_p = \sqrt{\hbar c/G} \approx 2.176 \times 10^{-8}$ kg ≈ 22 micrograms. Mass where Schwarzschild radius equals Planck length. In encoder model: the 1-bit sweet spot. See [[Planck Mass as Critical Threshold]].

**Planck Temperature** — $T_p = \sqrt{\hbar c^5/(G k_B^2)} \approx 1.417 \times 10^{32}$ K. Highest meaningful temperature (above this, black holes form from thermal fluctuations). See [[Planck Units]].

**Planck Time** — $t_p = \sqrt{\hbar G/c^5} \approx 5.391 \times 10^{-44}$ s. Shortest meaningful time interval. In encoder model: fundamental "tick rate" of the universe. See [[Planck Units]].

**Power Law** — Relationship of form $y = A x^b$ where $b$ is the exponent. Appears linear on log-log plot with slope $b$. In encoder model: suppression factor $\propto N^{0.5}$, alignment time $\propto N^{1.96}$. See [[Power Law Scaling]].

---

## Q

**Quantum Error Correction (QEC)** — Techniques to protect quantum information from decoherence. Holographic QEC (HaPPY code) connects to AdS/CFT — bulk spacetime emerges from boundary QEC structure. See [[Quantum Error Correction]].

**Qubit** — Quantum bit. Can be in superposition $|\psi\rangle = \alpha|0\rangle + \beta|1\rangle$ where $|\alpha|^2 + |\beta|^2 = 1$. Unit of quantum information. See [[Qubits vs Classical Bits]].

---

## R

**Random Walk** — Stochastic process where position updates by random steps. On cyclic group $\mathbb{Z}_N$: return time is $O(N^2)$. Models alignment dynamics in encoder framework. See [[Random Walks on Cyclic Groups]].

**Recursive Loop** — In encoder model, a bit that references itself: `bit[i] → bit[i]`. Informationally static (time doesn't pass). Maps to singularity in black hole. See [[The Gray Code Universe Hypothesis]].

**Reflected Binary Code** — Another name for Gray code. "Reflected" because second half of sequence is first half reversed with leading 1 prepended. See [[Gray Code]].

**Reinforcement Learning** — Machine learning where agent learns policy by trial and error in environment. Shannon's Theseus (1950) was early example: maze-solving mouse with relay-based memory. See [[Reinforcement Learning]], [[Shannon's Theseus]].

**Return Time** — In random walk theory, expected number of steps to return to starting position. For random walk on $\mathbb{Z}_N$: $\Theta(N^2)$. See [[Random Walks on Cyclic Groups]].

**Ring Singularity** — Singularity of a rotating (Kerr) black hole. Has form of a ring at $r=0$, $\theta = \pi/2$ in Boyer-Lindquist coordinates. In encoder model: possibly a multi-bit recursive loop. See [[Kerr Black Holes]].

**Rotary Encoder** — Physical device that converts angular position to digital signal. Uses Gray code to prevent glitch states. Analogy: black hole = rotary encoder with $N$ positions (Planck areas). See [[Rotary Encoders]].

---

## S

**Schwarzschild Radius** — Radius of the event horizon for a non-rotating black hole: $r_s = 2GM/c^2$. For Sun: 2.95 km. For Earth: 8.87 mm. For Planck mass: $2l_p$ ≈ 3.2×10⁻³⁵ m. See [[Schwarzschild Radius]].

**Scrambling Time** — Time for a black hole to fully scramble (mix) information: $t_{scramble} \sim (r_s/c) \ln S_{BH}$. Much faster than evaporation ($\ln N$ vs $N^{1.5}$). See [[Open Questions and Future Work]].

**Sgr A*** — Supermassive black hole (4 million solar masses) at center of Milky Way. Imaged by EHT in 2022. Closest supermassive black hole to Earth (~26,000 light years). See [[Event Horizon Telescope Observations]].

**Shannon Entropy** — Measure of information content: $H = -\sum_i p_i \log_2 p_i$ where $p_i$ are probabilities. Measured in bits. Introduced by Claude Shannon (1948). See [[Shannon Entropy]].

**Singularity** — Point (or ring in Kerr case) where spacetime curvature becomes infinite. At center of black hole, $r=0$. Physics as we know it breaks down. Quantum gravity needed. In encoder model: recursive bit loop where time stops.

**Spectral Gap** — Difference between first two eigenvalues of graph Laplacian. Related to mixing time of random walks. Larger gap = faster mixing. See [[Spectral Gap and Mixing Time [EXTENDED]]].

**Stefan-Boltzmann Law** — Radiated power from blackbody: $L = \sigma A T^4$ where $\sigma = \pi^2 k_B^4/(60\hbar^3 c^2)$ for quantum fields. Applied to Hawking radiation. See [[Stefan-Boltzmann Law]].

**Suppression Factor** — Ratio $S = t_{evap}/(N t_p)$ measuring how much slower evaporation is than naive one-bit-per-tick estimate. In encoder model: $S = 208.4 \sqrt{N}$. See [[Key Results Summary]].

**Superposition** — Quantum state existing in combination of basis states: $|\psi\rangle = \alpha|0\rangle + \beta|1\rangle$. Distinguishes qubits from classical bits. See [[Qubits vs Classical Bits]].

---

## T

**Thermodynamic Entropy** — Measure of number of microstates: $S = k_B \ln \Omega$ (Boltzmann). For black holes: $S = k_B A/(4l_p^2)$ (Bekenstein-Hawking). See [[Entropy and the Arrow of Time]].

**Theseus** — Electromechanical maze-solving mouse built by Claude Shannon (1950). Used relay-based memory to learn optimal path. Early example of reinforcement learning and information processing in physical systems. See [[Shannon's Theseus]].

**Timing Attack** — In encoder model, hypothetical scenario where two pieces of information "collude" to create 2-bit recursive loop. Simulations show no advantage: reduces to 1-body problem via relative coordinates. See [[Key Results Summary]].

**Traversal Cost** — Number of Gray code flips needed to visit all positions. For reflected $n$-bit Gray code: $2^n - 1$ flips for full cycle. Related to suppression factor in encoder evaporation. See [[Gray Code]].

---

## U

**Unitarity** — Property of quantum mechanics that evolution is reversible: if $U$ is unitary, $U U^\dagger = I$. Requires information conservation. Hawking radiation (thermal, featureless) seemed to violate this, leading to information paradox. See [[Unitarity]].

**Unruh Effect** — Accelerating observer sees thermal radiation (Unruh temperature) where inertial observer sees vacuum. Closely related to Hawking radiation. $T_{Unruh} = \hbar a/(2\pi c k_B)$ where $a$ is acceleration.

---

## V

**Verlinde's Entropic Gravity** — Proposal by Erik Verlinde (2011) that gravity is not fundamental but an entropic force arising from information storage on holographic screens. Derives Newton's law from thermodynamics. See [[Verlinde's Entropic Gravity [EXTENDED]]].

**Virtual Particles** — Quantum fluctuations of vacuum. Near black hole horizon, one particle falls in (negative energy), other escapes (Hawking radiation). Not directly observable but calculational tool. See [[Hawking Radiation]].

---

## W

**Wheeler-DeWitt Equation** — Equation attempting to describe quantum state of the universe as a whole. "Wave function of the universe." Time parameter disappears (problem of time in quantum gravity).

---

## Z

**$\mathbb{Z}_N$** — Cyclic group of integers modulo $N$. Elements: $\{0, 1, 2, ..., N-1\}$ with addition mod $N$. Random walk on $\mathbb{Z}_N$ models alignment dynamics in encoder. See [[Random Walks on Cyclic Groups]], [[Cayley Graphs [EXTENDED]]].

---

## Symbols

**$A$** — Area (typically horizon area of black hole)

**$c$** — Speed of light ≈ 2.998×10⁸ m/s

**$E_p$** — Planck energy ≈ 1.956×10⁹ J

**$G$** — Gravitational constant ≈ 6.674×10⁻¹¹ m³/(kg·s²)

**$\hbar$** — Reduced Planck constant ≈ 1.055×10⁻³⁴ J·s

**$H$** — Shannon entropy (information theory)

**$J$** — Angular momentum

**$k_B$** — Boltzmann constant ≈ 1.381×10⁻²³ J/K

**$l_p$** — Planck length ≈ 1.616×10⁻³⁵ m

**$L$** — Luminosity (radiated power)

**$M$** — Mass

**$M_p$** — Planck mass ≈ 2.176×10⁻⁸ kg

**$M_\odot$** — Solar mass ≈ 1.989×10³⁰ kg

**$N$** — Number of encoder positions (bits)

**$r_s$** — Schwarzschild radius

**$S$** — Entropy or suppression factor (context-dependent)

**$T_H$** — Hawking temperature

**$T_p$** — Planck temperature ≈ 1.417×10³² K

**$t_p$** — Planck time ≈ 5.391×10⁻⁴⁴ s

**$\Omega$** — Number of microstates (solid angle in different context)

---

## See Also

- [[Home]] — Project overview
- [[The Gray Code Universe Hypothesis]] — Core framework
- All concept pages linked throughout this glossary

---

## References

This glossary compiles terms from:
1. Bekenstein, J. D. (1973). "Black Holes and Entropy." *Phys. Rev. D*
2. Hawking, S. W. (1975). "Particle Creation by Black Holes." *Commun. Math. Phys.*
3. Shannon, C. E. (1948). "A Mathematical Theory of Communication." *Bell System Technical Journal*
4. Susskind, L. (1995). "The World as a Hologram." *J. Math. Phys.*
5. Wald, R. M. (1984). *General Relativity.* University of Chicago Press
6. Nielsen, M. & Chuang, I. (2000). *Quantum Computation and Quantum Information.* Cambridge University Press
