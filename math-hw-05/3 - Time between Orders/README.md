# Task 3: Analysis of Time Between Orders in an Online Store

## Problem Overview
We are analyzing the flow of orders in an online store using the **Exponential Distribution**. This distribution is chosen because it models the time intervals between independent random events that occur at a constant average rate.

**Parameters:**
- **Rate ($\lambda$):** 0.1 orders per minute (1 order every 10 minutes).
- **Scale ($\beta = 1/\lambda$):** 10 minutes.

## Calculation Results

### 1. Numerical Characteristics
We calculated the mathematical expectation (mean) and standard deviation. For an exponential distribution, these values are identical.
- **Mean ($E[T]$):** 10.0 minutes.
- **Standard Deviation ($\sigma$):** 10.0 minutes.
*Analysis:* On average, a new order arrives every 10 minutes. The high standard deviation indicates significant variability in arrival times; sometimes orders come effectively "back-to-back," and other times there are long lulls.

### 2. Probability of Short Wait ($T < 5$)
We calculated the probability that the next order arrives in less than 5 minutes.
- **$P(T < 5)$:** 0.3935 (39.35%)
*Analysis:* There is a roughly 40% chance that an order will arrive shortly (within half the average time). This reflects the property of the exponential distribution where probability density is highest near zero.

### 3. Probability of Long Wait ($T > 15$)
We calculated the probability of waiting more than 15 minutes.
- **$P(T > 15)$:** 0.2231 (22.31%)
*Analysis:* There is a ~22% chance of a "quiet period" lasting significantly longer (1.5x) than the average wait time.

### 4. Probability of Interval ($5 < T < 15$)
We calculated the probability that the order arrives between 5 and 15 minutes.
- **$P(5 < T < 15)$:** 0.3834 (38.34%)
*Analysis:* This interval represents the "middle" range. It is interesting to note that this probability (~38%) is nearly identical to the probability of the order arriving in the first 5 minutes (~39%).

### 5. Median Waiting Time
We found the time $t$ for which the probability of arrival is 50%.
- **Median:** 6.93 minutes.
*Analysis:* The median (6.93 min) is significantly lower than the mean (10 min). This confirms that the distribution is **right-skewed**. While the *average* wait is 10 minutes (pulled up by occasional very long waits), in 50% of cases, the next order actually arrives in under 7 minutes.

## Conclusion
The analysis confirms the characteristic behavior of the Exponential Distribution in an e-commerce context:
1.  **Skewness:** Most orders arrive relatively quickly (median < mean).
2.  **Variability:** There is a substantial probability of both very short intervals (39% < 5 min) and long lulls (22% > 15 min).
3.  **Predictability:** While individual arrival times are random, the aggregate statistics allow for precise capacity planning (e.g., server load or staffing).