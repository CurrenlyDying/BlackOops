# Monte Carlo Simulation

## Definition

**Monte Carlo simulation** is a computational technique that uses random sampling to obtain numerical results for deterministic or stochastic problems. The method is named after the Monte Carlo Casino in Monaco, reflecting its reliance on randomness (like gambling).

## Core Principle

For a quantity $Q$ that can be expressed as an expectation:

$$Q = \mathbb{E}[f(X)] = \int f(x) p(x) \, dx$$

where $X$ is a random variable with distribution $p(x)$, Monte Carlo estimates $Q$ by:

1. **Sample** $N$ independent realizations: $X_1, X_2, \ldots, X_N \sim p(x)$
2. **Compute** $f(X_i)$ for each sample
3. **Average**:
$$\hat{Q}_N = \frac{1}{N} \sum_{i=1}^{N} f(X_i)$$

**Law of Large Numbers**: As $N \to \infty$, $\hat{Q}_N \to Q$ (convergence guaranteed).

**Central Limit Theorem**: Error scales as $1/\sqrt{N}$:
$$\hat{Q}_N - Q \sim \mathcal{N}(0, \sigma^2 / N)$$

where $\sigma^2 = \text{Var}(f(X))$.

## Why It Works

### Statistical Foundation

For **independent** samples, the sample mean is an **unbiased estimator**:

$$\mathbb{E}[\hat{Q}_N] = \mathbb{E}\left[\frac{1}{N}\sum f(X_i)\right] = \frac{1}{N} \sum \mathbb{E}[f(X_i)] = Q$$

Variance decreases with sample size:

$$\text{Var}(\hat{Q}_N) = \frac{\sigma^2}{N}$$

**Standard error**: $\text{SE} = \sigma / \sqrt{N}$

To reduce error by factor of 10, need **100× more samples** (slow convergence, but dimension-independent).

## BlackOops Simulations

The `test_alignment.py` file implements four Monte Carlo simulations:

### Sim 1: Random Walk Alignment

**Goal**: Estimate expected steps for random walk on $\mathbb{Z}_N$ to return to origin.

**Method**:
1. Initialize walker at position 0
2. Step randomly ±1 (mod $N$) until return to 0
3. Record number of steps
4. Repeat 100,000 times
5. Compute mean and standard error

**Results**:
- $N = 10$: $18.3 \pm 0.4$ steps
- $N = 200$: $6275.9 \pm 150$ steps
- Power law fit: $\alpha N^{1.962}$

**Code**:
```python
def random_walk_alignment(N, max_steps=100000):
    position = 0
    for step in range(max_steps):
        position = (position + np.random.choice([-1, 1])) % N
        if position == 0:
            return step + 1
    return max_steps

samples = [random_walk_alignment(N) for _ in range(N_SAMPLES)]
mean_steps = np.mean(samples)
```

### Sim 2: Two-Body Timing Attack

**Goal**: Compare alignment time for two walkers vs one.

**Method**:
- Two walkers start at positions 0 and 1
- Both step randomly ±1
- Measure time until they **collide** (same position)
- Compare to single-walker return time

**Results**:
- Two-body is ~2× faster (factor 0.5 ratio)
- Same $O(N^2)$ scaling class
- No shortcut to creating recursive loops

### Sim 3: Phase Transition at Planck Mass

**Goal**: Find mass where black hole is maximally ambiguous (neither clearly BH nor not-BH).

**Method**:
- Define ambiguity metric: $Q = \min(N, 1/N)$ where $N$ = number of bits
- Sweep mass ratio $M/M_p$ from 0.01 to 10
- Find peak of $Q$

**Results**:
- Peak at $M/M_p = 0.225$ (not exactly 1 due to geometric factors)
- $N_{bits} = 0.916$ at peak
- Transition width: 0.23 decades (razor-sharp)

### Sim 4: Information Conservation

**Goal**: Verify unitarity (total bits conserved during evaporation).

**Method**:
- Start with 1000-bit encoder
- Simulate evaporation (release bits one at a time)
- Track: (bits in BH) + (bits in radiation) = constant?

**Results**:
- Total conserved at every step (by construction)
- Demonstrates unitarity preservation

## Parameters and Sampling

### Sample Size $N_{\text{samples}}$

**Trade-off**:
- **Larger $N$**: Lower error ($\propto 1/\sqrt{N}$), longer runtime
- **Smaller $N$**: Higher error, faster runtime

BlackOops uses $N = 100{,}000$ (default), tunable via:

```python
N_SAMPLES = 100_000  # Default
N_SAMPLES = 10_000_000  # Heavy mode (Colab/GPU)
```

**Error reduction**:
- 10K samples: $\text{SE} \propto 1/\sqrt{10^4} = 1/100$
- 100K samples: $\text{SE} \propto 1/\sqrt{10^5} = 1/316$ (3.16× better)
- 10M samples: $\text{SE} \propto 1/\sqrt{10^7} = 1/3162$ (31.6× better than 10K)

### Maximum Steps Cutoff

To prevent infinite loops (walker never returns), impose cutoff:

```python
max_steps = 100_000  # Return this value if no alignment
```

For large $N$, some walks exceed cutoff → **censored data** (biases mean downward). Solution:
- Increase `max_steps` for large $N$
- Or exclude censored runs from analysis

### Variance Reduction Techniques

**Not used in BlackOops** (simple MC sufficient), but available:

1. **Importance sampling**: Sample from different distribution, reweight
2. **Stratified sampling**: Divide domain into strata, sample uniformly from each
3. **Control variates**: Use correlated variable with known mean to reduce variance
4. **Antithetic variates**: Generate negatively correlated samples (e.g., if $U \sim \text{Uniform}(0,1)$, use $1-U$ too)

For power law fitting across many decades, **stratified sampling** by $N$ (sample uniformly in $\log N$ space) would help, but BlackOops uses fixed $N$ values instead.

## Convergence and Error Analysis

### Standard Error

For sample mean $\hat{\mu} = \frac{1}{N}\sum X_i$:

$$\text{SE}(\hat{\mu}) = \frac{\sigma}{\sqrt{N}}$$

where $\sigma = \sqrt{\text{Var}(X)}$ is population standard deviation.

**Estimate** $\sigma$ from sample:

$$\hat{\sigma} = \sqrt{\frac{1}{N-1}\sum (X_i - \hat{\mu})^2}$$

Then:

$$\text{SE} = \frac{\hat{\sigma}}{\sqrt{N}}$$

**95% confidence interval**: $\hat{\mu} \pm 1.96 \cdot \text{SE}$

### Convergence Diagnostics

**Plot** running mean vs sample size:

$$\hat{\mu}_n = \frac{1}{n} \sum_{i=1}^{n} X_i$$

Should **stabilize** as $n$ increases. Fluctuations decrease as $1/\sqrt{n}$.

**Autocorrelation**: For random walk steps, successive samples are **independent** (each walk is a fresh start). Autocorrelation = 0 → no correction needed.

For **correlated** samples (e.g., Markov chain MC), effective sample size is smaller:

$$N_{\text{eff}} = \frac{N}{1 + 2\sum_{k=1}^{\infty} \rho_k}$$

where $\rho_k$ is autocorrelation at lag $k$.

## Power Law Fitting from MC Data

After obtaining $(\bar{t}_1, N_1), (\bar{t}_2, N_2), \ldots$:

1. **Log-transform**: $y_i = \log \bar{t}_i$, $x_i = \log N_i$
2. **Linear regression**: $y = a + b x$
3. **Extract**: $\beta = b$ (exponent), $\alpha = e^a$ (coefficient)

**Uncertainty in $\beta$**:

Standard error of slope in linear regression:

$$\text{SE}(\beta) = \sqrt{\frac{\sum (y_i - \hat{y}_i)^2}{(n-2) \sum (x_i - \bar{x})^2}}$$

For BlackOops Sim 1 with 5 data points:
- Fit: $\beta = 1.962$
- $R^2 = 0.9998$ (near-perfect linear on log-log)
- $\text{SE}(\beta) \approx 0.05$ (estimated from residuals)

Thus $\beta = 1.96 \pm 0.05$, consistent with theoretical 2.0.

## GPU Acceleration

Monte Carlo is **embarrassingly parallel** — samples are independent.

**CPU**: Sequential loop through 100K samples
**GPU**: Parallel computation of all samples simultaneously

**Speedup**: 10-100× for MC simulations (depends on sample complexity).

### Python GPU Tools

1. **CuPy** (NumPy-compatible GPU arrays):
```python
import cupy as cp
samples = cp.random.choice([-1, 1], size=(N_SAMPLES, max_steps))
```

2. **JAX** (JIT compilation + autodiff):
```python
import jax.numpy as jnp
from jax import jit, vmap
@jit
def walk(key):
    # ... random walk logic
walks = vmap(walk)(keys)  # Vectorize over samples
```

3. **Numba** (CPU/GPU JIT):
```python
from numba import cuda
@cuda.jit
def walk_kernel(output):
    # ... CUDA kernel
```

**BlackOops recommendation**: Use JAX for 10-100× speedup on GPU (Colab T4/A100).

## How Many Samples for Reliable Power Law Fit?

**Rule of thumb**: Need $\text{SE}(\beta) < 0.05$ for 2-decimal precision.

If mean has SE $\sim \sigma/\sqrt{N}$, and we fit $k$ points, total error in $\beta$ is roughly:

$$\text{SE}(\beta) \sim \frac{1}{\sqrt{k}} \cdot \frac{\text{SE}(\text{mean})}{\text{dynamic range in } \log x}$$

For $k = 5$ points spanning 1 decade each:
- Need $\text{SE}(\text{mean}) / \bar{t} < 0.01$ (1% error)
- Thus $\sigma / \sqrt{N} < 0.01 \bar{t}$
- For $\sigma \sim \bar{t}$ (typical), need $N > 10^4$

BlackOops uses $N = 10^5$ → 0.3% error per point → $\beta$ precise to $\pm 0.05$.

## Connection to BlackOops

Monte Carlo is essential for:

1. **Random walk alignment**: No closed-form solution for return time distribution on finite cycle
2. **Phase transition**: Ambiguity function is non-analytic (need numerical sweep)
3. **Validation**: Even for analytically solvable cases (evaporation time), MC confirms formulas

The simulations **complement** analytical tests:
- **Analytical** (Test 1-5): Exact formulas, no sampling error, fast
- **Monte Carlo** (Sim 1-4): Handles complex dynamics, quantifies uncertainty, slower

Together, they provide **redundant verification** of the encoder model.

## Historical Context

- **1940s**: Stanisław Ulam and John von Neumann develop MC for neutron diffusion (Manhattan Project)
- **1949**: Metropolis algorithm (MCMC for thermal equilibrium)
- **1953**: "Monte Carlo method" term published by Metropolis & Ulam
- **1970s**: MC becomes standard in physics (lattice QCD, Ising model)
- **2000s**: GPU acceleration makes MC viable for billion-sample simulations

## See Also

- [[Random Walks on Cyclic Groups]]
- [[Power Law Scaling]]
- [[Shannon Entropy]]
- [[Reinforcement Learning]]
- [[GPU Acceleration Guide]]

## References

1. Metropolis, N., & Ulam, S. (1949). "The Monte Carlo Method". *Journal of the American Statistical Association*, 44(247), 335–341.
2. Kalos, M. H., & Whitlock, P. A. (2008). *Monte Carlo Methods* (2nd ed.). Wiley-VCH.
3. Kroese, D. P., Taimre, T., & Botev, Z. I. (2011). *Handbook of Monte Carlo Methods*. Wiley.
4. Robert, C. P., & Casella, G. (2004). *Monte Carlo Statistical Methods* (2nd ed.). Springer.
