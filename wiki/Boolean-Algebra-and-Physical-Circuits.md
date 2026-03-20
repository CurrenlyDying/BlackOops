# Boolean Algebra & Physical Circuits

## Shannon's 1937 Master's Thesis

Claude Shannon's 1937 MIT master's thesis, "A Symbolic Analysis of Relay and Switching Circuits," established the foundational principle that **computation is substrate-independent**.

Shannon demonstrated that:
1. Boolean algebra (George Boole, 1854) — a purely mathematical system of logic with operations AND, OR, NOT
2. Physical relay circuits — electromechanical switches used in telephone exchanges

...are **isomorphic**. Any logical operation can be implemented in hardware, and any circuit can be analyzed as a logical formula.

## The Mapping

| Boolean Operation | Relay Circuit | Modern Transistor |
|-------------------|---------------|-------------------|
| $A \land B$ (AND) | Relays in series | NAND gate (inverted) |
| $A \lor B$ (OR) | Relays in parallel | NOR gate (inverted) |
| $\neg A$ (NOT) | Normally-closed relay | Inverter |
| $A \oplus B$ (XOR) | $(A \land \neg B) \lor (\neg A \land B)$ | XOR gate |

## Physical Realization

In Shannon's era:
- **Relay**: Electromagnet that closes/opens a switch when energized
- **State**: Current flowing (1) or not flowing (0)
- **Speed**: Milliseconds per operation (mechanical inertia)

Today:
- **Transistor**: Semiconductor device controlling current flow
- **State**: Voltage high (1) or low (0)
- **Speed**: Picoseconds per operation (electron mobility)

The **logic** is identical. The **physics** is irrelevant.

## Substrate Independence

Shannon's insight: **Information processing is medium-independent.** The same computation can be executed by:
- Mechanical relays (1940s)
- Vacuum tubes (1950s)
- Transistors (1960s–present)
- Quantum gates (2020s+)
- Hypothetically: water pipes, DNA strands, or black hole horizons

This is why we can speak meaningfully about "the universe computing" or "black holes processing information" — if physical state transitions obey logical rules, they **are** computation, regardless of substrate.

## Implications for BlackOops

The BlackOops framework extends substrate independence to **spacetime itself**:

- **Claim**: The universe encodes state transitions like a Gray code rotary encoder
- **Evidence**: Quantum evolution is unitary (reversible), continuous (no jumps), and local (no faster-than-light)
- **Mapping**: Planck-scale state transitions = bit flips in a cosmic Gray code sequence

Just as Shannon showed that relay circuits obey Boolean algebra whether engineers knew it or not, BlackOops hypothesizes that spacetime obeys Gray code constraints whether physicists knew it or not.

### The Gray Code Constraint

In standard binary counting (substrate: place-value notation):
- 7 = `0111`
- 8 = `1000`

Three bits flip simultaneously. This requires **coordinated global change**.

In Gray code (substrate: single-bit transitions):
- 7 = `0100`
- 8 = `1100`

One bit flips. This is **locally implementable**.

The universe uses Gray code because **locality forbids simultaneous distant changes**. Information propagates at $c$. Causality enforces the single-bit-flip rule.

## Historical Context

- **1854**: George Boole publishes *The Laws of Thought*, inventing Boolean algebra
- **1937**: Claude Shannon connects Boolean algebra to circuits (MIT thesis)
- **1948**: Shannon publishes information theory, founding the field
- **1960**: Landauer shows computation has thermodynamic cost (erasure requires energy)
- **1973**: Bekenstein argues black holes have entropy → information is physical
- **2026**: BlackOops formalizes the Gray code constraint as a law of nature

## Numerical Example: Full Adder

A **1-bit full adder** adds three bits ($A$, $B$, carry-in $C_{in}$) and outputs a sum $S$ and carry-out $C_{out}$.

Boolean expressions:
$$S = A \oplus B \oplus C_{in}$$
$$C_{out} = (A \land B) \lor (C_{in} \land (A \oplus B))$$

In Shannon's framework, this maps to:
- 5 relay circuits (2 XOR gates, 2 AND gates, 1 OR gate)
- Total: ~10 relays (assuming XOR = 4 relays each)

Modern CPU: Same logic, ~20 transistors, executes in <1 nanosecond.

## Connection to BlackOops

The `EncoderState` class in `constants.py` implements **physical-to-informational** mappings:
- `mass_kg` → `n_bits` (Bekenstein-Hawking entropy)
- `hawking_temperature` → `bits_per_planck_time` (information flow rate)

This is Shannon's program applied to black holes: **translate physics into information theory**, then compute.

The surprising result: the physics obeys Gray code constraints (unitary quantum evolution = single-bit transitions), and the thermodynamics emerges from combinatorics (entropy = encoder positions).

## See Also

- [[Shannon Entropy]]
- [[Gray Code]]
- [[Shannon's Theseus]]
- [[Unitarity]]
- [[Landauer's Principle]]
- [[Quantum State Evolution]]

## References

1. Shannon, C. E. (1938). "A Symbolic Analysis of Relay and Switching Circuits". *MIT Master's Thesis*.
2. Boole, G. (1854). *An Investigation of the Laws of Thought*. Walton and Maberly.
3. Landauer, R. (1961). "Irreversibility and Heat Generation in the Computing Process". *IBM Journal of Research and Development*, 5(3), 183–191.
4. Fredkin, E., & Toffoli, T. (1982). "Conservative Logic". *International Journal of Theoretical Physics*, 21(3–4), 219–253.
