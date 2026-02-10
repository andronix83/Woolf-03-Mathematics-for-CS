import math
from fractions import Fraction


def solve_battery_problem():
    # Parameters
    total_batteries = 12
    working_batteries = 8
    defective_batteries = 4
    selected = 3

    print("--- Task 2: Battery Quality Control Analysis ---\n")

    # --- Part 1: All 3 working (Multiplication Rule) ---
    # P(G1) * P(G2|G1) * P(G3|G1,G2)
    p1 = Fraction(working_batteries, total_batteries)
    p2 = Fraction(working_batteries - 1, total_batteries - 1)
    p3 = Fraction(working_batteries - 2, total_batteries - 2)

    prob_all_good_mult = p1 * p2 * p3
    print(f"1. P(3 Good) via Multiplication Rule: {prob_all_good_mult} ({float(prob_all_good_mult):.4f})")

    # --- Part 2: All 3 working (Combinatorial Method) ---
    # C(8, 3) / C(12, 3)
    total_combinations = math.comb(total_batteries, selected)
    favorable_combinations_all_good = math.comb(working_batteries, 3)

    prob_all_good_comb = Fraction(favorable_combinations_all_good, total_combinations)
    print(f"2. P(3 Good) via Combinatorics:       {prob_all_good_comb} ({float(prob_all_good_comb):.4f})")

    if prob_all_good_mult == prob_all_good_comb:
        print("   -> Match Confirmed")
    else:
        print("   -> Mismatch!")

    print("\n" + "-" * 40 + "\n")

    # --- Part 3: Exactly 2 working (Multiplication Rule) ---
    # Scenarios: GGD, GDG, DGG
    # Each scenario has the same numerator factors (8*7*4) and denominator (12*11*10)
    # P(GGD)
    p_ggd = Fraction(working_batteries, total_batteries) * \
            Fraction(working_batteries - 1, total_batteries - 1) * \
            Fraction(defective_batteries, total_batteries - 2)

    # Since order matters in calculation but results are symmetrical:
    prob_2_good_mult = 3 * p_ggd
    print(f"3a. P(2 Good) via Multiplication Rule: {prob_2_good_mult} ({float(prob_2_good_mult):.4f})")

    # --- Part 3: Exactly 2 working (Combinatorial Method) ---
    # (C(8, 2) * C(4, 1)) / C(12, 3)
    ways_2_good = math.comb(working_batteries, 2)
    ways_1_bad = math.comb(defective_batteries, 1)
    favorable_combinations_2_good = ways_2_good * ways_1_bad

    prob_2_good_comb = Fraction(favorable_combinations_2_good, total_combinations)
    print(f"3b. P(2 Good) via Combinatorics:       {prob_2_good_comb} ({float(prob_2_good_comb):.4f})")

    if prob_2_good_mult == prob_2_good_comb:
        print("   -> Match Confirmed")
    else:
        print("   -> Mismatch!")


if __name__ == "__main__":
    solve_battery_problem()