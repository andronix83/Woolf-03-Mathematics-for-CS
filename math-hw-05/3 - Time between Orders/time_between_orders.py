from scipy.stats import expon

# --- Configuration ---
# lambda = 6 orders/hour = 0.1 orders/minute
lambda_param = 0.1
# Scale parameter (beta) is 1 / lambda
scale_param = 1 / lambda_param

print(f"--- Task Parameters ---")
print(f"Rate (lambda): {lambda_param} orders/min")
print(f"Scale (1/lambda): {scale_param} min")
print("-" * 30)

# --- Task 1: Expected Value (E[T]) and Standard Deviation (sigma) ---
mean_val = expon.mean(scale=scale_param)
std_dev = expon.std(scale=scale_param)

print(f"1. Mean (E[T]): {mean_val:.2f} minutes")
print(f"   Standard Deviation (sigma): {std_dev:.2f} minutes")

# --- Task 2: Probability next order arrives in < 5 mins ---
prob_less_5 = expon.cdf(5, scale=scale_param)

print(f"2. P(T < 5 min): {prob_less_5:.4f} (approx {prob_less_5*100:.1f}%)")

# --- Task 3: Probability waiting > 15 mins ---
# Using Survival Function (1 - CDF) as requested by the logic P(T > x)
prob_more_15 = 1 - expon.cdf(15, scale=scale_param)

print(f"3. P(T > 15 min): {prob_more_15:.4f} (approx {prob_more_15*100:.1f}%)")

# --- Task 4: Probability order arrives between 5 and 15 mins ---
# Calculated as F(15) - F(5)
prob_between_5_15 = expon.cdf(15, scale=scale_param) - expon.cdf(5, scale=scale_param)

print(f"4. P(5 < T < 15 min): {prob_between_5_15:.4f} (approx {prob_between_5_15*100:.1f}%)")

# --- Task 5: Median waiting time ---
# Using PPF (Percent Point Function / Inverse CDF) for probability 0.5
median_val = expon.ppf(0.5, scale=scale_param)

print(f"5. Median waiting time: {median_val:.4f} minutes")