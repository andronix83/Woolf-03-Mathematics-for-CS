# Task 4: Complex Production Analysis

## 1. Productivity Dynamics Analysis
The productivity function is defined as $P(t) = 100 + 40t - 4t^2$. To understand how productivity changes during the 10-hour shift, we analyzed the derivative $P'(t)$ at specific time points using `scipy.optimize.approx_fprime`.

**Observations:**
* **At t = 2 hours:** The rate of change is **24.00**. Since the derivative is positive, productivity is **increasing**.
* **At t = 5 hours:** The rate of change is approximately **0.00**. This indicates a stationary point where the function reaches its extremum.
* **At t = 8 hours:** The rate of change is **-24.00**. Since the derivative is negative, productivity is **decreasing**.

**Conclusion:** The shift starts with increasing productivity, peaks in the middle, and declines towards the end of the shift.

## 2. Peak Productivity
Using `minimize_scalar` (maximizing $P(t)$), we determined the exact moment of highest efficiency.

* **Peak Time ($t^*$):** 5.00 hours.
* **Max Productivity ($P(t^*)$):** 200.00 units/hour.

## 3. Total Production Volume
Using `scipy.integrate.quad`, we calculated the total number of units produced over the entire 10-hour shift ($\int_0^{10} P(t) dt$).

* **Total Units:** 1666.67 units.

## 4. Initial Parameter Determination
We solved the budget constraint system of linear equations using `numpy.linalg.solve`:
$$
\begin{cases} 
2x + y = 20 \\ 
x + 3y = 25 
\end{cases}
$$

* **Initial Solution:** $x_0 = 7.00$, $y_0 = 6.00$.

## 5. Cost Minimization
We optimized the cost function $C(x, y) = x^2 + y^2 - 10x - 8y + 50$ starting from the initial point $(7, 6)$ using the **BFGS** algorithm.

* **Optimal Raw Material ($x^*$):** 5.00
* **Optimal Energy ($y^*$):** 4.00
* **Minimum Unit Cost:** 9.00 UAH

## 6. Final Financial Calculation
The final total cost of production for the shift is calculated by multiplying the total production volume by the minimized unit cost.

$$\text{Total Cost} = 1666.67 \times 9.00 \approx 15000.00 \text{ UAH}$$

**Final Result:** The optimal operation of the plant results in a total cost of **15,000.00 UAH** for the shift.