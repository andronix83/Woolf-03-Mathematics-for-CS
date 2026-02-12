import math
from scipy import stats

# --- Given Data ---
mu_0 = 72          # Population mean (historical)
x_bar = 76.8       # Sample mean
s = 14.2           # Sample standard deviation
n = 35             # Sample size
alpha = 0.05       # Significance level

# --- Step 2: Calculate Standard Error (SE) ---
se = s / math.sqrt(n)

# --- Step 3: Calculate t-statistic ---
t_stat = (x_bar - mu_0) / se

# --- Step 4: Calculate p-value ---
# Degrees of freedom
df = n - 1
# For a two-tailed test using cdf:
# Area to the left of negative |t| multiplied by 2
p_value = 2 * stats.t.cdf(-abs(t_stat), df)

# --- Step 5: Construct 95% Confidence Interval ---
# Find critical t-value (t_crit) using ppf for 97.5% (two-tailed 5% alpha)
t_crit = stats.t.ppf(1 - alpha/2, df)

# Calculate Margin of Error
margin_of_error = t_crit * se

# Calculate Interval
ci_lower = x_bar - margin_of_error
ci_upper = x_bar + margin_of_error

# --- Step 6: Conclusion ---
reject_null = p_value < alpha

# --- Output Results ---
print(f"1. Hypotheses: H0: mu = {mu_0}, H1: mu != {mu_0}")
print(f"2. Standard Error (SE): {se:.4f}")
print(f"3. t-statistic: {t_stat:.4f}")
print(f"4. p-value: {p_value:.4f}")
print(f"5. Critical t-value (t_crit): {t_crit:.4f}")
print(f"   95% Confidence Interval: [{ci_lower:.4f}, {ci_upper:.4f}]")
print("-" * 30)
print("6. Conclusion:")

if reject_null:
    print("   Reject Null Hypothesis.")
    print("   There is sufficient evidence to claim the new method influenced results.")
else:
    print("   Fail to reject Null Hypothesis.")
    print("   There is NO sufficient evidence to claim the new method influenced results.")