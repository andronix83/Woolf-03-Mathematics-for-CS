import numpy as np
from scipy.optimize import linprog

# --- 1. Define the Coefficients ---

# Objective function coefficients (Profit to maximize).
# Since linprog minimizes, we pass negative values
c = [-500, -800]

# Left-hand side of the inequality constraints (A_ub * x <= b_ub)
A_ub = [
    [2, 4],  # Coefficients for Wood
    [3, 2]  # Coefficients for Labor
]

# Right-hand side of the inequality constraints (Resource limits)
b_ub = [120, 90]

# Bounds for variables (x >= 0, y >= 0)
x_bounds = (0, None)
y_bounds = (0, None)

# --- 2. Solve the Linear Programming Problem ---

result = linprog(
    c,
    A_ub=A_ub,
    b_ub=b_ub,
    bounds=[x_bounds, y_bounds],
    method='highs'
)

# --- 3. Output and Analyze Results ---

if result.success:
    # Extract optimal values
    optimal_chairs = result.x[0]
    optimal_tables = result.x[1]
    max_profit = -result.fun  # Negate back to get positive profit

    print("Optimization Successful!")
    print("-" * 30)
    print(f"Optimal number of Chairs (x): {optimal_chairs:.2f}")
    print(f"Optimal number of Tables (y): {optimal_tables:.2f}")
    print(f"Maximum Profit: {max_profit:.2f} UAH")
    print("-" * 30)

    # --- Resource Usage Analysis ---

    # Calculate used resources based on optimal x and y
    wood_used = 2 * optimal_chairs + 4 * optimal_tables
    labor_used = 3 * optimal_chairs + 2 * optimal_tables

    # Define total capacities for comparison
    wood_total = 120
    labor_total = 90

    print("Resource Usage Analysis:")
    print(f"Wood:  Used {wood_used:.2f} / {wood_total} m^2 (Remaining: {wood_total - wood_used:.2f} m^2)")
    print(f"Labor: Used {labor_used:.2f} / {labor_total} hours (Remaining: {labor_total - labor_used:.2f} hours)")

else:
    print("Optimization failed:", result.message)