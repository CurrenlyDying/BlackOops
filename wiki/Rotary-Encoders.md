# Rotary Encoders

## Definition

A **rotary encoder** is an electromechanical device that converts angular position or motion of a shaft into an analog or digital output signal. Rotary encoders are fundamental components in robotics, CNC machines, motor control systems, and precision measurement instruments.

## Types of Rotary Encoders

### Absolute Encoders

**Absolute encoders** provide a unique code word for each angular position. When power is lost and restored, the encoder immediately knows its position without needing to move.

**Implementation**: Multi-track disk with concentric rings (one per bit). Each ring has opaque/transparent segments read by optical sensors. The pattern encodes the position directly.

**Advantages**:
- No homing sequence needed after power-up
- Position information never lost
- Suitable for safety-critical applications

**Disadvantages**:
- More complex (requires $n$ sensors for $n$-bit resolution)
- More expensive than incremental encoders

### Incremental Encoders

**Incremental encoders** output pulses corresponding to motion. They track *changes* in position, not absolute position.

**Implementation**: Single or dual track with evenly-spaced marks. Each mark transition generates a pulse. Quadrature encoding (two tracks 90° out of phase) determines direction.

**Advantages**:
- Simple and cheap
- High resolution possible (many pulses per revolution)

**Disadvantages**:
- Position lost on power cycle (must re-home)
- Cumulative errors if pulses are missed

## Angular Resolution

**Resolution** is the smallest angular increment the encoder can distinguish:

$$\text{Resolution} = \frac{360°}{2^n} = \frac{2\pi}{2^n} \text{ radians}$$

for an $n$-bit absolute encoder.

### Examples:

| Bits $n$ | Positions $2^n$ | Angular Resolution | Per Position (sr) |
|----------|----------------|-------------------|-------------------|
| 8 | 256 | 1.406° | 0.0491 sr |
| 10 | 1024 | 0.352° | 0.0123 sr |
| 12 | 4096 | 0.088° | 0.00307 sr |
| 16 | 65,536 | 0.0055° | 0.000191 sr |
| 20 | 1,048,576 | 0.00034° | 1.20 × 10⁻⁵ sr |

(Solid angle per position: $4\pi / 2^n$ steradians)

## Why Gray Code?

Rotary encoders using **standard binary encoding** suffer from **glitch states** during transitions.

**Problem**: When rotating from position 7 (binary `0111`) to position 8 (binary `1000`), all four bits must change simultaneously. If sensors are slightly misaligned or have different response times, the encoder might briefly read:
- `0110` (6)
- `0101` (5)
- `1111` (15)
- or any other invalid intermediate value

This is catastrophic for control systems (e.g., a robot arm suddenly "thinks" it jumped from 7 to 15).

**Solution**: Use **Gray code** encoding, where only one bit changes between adjacent positions.

| Position | Binary | Gray Code |
|----------|--------|-----------|
| 6 | 0110 | 0101 |
| 7 | 0111 | 0100 |
| 8 | 1000 | 1100 |

Now the transition 7 → 8 flips only bit 3. Even if the sensor is misaligned, it reads either `0100` (7) or `1100` (8) — never a glitch.

### Physical Realization

A 3-bit Gray code absolute encoder disk:

```
      Bit 2  Bit 1  Bit 0
       ___    ___    ___
      /   \  /   \  /   \
Track 0: ████░░░░████░░░░
Track 1: ░░████████░░░░░░
Track 2: ░░░░████████████
       (concentric rings on disk)
```

Each ring is read by an optical sensor (LED + photodetector). Black = 1, white = 0. As the disk rotates, only one track changes at a time.

## Analogy to Physical State Transitions

The BlackOops framework uses rotary encoders as a **conceptual model** for how the universe manages state transitions.

**Claim**: Just as Gray code encoders prevent glitches by enforcing single-bit transitions, the universe prevents "glitches" (violations of unitarity, causality, locality) by enforcing **single-bit state transitions** at the Planck scale.

| Encoder Property | Physical Analog |
|------------------|----------------|
| Angular resolution | Planck area $l_p^2 \approx 2.612 \times 10^{-70}$ m² |
| Total positions $N$ | Bekenstein-Hawking entropy $S = A/(4l_p^2)$ |
| Single-bit-flip rule | Unitary quantum evolution (continuous, no jumps) |
| Glitch-free reading | Holographic principle (info on horizon, not "in transit") |
| Sensor misalignment | Quantum uncertainty / measurement back-reaction |

A black hole horizon is an "encoder disk" with $N \sim 10^{77}$ positions (for solar mass). Each position differs from its neighbors by exactly one Planck-area bit. Hawking radiation "reads out" the encoder state one bit at a time.

## Connection to BlackOops

In `constants.py`, the `EncoderState` class models black holes as rotary encoders:

```python
@property
def angular_resolution_sr(self) -> float:
    """Angular resolution per bit [steradians].
    Total solid angle (4π) divided by number of bits."""
    return 4 * pi / self.n_bits
```

For a solar-mass black hole:
- $N = 1.514 \times 10^{77}$ bits
- Angular resolution: $8.31 \times 10^{-77}$ steradians per bit
- Linear resolution at horizon: $\sim l_p$ (one Planck length)

This is the "encoder disk" the universe uses to track the black hole's state. The Gray code constraint ensures that when the black hole radiates one bit (Hawking radiation), only that one bit changes — the rest of the horizon remains coherent.

### Alignment Problem

In a physical rotary encoder, if you try to **write** to the encoder (update its position) faster than its angular resolution allows, the write fails or produces garbage. Similarly, in the BlackOops model:

- **Infalling information** tries to "write" to the black hole encoder
- If it arrives **faster than the encoder can process** (faster than Planck time $t_p$), the information cannot align with a specific encoder position
- Probability of alignment per tick: $P \sim 1/N$

For $N \sim 10^{77}$, the alignment probability is $\sim 10^{-77}$ per Planck time. This is why information stays on the horizon (holographic principle) rather than reaching the singularity — it can't "find" an available encoder position fast enough.

## Numerical Example: Planck-Mass Black Hole

At $M = m_p = 2.176 \times 10^{-8}$ kg:
- Schwarzschild radius: $r_s = 2 l_p = 3.23 \times 10^{-35}$ m
- Horizon area: $A = 4\pi (2l_p)^2 = 16\pi l_p^2$
- Number of bits: $N = 16\pi l_p^2 / (4 l_p^2 \ln 2) = 4\pi / \ln 2 \approx 18.13$ bits

This is a **~5-bit encoder** (since $2^4 = 16 < 18 < 32 = 2^5$). Angular resolution: $4\pi / 18.13 \approx 0.693$ steradians per bit.

This encoder can distinguish ~18 angular positions. It's the smallest black hole that's still meaningfully a "black hole" before quantum gravity effects dominate completely.

## Historical Applications

- **1940s**: Rotary encoders used in military radar systems for antenna position tracking
- **1960s**: Optical encoders replace mechanical contacts (longer lifespan, higher resolution)
- **1980s**: Magnetic encoders emerge (immune to dust/oil contamination)
- **2000s**: Absolute encoders with 20+ bit resolution (sub-arcsecond precision) become standard in robotics

## See Also

- [[Gray Code]]
- [[Boolean Algebra & Physical Circuits]]
- [[Shannon Entropy]]
- [[Bekenstein-Hawking Entropy]]
- [[Quantum State Evolution]]
- [[Planck Units]]

## References

1. Gray, F. (1953). "Pulse Code Communication". U.S. Patent 2,632,058.
2. Heidenhain Corp. "Rotary Encoders Technical Information". https://www.heidenhain.com
3. Petersen, T. K., & Stein, M. (2020). "Gray Code Encoders in Control Systems". *IEEE Transactions on Industrial Electronics*, 67(3), 2145–2154.
4. Hughes, E. (2015). *Electrical and Electronic Technology* (11th ed.). Pearson.
