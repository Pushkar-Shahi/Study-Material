<div align="center">

# <span style="color:#E07B00">🟠 Basic Sorting Algorithms — Part 2 (Insertion Sort & Classic Problems)</span>

![Section](https://img.shields.io/badge/Algorithm-Sorting-E07B00) ![Language](https://img.shields.io/badge/Language-C++-00599C?logo=c%2B%2B&logoColor=white)

</div>

---

## 🃏 1. Insertion Sort

Works like **sorting a hand of playing cards**. Take each new card and insert it into its correct position among the already-sorted cards in your hand.

For the array `{4, 1, 7, 3, 9, 2, 0, 8}`:
- Start at index 1. Pick `1`. Compare left: `4 > 1`, shift `4` right. Insert `1` at position 0. → `{1, 4, 7, 3, 9, 2, 0, 8}`
- Pick `7`. `4 < 7`, no shift needed. → `{1, 4, 7, 3, ...}`
- Pick `3`. Shift `7`, shift `4`, insert `3`. → `{1, 3, 4, 7, ...}` ... and so on.

```cpp
void insertionSort(int arr[], int n) {
    for(int i = 1; i < n; i++) {
        int key = arr[i]; // The element to be inserted
        int j = i - 1;
        // Shift elements that are greater than key to one position right
        while(j >= 0 && arr[j] > key) {
            arr[j + 1] = arr[j];
            j--;
        }
        arr[j + 1] = key; // Insert key at the correct position
    }
}
```

### ⏳ Time Complexity

| Case | Condition | Time |
|---|---|:---:|
| **Best Case** | Array is already sorted (no shifts needed in while loop) | $\mathcal{O}(n)$ |
| **Average Case** | Random order | $\mathcal{O}(n^2)$ |
| **Worst Case** | Array is sorted in reverse | $\mathcal{O}(n^2)$ |
| **Auxiliary Space** | In-place sorting | $\mathcal{O}(1)$ |

### ⚖️ Stability of Insertion Sort

Insertion Sort is **✅ Stable**. The `while` condition uses strict `>`, so equal elements are not shifted, preserving their relative order.

---

## 💡 2. Classic Problems Using Sorting

### Kth Smallest Element

**Brute Force:** Sort the array, then return `arr[k - 1]`. Time: $\mathcal{O}(n \log n)$.

> [!TIP]
> A more optimal approach uses a **Max-Heap of size k** to get $\mathcal{O}(n \log k)$, but sorting is the simplest approach to know.

### 2-Sum: Find a Pair with Given Sum (Leetcode 1)

Given an array and a target sum, find if any two elements add up to it.

**Approach 1 (Brute Force):** Nested loops. $\mathcal{O}(n^2)$.
**Approach 2 (Sort + Two Pointers):**
1. Sort the array: $\mathcal{O}(n \log n)$.
2. Use two pointers `lo = 0`, `hi = n-1`.
3. If `arr[lo] + arr[hi] == sum` → Found!
4. If the sum is **too small** → `lo++` (increase the left value)
5. If the sum is **too large** → `hi--` (decrease the right value)

```cpp
sort(arr, arr + n);
int lo = 0, hi = n - 1;
while(lo < hi) {
    int s = arr[lo] + arr[hi];
    if(s == target) return true;
    else if(s < target) lo++;
    else hi--;
}
```

---

## 🔗 3. Common Elements (Intersection/Union of Arrays)

### Common Elements in 3 Sorted Arrays
Given 3 sorted arrays, find the elements common to all three.

**Approach (3-Pointer):**
- Use three pointers `i`, `j`, `k`, one for each array.
- If `arr1[i] == arr2[j] == arr3[k]` → Add to result, advance all three.
- Otherwise, advance the pointer pointing to the **smallest** element.

### Homework Problems

| Problem | Concept |
|---|---|
| **Union of 2 Sorted Arrays** | Merge like merge-sort; use two pointers, add unique elements to result. |
| **Intersection of 2 Sorted Arrays (Distinct)** | Two pointers; only add element when both pointers match. |

---

### 🛠️ MLOps Perspective: Why These Problems Matter
> [!IMPORTANT]
> These "classic" array problems are the building blocks of real ML data pipelines:
> - **2-Sum / Two Pointers:** The two-pointer technique on sorted data is used in recommendation system pipelines to efficiently find matching user-item pairs from two sorted lists of IDs.
> - **Union/Intersection of Sorted Arrays:** This is exactly what happens when you merge training datasets from multiple sources. Efficiently computing the union (full combined dataset) or intersection (only samples present in all datasets) is a fundamental ETL (Extract, Transform, Load) operation in MLOps.

---

<div align="center">

⬅️ [Previous: Basic Sorting Algorithms Part 1](./BasicSortingAlgos_1.md) &nbsp;&nbsp;|&nbsp;&nbsp; ➡️ [Next: Strings Part 1](../Strings/Strings_1.md)

</div>
