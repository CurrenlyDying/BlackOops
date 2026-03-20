# Shannon Entropy

## Definition

**Shannon entropy** is the fundamental measure of information content and uncertainty in a message or probability distribution. It quantifies the average number of bits needed to encode a message optimally.

For a discrete random variable $X$ with possible values $\{x_1, x_2, ..., x_n\}$ and probability mass function $p(x_i)$, the Shannon entropy is:

$$H(X) = -\sum_{i=1}^{n} p(x_i) \log_2 p(x_i)$$

By convention, $0 \log 0 = 0$ (since $\lim_{p \to 0} p \log p = 0$).

## Key Properties

- **Units**: Measured in **bits** when using $\log_2$, or **nats** when using natural logarithm $\ln$.
- **Maximum entropy**: Achieved when all outcomes are equally likely: $H_{max} = \log_2 n$ for $n$ outcomes.
- **Minimum entropy**: $H = 0$ when the outcome is deterministic (one probability = 1, all others = 0).
- **Non-negative**: $H(X) \geq 0$ always.

## Physical Interpretation

Shannon's 1948 paper "A Mathematical Theory of Communication" established that information is:

1. **Quantifiable** — can be measured in discrete units (bits)
2. **Medium-independent** — the same information can be encoded in telegraph signals, radio waves, or magnetic storage
3. **Subject to fundamental limits** — channel capacity sets maximum reliable transmission rate

The bit emerged as the fundamental unit of information, analogous to how the meter is the fundamental unit of length.

## Numerical Example

For a fair coin flip ($p(H) = p(T) = 0.5$):

$$H = -[0.5 \log_2(0.5) + 0.5 \log_2(0.5)] = -[0.5 \times (-1) + 0.5 \times (-1)] = 1 \text{ bit}$$

For a biased coin ($p(H) = 0.9, p(T) = 0.1$):

$$H = -[0.9 \log_2(0.9) + 0.1 \log_2(0.1)] \approx 0.469 \text{ bits}$$

The biased coin has lower entropy because the outcome is more predictable.

## Connection to Thermodynamic Entropy

Shannon entropy is mathematically identical to Boltzmann's thermodynamic entropy (up to constants):

$$S_{Boltzmann} = k_B \ln W$$

where $W$ is the number of microstates and $k_B = 1.380649 \times 10^{-23}$ J/K is Boltzmann's constant. The connection is:

$$S_{Boltzmann} = k_B \ln(2) \cdot H_{Shannon}$$

This bridge between information theory and thermodynamics is central to modern physics, particularly in black hole thermodynamics.

## Connection to BlackOops

In the BlackOops framework:

- **Bekenstein-Hawking entropy** $S = A/(4l_p^2)$ represents the information content of a black hole horizon
- Each Planck area ($l_p^2 \approx 2.612 \times 10^{-70}$ m²) corresponds to ~1 nat of entropy
- Converting to bits: $N_{bits} = S / \ln(2)$, giving the number of encoder positions
- The framework interprets black hole evaporation as entropy (information) being released at a rate constrained by the Gray code single-bit-flip rule

A solar-mass black hole has $N \approx 10^{77}$ bits of entropy — that's how many encoder positions it has. Shannon entropy quantifies exactly this: the information capacity of the horizon.

## Historical Context

- **1948**: Claude Shannon publishes "A Mathematical Theory of Communication" at Bell Labs
- **1972**: Jacob Bekenstein proposes black holes have entropy proportional to horizon area
- **1995**: Ted Jacobson derives Einstein's equations from thermodynamic entropy on horizons
- **2000s**: AdS/CFT correspondence formalizes holographic duality between entropy in bulk and boundary

## See Also

- [[Bekenstein-Hawking Entropy]]
- [[Unitarity]]
- [[Boolean Algebra & Physical Circuits]]
- [[Shannon's Theseus]]
- [[Entropy and the Arrow of Time]]
- [[Landauer's Principle]]

## References

1. Shannon, C. E. (1948). "A Mathematical Theory of Communication". *Bell System Technical Journal*, 27(3), 379–423.
2. Cover, T. M., & Thomas, J. A. (2006). *Elements of Information Theory* (2nd ed.). Wiley.
3. Bekenstein, J. D. (1973). "Black Holes and Entropy". *Physical Review D*, 7(8), 2333–2346.
4. Jaynes, E. T. (1957). "Information Theory and Statistical Mechanics". *Physical Review*, 106(4), 620–630.
