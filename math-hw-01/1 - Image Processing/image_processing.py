import numpy as np

# 1. Define the matrices

# Matrix M (Image)
M = np.array([
    [100, 150, 200],
    [50, 100, 150],
    [0, 50, 100]
])

# Matrix E (Effect)
E = np.array([
    [20, 30, 40],
    [10, 20, 30],
    [5, 10, 15]
])

print("Original Matrix M:\n", M)
print("\nEffect Matrix E:\n", E)
print("-" * 30)

# 2. Change Contrast
# Task: Decrease brightness by multiplying by scalar 0.5
lambda_val = 0.5
contrast_result = M * lambda_val

print("1. Change Contrast (M * 0.5):\n", contrast_result)

# 3. Brightness Correction
# Task: Add scalar 25 to every element
c_val = 25
brightness_result = M + c_val

print("\n2. Brightness Correction (M + 25):\n", brightness_result)

# 4. Blending
# Task: Linear combination 0.8 * M + 0.2 * E
blend_result = (0.8 * M) + (0.2 * E)

print("\n3. Blending (0.8*M + 0.2*E):\n", blend_result)