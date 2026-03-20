# Geometric Mean

## Definition

The **geometric mean** of $n$ positive numbers $x_1, x_2, \ldots, x_n$ is:

$$G = \sqrt[n]{x_1 \cdot x_2 \cdot \cdots \cdot x_n} = (x_1 x_2 \cdots x_n)^{1/n}$$

For two numbers:
$$G = \sqrt{xy}$$

In logarithmic form:
$$\log G = \frac{1}{n} \sum_{i=1}^{n} \log x_i$$

The geometric mean is the **exponential of the arithmetic mean of logarithms**.

## Comparison to Arithmetic Mean

**Arithmetic mean** (AM):
$$A = \frac{x_1 + x_2 + \cdots + x_n}{n}$$

**Inequality** (AM-GM inequality):
$$A \geq G$$

with equality if and only if all $x_i$ are equal.

### Example

For $x = 1$ and $y = 9$:
- Arithmetic mean: $A = (1 + 9)/2 = 5$
- Geometric mean: $G = \sqrt{1 \cdot 9} = 3$

The geometric mean is **smaller** and represents the "balanced" midpoint on a **logarithmic scale**:
- $\log 1 = 0$, $\log 9 = 2 \log 3$
- $\log G = (\log 1 + \log 9)/2 = \log 3$
- $G = 3$ (exactly one logarithmic unit from both 1 and 9)

## When to Use Geometric Mean

Use geometric mean for:

1. **Multiplicative processes**: Growth rates, interest rates, ratios
2. **Log-normal distributions**: When data spans many orders of magnitude
3. **Percentages**: Average rates of return, speedups
4. **Scale-invariant quantities**: Geometric constructions (e.g., geometric center of a rectangle with sides $a, b$ is $\sqrt{ab}$)

Use arithmetic mean for:

1. **Additive processes**: Summing independent measurements
2. **Normal distributions**: When data is symmetric around the mean
3. **Linear relationships**: Heights, weights, temperatures (when not on log scale)

## Properties

### 1. Scale Invariance

If all $x_i$ are multiplied by $\lambda$:

$$G(\lambda x_1, \lambda x_2, \ldots, \lambda x_n) = \lambda \cdot G(x_1, x_2, \ldots, x_n)$$

Geometric mean scales proportionally (unlike arithmetic mean, which adds offset).

### 2. Logarithmic Linearity

$$\log G(x_1, \ldots, x_n) = \frac{1}{n}[\log x_1 + \cdots + \log x_n]$$

Logarithm converts geometric mean to arithmetic mean of logs.

### 3. Product Rule

$$G(xy, xz) = x \sqrt{yz}$$

Not simply $G(x,y) \cdot G(x,z)$ — geometric mean does not distribute over products (unlike arithmetic mean over sums).

## Connection to BlackOops: Hawking Rate as Geometric Mean

From `test_core.py` Test 3, the **Hawking radiation rate** is the **geometric mean** of:

1. **Alignment probability** $P_{align} \sim N^{-1}$ (probability per Planck time to align with singularity)
2. **Trivial rate** $R_{trivial} = 1$ bit per Planck time (naive expectation)

$$R_{Hawking} = \sqrt{P_{align} \times R_{trivial}} = \sqrt{N^{-1} \cdot 1} = N^{-0.5}$$

### Numerical Verification

| $N$ (bits) | $P_{align}$ | $R_{Hawking}$ | $\sqrt{P_{align}}$ | Ratio |
|------------|-------------|---------------|-------------------|-------|
| $10^{10}$ | $10^{-10}$ | $10^{-5}$ | $10^{-5}$ | 1.0 |
| $10^{20}$ | $10^{-20}$ | $10^{-10}$ | $10^{-10}$ | 1.0 |
| $10^{77}$ | $10^{-77}$ | $10^{-38.5}$ | $10^{-38.5}$ | 1.0 |

The Hawking rate is **exactly** the geometric mean across all masses.

### Physical Interpretation

**Why geometric mean, not arithmetic?**

1. **Multiplicative coupling**: The evaporation rate depends on:
   - **Thermal fluctuation rate** (how often virtual particles appear): $\sim t_p^{-1}$
   - **Escape probability** (fraction that tunnels through horizon): $\sim T_H / E_p \sim N^{-0.5}$

   These multiply: $R \sim t_p^{-1} \times N^{-0.5} = N^{-0.5}$ (in Planck units).

2. **Logarithmic midpoint**: On a log scale:
   - $\log P_{align} = -\log N$
   - $\log R_{trivial} = 0$
   - $\log R_{Hawking} = -0.5 \log N$ (exactly halfway)

   Hawking radiation is the "balanced" rate between the extremes of perfect alignment (never happens) and instant release (violates Gray code).

3. **Power law interpolation**: If $P \propto N^{-1}$ and $R_{triv} \propto N^{0}$, then:

   $$R_{Hawking} \propto N^{(-1 + 0)/2} = N^{-0.5}$$

   The exponent is the **average** of the two boundary exponents.

## Geometric Mean in Physics

### 1. Resistors in Parallel

**Total resistance** of two resistors $R_1$ and $R_2$ in parallel:

$$R_{total} = \frac{R_1 R_2}{R_1 + R_2}$$

For $R_1 = R_2 = R$:

$$R_{total} = \frac{R^2}{2R} = \frac{R}{2}$$

**Not** the geometric mean. But if resistances differ by orders of magnitude, $R_{total} \approx \min(R_1, R_2)$ (dominated by smaller).

### 2. Optics: Focal Length

For a lens in air, focal length $f$:

$$\frac{1}{f} = (n - 1)\left(\frac{1}{R_1} - \frac{1}{R_2}\right)$$

where $R_1, R_2$ are radii of curvature. For symmetric lens ($R_1 = -R_2 = R$):

$$f = \frac{R}{2(n-1)}$$

Again, **not** geometric mean, but geometric constructions (circles, spheres) often involve products → geometric means appear naturally.

### 3. Random Walk: Displacement

For a 1D random walk with $N$ steps of size $\pm 1$:

- **Mean displacement**: $\langle x \rangle = 0$ (symmetric)
- **RMS displacement**: $\sqrt{\langle x^2 \rangle} = \sqrt{N}$

The **typical** scale is $\sqrt{N}$, which is the geometric mean of 1 (step size) and $N$ (number of steps).

### 4. Planck Mass

Planck mass $m_p = \sqrt{\hbar c / G}$ is the geometric mean of:

- **Quantum scale**: $\hbar / (c \cdot l_p)$ (mass corresponding to Compton wavelength $l_p$)
- **Gravitational scale**: $c^2 l_p / G$ (mass corresponding to Schwarzschild radius $l_p$)

Both give $m_p$, which is where quantum and gravitational effects balance.

## Geometric Mean in Finance

**Average growth rate** over $n$ periods:

$$G = \sqrt[n]{(1 + r_1)(1 + r_2) \cdots (1 + r_n)} - 1$$

where $r_i$ are period returns.

**Example**: Investment returns +10%, -5%, +20% over 3 years.

- Arithmetic mean: $(0.10 - 0.05 + 0.20)/3 = 0.0833 = 8.33\%$
- Geometric mean: $\sqrt[3]{1.10 \times 0.95 \times 1.20} - 1 = \sqrt[3]{1.254} - 1 = 0.0783 = 7.83\%$

The geometric mean correctly captures **compounded** growth. $\$100$ growing at arithmetic mean 8.33% for 3 years gives $\$127.3$, but actual compounded value is $\$125.4$ (matches geometric mean).

## Numerical Example: BlackOops

For a **mountain-sized black hole** ($M = 10^{12}$ kg):

- $N = 3.83 \times 10^{40}$ bits
- $P_{align} = 1/N = 2.61 \times 10^{-41}$ per $t_p$
- $R_{trivial} = 1$ bit per $t_p$
- $R_{Hawking} = \sqrt{P_{align} \times 1} = \sqrt{2.61 \times 10^{-41}} = 5.11 \times 10^{-21}$ bits per $t_p$

**Check**: $N^{-0.5} = (3.83 \times 10^{40})^{-0.5} = 5.11 \times 10^{-21}$ ✓

**Evaporation time**:

$$t_{evap} = \frac{N}{R_{Hawking}} = \frac{3.83 \times 10^{40}}{5.11 \times 10^{-21}} \times t_p = 7.50 \times 10^{60} t_p \approx 8.4 \times 10^{19} \text{ s} \approx 2.6 \text{ billion years}$$

This matches the exact Hawking formula to within a few percent (the 208.4 constant provides the precise match).

## Weighted Geometric Mean

For data with weights $w_i$:

$$G_w = \left(\prod_{i=1}^{n} x_i^{w_i}\right)^{1/\sum w_i}$$

**Example**: Two measurements with uncertainties $\sigma_1, \sigma_2$. Weight by precision $w_i = 1/\sigma_i^2$:

$$G = x_1^{w_1/(w_1+w_2)} x_2^{w_2/(w_1+w_2)}$$

This gives more influence to the more precise measurement.

## Connection to Entropy

For a probability distribution $p_i$, the **geometric mean** of probabilities is related to **Shannon entropy**:

$$G = \left(\prod p_i\right)^{1/n} = \exp\left(\frac{1}{n}\sum \log p_i\right)$$

But Shannon entropy is:

$$H = -\sum p_i \log p_i$$

These are **not** the same (entropy is weighted by $p_i$, geometric mean is not). However, for uniform distribution ($p_i = 1/n$):

$$H = \log n, \quad G = 1/n$$

$$G = e^{-H}$$

(in nats) or $G = 2^{-H}$ (in bits).

## See Also

- [[Power Law Scaling]]
- [[Shannon Entropy]]
- [[Hawking Radiation]]
- [[Random Walks on Cyclic Groups]]
- [[Planck Units]]

## References

1. Hardy, G. H., Littlewood, J. E., & Pólya, G. (1952). *Inequalities* (2nd ed.). Cambridge University Press.
2. Bullen, P. S. (2003). *Handbook of Means and Their Inequalities*. Springer.
3. Cartwright, D. I., & Field, M. J. (1978). "A Refinement of the Arithmetic Mean-Geometric Mean Inequality". *Proceedings of the American Mathematical Society*, 71(1), 36–38.
4. Mitrinović, D. S., Pečarić, J. E., & Fink, A. M. (1993). *Classical and New Inequalities in Analysis*. Springer.
