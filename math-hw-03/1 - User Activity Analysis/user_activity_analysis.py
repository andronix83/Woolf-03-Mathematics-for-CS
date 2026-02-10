import numpy as np
from scipy.optimize import approx_fprime

def f_func(t):
    """
    Calculates the number of active sessions.
    f(t) = 1000 * t * e^(-0.2t)
    """
    # Note: inputs to approx_fprime are arrays, so we ensure t is handled correctly
    return 1000 * t * np.exp(-0.2 * t)

def analytical_derivative(t):
    """
    Calculates the derivative analytically derived in Step 1.
    f'(t) = 200 * e^(-0.2t) * (5 - t)
    """
    return 200 * np.exp(-0.2 * t) * (5 - t)

def main():
    # Time points to analyze: 10:00 (t=2), 14:00 (t=6), 18:00 (t=10)
    time_points = [2, 6, 10]
    epsilon = 1e-6  # Step size for numerical differentiation

    print(f"{'Time (t)':<10} | {'Numerical f\'(t)':<18} | {'Analytical f\'(t)':<18} | {'Difference':<12}")
    print("-" * 65)

    for t in time_points:
        # 1. Numerical Calculation using scipy.optimize.approx_fprime
        # approx_fprime takes (xk, f, epsilon)
        f_prime_num = approx_fprime([t], f_func, epsilon)[0]

        # 2. Analytical Calculation
        f_prime_ana = analytical_derivative(t)

        # 3. Comparison
        diff = abs(f_prime_num - f_prime_ana)

        print(f"{t:<10} | {f_prime_num:<18.4f} | {f_prime_ana:<18.4f} | {diff:<12.2e}")

    # Business Interpretation helpers
    print("\n--- Business Interpretation ---")
    print(f"Rate of change at 10:00 (t=2): {analytical_derivative(2):.2f} sessions/hour")
    print(f"Rate of change at 18:00 (t=10): {analytical_derivative(10):.2f} sessions/hour")


if __name__ == "__main__":
    main()