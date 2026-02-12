import numpy as np
import pandas as pd

# --- Data Definition ---
# Ratings (X): 1 to 5 stars
ratings = np.array([1, 2, 3, 4, 5])
# Count of reviews for each rating
counts = np.array([120, 180, 320, 580, 800])

# 0. Total number of reviews
total_reviews = np.sum(counts)

# --- Task 1: Calculate PMF (Probability Mass Function) ---
pmf = counts / total_reviews

# --- Task 2: Calculate CDF (Cumulative Distribution Function) ---
cdf = np.cumsum(pmf)

# --- Task 3: Display Table (Rating, PMF, CDF) ---
df_results = pd.DataFrame({
    'Rating (x)': ratings,
    'PMF P(X=x)': pmf,
    'CDF F(x)': cdf
})

print("--- Probability Distribution Table ---")
print(df_results.to_string(index=False))
print("-" * 30)

# --- Task 4: Numerical Characteristics ---
mean_val = np.sum(ratings * pmf)

# Variance Var(X) = E[X^2] - (E[X])^2
expected_x_squared = np.sum((ratings ** 2) * pmf)
variance_val = expected_x_squared - (mean_val ** 2)

# Standard Deviation sigma = sqrt(Var(X))
std_dev_val = np.sqrt(variance_val)

print(f"Expected Value E[X]: {mean_val:.4f}")
print(f"Variance Var(X): {variance_val:.4f}")
print(f"Standard Deviation (sigma): {std_dev_val:.4f}")
print("-" * 30)

# --- Task 5: Probability of Negative Rating (1 or 2 stars) ---
# P(X <= 2) is simply the CDF value at index 1 (corresponding to rating 2)
prob_negative = cdf[1]
print(f"Probability of negative rating (1 or 2 stars) P(X <= 2): {prob_negative:.4f}")

# --- Task 6: Probability of High Rating (4 or more stars) ---
prob_high = pmf[3] + pmf[4]
print(f"Probability of high rating (>= 4 stars) P(X >= 4): {prob_high:.4f}")

# --- Task 7: Median Rating ---
# The smallest x for which F(x) >= 0.5
median_index = np.where(cdf >= 0.5)[0][0]
median_rating = ratings[median_index]

print(f"Median Rating: {median_rating}")