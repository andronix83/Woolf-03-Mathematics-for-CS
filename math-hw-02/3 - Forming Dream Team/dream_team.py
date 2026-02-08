import math


def calculate_team_combinations():
    """
    Calculates the number of unique ways to form a project team
    based on the provided candidate pools and requirements.
    """

    # --- Input Data ---
    # Number of available candidates in each pool
    total_backend_devs = 8
    total_frontend_devs = 6
    total_designers = 4

    # Required number of specialists for the team
    required_backend = 2
    required_frontend = 2
    required_designers = 1

    # --- Calculations ---
    # 1. Calculate combinations for Back-end developers: C(8, 2)
    backend_combinations = math.comb(total_backend_devs, required_backend)

    # 2. Calculate combinations for Front-end developers: C(6, 2)
    frontend_combinations = math.comb(total_frontend_devs, required_frontend)

    # 3. Calculate combinations for Designers: C(4, 1)
    designer_combinations = math.comb(total_designers, required_designers)

    # 4. Calculate total unique teams using the Multiplication Rule
    total_team_combinations = (
            backend_combinations * frontend_combinations * designer_combinations
    )

    # --- Output Results ---
    print("--- Dream Team Formation Analysis ---")
    print(f"Back-end combinations (choose {required_backend} from {total_backend_devs}): {backend_combinations}")
    print(f"Front-end combinations (choose {required_frontend} from {total_frontend_devs}): {frontend_combinations}")
    print(f"Designer combinations (choose {required_designers} from {total_designers}):   {designer_combinations}")
    print("-" * 35)
    print(f"Total unique team compositions: {total_team_combinations}")


if __name__ == "__main__":
    calculate_team_combinations()