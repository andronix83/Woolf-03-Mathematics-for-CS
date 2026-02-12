# Task 4: Student Scores Statistical Analysis

## 1. Hypotheses Formulation
- **Null Hypothesis ($H_0$):** $\mu = 72$
  The mean score of students this year is equal to last year's average (72). The methodology change had no effect.
- **Alternative Hypothesis ($H_1$):** $\mu \neq 72$
  The mean score is different from 72. The methodology change influenced the results.

## 2. Standard Error Calculation
The Standard Error (SE) estimates the variability of the sample mean.
$$SE = \frac{14.2}{\sqrt{35}} \approx 2.4002$$

## 3. t-statistic
The t-score indicates how many standard errors the sample mean is from the population mean.
$$t = \frac{76.8 - 72}{2.4002} \approx 1.9998$$

## 4. p-value
For a two-tailed test with $df=34$:
- **p-value $\approx 0.0535$**

## 5. 95% Confidence Interval
Using the t-distribution for $df=34$, the critical value $t_{crit} \approx 2.0322$.
- Margin of Error: $2.0322 \times 2.4002 \approx 4.8778$
- **Interval:** $[71.9222, 81.6778]$

## 6. Conclusion
- **Significance Level ($\alpha$):** 0.05
- **Decision:** Since the p-value ($0.0535$) is greater than $\alpha$ ($0.05$), we **fail to reject the Null Hypothesis**.
- **Interpretation:** Although the sample mean (76.8) is higher than 72, the difference is not statistically significant at the 5% level. We cannot assert with 95% confidence that the new methodology changed the results.
*(Note: The result is very close to the boundary, as the confidence interval [71.92, 81.68] barely includes the value 72).*