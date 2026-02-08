# Task 3: Dream Team Formation Analysis

## Problem Statement
The goal is to assemble a specific 5-person MVP development team from a pre-vetted pool of candidates. The order of selection is irrelevant, making this a combinatorial problem.

**Team Structure Requirements:**
1.  **Back-end:** Choose 2 from 8 candidates.
2.  **Front-end:** Choose 2 from 6 candidates.
3.  **Design:** Choose 1 from 4 candidates.

## Methodology
We use the **Combination Formula** $C(n, k)$ for each independent group because the order of selection within a group does not matter.

$$C(n, k) = \frac{n!}{k!(n-k)!}$$

To find the total number of possible teams, we apply the **Rule of Product (Multiplication Rule)**, multiplying the number of possibilities for each independent group.

## Calculation Steps

### 1. Back-end Developers
We need to select 2 distinct developers from a set of 8.
$$C(8, 2) = \frac{8 \times 7}{2 \times 1} = 28 \text{ ways}$$

### 2. Front-end Developers
We need to select 2 distinct developers from a set of 6.
$$C(6, 2) = \frac{6 \times 5}{2 \times 1} = 15 \text{ ways}$$

### 3. UI/UX Designers
We need to select 1 designer from a set of 4.
$$C(4, 1) = 4 \text{ ways}$$

## Final Conclusion
By multiplying the independent possibilities, we determine the total number of unique team structures:

$$Total = 28 \text{ (Back-end)} \times 15 \text{ (Front-end)} \times 4 \text{ (Design)}$$
$$Total = 1680$$

**Result:** There are **1,680** unique ways to form the "Dream Team" for the startup.