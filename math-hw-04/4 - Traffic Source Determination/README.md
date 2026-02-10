# Task 4: Traffic Source Determination Analysis

## 1. Analytical Solution

### Part 1: Total Probability of Purchase
To determine the overall likelihood that a random visitor makes a purchase, we apply the Law of Total Probability. This aggregates the purchase probabilities from all traffic sources weighted by their traffic volume.

**Formula:**
$$P(A) = P(H_1)P(A|H_1) + P(H_2)P(A|H_2) + P(H_3)P(A|H_3)$$

**Calculation:**
- **Search Ads Contribution:** $0.50 \times 0.04 = 0.020$
- **Social Media Contribution:** $0.30 \times 0.02 = 0.006$
- **Email Contribution:** $0.20 \times 0.08 = 0.016$

$$P(A) = 0.020 + 0.006 + 0.016 = 0.042$$

**Result:** The general purchase probability is **4.2%**.

### Part 2: Posterior Probability (Bayes' Theorem)
We need to determine the probability that a purchaser came specifically from the Email Marketing campaign ($H_3$).

**Formula:**
$$P(H_3 | A) = \frac{P(A | H_3) \cdot P(H_3)}{P(A)}$$

**Calculation:**
- Numerator (Likelihood $\times$ Prior): $0.08 \times 0.20 = 0.016$
- Denominator (Total Probability): $0.042$

$$P(H_3 | A) = \frac{0.016}{0.042} \approx 0.38095$$

**Result:** There is a **38.1%** probability that a converting user came from the email campaign.

## 2. Conclusions

1.  **Efficiency Paradox:** While Search Ads bring the most volume (50%), Email Marketing is significantly more efficient at converting users (8% vs 4%).
2.  **Impact of Conversion Rate:** Despite Email Marketing having the lowest traffic share (20%), its high conversion rate drives its "share of wallet" (posterior probability) up to 38.1%. It is nearly as valuable in absolute sales numbers as Search Ads, which contribute $0.020 / 0.042 \approx 47.6\%$ of sales.
3.  **Algorithmic Approach:** The problem is solved programmatically using a generalized function `bayes_source`, which normalizes the element-wise product of priors and likelihoods. This confirms the manual calculations are correct.