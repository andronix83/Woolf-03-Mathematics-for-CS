# Task 2: Order Delivery Reliability Analysis

## 1. Statistical Characteristics
We modeled the number of on-time deliveries $X$ as a Binomial distribution $X \sim B(50, 0.88)$.

* **Expected Value ($E[X] = 44$):**
    On average, we can expect 44 out of 50 orders to be delivered on time daily. This serves as our baseline for performance.
* **Standard Deviation ($\sigma \approx 2.30$):**
    The typical fluctuation from the average is about 2.3 orders. This means usually, the number of on-time orders will fall between 41 and 47 (roughly $E[X] \pm 1\sigma$).

## 2. Probability Analysis

### Perfect Performance
* **$P(X=50) \approx 0.17\%$**
    The probability of a "perfect day" (100% on-time delivery) is extremely low. It is statistically unreasonable to expect perfection given the current success rate of 0.88.

### Targeted Performance
* **$P(X=45) \approx 16.9\%$**
    There is a moderate chance of getting exactly 45 orders on time (slightly above the average).
* **$P(42 \le X \le 46) \approx 74.8\%$**
    There is a high probability (~75%) that the number of on-time orders falls within this range. This confirms that the process is relatively stable around the mean.

### Risk Assessment (Late Deliveries)
* **$P(\text{Late} > 5) = P(X < 45) \approx 59.8\%$**
    There is a nearly 60% chance that more than 5 orders will be late on any given day.
    * *Interpretation:* Since $X < 45$ essentially means performing below the exact specific target of 45, and our mean is 44, it is statistically expected that we will often have more than 5 late packages.

## Conclusion
The delivery system is stable but consistently produces roughly 6 late packages per day (Mean $50 - 44 = 6$).
To reliably achieve fewer than 5 late packages daily, the underlying probability $p=0.88$ must be improved, as the current variance and mean make "more than 5 late" the dominant outcome (~60% probability).