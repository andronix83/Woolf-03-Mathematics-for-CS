import numpy as np


def solve_production_problem():
    # 1. Form the coefficient matrix A and the dependent variable vector b
    # Rows represent components: Motors, Controllers, Batteries
    # Columns represent drone types: Scout, Kamikaze, Heavy Cargo
    A = np.array([
        [4, 4, 6],  # Motors equation
        [1, 1, 2],  # Controllers equation
        [1, 2, 4]  # Batteries equation
    ])

    b = np.array([460, 130, 240])

    print("Matrix A (Coefficients):")
    print(A)
    print("\nVector b (Total Components):")
    print(b)

    # 2. Check if the system has a unique solution by calculating the determinant
    det_A = np.linalg.det(A)
    print(f"\nDeterminant of A: {det_A:.2f}")

    if np.isclose(det_A, 0):
        print("The determinant is zero. The system does not have a unique solution.")
        return
    else:
        print("The determinant is non-zero. A unique solution exists.")

    # 3. Solve the system Ax = b for x
    x = np.linalg.solve(A, b)

    # Rounding to handle potential floating point inaccuracies,
    # though exact integers are expected for this problem.
    scout_count = int(np.round(x[0]))
    kamikaze_count = int(np.round(x[1]))
    cargo_count = int(np.round(x[2]))

    print("\nSolution vector x (Quantities of drones):")
    print(f"Scout (x1): {scout_count}")
    print(f"Kamikaze (x2): {kamikaze_count}")
    print(f"Heavy Cargo (x3): {cargo_count}")

    # 4. Verify the correctness of calculations: A * x should equal b
    check_b = np.dot(A, x)

    print("\nVerification (A * x):")
    print(check_b)

    # Check if the calculated b matches the original b (allowing for small float errors)
    is_correct = np.allclose(check_b, b)
    print(f"\nVerification successful: {is_correct}")


if __name__ == "__main__":
    solve_production_problem()