import numpy as np


def calculate_cosine_similarity(v1, v2):
    """
    Calculates the cosine similarity between two vectors.
    Formula: (v1 . v2) / (||v1|| * ||v2||)
    """
    dot_product = np.dot(v1, v2)
    norm_v1 = np.linalg.norm(v1)
    norm_v2 = np.linalg.norm(v2)

    # Avoid division by zero if a zero vector is passed
    if norm_v1 == 0 or norm_v2 == 0:
        return 0.0

    return dot_product / (norm_v1 * norm_v2)


def main():
    # 1. Create user profile vector and movie vectors
    user_vector = np.array([8, 2, 5])

    movies = {
        "Film A": np.array([9, 1, 2]),
        "Film B": np.array([1, 9, 8]),
        "Film C": np.array([7, 2, 6])
    }

    print(f"User Vector: {user_vector}")
    print("-" * 30)

    best_movie_name = None
    highest_score = -1.0

    # 3. Calculate similarity for each movie
    for name, movie_vector in movies.items():
        score = calculate_cosine_similarity(user_vector, movie_vector)

        # 4. Output similarity coefficients
        print(f"{name} Vector: {movie_vector}")
        print(f"Similarity Score: {score:.4f}")
        print("-" * 30)

        # Track the best match
        if score > highest_score:
            highest_score = score
            best_movie_name = name

    # 5. Output the result
    print(f"Recommendation: The most suitable movie is '{best_movie_name}' "
          f"with a score of {highest_score:.4f}")


if __name__ == "__main__":
    main()