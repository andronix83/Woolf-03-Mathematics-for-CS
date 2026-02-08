"""
Task 4: Analysis of the company's social network.
Course: Mathematics in Computer Science.

Objective:
1. Construct three graph representations: Adjacency Matrix, Adjacency List, Edge List.
2. Calculate vertex degrees and identify the most/least communicative employees.
3. Verify the Handshaking Lemma (Sum of degrees = 2 * Number of edges).
"""


def main():
    # 1. Define the nodes (employees) to establish an index mapping for the matrix
    employees = ['Anna', 'Bogdan', 'Viktor', 'Hanna', 'Dmytro', 'Yevhen']
    n = len(employees)

    # Map names to indices for matrix operations
    name_to_index = {name: i for i, name in enumerate(employees)}

    # ---------------------------------------------------------
    # Representation 2: Adjacency List (Dictionary)
    # ---------------------------------------------------------
    # We define this first as it is the most natural way to input the raw data
    adj_list = {
        'Anna': ['Bogdan', 'Viktor', 'Hanna'],
        'Bogdan': ['Anna', 'Viktor', 'Dmytro'],
        'Viktor': ['Anna', 'Bogdan', 'Hanna', 'Dmytro'],
        'Hanna': ['Anna', 'Viktor', 'Yevhen'],
        'Dmytro': ['Bogdan', 'Viktor', 'Yevhen'],
        'Yevhen': ['Hanna', 'Dmytro']
    }

    print("--- 1. Adjacency List (Dictionary) ---")
    for employee, contacts in adj_list.items():
        print(f"{employee}: {contacts}")
    print()

    # ---------------------------------------------------------
    # Representation 1: Adjacency Matrix (Nested Lists)
    # ---------------------------------------------------------
    # Initialize an n x n matrix with zeros
    adj_matrix = [[0] * n for _ in range(n)]

    # Populate the matrix based on the adjacency list
    for user, neighbors in adj_list.items():
        u_idx = name_to_index[user]
        for neighbor in neighbors:
            v_idx = name_to_index[neighbor]
            adj_matrix[u_idx][v_idx] = 1

    print("--- 2. Adjacency Matrix (Nested Lists) ---")
    # Print header
    print("      ", end="")
    for name in employees:
        print(f"{name[:3]:>4}", end="")  # Print first 3 letters for compact view
    print()

    # Print rows
    for i, row in enumerate(adj_matrix):
        print(f"{employees[i]:<6}", end="")
        for val in row:
            print(f"{val:>4}", end="")
        print()
    print()

    # ---------------------------------------------------------
    # Representation 3: Edge List (List of Tuples)
    # ---------------------------------------------------------
    # We must ensure edges are unique (undirected graph).
    # E.g., ('Anna', 'Bogdan') is the same as ('Bogdan', 'Anna').
    edge_list = []
    seen_edges = set()

    for u in adj_list:
        for v in adj_list[u]:
            # Sort the pair to ensure unique storage regardless of direction
            edge = tuple(sorted((u, v)))
            if edge not in seen_edges:
                edge_list.append(edge)
                seen_edges.add(edge)

    print("--- 3. Edge List (List of Tuples) ---")
    for edge in edge_list:
        print(edge)
    print(f"\nTotal unique edges: {len(edge_list)}")
    print()

    # ---------------------------------------------------------
    # Step 2: Calculate Degrees & Identify Leaders
    # ---------------------------------------------------------
    print("--- Step 2: Degrees of Vertices ---")
    degrees = {node: len(neighbors) for node, neighbors in adj_list.items()}

    for node, deg in degrees.items():
        print(f"{node}: {deg}")

    # Find max and min degrees
    max_degree = max(degrees.values())
    min_degree = min(degrees.values())

    most_communicative = [k for k, v in degrees.items() if v == max_degree]
    least_communicative = [k for k, v in degrees.items() if v == min_degree]

    print(f"\nMost communicative (Degree {max_degree}): {', '.join(most_communicative)}")
    print(f"Least communicative (Degree {min_degree}): {', '.join(least_communicative)}")
    print()

    # ---------------------------------------------------------
    # Step 3: Verify Sum of Degrees Theorem (Handshaking Lemma)
    # ---------------------------------------------------------
    print("--- Step 3: Verify Handshaking Lemma ---")
    sum_of_degrees = sum(degrees.values())
    num_edges = len(edge_list)
    doubled_edges = 2 * num_edges

    print(f"Sum of all degrees: {sum_of_degrees}")
    print(f"Number of edges: {num_edges}")
    print(f"2 * Number of edges: {doubled_edges}")

    if sum_of_degrees == doubled_edges:
        print("RESULT: Theorem CONFIRMED. The sum of degrees equals twice the number of edges.")
    else:
        print("RESULT: Theorem FAILED.")


if __name__ == "__main__":
    main()