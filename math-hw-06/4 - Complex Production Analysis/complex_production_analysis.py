import numpy as np
from scipy.optimize import approx_fprime, minimize_scalar, minimize
from scipy.integrate import quad


def main():
    print("=== COMPLEX PRODUCTION ANALYSIS ===\n")

    # ---------------------------------------------------------
    # PART 1: PRODUCTIVITY ANALYSIS
    # ---------------------------------------------------------
    print("--- Part 1: Productivity Dynamics ---")

    # Define the productivity function P(t)
    def P(t):
        return 100 + 40 * t - 4 * t ** 2

    # 1. Analyze productivity dynamics using approx_fprime
    # We check the derivative at t = 2, 5, 8
    check_points = [2, 5, 8]
    epsilon = 1e-6  # Small step for finite difference approximation

    print(f"{'Time (t)':<10} | {'P\'(t) (Rate)':<15} | {'Trend'}")
    print("-" * 40)

    for t_val in check_points:
        # approx_fprime expects an array for x, so we wrap t_val in a list
        # We assume f takes an array, so we wrap the call to P inside the lambda
        deriv = approx_fprime([t_val], lambda x: P(x[0]), epsilon)[0]

        if deriv > 0.1:
            trend = "Increasing"
        elif deriv < -0.1:
            trend = "Decreasing"
        else:
            trend = "Stationary (Peak)"

        print(f"{t_val:<10} | {deriv:<15.4f} | {trend}")

    # 2. Find the moment of peak productivity
    # minimize_scalar finds the minimum, so we minimize -P(t) to find the max P(t)
    res_max = minimize_scalar(lambda t: -P(t), bounds=(0, 10), method='bounded')
    t_peak = res_max.x
    p_peak = P(t_peak)

    print(f"\nPeak productivity occurs at t = {t_peak:.2f} hours")
    print(f"Maximum productivity value P(t*) = {p_peak:.2f} units/hour")

    # 3. Calculate total production volume (Definite Integral)
    total_production, error = quad(P, 0, 10)
    print(f"Total production volume (Integral 0->10): {total_production:.2f} units")

    # ---------------------------------------------------------
    # PART 2: COST OPTIMIZATION
    # ---------------------------------------------------------
    print("\n--- Part 2: Cost Optimization ---")

    # 1. Determine initial parameters from the system of linear equations
    # System:
    # 2x + y = 20
    # x + 3y = 25

    A = np.array([
        [2, 1],
        [1, 3]
    ])
    b = np.array([20, 25])

    initial_params = np.linalg.solve(A, b)
    x0, y0 = initial_params
    print(f"Initial parameters (from linear system): x0 = {x0:.2f}, y0 = {y0:.2f}")

    # 2. Minimize production cost
    # Cost function C(x, y) = x^2 + y^2 - 10x - 8y + 50
    # The optimization function requires a single array argument [x, y]
    def cost_function(vars):
        x, y = vars
        return x ** 2 + y ** 2 - 10 * x - 8 * y + 50

    # Using BFGS method starting from the point calculated in the previous step
    res_min_cost = minimize(cost_function, initial_params, method='BFGS')

    opt_x, opt_y = res_min_cost.x
    min_unit_cost = res_min_cost.fun

    print(f"Optimal parameters: x* = {opt_x:.2f}, y* = {opt_y:.2f}")
    print(f"Minimum unit cost: {min_unit_cost:.2f} UAH")

    # ---------------------------------------------------------
    # PART 3: FINAL
    # ---------------------------------------------------------
    print("\n--- Final: Total Cost Calculation ---")

    total_cost = total_production * min_unit_cost
    print(f"Total Production Volume: {total_production:.2f}")
    print(f"Minimum Cost per Unit:   {min_unit_cost:.2f}")
    print(f"FINAL TOTAL COST:        {total_cost:.2f} UAH")


if __name__ == "__main__":
    main()