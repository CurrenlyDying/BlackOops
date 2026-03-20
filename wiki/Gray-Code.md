# Gray Code

## Definition

A **Gray code** (also called reflected binary code) is a binary numeral system where two successive values differ in only one bit position. It contrasts with standard binary, where incrementing a counter can flip multiple bits simultaneously.

## Construction: Reflected Binary

Gray codes are constructed recursively using **reflection**:

**1-bit Gray code:**
```
0: 0
1: 1
```

**2-bit Gray code** (reflect 1-bit, prepend 0 to top half, 1 to bottom half):
```
0: 00
1: 01
2: 11  ← differs from 01 by bit 1 only
3: 10  ← differs from 11 by bit 0 only
```

**3-bit Gray code:**
```
0: 000
1: 001
2: 011
3: 010
4: 110
5: 111
6: 101
7: 100
```

Notice: moving from `111` (5) to `101` (6) flips only bit 1. Moving from `100` (7) back to `000` (0) flips only bit 2. The code is **cyclic** — wraps around with single-bit transitions.

## Single-Bit-Flip Property

In standard binary:
- 7 = `0111`
- 8 = `1000`

**Three bits flip** (bits 0, 1, 2, 3 all change). If these bits are physically distributed or have propagation delays, the system can pass through intermediate invalid states (glitches).

In Gray code:
- 7 = `0100`
- 8 = `1100`

**One bit flips** (bit 3). No intermediate states exist. The transition is atomic.

## Rotary Encoder Application

Gray codes are ubiquitous in **rotary encoders** — mechanical/optical devices that measure angular position.

**Problem with binary encoding**: If a sensor straddles two bit positions during rotation, all bits might appear to flip simultaneously due to slight misalignment. A rotation from 7 to 8 could briefly read as `0101`, `1010`, or any intermediate value (glitch).

**Solution with Gray code**: Only one bit flips per increment. Even if the sensor is slightly misaligned, it reads either the old value or the new value — never a spurious intermediate.

### Absolute Encoders

An **absolute rotary encoder** has a coded disk with concentric tracks (one per bit). Each angular position corresponds to a unique code word.

Example: 3-bit encoder with 8 positions ($45°$ resolution):

| Angle | Binary | Gray |
|-------|--------|------|
| 0° | 000 | 000 |
| 45° | 001 | 001 |
| 90° | 010 | 011 |
| 135° | 011 | 010 |
| 180° | 100 | 110 |
| 225° | 101 | 111 |
| 270° | 110 | 101 |
| 315° | 111 | 100 |

The Gray code disk ensures glitch-free readings even during motion.

## Carry Propagation Analysis

In standard binary, incrementing requires **carry propagation**:
- $0111 \to 1000$ (decimal 7 → 8): carry ripples through all 4 bits
- Worst case: $2^n - 1 \to 2^n$ flips $n$ bits

Gray code has **zero carry propagation**: every transition flips exactly 1 bit. This is optimal for hardware (no ripple-carry logic needed) and optimal for physical systems (local transitions only).

## Traversal Cost: Visiting All Positions

**Question**: Starting at position 0, how many single-bit-flip steps are needed to visit all $N = 2^n$ positions in a Gray code?

**Answer**: Exactly $N$ steps — one step per position. Gray code defines a **Hamiltonian path** on the $n$-dimensional hypercube graph where vertices are $n$-bit strings and edges connect strings differing by 1 bit.

For cyclic Gray codes (which return to the start), this is a **Hamiltonian cycle**.

### Example: 3-bit (N=8)

Path: `000 → 001 → 011 → 010 → 110 → 111 → 101 → 100 → 000`
Steps: 8 transitions (including return to start)

This is **optimal** — you cannot visit 8 positions in fewer than 8 steps if each step flips only 1 bit.

## Comparison to Standard Binary

| Property | Binary | Gray Code |
|----------|--------|-----------|
| Bits flipped per increment | 1 to $n$ | Always 1 |
| Carry propagation | Yes | No |
| Cyclic | No* | Yes |
| Hamiltonian path | No | Yes |
| Hardware glitches | Possible | Impossible |

*Standard binary can be made cyclic (two's complement wraps), but transitions still flip multiple bits.

## Connection to BlackOops

The BlackOops framework hypothesizes that **the universe uses Gray code for state transitions** because:

1. **Unitarity requires continuity**: Quantum evolution operator $U(t)$ is continuous. No discontinuous jumps in state space.
2. **Locality forbids simultaneous distant changes**: Information propagates at $c$. A "carry bit" traveling faster than light would violate causality.
3. **Planck scale sets the bit size**: Each $l_p^2 \approx 2.612 \times 10^{-70}$ m² of horizon area is one bit. Transitions happen at Planck time $t_p \approx 5.391 \times 10^{-44}$ s intervals.

### Black Hole as Rotary Encoder

| Encoder Concept | Black Hole Physics |
|-----------------|-------------------|
| Total positions $N$ | Bekenstein-Hawking entropy $S = A/(4l_p^2)$ |
| Angular resolution | $4\pi / N$ steradians per bit |
| Single-bit-flip rule | Quantum state evolution (unitary, continuous) |
| Traversal cost | Hawking evaporation time $\propto N^{1.5}$ (see [[Key Results Summary]]) |
| Glitch-free transitions | Holographic principle (no information "in transit" to singularity) |

A solar-mass black hole ($M = 1.989 \times 10^{30}$ kg) has $N \approx 1.514 \times 10^{77}$ bits. Gray code ensures each bit flip is local and unambiguous. The evaporation time $t_{evap} \approx 6.619 \times 10^{74}$ s corresponds to releasing all $N$ bits with a $\sqrt{N}$ overhead factor (208.4× constant, see `test_core.py` Test 4).

## Graph-Theoretic Perspective

Gray code defines a path on the **$n$-cube graph** $Q_n$:
- Vertices: $2^n$ binary strings of length $n$
- Edges: connect strings differing by 1 bit
- Gray code: Hamiltonian cycle on $Q_n$

The cycle length is exactly $2^n$, which is optimal for visiting all vertices with single-edge steps.

## Numerical Example: 4-Bit Gray Code

| Decimal | Binary | Gray |
|---------|--------|------|
| 0 | 0000 | 0000 |
| 1 | 0001 | 0001 |
| 2 | 0010 | 0011 |
| 3 | 0011 | 0010 |
| 4 | 0100 | 0110 |
| 5 | 0101 | 0111 |
| 6 | 0110 | 0101 |
| 7 | 0111 | 0100 |
| 8 | 1000 | 1100 |
| ... | ... | ... |
| 15 | 1111 | 1000 |

Notice: 7 → 8 in binary flips 4 bits. In Gray code: `0100 → 1100` (1 bit).

## Conversion Formulas

**Binary to Gray**:
$$G_i = B_i \oplus B_{i+1}$$
where $\oplus$ is XOR and $B_n = 0$ (MSB has no higher bit).

**Gray to Binary**:
$$B_i = G_i \oplus B_{i+1}$$
(compute from MSB down).

## See Also

- [[Rotary Encoders]]
- [[Boolean Algebra & Physical Circuits]]
- [[Shannon Entropy]]
- [[Unitarity]]
- [[Quantum State Evolution]]
- [[Random Walks on Cyclic Groups]]
- [[Cayley Graphs]]

## References

1. Gray, F. (1953). "Pulse Code Communication". U.S. Patent 2,632,058.
2. Savage, C. (1997). "A Survey of Combinatorial Gray Codes". *SIAM Review*, 39(4), 605–629.
3. Knuth, D. E. (2011). *The Art of Computer Programming, Vol. 4A: Combinatorial Algorithms*. Addison-Wesley.
4. Petersen, T. K. (2015). "Two-dimensional Gray codes". *Discrete Mathematics*, 338(9), 1506–1514.
