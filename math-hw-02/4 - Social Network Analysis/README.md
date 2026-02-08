# Task 4: Company Social Network Analysis

## 1. Graph Representations

We analyzed a social network of a small IT company with 6 employees. The graph $G = (V, E)$ consists of:
* **Vertices ($V$):** 6 (Anna, Bogdan, Viktor, Hanna, Dmytro, Yevhen)
* **Edges ($E$):** 9 (representing unique communication channels)

### Data Structures Constructed:
1.  **Adjacency List:** A dictionary mapping each employee to a list of colleagues they communicate with. This is the most memory-efficient representation for sparse graphs.
2.  **Adjacency Matrix:** A $6 \times 6$ symmetric binary matrix where $A_{ij} = 1$ if employee $i$ talks to employee $j$, and $0$ otherwise.
3.  **Edge List:** A list of 9 unique tuples representing the communication links (e.g., `('Anna', 'Bogdan')`).

## 2. Vertex Degrees & Communication Analysis

The **degree** of a vertex represents the number of active contacts an employee has.

| Employee | Degree |
| :--- | :---: |
| **Viktor** | **4** |
| Anna | 3 |
| Bogdan | 3 |
| Hanna | 3 |
| Dmytro | 3 |
| **Yevhen** | **2** |

### Conclusions:
* **Most Communicative:** **Viktor** is the central hub of the network with **4** connections. He communicates with everyone except Yevhen.
* **Least Communicative:** **Yevhen** has the fewest connections (**2**), communicating only with Hanna and Dmytro.

## 3. Verification of the Handshaking Lemma

The **Handshaking Lemma** (or Sum of Degrees Theorem) states that for any finite undirected graph, the sum of the degrees of all vertices is equal to twice the number of edges:

$$\sum_{v \in V} \deg(v) = 2 \cdot |E|$$

### Calculation:
1.  **Sum of degrees:** $3 + 3 + 4 + 3 + 3 + 2 = 18$
2.  **Number of edges ($|E|$):** $9$
3.  **Twice the edges ($2 \cdot |E|$):** $2 \times 9 = 18$

### Result:
$$18 = 18$$

**The theorem is successfully verified.** The calculations confirm the graph data is consistent and the topology is valid.