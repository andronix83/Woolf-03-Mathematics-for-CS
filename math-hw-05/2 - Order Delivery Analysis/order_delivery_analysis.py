import scipy.stats as stats

# --- Configuration ---
n = 50          # Total number of orders
p = 0.88        # Probability of on-time delivery
q = 1 - p       # Probability of late delivery

# Initialize the Binomial distribution object
dist = stats.binom(n, p)

# --- Task 1: Expected Value and Standard Deviation ---
expected_value = dist.mean()
std_dev = dist.std()

print(f"1. Expected Value (E[X]): {expected_value}")
print(f"   Standard Deviation (sigma): {std_dev:.4f}")

# --- Task 2: Probability of exactly 50 on-time orders ---
prob_all_50 = dist.pmf(50)
print(f"2. P(X = 50): {prob_all_50:.6f}")

# --- Task 3: Probability of exactly 45 on-time orders ---
prob_exactly_45 = dist.pmf(45)
print(f"3. P(X = 45): {prob_exactly_45:.6f}")

# --- Task 4: Probability of 42 to 46 on-time orders ---
# Note: We subtract CDF(41) to EXCLUDE 41 and lower, keeping 42.
prob_between_42_46 = dist.cdf(46) - dist.cdf(41)
print(f"4. P(42 <= X <= 46): {prob_between_42_46:.6f}")

# --- Task 5: Probability that more than 5 orders are late ---
# "More than 5 late" means "Less than 45 on time"
prob_late_gt_5 = dist.cdf(44)
print(f"5. P(Late > 5) or P(X < 45): {prob_late_gt_5:.6f}")