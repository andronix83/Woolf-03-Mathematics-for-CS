# Task 1: Log Error Analytics

## Problem Definition
We are analyzing a system log with 500 events ($\Omega$). The events are categorized by two tags:
* $A$: Event has tag `DB` (Database error)
* $B$: Event has tag `NET` (Network error)

**Input Data:**
* $|\Omega| = 500$
* Errors with **only** `DB` tag ($|A \setminus B|$) = 85
* Errors with **only** `NET` tag ($|B \setminus A|$) = 60
* Errors with **both** tags ($|A \cap B|$) = 35

## Step-by-Step Solution

### 1. Probability of a DB Error: $P(A)$
To find the probability of a randomly selected event being a "Database error" ($A$), we must count all events that possess the `DB` tag. This includes events that are exclusively database errors and events that are also network errors.

* **Calculation of $|A|$:**
    $$|A| = |A \setminus B| + |A \cap B|$$
    $$|A| = 85 + 35 = 120$$

* **Probability:**
    $$P(A) = \frac{|A|}{|\Omega|} = \frac{120}{500} = 0.24$$

**Answer:** 0.24 (24%)

---

### 2. Probability of DB or NET: $P(A \cup B)$
We need to find the probability that an event contains the tag `DB` **OR** the tag `NET`. This is the union of the two sets.

* **Calculation of Union size $|A \cup B|$:**
    We sum the disjoint components:
    $$|A \cup B| = |A \setminus B| + |B \setminus A| + |A \cap B|$$
    $$|A \cup B| = 85 + 60 + 35 = 180$$
    
    *(Alternative verification using inclusion-exclusion principle):*
    $$|B| = 60 + 35 = 95$$
    $$|A \cup B| = |A| + |B| - |A \cap B| = 120 + 95 - 35 = 180$$

* **Probability:**
    $$P(A \cup B) = \frac{|A \cup B|}{|\Omega|} = \frac{180}{500} = 0.36$$

**Answer:** 0.36 (36%)

---

### 3. Probability of DB but not NET: $P(A \setminus B)$
We need to find the probability that an event has the `DB` tag but explicitly does **not** have the `NET` tag.

* **Calculation:**
    This value is given directly in the problem statement as "85 errors — only database".
    $$|A \setminus B| = 85$$

* **Probability:**
    $$P(A \setminus B) = \frac{|A \setminus B|}{|\Omega|} = \frac{85}{500} = 0.17$$

**Answer:** 0.17 (17%)

## Summary Table

| Metric | Notation | Count | Probability |
| :--- | :--- | :--- | :--- |
| **Only DB** | $A \setminus B$ | 85 | 0.17 |
| **Only NET** | $B \setminus A$ | 60 | 0.12 |
| **Both** | $A \cap B$ | 35 | 0.07 |
| **Total DB** | $A$ | 120 | **0.24** |
| **Union** | $A \cup B$ | 180 | **0.36** |