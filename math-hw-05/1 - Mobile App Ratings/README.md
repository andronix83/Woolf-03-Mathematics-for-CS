# Task 1: Mobile App Ratings Analysis

## 1. Probability Mass Function (PMF) & Cumulative Distribution Function (CDF)

Based on the 2000 reviews collected, we constructed the probability distribution for the random variable $X$ (user rating).

| Rating ($x$) | Count | PMF $P(X=x)$ | CDF $F(x)$ |
| :---: | :---: | :---: | :---: |
| 1 | 120 | 0.06 | 0.06 |
| 2 | 180 | 0.09 | 0.15 |
| 3 | 320 | 0.16 | 0.31 |
| 4 | 580 | 0.29 | 0.60 |
| 5 | 800 | 0.40 | 1.00 |

*Table 1: Distribution of ratings.*

## 2. Numerical Characteristics

We calculated the key statistical metrics to understand the central tendency and dispersion of the ratings.

* **Expected Value ($E[X]$):** $3.88$
    * *Calculation:* $1(0.06) + 2(0.09) + 3(0.16) + 4(0.29) + 5(0.40) = 3.88$
    * *Interpretation:* The average rating given by a random user is approximately 3.88 stars.

* **Variance ($Var(X)$):** $1.4456$
    * *Calculation:* $E[X^2] - (E[X])^2 = 16.5 - (3.88)^2 = 1.4456$
    
* **Standard Deviation ($\sigma$):** $1.2023$
    * *Calculation:* $\sqrt{1.4456} \approx 1.20$
    * *Interpretation:* On average, individual ratings deviate from the mean by about 1.2 stars, indicating a moderate spread in user opinion, though skewed towards higher values.

## 3. Probability Analysis

### Probability of a Negative Rating
We define a negative rating as 1 or 2 stars ($X \le 2$).
$$P(X \le 2) = F(2) = 0.15$$
**Conclusion:** There is a **15%** probability that a random user will leave a negative review.

### Probability of a High Rating
We define a high rating as 4 or more stars ($X \ge 4$).
$$P(X \ge 4) = P(X=4) + P(X=5) = 0.29 + 0.40 = 0.69$$
**Conclusion:** There is a **69%** probability that a random user will leave a high rating.

## 4. Median Rating
The median is the smallest value $x$ for which the cumulative probability $F(x) \ge 0.5$.

* $F(3) = 0.31$ (less than 0.5)
* $F(4) = 0.60$ (greater than 0.5)

**Conclusion:** The median rating is **4 stars**. This confirms that at least 50% of users rated the app 4 stars or higher.