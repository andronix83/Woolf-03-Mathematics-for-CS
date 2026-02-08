# Problem 1: Working with Images as Matrices

## Problem Statement
Digital images are stored in computers as arrays of numbers (matrices). We are working with a $3 \times 3$ pixel image fragment.

**Given:**

Image Matrix $M$:

$$
M = \begin{pmatrix} 
100 & 150 & 200 \\ 
50 & 100 & 150 \\ 
0 & 50 & 100 
\end{pmatrix}
$$

Effect Matrix $E$:

$$
E = \begin{pmatrix} 
20 & 30 & 40 \\ 
10 & 20 & 30 \\ 
5 & 10 & 15 
\end{pmatrix}
$$

---

## Analytical Solution

### 1. Change Contrast
**Task:** Reduce the image brightness by multiplying matrix $M$ by a scalar $\lambda = 0.5$.

$$
M_{contrast} = 0.5 \cdot \begin{pmatrix} 
100 & 150 & 200 \\ 
50 & 100 & 150 \\ 
0 & 50 & 100 
\end{pmatrix}
$$

**Calculation:**
* **Row 1:** $100 \cdot 0.5 = 50$, $150 \cdot 0.5 = 75$, $200 \cdot 0.5 = 100$
* **Row 2:** $50 \cdot 0.5 = 25$, $100 \cdot 0.5 = 50$, $150 \cdot 0.5 = 75$
* **Row 3:** $0 \cdot 0.5 = 0$, $50 \cdot 0.5 = 25$, $100 \cdot 0.5 = 50$

**Result:**

$$
M_{contrast} = \begin{pmatrix} 
50 & 75 & 100 \\ 
25 & 50 & 75 \\ 
0 & 25 & 50 
\end{pmatrix}
$$

---

### 2. Brightness Correction
**Task:** Add a scalar $c = 25$ to every element of matrix $M$.

$$
M_{brightness} = M + 25
$$

**Calculation:**
* **Row 1:** $100 + 25 = 125$, $150 + 25 = 175$, $200 + 25 = 225$
* **Row 2:** $50 + 25 = 75$, $100 + 25 = 125$, $150 + 25 = 175$
* **Row 3:** $0 + 25 = 25$, $50 + 25 = 75$, $100 + 25 = 125$

**Result:**

$$
M_{brightness} = \begin{pmatrix} 
125 & 175 & 225 \\ 
75 & 125 & 175 \\ 
25 & 75 & 125 
\end{pmatrix}
$$

---

### 3. Blending
**Task:** Create a new image as a linear combination: $0.8 \cdot M + 0.2 \cdot E$.

**Step A: Calculate scaled $M$ ($0.8 \cdot M$)**

$$
\begin{pmatrix} 
100(0.8) & 150(0.8) & 200(0.8) \\ 
50(0.8) & 100(0.8) & 150(0.8) \\ 
0(0.8) & 50(0.8) & 100(0.8) 
\end{pmatrix} = 
\begin{pmatrix} 
80 & 120 & 160 \\ 
40 & 80 & 120 \\ 
0 & 40 & 80 
\end{pmatrix}
$$

**Step B: Calculate scaled $E$ ($0.2 \cdot E$)**

$$
\begin{pmatrix} 
20(0.2) & 30(0.2) & 40(0.2) \\ 
10(0.2) & 20(0.2) & 30(0.2) \\ 
5(0.2) & 10(0.2) & 15(0.2) 
\end{pmatrix} = 
\begin{pmatrix} 
4 & 6 & 8 \\ 
2 & 4 & 6 \\ 
1 & 2 & 3 
\end{pmatrix}
$$

**Step C: Sum the matrices**

$$
M_{blend} = \begin{pmatrix} 
80+4 & 120+6 & 160+8 \\ 
40+2 & 80+4 & 120+6 \\ 
0+1 & 40+2 & 80+3 
\end{pmatrix}
$$

**Result:**

$$
M_{blend} = \begin{pmatrix} 
84 & 126 & 168 \\ 
42 & 84 & 126 \\ 
1 & 42 & 83 
\end{pmatrix}
$$