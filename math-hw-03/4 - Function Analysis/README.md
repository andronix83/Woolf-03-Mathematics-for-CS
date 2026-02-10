# Task 4: Analysis of a Function of Two Variables

## 1. Analytical Partial Derivatives
Given the function:
$$f(x, y) = 0.5x^2 + 0.3y^2 + 0.2xy + 10x + 5y$$

The partial derivatives are calculated as follows:

**Partial derivative with respect to x:**
$$\frac{\partial f}{\partial x} = \frac{\partial}{\partial x}(0.5x^2 + 10x + 0.2xy) = x + 10 + 0.2y$$

**Partial derivative with respect to y:**
$$\frac{\partial f}{\partial y} = \frac{\partial}{\partial y}(0.3y^2 + 5y + 0.2xy) = 0.6y + 5 + 0.2x$$

## 2. Gradient Calculation at Point (10, 20)

### Analytical Method
Substituting $x=10$ and $y=20$ into the formulas above:
- $\frac{\partial f}{\partial x} = 10 + 10 + 0.2(20) = 24$
- $\frac{\partial f}{\partial y} = 0.6(20) + 5 + 0.2(10) = 12 + 5 + 2 = 19$

Analytical Gradient $\nabla f = (24, 19)$.

### Numerical Method
Using `scipy.optimize.approx_fprime`, the numerical gradient was calculated.
- Numerical Gradient Result: $\approx (24.0, 19.0)$

**Conclusion:** The analytical and numerical methods yield identical results (within floating-point precision limits), verifying the correctness of the derivation.

## 3. Function Change Estimation (Linear Approximation)

We estimate the change $\Delta f$ when moving from point $(10, 20)$ with steps $\Delta x = 0.5$ and $\Delta y = -0.3$.

**Formula:**
$$\Delta f \approx \frac{\partial f}{\partial x} \Delta x + \frac{\partial f}{\partial y} \Delta y$$

**Calculation:**
$$\Delta f \approx 24 \cdot (0.5) + 19 \cdot (-0.3)$$
$$\Delta f \approx 12 - 5.7 = 6.3$$

## 4. Comparison with Exact Change

To verify the accuracy of the approximation, we calculate the exact function values:
1. **Initial Value** $f(10, 20) = 410.0$
2. **New Value** $f(10.5, 19.7) = 416.422$
3. **Exact Change:** $416.422 - 410.0 = 6.422$

**Comparison:**
- Approximate Change: $6.3$
- Exact Change: $6.422$
- **Error:** $|6.422 - 6.3| = 0.122$

**Conclusion:** The linear approximation provides a close estimate to the actual function behavior for small steps, though a slight deviation exists due to the quadratic nature of the function (non-linearity).