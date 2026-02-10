import math
from itertools import combinations


def solve_reliability_task():
    # Define failure probabilities for each node
    nodes = {
        'A': 0.02,
        'B': 0.05,
        'C': 0.03,
        'D': 0.04
    }

    # Calculate working probabilities (1 - failure_probability)
    # Using a dictionary comprehension
    working_probs = {k: 1 - v for k, v in nodes.items()}

    print("--- Probabilities ---")
    print(f"Failure: {nodes}")
    print(f"Working: {working_probs}\n")

    # --- Task 1: Probability that ALL nodes work ---
    # Formula: P(A_work) * P(B_work) * P(C_work) * P(D_work)
    p_all_work = 1.0
    for prob in working_probs.values():
        p_all_work *= prob

    print(f"1. Probability all nodes work: {p_all_work:.7f}")

    # --- Task 2: Probability that AT LEAST ONE node fails ---
    # Formula: 1 - P(All nodes work)
    p_at_least_one_fail = 1.0 - p_all_work

    print(f"2. Probability at least one fails: {p_at_least_one_fail:.7f}")

    # --- Task 3: Probability that EXACTLY TWO nodes fail ---
    # We need to find every unique pair of nodes that could fail.
    # We use itertools.combinations to get unique pairs from keys ['A', 'B', 'C', 'D']
    node_names = list(nodes.keys())
    p_exactly_two_fail = 0.0

    # Get all combinations of 2 nodes (the ones that fail)
    failing_pairs = list(combinations(node_names, 2))

    print("\n--- Calculation for Task 3 (breakdown) ---")
    for pair in failing_pairs:
        # The pair represents the nodes that FAIL.
        # The 'others' represent the nodes that must WORK.
        failing_node_1, failing_node_2 = pair
        other_nodes = [n for n in node_names if n not in pair]

        # Calculate probability for this specific scenario
        # P(Fail1) * P(Fail2) * P(Work3) * P(Work4)
        prob_scenario = (
                nodes[failing_node_1] * nodes[failing_node_2] * working_probs[other_nodes[0]] * working_probs[
            other_nodes[1]]
        )

        print(
            f"Scenario {failing_node_1}&{failing_node_2} fail, {other_nodes[0]}&{other_nodes[1]} work: {prob_scenario:.7f}")
        p_exactly_two_fail += prob_scenario

    print(f"\n3. Probability exactly two nodes fail: {p_exactly_two_fail:.7f}")


if __name__ == "__main__":
    solve_reliability_task()