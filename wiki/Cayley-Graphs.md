# [EXTENDED] Cayley Graphs

## Overview

A **Cayley graph** is a graph that encodes the structure of a group using a generating set. It visualizes group elements as vertices and group operations as edges, making abstract algebra geometric and intuitive.

## Definition

For a group $G$ and generating set $S \subseteq G$ (with $S^{-1} = S$):

**Cayley graph** $\text{Cay}(G, S)$:
- **Vertices**: Elements of $G$
- **Edges**: $(g, gs)$ for all $g \in G, s \in S$

The graph is **directed** if $S \neq S^{-1}$, **undirected** otherwise.

## Example: Cyclic Group $\mathbb{Z}_N$

For $\mathbb{Z}_N = \{0, 1, 2, \ldots, N-1\}$ with generator $S = \{1, -1\}$ (addition mod $N$):

**Cayley graph**: Cycle graph $C_N$
- Vertices: $0, 1, 2, \ldots, N-1$ arranged in a circle
- Edges: $k \leftrightarrow (k+1) \bmod N$ for all $k$

This is the **encoder graph** in BlackOops: each position differs from neighbors by ±1 (Gray code single-bit-flip).

### Example: $\mathbb{Z}_5$

```
    0
   / \
  4   1
  |   |
  3 - 2
```

Each vertex has degree 2 (connected to $k-1$ and $k+1$ mod 5).

## Properties

### 1. Regularity

All vertices have the same degree $|S|$ (in undirected case, $|S|/2$ if $S = S^{-1}$).

**Black hole encoder**: Degree = 2 (move ±1 position)

### 2. Vertex Transitivity

Group action $g \cdot h = gh$ maps vertex $h$ to $gh$. This is an **automorphism** (preserves graph structure).

**Implication**: All vertices "look the same" — no preferred position on the encoder.

### 3. Diameter

**Diameter** $d(G, S)$: Maximum distance between any two vertices.

For $\mathbb{Z}_N$ with $S = \{±1\}$:
$$d = \lfloor N/2 \rfloor$$

(Farthest point is halfway around the cycle.)

**BlackOops**: Maximum alignment distance is $N/2$ encoder positions.

### 4. Spectral Gap

**Spectral gap** $\lambda$: Difference between largest and second-largest eigenvalue of adjacency matrix.

For $\mathbb{Z}_N$:
$$\lambda = 1 - \cos(2\pi/N) \approx 2\pi^2/N^2 \quad \text{(large } N\text{)}$$

**Mixing time** $\sim 1/\lambda \sim N^2$ — how long random walk takes to reach equilibrium.

**BlackOops connection**: Alignment time $\sim N^2$ matches spectral gap prediction.

## Random Walks on Cayley Graphs

A **random walk** on $\text{Cay}(G, S)$:
1. Start at identity $e \in G$
2. At each step, multiply by random $s \in S$: $g \to gs$

For $\mathbb{Z}_N$ with $S = \{±1\}$, this is a **symmetric random walk on a cycle**.

**Return time**: Expected steps to return to starting position.

- **Infinite line** ($\mathbb{Z}$): $\mathbb{E}[\tau] = \infty$ (recurrent but not positive recurrent)
- **Cycle** ($\mathbb{Z}_N$): $\mathbb{E}[\tau] = N$ (positive recurrent)

**BlackOops Sim 1**: Observed $\mathbb{E}[\tau] \propto N^{1.96} \approx N^2$, matching theory (with prefactor ~0.34).

## Higher-Dimensional Cayley Graphs

### $\mathbb{Z}^2$ (2D Integer Lattice)

Generators: $S = \{(±1, 0), (0, ±1)\}$

**Graph**: Infinite square grid

**Random walk**: 2D Brownian motion (diffusive)

**Return time**: $\mathbb{E}[\tau] \sim N^2 \log N$ for $N \times N$ toroidal lattice

**Relevance**: Black hole horizon is a 2D surface → encoder is closer to $\mathbb{Z}^2$ than $\mathbb{Z}_N$ (explains $N^2$ scaling vs $N$).

### Hypercube $\mathbb{Z}_2^n$

Generators: $S = \{e_1, e_2, \ldots, e_n\}$ (flip one bit)

**Graph**: $n$-dimensional hypercube $Q_n$
- $2^n$ vertices (all $n$-bit strings)
- Each vertex has degree $n$

**Gray code** is a **Hamiltonian path** on $Q_n$ — visits all vertices exactly once.

**BlackOops interpretation**: An $N$-bit encoder is an $n = \log_2 N$ dimensional hypercube. Gray code traversal is a path through this hypercube.

## Expansion and Mixing

**Expander graph**: Cayley graph with large spectral gap (fast mixing).

**Ramanujan graphs**: Optimal expanders (spectral gap as large as possible for given degree).

**Cycle graph $C_N$**: **Not** an expander (spectral gap $\sim 1/N^2$ is small).

**Consequence for BlackOops**: Alignment is **slow** (not fast-mixing) because encoder is a cycle, not an expander.

If encoder were an expander:
- Alignment time $\sim \log N$ (polylog, not polynomial)
- Evaporation would dominate alignment easily
- Holographic principle would be even stronger

But cycles are **natural** for rotary encoders (physical geometry dictates structure).

## Cayley Graphs and Group Theory

### Abelian Groups

For abelian (commutative) groups, Cayley graphs have nice properties:
- **Vertex-transitive** (all vertices equivalent)
- **Edge-transitive** (all edges equivalent)
- **High symmetry**

$\mathbb{Z}_N$ is abelian → $\text{Cay}(\mathbb{Z}_N, \{±1\})$ is maximally symmetric.

### Non-Abelian Groups

For non-abelian groups (e.g., permutation groups $S_n$), Cayley graphs are more complex:
- Vertices still equivalent (by definition)
- But graph structure can be intricate

**Example**: $S_3$ (permutations of 3 elements) with generators = transpositions → Cayley graph has 6 vertices, hexagonal structure.

## Connection to BlackOops

The BlackOops encoder is **exactly** the Cayley graph $\text{Cay}(\mathbb{Z}_N, \{±1\})$:

| Cayley Graph Concept | BlackOops Encoder |
|---------------------|-------------------|
| Vertices | Encoder positions (Planck-area patches on horizon) |
| Edges | Gray code single-bit-flip transitions |
| Group operation (addition) | State evolution (unitary time step) |
| Random walk | Infalling information trying to align |
| Return time $\sim N$ | Naive alignment time (linearexpectation) |
| Hitting time $\sim N^2/4$ | Actual alignment time (to antipodal point) |
| Diameter $N/2$ | Maximum encoder distance |
| Spectral gap $\sim 1/N^2$ | Mixing timescale |

The **entire BlackOops framework** is a random walk on a Cayley graph. All the scaling laws ($N^{1.5}$ evaporation, $N^{2.0}$ alignment) emerge from the **graph structure**.

### Why Cyclic Group?

The encoder is $\mathbb{Z}_N$ (cyclic) because:

1. **Physical geometry**: Horizon is a 2D sphere (closed surface, no boundary)
2. **Unitarity**: Quantum evolution is reversible → group (not semigroup)
3. **Single-bit-flip**: Gray code constraint → generators $S = \{±1\}$
4. **Homogeneity**: All Planck patches equivalent → abelian group

These constraints uniquely determine $\text{Cay}(\mathbb{Z}_N, \{±1\})$.

## Spectral Graph Theory

**Adjacency matrix** $A$ of Cayley graph:
$$A_{ij} = \begin{cases} 1 & \text{if } (i,j) \text{ is edge} \\ 0 & \text{otherwise} \end{cases}$$

**Eigenvalues** $\{\lambda_0, \lambda_1, \ldots, \lambda_{N-1}\}$ determine:
- **Mixing time**: $\sim 1/(\lambda_0 - \lambda_1)$
- **Expansion**: $\sim \lambda_1$
- **Random walk return prob**: $\sim \sum_k \lambda_k^t / N$ at time $t$

For $\mathbb{Z}_N$:
$$\lambda_k = 2\cos(2\pi k / N), \quad k = 0, 1, \ldots, N-1$$

Largest: $\lambda_0 = 2$ (constant eigenvector)
Second: $\lambda_1 = 2\cos(2\pi/N) \approx 2 - 2\pi^2/N^2$

**Spectral gap**: $2 - \lambda_1 = 2\pi^2 / N^2$ → mixing time $\sim N^2 / (2\pi^2)$.

**BlackOops numerics**: Alignment time $\approx 0.34 N^2 = N^2 / 2.94 \approx N^2 / \pi$ (close to $N^2 / (2\pi^2) \times 2\pi = N^2 / \pi$).

## Applications Beyond BlackOops

Cayley graphs appear in:

1. **Crystallography**: Atomic lattices as Cayley graphs of space groups
2. **Network topology**: Interconnect networks in supercomputers (e.g., hypercube, torus)
3. **Error-correcting codes**: Code graph = Cayley graph of syndrome space
4. **Quantum computing**: Quantum walk on Cayley graph (quantum speedup for search)
5. **Cryptography**: Cayley hash functions (collision resistance from expander properties)

## See Also

- [[Random Walks on Cyclic Groups]]
- [[Gray Code]]
- [[Spectral Gap and Mixing Time]]
- [[Monte Carlo Simulation]]
- [[Power Law Scaling]]

## References

1. Diaconis, P. (1988). *Group Representations in Probability and Statistics*. Institute of Mathematical Statistics.
2. Davidoff, G., Sarnak, P., & Valette, A. (2003). *Elementary Number Theory, Group Theory, and Ramanujan Graphs*. Cambridge University Press.
3. Aldous, D., & Fill, J. (2002). *Reversible Markov Chains and Random Walks on Graphs*. https://www.stat.berkeley.edu/~aldous/RWG/book.html
4. Lovász, L. (1993). "Random Walks on Graphs: A Survey". *Combinatorics, Paul Erdős is Eighty*, 2, 1–46.
