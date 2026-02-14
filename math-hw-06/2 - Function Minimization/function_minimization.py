import numpy as np
from scipy.optimize import minimize


def objective_function(vars):
    """
    Defines the function f(x, y) = x^2 + xy + y^2 - 6x - 9y + 20
    """
    x, y = vars
    return x ** 2 + x * y + y ** 2 - 6 * x - 9 * y + 20


def run_optimization():
    print("--- Task 3: Numerical Optimization ---")

    initial_guess = [0, 0]

    # Perform minimization using BFGS method
    result = minimize(objective_function, initial_guess, method='BFGS')

    if result.success:
        print(f"Optimization successful!")
        print(f"Found Minimum at (x, y): ({result.x[0]:.4f}, {result.x[1]:.4f})")
        print(f"Function Value at Minimum: {result.fun:.4f}")
    else:
        print("Optimization failed:", result.message)

    print("\n--- Task 4: Stability Check ---")

    # List of starting points
    starting_points = [
        [0, 0],
        [10, 10],
        [-5, 15]
    ]

    for i, start_point in enumerate(starting_points):
        res = minimize(objective_function, start_point, method='BFGS')
        print(
            f"Run {i + 1} | Start: {start_point} -> Converged to: ({res.x[0]:.4f}, {res.x[1]:.4f}) | Value: {res.fun:.4f}")


if __name__ == "__main__":
    run_optimization()