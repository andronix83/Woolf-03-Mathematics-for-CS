# Task 4: Trend Forecast (Least Squares Method)

## 1. Matrix Formulation
To find the linear trend $y = kt + b$, we represent the data points as a system of linear equations $A\mathbf{x} = \mathbf{y}$.

**Data:**
* Time ($t$): $[1, 2, 3, 4, 5]$
* Load ($y$): $[22, 28, 37, 45, 53]$

$$
A = \begin{bmatrix}
1 & 1 \\
2 & 1 \\
3 & 1 \\
4 & 1 \\
5 & 1
\end{bmatrix}, \quad
\mathbf{y} = \begin{bmatrix}
22 \\
28 \\
37 \\
45 \\
53
\end{bmatrix}, \quad
\mathbf{x} = \begin{bmatrix} k \\ b \end{bmatrix}
$$

## 2. Normal Equation
The optimal coefficients $\mathbf{x}$ are found by solving the Normal Equation:
$$A^T A \mathbf{x} = A^T \mathbf{y}$$

### Step 2.1: Calculate $A^T A$
$$
\begin{aligned}
A^T A &= \begin{bmatrix} 1 & 2 & 3 & 4 & 5 \\ 1 & 1 & 1 & 1 & 1 \end{bmatrix} \cdot \begin{bmatrix} 1 & 1 \\ 2 & 1 \\ 3 & 1 \\ 4 & 1 \\ 5 & 1 \end{bmatrix} \\
&= \begin{bmatrix} 1^2+2^2+3^2+4^2+5^2 & 1+2+3+4+5 \\ 1+2+3+4+5 & 1+1+1+1+1 \end{bmatrix} \\
&= \begin{bmatrix} 55 & 15 \\ 15 & 5 \end{bmatrix}
\end{aligned}
$$

### Step 2.2: Calculate $A^T \mathbf{y}$
$$
\begin{aligned}
A^T \mathbf{y} &= \begin{bmatrix} 1 & 2 & 3 & 4 & 5 \\ 1 & 1 & 1 & 1 & 1 \end{bmatrix} \cdot \begin{bmatrix} 22 \\ 28 \\ 37 \\ 45 \\ 53 \end{bmatrix} \\
&= \begin{bmatrix} 1(22) + 2(28) + 3(37) + 4(45) + 5(53) \\ 22 + 28 + 37 + 45 + 53 \end{bmatrix} \\
&= \begin{bmatrix} 634 \\ 185 \end{bmatrix}
\end{aligned}
$$

## 3. Solving the System
We solve $\begin{bmatrix} 55 & 15 \\ 15 & 5 \end{bmatrix} \begin{bmatrix} k \\ b \end{bmatrix} = \begin{bmatrix} 634 \\ 185 \end{bmatrix}$ using the inverse matrix method.

The determinant is $\det(A^T A) = 55(5) - 15(15) = 50$.

$$
\begin{aligned}
\mathbf{x} &= (A^T A)^{-1} \cdot (A^T \mathbf{y}) \\
&= \frac{1}{50} \begin{bmatrix} 5 & -15 \\ -15 & 55 \end{bmatrix} \cdot \begin{bmatrix} 634 \\ 185 \end{bmatrix} \\
&= \begin{bmatrix} 0.1 & -0.3 \\ -0.3 & 1.1 \end{bmatrix} \cdot \begin{bmatrix} 634 \\ 185 \end{bmatrix} \\
&= \begin{bmatrix} 7.9 \\ 13.3 \end{bmatrix}
\end{aligned}
$$

**Coefficients:** $k = 7.9$, $b = 13.3$.

## 4. Final Trend and Forecast
The trend equation is:
$$\hat{y} = 7.9t + 13.3$$

**Forecast for $t = 6$:**
$$\hat{y}_6 = 7.9(6) + 13.3 = 47.4 + 13.3 = 60.7$$