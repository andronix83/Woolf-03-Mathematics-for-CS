import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt


# --- 1. Implement the Model ---
def learning_rate(t, K, M, r):
    """
    Calculates the rate of change of knowledge dK/dt.
    """
    return r * (M - K)


# --- Define an event to find when Knowledge reaches 90% ---
# FIX: Added *args to accept M and r which are passed by solve_ivp automatically
def reach_90_percent(t, K, *args):
    # We want K = 90, so we return K - 90.
    # K is passed as an array, so we access K[0]
    return K[0] - 90


# Stop the integration when the event occurs
# reach_90_percent.terminal = True
# Direction 1 means we only care when K is increasing through 90
reach_90_percent.direction = 1

# --- 2. Numerical Solution & 3. Investigation ---
# Constants
M = 100
r = 0.15
t_span = (0, 30)  # Simulate for 30 days
initial_conditions = [5, 10, 20]  # Different starting knowledge levels (K0)

results = {}

plt.figure(figsize=(10, 6))

for K0 in initial_conditions:
    # Solve the ODE
    # args=(M, r) are passed to BOTH learning_rate AND reach_90_percent
    sol = solve_ivp(
        fun=learning_rate,
        t_span=t_span,
        y0=[K0],
        args=(M, r),
        dense_output=True,
        events=reach_90_percent
    )

    # Store the time it took to reach 90%
    if sol.t_events and len(sol.t_events[0]) > 0:
        time_to_90 = sol.t_events[0][0]
        results[K0] = time_to_90
    else:
        time_to_90 = None
        results[K0] = None

    # Plotting the curve
    t_plot = np.linspace(0, 30, 100)
    K_plot = sol.sol(t_plot)[0]
    plt.plot(t_plot, K_plot, label=f'Start K(0)={K0}%')

    # Mark the 90% point on the graph
    if time_to_90:
        plt.scatter([time_to_90], [90], color='red', zorder=5)
        # Offset text slightly for readability
        plt.text(time_to_90, 85, f'{time_to_90:.1f} days', fontsize=9)

# --- Visualization Settings ---
plt.axhline(y=90, color='gray', linestyle='--', alpha=0.7, label='Target (90%)')
plt.axhline(y=100, color='black', linestyle=':', alpha=0.5, label='Max (100%)')
plt.title('Learning Progress Over Time for Different Initial Levels')
plt.xlabel('Time (days)')
plt.ylabel('Knowledge Level (K)')
plt.legend()
plt.grid(True, which='both', linestyle='--', linewidth=0.5)
plt.show()

# --- Output Results to Console ---
print("--- Comparison Results ---")
for K0, time_val in results.items():
    if time_val:
        print(f"Student with initial K={K0}% reached 90% knowledge in {time_val:.2f} days.")
    else:
        print(f"Student with initial K={K0}% did not reach 90% within 30 days.")