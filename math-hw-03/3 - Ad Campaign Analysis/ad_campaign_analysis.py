import numpy as np
from scipy import integrate

def registration_rate(t):
    """
    Function representing the intensity of registrations per day.
    f(t) = 500 * e^(-0.3t)
    """
    return 500 * np.exp(-0.3 * t)

# --- Task 1 & 2: First 7 Days Analysis ---

# Analytical calculation (calculated manually)
analytical_7_days = (5000 / 3) * (1 - np.exp(-2.1))

# Numerical calculation using scipy.integrate.quad
numerical_7_days, error_7 = integrate.quad(registration_rate, 0, 7)

print(f"--- First 7 Days Analysis ---")
print(f"Analytical Result: {analytical_7_days:.4f}")
print(f"Numerical Result:  {numerical_7_days:.4f}")

# Verification check
if np.isclose(analytical_7_days, numerical_7_days):
    print(">> Verification Successful: Results match.")
else:
    print(">> Verification Failed.")

# --- Task 3: Theoretical Maximum ---

# Numerical calculation of improper integral (0 to infinity)
# np.inf represents infinity
theoretical_max, error_inf = integrate.quad(registration_rate, 0, np.inf)

print(f"\n--- Theoretical Maximum Analysis ---")
print(f"Theoretical Max Registrations: {theoretical_max:.4f}")

# --- Task 4: Efficiency Calculation ---

efficiency_percentage = (numerical_7_days / theoretical_max) * 100

print(f"\n--- Efficiency Analysis ---")
print(f"Percentage of max captured in week 1: {efficiency_percentage:.2f}%")