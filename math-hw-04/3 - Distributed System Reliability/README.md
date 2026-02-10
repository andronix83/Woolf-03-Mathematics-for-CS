# Task 3: Distributed System Reliability Analysis

## Problem Statement
We are designing a distributed system consisting of 4 independent nodes ($A, B, C, D$). The probability of failure for each node within one hour is given as:
- $P(A_{fail}) = 0.02$
- $P(B_{fail}) = 0.05$
- $P(C_{fail}) = 0.03$
- $P(D_{fail}) = 0.04$

## Definitions
Let $W_x$ denote the event that node $x$ works.
Let $F_x$ denote the event that node $x$ fails.

Since $W_x$ and $F_x$ are complementary events:
$P(W_x) = 1 - P(F_x)$

Calculated working probabilities:
- $P(W_A) = 0.98$
- $P(W_B) = 0.95$
- $P(W_C) = 0.97$
- $P(W_D) = 0.96$

---

## Solutions

### 1. Probability that all 4 nodes work
Since the nodes operate independently, the probability of the intersection of these events is the product of their individual probabilities.

$$P(\text{All Work}) = P(W_A) \times P(W_B) \times P(W_C) \times P(W_D)$$

$$P(\text{All Work}) = 0.98 \times 0.95 \times 0.97 \times 0.96$$

**Result:** $0.8669088$ (approx **0.8669**)

---

### 2. Probability that at least one node fails
This is the complement to the event "All nodes work".

$$P(\text{At least one fail}) = 1 - P(\text{All Work})$$

$$P(\text{At least one fail}) = 1 - 0.8669088$$

**Result:** $0.1330912$ (approx **0.1331**)

---

### 3. Probability that exactly two nodes fail
To solve this, we must sum the probabilities of all mutually exclusive scenarios where exactly two specific nodes fail while the other two work. There are $\binom{4}{2} = 6$ such combinations.

**Combinations:**

1.  **A & B fail:** $P(F_A)P(F_B)P(W_C)P(W_D) = 0.02 \times 0.05 \times 0.97 \times 0.96 = 0.0009312$
2.  **A & C fail:** $P(F_A)P(F_C)P(W_B)P(W_D) = 0.02 \times 0.03 \times 0.95 \times 0.96 = 0.0005472$
3.  **A & D fail:** $P(F_A)P(F_D)P(W_B)P(W_C) = 0.02 \times 0.04 \times 0.95 \times 0.97 = 0.0007372$
4.  **B & C fail:** $P(F_B)P(F_C)P(W_A)P(W_D) = 0.05 \times 0.03 \times 0.98 \times 0.96 = 0.0014112$
5.  **B & D fail:** $P(F_B)P(F_D)P(W_A)P(W_C) = 0.05 \times 0.04 \times 0.98 \times 0.97 = 0.0019012$
6.  **C & D fail:** $P(F_C)P(F_D)P(W_A)P(W_B) = 0.03 \times 0.04 \times 0.98 \times 0.95 = 0.0011172$

**Summation:**
$$P(\text{Exactly 2 fail}) = \sum P(\text{Combinations})$$
$$P(\text{Exactly 2 fail}) = 0.0009312 + 0.0005472 + 0.0007372 + 0.0014112 + 0.0019012 + 0.0011172$$

**Result:** $0.0066452$ (approx **0.0066**)