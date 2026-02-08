# Analytical Solution: Trend Forecast (Least Squares Method)

## Problem Statement
We are given a set of data points representing CPU load over time. The goal is to find a linear trend line $y = kt + b$ that best fits the data and use it to predict the load at the 6th hour.

**Data:**
* Time ($t$): $[1, 2, 3, 4, 5]$
* Load ($y$): $[22, 28, 37, 45, 53]$

## 1. Matrix Formulation
We interpret the linear relationship for each data point $i$ as:
$$k \cdot t_i + b = y_i$$

This can be written in matrix form $A\mathbf{x} = \mathbf{y}$, where $\mathbf{x} = \begin{bmatrix} k \\ b \end{bmatrix}$ is the vector of unknown coefficients.

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
\end{bmatrix}
$$

## 2. The Normal Equation
Since the points do not lie perfectly on a line, the system $A\mathbf{x} = \mathbf{y}$ is inconsistent (overdetermined). To find the "best" solution, we minimize the sum of squared errors $\|\mathbf{y} - A\mathbf{x}\|^2$. This leads to the **Normal Equation**:

$$A^T A \mathbf{x} = A^T \mathbf{y}$$

### Step 2.1: Calculate $A^T A$
$$
A^T = \begin{bmatrix}
1 & 2 & 3 & 4 & 5 \\
1 & 1 & 1 & 1 & 1
\end{bmatrix}
$$

$$
A^T A = \begin{bmatrix}
1 & 2 & 3 & 4 & 5 \\
1 & 1 & 1 & 1 & 1
\end{bmatrix}
\cdot
\begin{bmatrix}
1 & 1 \\
2 & 1 \\
3 & 1 \\
4 & 1 \\
5 & 1
\end{bmatrix}
=
\begin{bmatrix}
1^2+2^2+3^2+4^2+5^2 & 1+2+3+4+5 \\
1+2+3+4+5 & 1+1+1+1+1
\end{bmatrix}
$$

$$
A^T A = \begin{bmatrix}
55 & 15 \\
15 & 5
\end{bmatrix}
$$

### Step 2.2: Calculate $A^T \mathbf{y}$
$$
A^T \mathbf{y} = \begin{bmatrix}
1 & 2 & 3 & 4 & 5 \\
1 & 1 & 1 & 1 & 1
\end{bmatrix}
\cdot
\begin{bmatrix}
22 \\
28 \\
37 \\
45 \\
53
\end{bmatrix}
=
\begin{bmatrix}
1(22) + 2(28) + 3(37) + 4(45) + 5(53) \\
22 + 28 + 37 + 45 + 53
\end{bmatrix}
$$

$$
A^T \mathbf{y} = \begin{bmatrix}
22 + 56 + 111 + 180 + 265 \\
185
\end{bmatrix}
=
\begin{bmatrix}
634 \\
185
\end{bmatrix}
$$

## 3. Solving for Coefficients
We now solve the system:
$$
\begin{bmatrix}
55 & 15 \\
15 & 5
\end{bmatrix}
\begin{bmatrix}
k \\
b
\end{bmatrix}
=
\begin{bmatrix}
634 \\
185
\end{bmatrix}
$$

We can use the inverse matrix $(A^T A)^{-1}$. The determinant is:
$$\det(A^T A) = 55(5) - 15(15) = 275 - 225 = 50$$

The inverse is:
$$
(A^T A)^{-1} = \frac{1}{50} \begin{bmatrix}
5 & -15 \\
-15 & 55
\end{bmatrix}
=
\begin{bmatrix}
0.1 & -0.3 \\
-0.3 & 1.1
\end{bmatrix}
$$

Now, multiply by $A^T \mathbf{y}$:
$$
\mathbf{x} = \begin{bmatrix} k \\ b \end{bmatrix} = \begin{bmatrix}
0.1 & -0.3 \\
-0.3 & 1.1
\end{bmatrix}
\begin{bmatrix}
634 \\
185
\end{bmatrix}
$$

$$k = 0.1(634) - 0.3(185) = 63.4 - 55.5 = 7.9$$
$$b = -0.3(634) + 1.1(185) = -190.2 + 203.5 = 13.3$$

**Resulting Coefficients:**
* Slope ($k$): **7.9**
* Intercept ($b$): **13.3**

## 4. Forecast
The equation for the trend line is:
$$\hat{y} = 7.9t + 13.3$$

To predict the load at the 6th hour ($t=6$):
$$\hat{y}_{6} = 7.9(6) + 13.3$$
$$\hat{y}_{6} = 47.4 + 13.3$$
$$\hat{y}_{6} = 60.7$$

**Predicted CPU Load for 6th hour:** 60.7