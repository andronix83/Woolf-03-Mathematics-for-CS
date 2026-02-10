import numpy as np
from scipy.optimize import approx_fprime

def f_func(variables):
    """
    Defines the function f(x, y) = 0.5x^2 + 0.3y^2 + 0.2xy + 10x + 5y
    """
    x, y = variables
    return 0.5 * x**2 + 0.3 * y**2 + 0.2 * x * y + 10 * x + 5 * y

def analytical_gradient(x, y):
    """
    Calculates gradients using derived formulas.
    df/dx = x + 0.2y + 10
    df/dy = 0.6y + 0.2x + 5
    """
    df_dx = x + 0.2 * y + 10
    df_dy = 0.6 * y + 0.2 * x + 5
    return np.array([df_dx, df_dy])

# --- Main Execution ---

# 1. Setup
point = np.array([10.0, 20.0]) # Point (x, y)
epsilon = np.sqrt(np.finfo(float).eps) # Standard epsilon for approximation

# 2. Numerical Gradient Calculation (Task 2)
# approx_fprime(xk, f, epsilon) returns the gradient
grad_numerical = approx_fprime(point, f_func, epsilon)

# 3. Analytical Gradient Calculation & Comparison (Task 3)
grad_analytical = analytical_gradient(point[0], point[1])

print(f"--- Gradient Analysis at {point} ---")
print(f"Analytical Gradient: {grad_analytical}")
print(f"Numerical Gradient:  {grad_numerical}")
print(f"Difference:          {np.abs(grad_analytical - grad_numerical)}")

# 4. Function Change Estimation (Task 4)
delta_x = 0.5
delta_y = -0.3
deltas = np.array([delta_x, delta_y])

# Linear Approximation: df ≈ grad * delta
approx_change = np.dot(grad_analytical, deltas)

# Exact Change calculation
f_initial = f_func(point)
point_new = point + deltas
f_new = f_func(point_new)
exact_change = f_new - f_initial

print(f"\n--- Function Change Analysis ---")
print(f"Deltas -> dx: {delta_x}, dy: {delta_y}")
print(f"Approximate Change (Linear): {approx_change:.5f}")
print(f"Exact Change f({point_new}) - f({point}): {exact_change:.5f}")
print(f"Approximation Error: {np.abs(exact_change - approx_change):.5f}")