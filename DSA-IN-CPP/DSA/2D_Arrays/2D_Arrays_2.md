<div align="center">

# <span style="color:#1E6FEB">🟦 2D Arrays — Part 2 (Advanced Matrix Operations)</span>

![Section](https://img.shields.io/badge/Algorithm-2D_Arrays-1E6FEB) ![Language](https://img.shields.io/badge/Language-C++-00599C?logo=c%2B%2B&logoColor=white)

</div>

---

## 🔄 1. Matrix Rotation (Leetcode 48)

To rotate an $N \times N$ matrix by 90 degrees clockwise **in-place**:
You don't need complex math. It's a two-step process:

1. **Transpose the Matrix:** Swap `arr[i][j]` with `arr[j][i]`.
2. **Reverse Each Row:** Reverse the elements of every single row.

```cpp
// Step 1: Transpose
for(int i = 0; i < n; i++) {
    for(int j = i; j < n; j++) {
        swap(matrix[i][j], matrix[j][i]);
    }
}

// Step 2: Reverse each row
for(int i = 0; i < n; i++) {
    reverse(matrix[i].begin(), matrix[i].end());
}
```

---

## 📦 2. 2D Vectors in C++

Instead of fixed-size 2D arrays, C++ provides `vector<vector<int>>` which allows dynamic sizing (e.g., rows of different lengths, useful for graphs).

```cpp
int rows = 3, cols = 4;
vector<vector<int>> matrix(rows, vector<int>(cols, 0)); // Initializes a 3x4 matrix with 0s
```

---

## 🔺 3. Pascal's Triangle (Leetcode 118)

Pascal's Triangle is a classic 2D vector problem where each row has a different length (Row $i$ has $i+1$ elements).
**Core Logic:**
An element is the sum of the two elements directly above it in the previous row.
`arr[i][j] = arr[i-1][j-1] + arr[i-1][j]`

*(Note: The first and last elements of every row are always `1`).*

---

## ✖️ 4. Matrix Multiplication

Multiplying two matrices is a fundamental operation.
If Matrix $A$ is $(m \times n)$ and Matrix $B$ is $(p \times q)$:
- **Condition:** They can only be multiplied if $n == p$ (columns of $A$ == rows of $B$).
- **Result:** The resulting matrix $C$ will have dimensions $(m \times q)$.

### 💻 Core Logic
To find the element at $C[i][j]$, you take the dot product of the $i$-th row of $A$ and the $j$-th column of $B$.

```cpp
// C is initialized as an m x q matrix of 0s
for(int i = 0; i < m; i++) {
    for(int j = 0; j < q; j++) {
        for(int k = 0; k < n; k++) {
            C[i][j] += A[i][k] * B[k][j];
        }
    }
}
```
**Time Complexity:** $\mathcal{O}(m \times n \times q)$ (For square matrices, $\mathcal{O}(n^3)$).

---

### 🛠️ MLOps Perspective: Matrix Multiplication
> [!IMPORTANT]
> The nested triple-loop Matrix Multiplication ($\mathcal{O}(n^3)$) shown above is the mathematical foundation of **Deep Learning**.
> - **Neural Networks:** Every fully connected layer in a neural network is just computing $\mathbf{Y} = \mathbf{W}\mathbf{X} + \mathbf{b}$. This is exactly Matrix Multiplication.
> - **Why GPUs?** Doing three nested `for` loops in C++ is incredibly slow for a $1000 \times 1000$ matrix. GPUs (like NVIDIA) are specifically designed to parallelize the inner `k` loop, doing thousands of these multiplications simultaneously. 
> - **BLAS:** In MLOps, you never write these raw loops. We rely on BLAS (Basic Linear Algebra Subprograms) libraries that use advanced algorithms (like Strassen's) to beat the $\mathcal{O}(n^3)$ time limit.

---

<div align="center">

⬅️ [Previous: 2D Arrays Part 1](./2D_Arrays_1.md) &nbsp;&nbsp;|&nbsp;&nbsp; ➡️ [Next: 2D Arrays Part 3](./2D_Arrays_3.md)

</div>
