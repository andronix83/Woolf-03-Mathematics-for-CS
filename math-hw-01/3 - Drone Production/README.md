# Task 3: Production Analysis

## Problem Statement

We need to recover the number of drones produced for three specific models based on the total consumption of components. The problem is modeled as a system of linear equations in the form $A\mathbf{x} = \mathbf{b}$.

**Variables:**
* $x_1$: Number of "Scout" drones
* $x_2$: Number of "Kamikaze" drones
* $x_3$: Number of "Heavy Cargo" drones

## 1. Matrix Formulation

Based on the problem description, we construct the coefficient matrix $A$ (resources per drone) and vector $\mathbf{b}$ (total resources used).

Rows represent: Motors, Flight Controllers, and Batteries.
Columns represent: Scout, Kamikaze, and Heavy Cargo.

$$
A = \begin{pmatrix} 
4 & 4 & 6 \\ 
1 & 1 & 2 \\ 
1 & 2 & 4 
\end{pmatrix}
$$

$$
\mathbf{b} = \begin{pmatrix} 460 \\ 130 \\ 240 \end{pmatrix}
$$

The equation to solve is:

$$
\begin{pmatrix} 4 & 4 & 6 \\ 1 & 1 & 2 \\ 1 & 2 & 4 \end{pmatrix} \times \begin{pmatrix} x_1 \\ x_2 \\ x_3 \end{pmatrix} = \begin{pmatrix} 460 \\ 130 \\ 240 \end{pmatrix}
$$

## 2. Existence of Solution

To ensure a unique solution exists, we calculate the determinant of matrix $A$ ($\det(A)$).

$$
\det(A) = 4(1\cdot4 - 2\cdot2) - 4(1\cdot4 - 2\cdot1) + 6(1\cdot2 - 1\cdot1)
$$
$$
\det(A) = 4(0) - 4(2) + 6(1)
$$
$$
\det(A) = 0 - 8 + 6 = -2
$$

Since $\det(A) \neq 0$, the system has a unique solution.

## 3. Solution

Using Gaussian elimination or matrix inversion (implemented via `numpy.linalg.solve`), we find vector $\mathbf{x}$:

$$
\mathbf{x} = \begin{pmatrix} 20 \\ 50 \\ 30 \end{pmatrix}
$$

## 4. Interpretation

The factory produced the following quantities:
* **Scout:** 20 units
* **Kamikaze:** 50 units
* **Heavy Cargo:** 30 units

## 5. Verification

We multiply the original matrix $A$ by our result $\mathbf{x}$ to check if we get vector $\mathbf{b}$:

$$
\begin{cases}
4(20) + 4(50) + 6(30) = 80 + 200 + 180 = 460 \quad \text{(Matches Motors)} \\
1(20) + 1(50) + 2(30) = 20 + 50 + 60 = 130 \quad \text{(Matches Controllers)} \\
1(20) + 2(50) + 4(30) = 20 + 100 + 120 = 240 \quad \text{(Matches Batteries)}
\end{cases}
$$

The calculation is correct.