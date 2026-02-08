# Task 2: Search for Similar Movies

## Problem Statement
We need to determine which movie fits the user's profile best by comparing the angle between feature vectors in a multidimensional space. We use **Cosine Similarity** as the metric.

**User Profile Vector:**
$$\mathbf{u} = (8, 2, 5)$$

**Movie Vectors:**
* Film A: $\mathbf{v}_A = (9, 1, 2)$
* Film B: $\mathbf{v}_B = (1, 9, 8)$
* Film C: $\mathbf{v}_C = (7, 2, 6)$

**Formula:**
$$\cos \theta = \frac{\mathbf{u} \cdot \mathbf{v}}{\|\mathbf{u}\| \|\mathbf{v}\|}$$
Where $\mathbf{u} \cdot \mathbf{v}$ is the dot product and $\|\mathbf{v}\|$ is the Euclidean norm (length).

---

## 1. Calculate User Vector Norm
First, we calculate the length of the user vector $\mathbf{u}$.

$$\|\mathbf{u}\| = \sqrt{8^2 + 2^2 + 5^2} = \sqrt{64 + 4 + 25} = \sqrt{93} \approx 9.64365$$

---

## 2. Calculate Similarity for Each Movie

### Film A (Action)
* **Vector:** $\mathbf{v}_A = (9, 1, 2)$
* **Norm $\|\mathbf{v}_A\|$:**
    $$\sqrt{9^2 + 1^2 + 2^2} = \sqrt{81 + 1 + 4} = \sqrt{86} \approx 9.27362$$
* **Dot Product ($\mathbf{u} \cdot \mathbf{v}_A$):**
    $$(8 \cdot 9) + (2 \cdot 1) + (5 \cdot 2) = 72 + 2 + 10 = 84$$
* **Cosine Similarity:**
    $$\cos \theta_A = \frac{84}{\sqrt{93} \cdot \sqrt{86}} \approx \frac{84}{89.4315} \approx \mathbf{0.9393}$$

### Film B (Comedy)
* **Vector:** $\mathbf{v}_B = (1, 9, 8)$
* **Norm $\|\mathbf{v}_B\|$:**
    $$\sqrt{1^2 + 9^2 + 8^2} = \sqrt{1 + 81 + 64} = \sqrt{146} \approx 12.08305$$
* **Dot Product ($\mathbf{u} \cdot \mathbf{v}_B$):**
    $$(8 \cdot 1) + (2 \cdot 9) + (5 \cdot 8) = 8 + 18 + 40 = 66$$
* **Cosine Similarity:**
    $$\cos \theta_B = \frac{66}{\sqrt{93} \cdot \sqrt{146}} \approx \frac{66}{116.5247} \approx \mathbf{0.5664}$$

### Film C (Drama)
* **Vector:** $\mathbf{v}_C = (7, 2, 6)$
* **Norm $\|\mathbf{v}_C\|$:**
    $$\sqrt{7^2 + 2^2 + 6^2} = \sqrt{49 + 4 + 36} = \sqrt{89} \approx 9.43398$$
* **Dot Product ($\mathbf{u} \cdot \mathbf{v}_C$):**
    $$(8 \cdot 7) + (2 \cdot 2) + (5 \cdot 6) = 56 + 4 + 30 = 90$$
* **Cosine Similarity:**
    $$\cos \theta_C = \frac{90}{\sqrt{93} \cdot \sqrt{89}} \approx \frac{90}{90.9780} \approx \mathbf{0.9892}$$

---

## 3. Conclusion

Comparing the calculated coefficients:

| Movie | Similarity Score |
| :--- | :--- |
| **Film A** | 0.9393 |
| **Film B** | 0.5664 |
| **Film C** | **0.9892** |

**Result:**
The movie with the highest similarity score is **Film C**. It is statistically the closest match to the user's profile.