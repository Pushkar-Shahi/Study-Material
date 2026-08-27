<div align="center">

# <span style="color:#1E6FEB">🟦 2D Arrays — Part 3 (Advanced Algorithms)</span>

![Section](https://img.shields.io/badge/Algorithm-2D_Arrays-1E6FEB) ![Language](https://img.shields.io/badge/Language-C++-00599C?logo=c%2B%2B&logoColor=white)

</div>

---

## 🔍 1. Search in a 2D Matrix II (Leetcode 240)

Given a matrix where every row is sorted left-to-right and every column is sorted top-to-bottom, find a target value.

- **Brute Force:** Traverse everything $\mathcal{O}(m \times n)$.
- **Optimal $\mathcal{O}(m + n)$:** Start at the **top-right** corner (or bottom-left).
  - If `current > target`: Move Left (the entire column is larger, so ignore it).
  - If `current < target`: Move Down (the entire row is smaller, so ignore it).
  - If `current == target`: Found!

```cpp
int r = 0, c = cols - 1;
while(r < rows && c >= 0) {
    if(matrix[r][c] == target) return true;
    else if(matrix[r][c] > target) c--; // Go Left
    else r++; // Go Down
}
```

---

## 🌀 2. Spiral Matrix Traversal (Leetcode 54)

Traverse a matrix in a spiral order (Right → Down → Left → Up).
You need 4 boundary variables: `minr`, `maxr`, `minc`, `maxc`.

### 💡 Core Logic
```cpp
while(minr <= maxr && minc <= maxc) {
    // 1. Top row (Left to Right)
    for(int j = minc; j <= maxc; j++) cout << arr[minr][j];
    minr++; // Shrink top boundary

    // 2. Right column (Top to Bottom)
    for(int i = minr; i <= maxr; i++) cout << arr[i][maxc];
    maxc--; // Shrink right boundary

    // 3. Bottom row (Right to Left)
    for(int j = maxc; j >= minc; j--) cout << arr[maxr][j];
    maxr--; // Shrink bottom boundary

    // 4. Left column (Bottom to Top)
    for(int i = maxr; i >= minr; i--) cout << arr[i][minc];
    minc++; // Shrink left boundary
}
```
*(Note: Edge cases where matrix is not a perfect square require additional boundary checks before steps 3 and 4).*

---

## 💣 3. Set Matrix Zeros (Leetcode 73)

If an element is `0`, set its entire row and column to `0`.

### Method 1: Brute Force (Worst)
- Copy the matrix. Traverse the original. If `0`, update the copy's row and col.
- **Space:** $\mathcal{O}(m \times n)$ | **Time:** $\approx \mathcal{O}(n^3)$

### Method 2: Better Approach
- Use two boolean arrays: `row[m]` and `col[n]`. 
- If `arr[i][j] == 0`, mark `row[i] = true` and `col[j] = true`. 
- Traverse again and set zeros based on the boolean arrays.
- **Space:** $\mathcal{O}(m + n)$ | **Time:** $\mathcal{O}(m \times n)$

### Method 3: Optimal (In-Place)
- Use the **0th row and 0th column** of the matrix itself to act as your boolean tracking arrays!
- **Space:** $\mathcal{O}(1)$ | **Time:** $\mathcal{O}(m \times n)$
- *Challenge:* You must handle the intersection `arr[0][0]` carefully to know if the 0th row or 0th col inherently had a zero before you started overwriting them.

---

### 🛠️ MLOps Perspective: Spatial Locality
> [!NOTE]
> Why does $\mathcal{O}(m+n)$ spatial optimization matter in MLOps?
> - **In-place Operations:** When you are processing a 100GB batched image tensor for computer vision, allocating an extra $\mathcal{O}(m \times n)$ (Method 1) matrix in GPU VRAM will instantly throw an `CUDA Out of Memory` (OOM) error.
> - Method 3 (In-Place modification) is a core software engineering principle for deep learning pipelines where memory is often a stricter bottleneck than compute time.

---

<div align="center">

⬅️ [Previous: 2D Arrays Part 2](./2D_Arrays_2.md)

</div>
