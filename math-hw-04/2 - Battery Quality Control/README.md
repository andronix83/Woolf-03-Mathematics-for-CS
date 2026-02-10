# Task 2: Battery Quality Control

## Problem Overview
We analyzed a scenario involving a set of 12 batteries (8 working, 4 defective) where 3 batteries are selected randomly without replacement.

## 1. Probability of All 3 Batteries Being Working
We calculated this probability using two methods:

* **Multiplication Rule (Conditional Probability):**
    We multiplied the sequential probabilities of drawing a working battery at each step:
    $$\frac{8}{12} \times \frac{7}{11} \times \frac{6}{10} = \frac{14}{55}$$

* **Combinatorial Method ($C_n^k$):**
    We calculated the ratio of ways to choose 3 working batteries to the total ways to choose any 3 batteries:
    $$\frac{C(8, 3)}{C(12, 3)} = \frac{56}{220} = \frac{14}{55}$$

**Conclusion:** Both methods yielded the identical result of **14/55** (approx. **25.45%**).

## 2. Probability of Exactly 2 Batteries Being Working
We calculated the probability that exactly 2 batteries are working (and 1 is defective):

* **Multiplication Rule:**
    We identified three distinct sequences (Good-Good-Defective, Good-Defective-Good, Defective-Good-Good). The probability of one sequence is $\frac{8}{12} \times \frac{7}{11} \times \frac{4}{10}$. Since there are 3 such arrangements:
    $$3 \times \frac{224}{1320} = \frac{28}{55}$$

* **Combinatorial Method:**
    We calculated the number of ways to choose 2 working batteries from 8 ($C(8,2)$) and 1 defective from 4 ($C(4,1)$):
    $$\frac{C(8, 2) \times C(4, 1)}{C(12, 3)} = \frac{28 \times 4}{220} = \frac{112}{220} = \frac{28}{55}$$

**Conclusion:** Both methods yielded the identical result of **28/55** (approx. **50.91%**).