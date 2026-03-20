# Reinforcement Learning

## Definition

**Reinforcement Learning** (RL) is a branch of machine learning where an agent learns to make decisions by interacting with an environment, receiving rewards or penalties, and optimizing its behavior to maximize cumulative reward over time.

## Core Components

### 1. Agent
The decision-maker (e.g., robot, game player, algorithm).

### 2. Environment
The system the agent interacts with (e.g., maze, game board, physical world).

### 3. State $s \in S$
Current situation of the environment (e.g., position in maze, board configuration).

### 4. Action $a \in A$
Choice the agent can make (e.g., move north, play move, apply force).

### 5. Reward $r(s, a)$
Immediate feedback signal (e.g., +1 for reaching goal, -1 for hitting wall, 0 otherwise).

### 6. Policy $\pi(a|s)$
Strategy: probability of taking action $a$ in state $s$.

### 7. Value Function $V^\pi(s)$
Expected cumulative reward starting from state $s$ under policy $\pi$:

$$V^\pi(s) = \mathbb{E}_\pi\left[\sum_{t=0}^{\infty} \gamma^t r_t \mid s_0 = s\right]$$

where $\gamma \in [0, 1]$ is the **discount factor** (future rewards weighted less).

### 8. Q-Function $Q^\pi(s, a)$
Expected cumulative reward starting from state $s$, taking action $a$, then following policy $\pi$:

$$Q^\pi(s, a) = \mathbb{E}_\pi\left[\sum_{t=0}^{\infty} \gamma^t r_t \mid s_0 = s, a_0 = a\right]$$

## The RL Problem

**Goal**: Find the **optimal policy** $\pi^*$ that maximizes expected cumulative reward:

$$\pi^* = \arg\max_\pi V^\pi(s_0)$$

for the initial state $s_0$ (or all states).

**Bellman Optimality Equation**:

$$V^*(s) = \max_a \left[r(s, a) + \gamma \sum_{s'} P(s'|s, a) V^*(s')\right]$$

where $P(s'|s, a)$ is the transition probability (environment dynamics).

## Key Algorithms

### 1. Q-Learning (Off-Policy TD)

Update rule:

$$Q(s, a) \leftarrow Q(s, a) + \alpha \left[r + \gamma \max_{a'} Q(s', a') - Q(s, a)\right]$$

where:
- $\alpha$ is learning rate
- $\gamma$ is discount factor
- $s'$ is next state
- $r$ is reward received

**Converges** to $Q^*$ (optimal Q-function) under mild conditions.

### 2. SARSA (On-Policy TD)

$$Q(s, a) \leftarrow Q(s, a) + \alpha \left[r + \gamma Q(s', a') - Q(s, a)\right]$$

where $a'$ is the **actual** action taken (not max), making it on-policy.

### 3. Policy Gradient

Directly optimize policy parameters $\theta$:

$$\nabla_\theta J(\theta) = \mathbb{E}_{\pi_\theta}\left[\sum_t \nabla_\theta \log \pi_\theta(a_t|s_t) \cdot R_t\right]$$

Used in deep RL (e.g., AlphaGo, ChatGPT RLHF).

### 4. Deep Q-Networks (DQN)

Approximate $Q(s, a)$ with a neural network:

$$Q(s, a; \theta) \approx Q^*(s, a)$$

Trained via:
- **Experience replay**: Store $(s, a, r, s')$ tuples, sample mini-batches
- **Target network**: Separate network for stable targets

Breakthrough: Atari game playing (2013, DeepMind).

## Exploration vs Exploitation

**Dilemma**: Should the agent:
- **Explore**: Try new actions to discover better strategies
- **Exploit**: Use known-best actions to maximize immediate reward

**Solutions**:

1. **$\epsilon$-greedy**:
   - With probability $\epsilon$: choose random action (explore)
   - With probability $1-\epsilon$: choose $\arg\max_a Q(s, a)$ (exploit)

2. **Upper Confidence Bound (UCB)**:
   $$a = \arg\max_a \left[Q(s, a) + c\sqrt{\frac{\log t}{N(s, a)}}\right]$$
   where $N(s, a)$ is visit count (favors under-explored actions).

3. **Boltzmann (softmax)**:
   $$P(a|s) \propto e^{Q(s, a) / T}$$
   where $T$ is temperature (high $T$ = more random, low $T$ = more greedy).

## Connection to Shannon's Theseus

**Shannon's 1950 Theseus mouse** (see [[Shannon's Theseus]]) is an early example of RL:

| Theseus | Modern RL |
|---------|-----------|
| Maze squares | States $s$ |
| Move directions (N/S/E/W) | Actions $a$ |
| Reaching goal | Reward $r = +1$ |
| Relay memory | Q-table $Q(s, a)$ |
| Exploration (random moves) | $\epsilon$-greedy |
| Exploitation (stored path) | Greedy policy |

Shannon didn't call it "RL" (term coined by Minsky in 1954), but the structure is identical.

### Entropy Reduction as Learning

Shannon described Theseus in terms of **entropy reduction**:

- **Before**: Entropy $H = \log_2 N$ (goal could be any of $N$ squares)
- **After**: Entropy $H = 0$ (goal location known)
- **Information gained**: $\Delta I = \log_2 N$ bits

This connects RL to information theory: **learning = entropy reduction** = acquiring information about the environment.

## Connection to BlackOops

The BlackOops encoder model can be viewed as a **RL problem**:

### Black Hole as Maze

| BlackOops | RL |
|-----------|-----|
| Infalling information | Agent |
| Encoder positions $\mathbb{Z}_N$ | State space $S$ |
| Step ±1 (Gray code) | Action space $A$ |
| Align with singularity | Goal state |
| Alignment probability $1/N$ | Reward signal (sparse) |
| Random walk | Exploration policy |

**Question**: Can infalling information "learn" to find the singularity faster than random?

**Answer from Sim 2 (Two-Body)**: No. Even with two walkers (simulating "coordination"), alignment time scales as $O(N^2)$ — no shortcut exists. The singularity is **not learnable** from the horizon's perspective.

### Optimization Interpretation

**Policy**: How to traverse encoder positions to maximize evaporation rate.

**Constraint**: Gray code (only ±1 steps allowed).

**Reward**: Negative of evaporation time (want to minimize).

**Optimal policy**: Release bits at Hawking rate $\propto N^{-0.5}$ (not faster, not slower).

This is **thermodynamic optimization** — the black hole "learns" to radiate at the rate that balances:
- **Gravitational collapse** (pulls info inward): $\propto N^{-1}$
- **Quantum fluctuations** (push info outward): $\propto 1$

The Nash equilibrium is $\sqrt{N^{-1} \times 1} = N^{-0.5}$ (geometric mean).

## Deep RL and Black Holes

**Speculative**: Could RL be used to:

1. **Optimize encoder traversal**: Find Gray code paths that minimize evaporation time (already optimal?)
2. **Predict Hawking spectrum**: Train NN to predict particle emission given horizon state
3. **Discover holographic duality**: Learn mapping between bulk (3D black hole) and boundary (2D CFT) via RL in AdS/CFT

This is unexplored territory — RL in quantum gravity is a frontier research area.

## Multi-Armed Bandits

A simplified RL problem:

- $K$ slot machines ("arms"), each with unknown payout distribution
- At each step, pull one arm, receive reward
- Goal: Maximize total reward (identify best arm quickly)

**Regret**: Difference between optimal strategy and actual performance.

**UCB algorithm** achieves $O(\sqrt{KT \log T})$ regret after $T$ pulls.

**Connection**: Encoder positions as "arms," alignment as "reward." But all arms are identical (uniform distribution) → no advantage to learning.

## Temporal Difference (TD) Learning

Core idea: Update value estimates based on **difference** between prediction and reality:

$$V(s) \leftarrow V(s) + \alpha [r + \gamma V(s') - V(s)]$$

**TD error**: $\delta = r + \gamma V(s') - V(s)$

**Interpretation**: "Surprise" signal — how much better/worse is the outcome than expected?

**Neuroscience connection**: Dopamine neurons encode TD error (reward prediction error). RL models match brain activity.

## Policy Iteration vs Value Iteration

### Value Iteration

1. Initialize $V(s) = 0$ for all $s$
2. Repeat until convergence:
   $$V(s) \leftarrow \max_a \left[r(s, a) + \gamma \sum_{s'} P(s'|s, a) V(s')\right]$$
3. Extract policy: $\pi(s) = \arg\max_a [r(s, a) + \gamma \sum_{s'} P(s'|s, a) V(s')]$

### Policy Iteration

1. Initialize policy $\pi$ (e.g., random)
2. Repeat:
   - **Policy evaluation**: Compute $V^\pi$ for current policy
   - **Policy improvement**: Update $\pi(s) = \arg\max_a Q^\pi(s, a)$
3. Stop when $\pi$ stops changing

Both converge to optimal policy $\pi^*$. Policy iteration often faster (fewer iterations).

## Applications

- **Robotics**: Locomotion, manipulation, navigation
- **Games**: Chess, Go, Atari, StarCraft (AlphaStar)
- **Finance**: Portfolio optimization, trading strategies
- **Healthcare**: Treatment planning, drug discovery
- **Natural language**: Chatbot fine-tuning (RLHF in GPT-4, Claude)
- **Energy**: Smart grid management, HVAC control

## Historical Milestones

- **1950**: Shannon's Theseus mouse (proto-RL)
- **1954**: Minsky coins "reinforcement learning"
- **1989**: Watkins develops Q-learning
- **1992**: TD-Gammon (backgammon RL) reaches expert level
- **2013**: DQN plays Atari at human level (DeepMind)
- **2016**: AlphaGo defeats world champion Lee Sedol
- **2017**: AlphaZero masters chess, shogi, Go via self-play
- **2019**: OpenAI Five beats Dota 2 professionals
- **2022**: ChatGPT uses RLHF (RL from Human Feedback)

## See Also

- [[Shannon's Theseus]]
- [[Shannon Entropy]]
- [[Random Walks on Cyclic Groups]]
- [[Monte Carlo Simulation]]
- [[Boolean Algebra & Physical Circuits]]

## References

1. Sutton, R. S., & Barto, A. G. (2018). *Reinforcement Learning: An Introduction* (2nd ed.). MIT Press. http://incompleteideas.net/book/the-book-2nd.html
2. Watkins, C. J. C. H. (1989). "Learning from Delayed Rewards". *PhD Thesis*, University of Cambridge.
3. Mnih, V., et al. (2015). "Human-Level Control Through Deep Reinforcement Learning". *Nature*, 518(7540), 529–533.
4. Silver, D., et al. (2017). "Mastering the Game of Go Without Human Knowledge". *Nature*, 550(7676), 354–359.
