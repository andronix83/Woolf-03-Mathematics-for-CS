import numpy as np


def solve_trend_forecast():
    # --- Input Data ---
    # Time (t) in hours
    t = np.array([1, 2, 3, 4, 5])
    # CPU Load (y)
    y = np.array([22, 28, 37, 45, 53])

    print("--- Main Task: Trend Forecast using lstsq ---")

    # Step 1: Form matrix A.
    # The equation is y = k*t + b.
    # To solve for vector x = [k, b], matrix A must have a column of t and a column of 1s.
    A = np.column_stack((t, np.ones(len(t))))

    print(f"Matrix A:\n{A}")

    # Step 2: Find coefficients k and b using np.linalg.lstsq
    # rcond=None is used to silence a warning about future numpy versions
    solution, residuals, rank, s = np.linalg.lstsq(A, y, rcond=None)
    k, b = solution

    print(f"\nCalculated coefficients:\nSlope (k): {k:.4f}\nIntercept (b): {b:.4f}")

    # Step 3: Calculate the forecast for the 6th hour
    t_predict = 6
    y_predict = k * t_predict + b

    # Step 4: Output the equation and the forecast
    print(f"\nTrend Equation: y = {k:.2f} * t + {b:.2f}")
    print(f"Forecast for hour {t_predict}: {y_predict:.2f}")

    print("\n" + "=" * 40 + "\n")

    print("--- Optional Task (Bonus): Normal Equation ---")

    # The Normal Equation is: (A^T * A) * x = A^T * y

    # Step 1: Calculate A^T * A
    At_A = A.T @ A
    print(f"A^T * A:\n{At_A}")

    # Step 2: Calculate A^T * y
    At_y = A.T @ y
    print(f"A^T * y:\n{At_y}")

    # Step 3: Solve the system using np.linalg.solve
    # This manually finds the optimal coefficients vector x = [k, b]
    manual_solution = np.linalg.solve(At_A, At_y)
    k_manual, b_manual = manual_solution

    print(f"\nManual coefficients via Normal Equation:\nSlope (k): {k_manual:.4f}\nIntercept (b): {b_manual:.4f}")

    # Step 4: Compare results
    # We use np.allclose to check if floating point numbers are effectively equal
    match = np.allclose(solution, manual_solution)
    print(f"\nDo the results match 'lstsq'? {match}")


if __name__ == "__main__":
    solve_trend_forecast()