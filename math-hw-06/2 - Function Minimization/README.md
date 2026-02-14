# Task 2: Function Minimization Analysis

## 1. Analytical Derivation
**Objective Function:**
$$f(x, y) = x^2 + xy + y^2 - 6x - 9y + 20$$

**Gradient Calculation:**
To find the critical point, we solved the system where $\nabla f = 0$:
1. $\frac{\partial f}{\partial x} = 2x + y - 6 = 0$
2. $\frac{\partial f}{\partial y} = x + 2y - 9 = 0$

Solving this linear system yielded the critical point: **$(x^*, y^*) = (1, 4)$**.

## 2. Extremum Classification
We analyzed the Hessian Matrix $H$ at point $(1, 4)$:
$$H = \begin{pmatrix} 2 & 1 \\ 1 & 2 \end{pmatrix}$$

**Eigenvalues:**
The characteristic equation $\det(H - \lambda I) = 0$ resulted in eigenvalues:
* $\lambda_1 = 1$
* $\lambda_2 = 3$

Since $\lambda_1 > 0$ and $\lambda_2 > 0$, the matrix is **positive definite**.
**Conclusion:** The point $(1, 4)$ represents a **strict local minimum**.

## 3. Numerical Verification
Using Python's `scipy.optimize.minimize` with the BFGS method:
* **Calculated Minimum:** $x \approx 1.0000$, $y \approx 4.0000$
* **Function Value:** $f(1, 4) = -1.0$

This perfectly matches the analytical solution.

## 4. Stability Analysis
The optimization was tested from three distinct starting points to ensure solution stability:
1.  Start $(0, 0) \rightarrow$ Converged to $(1.0, 4.0)$
2.  Start $(10, 10) \rightarrow$ Converged to $(1.0, 4.0)$
3.  Start $(-5, 15) \rightarrow$ Converged to $(1.0, 4.0)$

**Final Conclusion:**
The numerical method is robust. Regardless of the initialization within the tested range, the algorithm consistently converges to the analytical minimum of $(1, 4)$.