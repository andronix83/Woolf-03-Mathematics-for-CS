# Task 1: User Activity Dynamics Analysis Report

## 1. Analytical Derivative
We derived the rate of change of active sessions $f(t)$ using the product rule.
**Formula:**
$$f'(t) = 1000 e^{-0.2t} (1 - 0.2t) = 200 e^{-0.2t} (5 - t)$$

## 2. Peak Load Moment
We determined the maximum load by setting the derivative to zero ($f'(t) = 0$).
* **Calculated time ($t^*$):** 5 hours from start.
* **Clock time:** The workday starts at 8:00, so the peak occurs at **13:00**.

## 3. Numerical vs Analytical Comparison
We calculated the derivative at three specific moments ($t=2, 6, 10$) using both `scipy.optimize.approx_fprime` and our analytical formula.

| Time (t) | Time (Clock) | Numerical f'(t) | Analytical f'(t) | Accuracy |
| :--- | :--- | :--- | :--- | :--- |
| **t = 2** | 10:00 | 402.19 | 402.19 | High Match |
| **t = 6** | 14:00 | -60.24 | -60.24 | High Match |
| **t = 10** | 18:00 | -135.34 | -135.34 | High Match |

The numerical values match the analytical values with high precision, confirming the correctness of the derived formula.

## 4. Business Interpretation & Recommendations

### What does a positive derivative at 10:00 mean?
At 10:00 ($t=2$), the derivative is **positive (+402.19)**.
**Meaning:** The number of active users is **growing rapidly**.
**Implication for IT:** This is the "ramp-up" phase. The auto-scaling system must be aggressive in provisioning new instances to handle the incoming surge of traffic to prevent latency.

### What does a negative derivative at 18:00 mean?
At 18:00 ($t=10$), the derivative is **negative (-135.34)**.
**Meaning:** The number of active users is **decreasing**.
**Implication for IT:** The platform is cooling down. Resources can be gradually released (scaled down) to save costs, as demand is dropping.

### When to have maximum servers active?
The peak load occurs strictly at **13:00** ($t=5$, where $f'(t)=0$).
**Recommendation:** The maximum number of servers should be provisioned and fully ready shortly before **13:00** to handle the peak volume of concurrent sessions.