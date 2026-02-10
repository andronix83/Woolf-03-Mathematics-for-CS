# Analysis of Ad Campaign Effectiveness (Task 3)

## 1. Overview
This report analyzes the registration dynamics for the new online course based on the provided intensity function $f(t) = 500 \cdot e^{-0.3t}$. The goal is to evaluate the first week's performance against the theoretical maximum reach.

## 2. Analytical Calculation (First 7 Days)
To find the total registrations in the first week, we calculated the definite integral of the intensity function from $t=0$ to $t=7$.

**Formula:**
$$\int_{0}^{7} 500 \cdot e^{-0.3t} dt$$

**Derivation:**
Using the Newton-Leibniz formula, the antiderivative is $F(t) = -\frac{500}{0.3}e^{-0.3t}$.
$$F(7) - F(0) = -\frac{5000}{3}(e^{-2.1} - 1) \approx 1462.57$$

**Result:**
Analytically, we expect approximately **1,463 registrations** in the first 7 days.

## 3. Numerical Verification
Using the `scipy.integrate.quad` library, we performed a numerical integration of the function.

* **Analytical Result:** 1462.5714
* **Numerical Result:** 1462.5714

The numerical method confirms the analytical derivation is correct.

## 4. Theoretical Maximum (Improper Integral)
To understand the total potential of the campaign if left to run indefinitely (assuming no other external factors change), we calculated the improper integral from $0$ to $\infty$.

$$\int_{0}^{\infty} 500 \cdot e^{-0.3t} dt = \lim_{t \to \infty} \left[ -\frac{5000}{3}e^{-0.3t} \right]_0^t = \frac{5000}{3}$$

**Result:**
The theoretical maximum number of registrations is approximately **1,667**.

## 5. Efficiency Conclusion
Comparing the first week's performance to the theoretical maximum:

$$\text{Efficiency} = \frac{1462.57}{1666.67} \times 100\% \approx 87.75\%$$

**Conclusion:**
The ad campaign is highly front-loaded. **87.75%** of all potential registrations are acquired within the first 7 days. This suggests that extending the active promotion phase significantly beyond one week may result in diminishing returns, as the registration intensity drops sharply after the first week.# Homework #3