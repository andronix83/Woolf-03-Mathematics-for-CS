# Task 1: Optimal Product Pricing Analysis

## 1. Analytical Solution
**Objective:** Find the price $x$ that maximizes the profit function $P(x)$.

**Derivation:**
Given the profit function:
$$P(x) = (x - 800)(2000 - 0.8x)$$

Expanding and simplifying the expression:
$$P(x) = -0.8x^2 + 2640x - 1600000$$

Finding the first derivative $P'(x)$:
$$P'(x) = -1.6x + 2640$$

Setting $P'(x) = 0$ to find the critical point:
$$1.6x = 2640 \implies x^* = 1650$$

## 2. Extremum Verification
To verify the nature of the critical point, we compute the second derivative $P''(x)$:
$$P''(x) = -1.6$$

**Conclusion:**
Since $P''(x) < 0$, the function is strictly concave down. This confirms that the price **$x = 1650$ UAH** corresponds to the **maximum profit**.

## 3. Numerical Verification
Using the `minimize_scalar` function from the `scipy.optimize` library within the bounds $[800, 2500]$, we obtained the following results:
- **Optimal Price (Numerical):** ~1650.00 UAH
- **Maximum Profit (Numerical):** ~578,000.00 UAH

## 4. Final Conclusion
The analytical derivation matches the numerical optimization results.

- **Optimal Price:** 1650 UAH
- **Maximum Monthly Profit:** 578,000 UAH

The company should set the price of the wireless headphones to **1650 UAH** to achieve the maximum possible monthly profit.