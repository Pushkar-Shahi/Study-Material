<div align="center">

# <span style="color:#2E8B57">🔍 Binary Search — Part 1</span>

![Section](https://img.shields.io/badge/Algorithm-Binary_Search-2E8B57) ![Language](https://img.shields.io/badge/Language-C++-00599C?logo=c%2B%2B&logoColor=white)

</div>

---

## 🎯 1. Binary Search Algorithm (Leetcode 704)

Binary search is an efficient algorithm for finding an item from a **sorted** list of items. It works by repeatedly dividing in half the portion of the list that could contain the item.

### 💻 Standard Implementation

```cpp
int search(vector<int>& arr, int tar) {
    int lo = 0;
    int hi = arr.size() - 1;

    while(lo <= hi) {
        int mid = lo + (hi - lo) / 2; // Prevents integer overflow

        if(arr[mid] > tar) {
            hi = mid - 1; // Target is in the left half
        } 
        else if(arr[mid] < tar) {
            lo = mid + 1; // Target is in the right half
        } 
        else {
            return mid; // Target found
        }
    }
    return -1; // Target not found
}
```

### ⏳ Time Complexity Analysis

At each step, the search space is divided by 2:
`n → n/2 → n/4 → n/8 ... → 1`

Total number of steps is $\log_2 n$.
**Time Complexity:** $\mathcal{O}(\log n)$

---

## ⚠️ 2. The `mid` Calculation Blunder

Calculating `mid = (lo + hi) / 2` can cause an **Integer Overflow** if `lo` and `hi` are very large (e.g., near $2^{31} - 1$). 

> [!TIP]
> **Correct Formula:** `mid = lo + (hi - lo) / 2;`

> [!WARNING]
> **Heavy Blunder:** `mid = (lo / 2) + (hi / 2)`
> If `lo = 3` and `hi = 5`, the correct mid is `(3+5)/2 = 4`.
> But integer division gives: `3/2 + 5/2 = 1 + 2 = 3`. (Incorrect!)

---

## 📉 3. Bounds in C++

### Lower Bound
Find the smallest index where `arr[i] >= tar`.
**C++ STL:** `lower_bound(arr.begin(), arr.end(), target)`
- If the target exists, it gives the first occurrence.
- Otherwise, it gives the smallest element which is strictly greater than the target.

```cpp
int l = 0, h = n - 1, lb = n;
while(l <= h) {
    int m = l + (h - l) / 2;
    if(arr[m] < tar) {
        l = m + 1;
    } else { // arr[m] >= tar
        lb = m;
        h = m - 1;
    }
}
```

### Upper Bound
Find the smallest index where `arr[i] > tar` (strictly greater).
**C++ STL:** `upper_bound(arr.begin(), arr.end(), target)`

---

## 💡 4. Related Problems & Homework

| Problem | Type | Concept |
|---|---|---|
| **First and Last Occurrence** | Leetcode 34 | Apply Binary Search twice (find first occ, then last occ). |
| **Search Insert Position** | Leetcode 35 | Same as finding the **Lower Bound** of the target. |
| **Maximum Count of Pos/Neg** | Leetcode 2529 | Use binary search to find the transition between negatives and positives. |
| **Decreasing Order Search** | Homework | Adjust conditions: if `arr[m] > tar`, search right (`lo = m + 1`). |
| **Floor in Sorted Array** | Homework | Largest element $\le$ target (opposite of lower bound logic). |

---

### 🛠️ MLOps Perspective: Binary Search
> [!IMPORTANT]
> You might think you don't need Binary Search in ML, but you use it constantly under the hood:
> - **Hyperparameter Tuning:** When tuning a parameter (like learning rate or tree depth), algorithms like Optuna often use bisecting logic to hone in on the optimal region of the search space.
> - **Vector Databases:** Tools like Faiss (Facebook AI Similarity Search) use tree-based indexes. Searching a sorted tree structure is functionally a binary/multi-way search, giving $\mathcal{O}(\log n)$ retrieval for your RAG pipelines instead of $\mathcal{O}(n)$ linear scans.
> - **Handling Overflow:** The `mid` calculation bug is a classic example of why we use robust numeric libraries (like NumPy) which handle large-scale matrix indexing safely under the hood.

---

<div align="center">

➡️ [Next: Binary Search Part 2](./Binary_Search_2.md)

</div>
