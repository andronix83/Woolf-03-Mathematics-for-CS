def solve_probability_task():
    """
    Calculates probabilities for Log Error Analytics task based on Set Theory.
    """

    # 1. Define the counts given in the problem statement
    total_events_omega = 500

    # "85 — errors only database" -> Set Difference (A \ B)
    count_only_db = 85

    # "60 — errors only network" -> Set Difference (B \ A)
    count_only_net = 60

    # "35 — errors having both" -> Intersection (A ∩ B)
    count_both = 35

    # 2. Derive the total counts for the main sets A and B
    # |A| = |A \ B| + |A ∩ B|
    count_A_total = count_only_db + count_both

    # |B| = |B \ A| + |A ∩ B| (Not strictly needed for the questions, but good for completeness)
    count_B_total = count_only_net + count_both

    # 3. Calculate Probabilities

    # Question 1: Probability of event 'DB' (P(A))
    # Grading Criteria: Correctly define event space and calculate P(A)
    p_A = count_A_total / total_events_omega

    # Question 2: Probability of 'DB' OR 'NET' (P(A U B))
    # Grading Criteria: Union of events
    # Calculation: Sum of disjoint sets (Only DB + Only NET + Both)
    count_union = count_only_db + count_only_net + count_both
    p_A_union_B = count_union / total_events_omega

    # Question 3: Probability of 'DB' but NOT 'NET' (P(A \ B))
    # Grading Criteria: Difference of events
    p_A_diff_B = count_only_db / total_events_omega

    # 4. Output Results
    print(f"--- Task 1: Log Error Analytics Results ---")
    print(f"Total Events (Omega): {total_events_omega}")
    print(f"Count A (Total DB): {count_A_total}")
    print(f"Count Union (DB or NET): {count_union}")
    print("-" * 30)
    print(f"1. Probability of DB error P(A):       {p_A:.2f} ({p_A * 100:.0f}%)")
    print(f"2. Probability of DB or NET P(A U B):  {p_A_union_B:.2f} ({p_A_union_B * 100:.0f}%)")
    print(f"3. Probability of DB not NET P(A \\ B): {p_A_diff_B:.2f} ({p_A_diff_B * 100:.0f}%)")


if __name__ == "__main__":
    solve_probability_task()