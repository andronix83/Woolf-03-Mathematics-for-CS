import scipy.optimize as optimize


def solve_optimization_problem():
    """
    Finds the optimal price to maximize profit for wireless headphones.
    """

    # Define the profit function P(x)
    # P(x) = (price - cost) * demand
    # Since minimize_scalar finds the minimum, we minimize the negative profit (-P(x))
    def negative_profit(x):
        return -((x - 800) * (2000 - 0.8 * x))

    # Search for the optimal price in the interval [800, 2500]
    result = optimize.minimize_scalar(
        negative_profit,
        bounds=(800, 2500),
        method='bounded'
    )

    if result.success:
        optimal_price_numeric = result.x
        max_profit_numeric = -result.fun  # Invert back to get positive profit

        print(f"--- Numerical Optimization Results ---")
        print(f"Optimization Success: {result.success}")
        print(f"Optimal Price (Numeric): {optimal_price_numeric:.2f} UAH")
        print(f"Maximum Profit (Numeric): {max_profit_numeric:.2f} UAH")
        return optimal_price_numeric, max_profit_numeric
    else:
        print("Optimization failed.")
        return None, None


if __name__ == "__main__":
    solve_optimization_problem()