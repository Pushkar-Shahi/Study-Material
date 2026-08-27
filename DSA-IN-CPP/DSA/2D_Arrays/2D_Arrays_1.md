<div align="center">

# <span style="color:#2E8B57">🔲 2D Arrays — Part 1 (Fundamentals)</span>

![Section](https://img.shields.io/badge/Algorithm-2D_Arrays-2E8B57) ![Language](https://img.shields.io/badge/Language-C++-00599C?logo=c%2B%2B&logoColor=white)

</div>

---

## 🔁 1. Pre-requisite: Merge Two Sorted Arrays (Leetcode 88)

Before diving into 2D arrays, a classic 1D array problem using two pointers:
Given two sorted arrays `a` and `b`, merge them into a sorted array `c`.

```cpp
int i = 0, j = 0, k = 0;
while(i < m && j < n) {
    if(a[i] < b[j]) {
        c[k] = a[i];
        i++;
    } else {
        c[k] = b[j];
        j++;
    }
    k++;
}
// Add remaining elements from a (if any)
// Add remaining elements from b (if any)
```
**Time Complexity:** $\mathcal{O}(m+n)$

---

## 🧱 2. Representation & Creation

A 2D array (or matrix) is essentially an **Array of Arrays**.

```cpp
int arr[3][4] = {
    {9, 4, 8, 4}, // Row 0
    {6, 1, 1, 5}, // Row 1
    {2, 2, 3, 6}  // Row 2
};
```
- Access an element: `arr[row][col]`
- `arr[1][2]` gives `1` (from the second row, third column).

---

## 🏃‍♂️ 3. Traversal (Input/Output)

To traverse a 2D array, you need **nested loops**.
- **Time Complexity:** $\mathcal{O}(m \times n)$

### Row-wise Traversal (Standard)
```cpp
for(int i = 0; i < m; i++) {       // Rows
    for(int j = 0; j < n; j++) {   // Columns
        cout << arr[i][j] << " ";
    }
}
```

### Column-wise Traversal
```cpp
for(int j = 0; j < n; j++) {       // Columns first
    for(int i = 0; i < m; i++) {   // Rows
        cout << arr[i][j] << " ";
    }
}
```

---

## 🐍 4. Standard Matrix Problems

### Print Matrix in Snake Pattern
Prints left-to-right on even rows, and right-to-left on odd rows.
- If `row % 2 == 0`: Traverse columns `0` to `n-1`
- If `row % 2 != 0`: Traverse columns `n-1` down to `0`

### Transpose of a Matrix (Leetcode 867)
To transpose a matrix (swap rows with columns) **in-place** (for square matrices), you swap across the diagonal.
```cpp
// Hint: swap(arr[i][j], arr[j][i])
for(int i = 0; i < n; i++) {
    for(int j = i; j < n; j++) { // Notice j starts at i
        swap(arr[i][j], arr[j][i]);
    }
}
```

---

## 💡 5. Homework & Practice Questions

| Problem | Goal |
|---|---|
| **Sum of Elements** | Traverse and sum all elements. |
| **Find Maximum Element** | Keep a `max` variable, update during traversal. |
| **Row with Max Sum** | Calculate sum per row, track the maximum sum and its row index. |
| **Min of Max / Max of Min** | Find the min element out of the max of each row; and vice versa. |

---

### 🛠️ MLOps Perspective: 2D Arrays & Matrices
> [!IMPORTANT]
> A 2D Array in C++ is conceptually the exact same thing as a 2D **Tensor** or a pandas **DataFrame** in Machine Learning.
> - **Images as 2D Arrays:** Every grayscale image fed into a Convolutional Neural Network (CNN) is a 2D array of pixels (0-255). 
> - **Transposing (Leetcode 867):** When multiplying weight matrices in neural networks ($\mathbf{W}^T \mathbf{X}$), you are constantly transposing 2D arrays. NumPy's `np.transpose()` runs highly optimized C++ code under the hood doing exactly what you learned here!

---

<div align="center">

➡️ [Next: 2D Arrays Part 2](./2D_Arrays_2.md)

</div>
