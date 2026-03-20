# Shannon's Theseus

## Overview

**Theseus** was an electromechanical maze-solving "mouse" built by Claude Shannon in 1950 at Bell Labs. It was one of the earliest examples of a machine that learned from experience — a precursor to modern reinforcement learning.

## The Device

Theseus consisted of:
- A 5×5 grid maze with movable walls (25 squares)
- A magnetic "mouse" (copper piece) that could be moved by electromagnets beneath the maze
- A relay-based memory system (~100 relays) that stored which squares had been explored and which led to the goal
- A control circuit that implemented a search strategy

The mouse would explore the maze randomly until it found the goal (a designated square). Once the goal was reached, the relay memory "remembered" the successful path. On subsequent runs, the mouse would navigate directly to the goal without exploring dead ends.

## How It Worked

### Memory Encoding

Each of the 25 maze squares had associated relay circuits encoding:
- Has this square been visited?
- From which direction did we arrive?
- Which direction led toward the goal?

The relays stored this information **persistently** — the maze "knew" the solution even after the mouse was reset to the start.

### Search Algorithm

1. **Exploration phase** (first run):
   - Move randomly (or semi-randomly, avoiding recently visited squares)
   - Mark each square as visited
   - When goal is reached, backtrack through memory to mark the successful path

2. **Exploitation phase** (subsequent runs):
   - Follow stored directions from memory
   - Navigate directly to goal

This is the **explore-exploit tradeoff**, central to reinforcement learning.

## Information-Theoretic Interpretation

Shannon described Theseus in terms of **entropy reduction**:

- **Initial state**: Mouse has no information about maze layout. Entropy is maximal: $H = \log_2(25) \approx 4.64$ bits (any of 25 squares could be the goal).
- **After first successful run**: Entropy is zero. The goal location is known with certainty: $H = 0$ bits.
- **Information gained**: $\Delta I = 4.64$ bits.

The relay memory physically stores this information. Shannon estimated the memory capacity as ~100 bits (total relay states), of which ~5 bits encoded the goal location and ~20 bits encoded the optimal path.

## Connection to Reinforcement Learning

Theseus anticipated key concepts in modern RL:

| Theseus (1950) | Modern RL (2020s) |
|----------------|-------------------|
| Maze squares | States $s \in S$ |
| Move directions (N/S/E/W) | Actions $a \in A$ |
| Reaching goal | Reward $R(s, a)$ |
| Relay memory | Q-table $Q(s, a)$ or neural network |
| Exploration (random moves) | $\epsilon$-greedy or UCB |
| Exploitation (stored path) | Greedy policy $\pi^*(s) = \arg\max_a Q(s,a)$ |

Shannon didn't use the term "reinforcement learning" (coined by Minsky in 1954), but the structure is identical.

## Entropy Reduction as Learning

Shannon's key insight: **Learning is entropy reduction**.

Before learning:
$$H_{before} = -\sum_{i=1}^{25} p_i \log_2 p_i = \log_2 25 \approx 4.64 \text{ bits}$$
(assuming uniform prior: $p_i = 1/25$ for all squares)

After learning:
$$H_{after} = -[1 \cdot \log_2(1) + 24 \cdot 0 \log_2(0)] = 0 \text{ bits}$$
(goal square has $p = 1$, all others $p = 0$)

The memory must **physically store** this information. Landauer's principle (1961) would later prove that erasing this information has a thermodynamic cost:
$$E_{erase} = k_B T \ln(2) \approx 3 \times 10^{-21} \text{ J per bit at } T = 300K$$

## Connection to BlackOops

The BlackOops framework can be viewed as modeling **black holes as "learning" systems**:

### Analogy: Maze = State Space, Mouse = Information

| Theseus | Black Hole |
|---------|-----------|
| 25 maze squares | $N = 10^{77}$ encoder positions (Bekenstein entropy) |
| Goal square | Singularity (recursive loop) |
| Relay memory (100 bits) | Horizon area (stores holographic info) |
| Exploration (random walk) | Infalling information trying to align |
| Success probability $1/25 = 0.04$ | Alignment probability $1/N \sim 10^{-77}$ per tick |
| Learning time: $\sim 25$ steps | Evaporation time: $\sim N^{1.5} \times t_p$ |

### Information Doesn't Reach the Goal

In Theseus, the mouse **always eventually finds the goal** (given enough random exploration). But in the black hole case:

- Random walk on $\mathbb{Z}_N$ (cyclic group): expected hitting time $\sim N^2$ steps
- Evaporation time: $\sim N^{1.5}$ steps
- The black hole **evaporates before the information aligns with the singularity**

This is why the holographic principle holds: information stays encoded on the horizon (the "memory relays") and never reaches the center (the "goal"). The black hole is a maze the mouse can never solve.

## Entropy and the Search Process

Shannon analyzed the maze-solving process as **entropy minimization**:

- Each random move that doesn't reach the goal provides ~1 bit of information ("the goal is not in square X")
- After eliminating 24 squares, the goal is determined
- Optimal search: $\log_2(25) \approx 4.64$ questions in the information-theoretic limit
- Random walk: $\sim 25$ steps on average (since it's a small grid, not the $N^2$ scaling of infinite lattices)

For the black hole encoder with $N = 10^{77}$ positions:
- Information-theoretic limit: $\log_2(N) \approx 77 \log_2(10) \approx 256$ bits of information needed to specify the singularity's "location" in encoder space
- Random walk: $\sim N^2 \sim 10^{154}$ Planck-time steps to align
- Evaporation: $\sim N^{1.5} \sim 10^{115}$ Planck-time steps

The gap ($N^{2.0}$ vs $N^{1.5}$) is why information never makes it to the center.

## Physical Details

- **Size**: ~3 feet × 3 feet maze board
- **Relays**: ~100 telephone relays (electromagnetic switches)
- **Speed**: ~1 move per second (limited by relay switching time)
- **Power**: ~100W (relays consume significant power when energized)
- **Memory persistence**: Indefinite (relays maintain state when powered)

Shannon demonstrated Theseus at the 1952 Cybernetics Conference, where it was seen as a landmark achievement in machine intelligence.

## Historical Context

- **1943**: McCulloch & Pitts model neurons as logic gates
- **1949**: Hebb proposes synaptic learning rule ("cells that fire together wire together")
- **1950**: Shannon builds Theseus, demonstrating learning in a physical machine
- **1951**: Minsky builds SNARC, first neural network hardware (40 synapses)
- **1954**: Minsky coins term "reinforcement learning"
- **1989**: Watkins develops Q-learning algorithm (used in modern deep RL)

## Numerical Example: Optimal Path Encoding

Suppose the maze has a 5-step optimal path from start to goal:
```
Start → East → East → North → North → Goal
```

This requires $\lceil \log_2(4^5) \rceil = \lceil 10 \rceil = 10$ bits to encode (4 directions, 5 steps).

Shannon's relay memory used ~20 bits for path storage, suggesting it stored not just the optimal path but also some dead-end information to avoid re-exploring them.

## See Also

- [[Shannon Entropy]]
- [[Boolean Algebra & Physical Circuits]]
- [[Reinforcement Learning]]
- [[Random Walks on Cyclic Groups]]
- [[Landauer's Principle]]
- [[Monte Carlo Simulation]]

## References

1. Shannon, C. E. (1952). "Presentation of a Maze-Solving Machine". *Proceedings of the 8th Cybernetics Conference*, 173–180.
2. Mindell, D. A. (2002). *Between Human and Machine: Feedback, Control, and Computing Before Cybernetics*. Johns Hopkins University Press.
3. Sutton, R. S., & Barto, A. G. (2018). *Reinforcement Learning: An Introduction* (2nd ed.). MIT Press.
4. Bell Labs. "Theseus Mouse Demonstration Video". AT&T Archives. https://techchannel.att.com/play-video.cfm/2012/1/27/AT&T-Archives-Theseus
