<div align="center">

# <span style="color:#D4A017">🟡 Basic Sorting Algorithms — Part 1</span>

![Section](https://img.shields.io/badge/Algorithm-Sorting-D4A017) ![Language](https://img.shields.io/badge/Language-C++-00599C?logo=c%2B%2B&logoColor=white)

</div>

---

## 📋 Contents

| # | Algorithm | Time (Best) | Time (Worst) |
|---|---|:---:|:---:|
| 1 | **Bubble Sort** | $\mathcal{O}(n)$ | $\mathcal{O}(n^2)$ |
| 2 | **Selection Sort** | $\mathcal{O}(n^2)$ | $\mathcal{O}(n^2)$ |
| 3 | **Insertion Sort** | $\mathcal{O}(n)$ | $\mathcal{O}(n^2)$ |

---

## ✅ 0. Pre-check: Is Array Already Sorted?

```cpp
bool isSorted(int arr[], int n) {
    for(int i = 0; i < n - 1; i++) {
        if(arr[i] > arr[i + 1]) return false;
    }
    return true;
}
```
**Time:** $\mathcal{O}(n)$

---

## 🫧 1. Bubble Sort

Repeatedly compare adjacent elements and **swap** them if they're in the wrong order. After each full pass, the **largest unsorted element "bubbles up"** to its correct position at the end.

```cpp
void bubbleSort(int arr[], int n) {
    for(int i = 0; i < n - 1; i++) {       // Passes (n-1 passes needed)
        for(int j = 0; j < n - 1 - i; j++) { // Inner comparison
            if(arr[j] > arr[j + 1]) {
                swap(arr[j], arr[j + 1]);
            }
        }
    }
}
```

> [!NOTE]
> After every pass `i`, the last `i+1` elements are already sorted, so we reduce the inner loop with `n - 1 - i`.

### ⚡ Optimised Bubble Sort
If no swaps occur in an entire pass, the array is already sorted — stop early!

```cpp
void bubbleSortOptimised(int arr[], int n) {
    for(int i = 0; i < n - 1; i++) {
        bool swapped = false;
        for(int j = 0; j < n - 1 - i; j++) {
            if(arr[j] > arr[j + 1]) {
                swap(arr[j], arr[j + 1]);
                swapped = true;
            }
        }
        if(!swapped) break; // Already sorted!
    }
}
```

| Case | Time Complexity |
|---|:---:|
| Best Case (already sorted) | $\mathcal{O}(n)$ |
| Average / Worst Case | $\mathcal{O}(n^2)$ |

### 🔄 Reverse Bubble Sort (Sort Descending)
Swap the comparison direction: `if(arr[j] < arr[j + 1])`.

---

## 💡 2. Related Problems

### Move All Zeros to End (Leetcode 283)
Move all `0`s to the end while maintaining the relative order of non-zero elements.
- Use a **two-pointer** approach: pointer `i` marks where the next non-zero should go.
- Or use a modified bubble sort logic, bubbling zeros to the right.

```cpp
int i = 0;
for(int j = 0; j < n; j++) {
    if(arr[j] != 0) {
        swap(arr[i], arr[j]);
        i++;
    }
}
```

---

## 🎯 3. Selection Sort

Find the **minimum element** in the unsorted portion and place it at the beginning.

```cpp
void selectionSort(int arr[], int n) {
    for(int i = 0; i < n - 1; i++) {
        int minIdx = i;
        for(int j = i + 1; j < n; j++) {
            if(arr[j] < arr[minIdx]) {
                minIdx = j;
            }
        }
        swap(arr[i], arr[minIdx]); // Place min in its correct position
    }
}
```

| Case | Time Complexity |
|---|:---:|
| Best / Average / Worst | $\mathcal{O}(n^2)$ |

> [!NOTE]
> Selection Sort always makes exactly $n-1$ swaps — much fewer than Bubble Sort in practice, which is useful when write operations (swaps) are expensive.

### Variant: Find Largest First (Sort Descending)
Change the inner loop to find `maxIdx` instead, and swap it to the end of the unsorted portion.

---

## ⚖️ 4. Stability of Sorting Algorithms

A sort is **stable** if equal elements appear in the same relative order in the output as they were in the input.

| Algorithm | Stable? | Reason |
|---|:---:|---|
| **Bubble Sort** | ✅ Yes | Only swaps when `arr[j] > arr[j+1]` (strict `>`), equal elements are never swapped. |
| **Selection Sort** | ❌ No | The swap can move an element past another equal element. |

> [!TIP]
> **When does stability matter?** Imagine sorting students first by grade, then by name. A stable sort ensures that among students with the same grade, the alphabetical name ordering is preserved.

---

### 🛠️ MLOps Perspective: Sorting & Data Preprocessing
> [!IMPORTANT]
> Sorting is a core preprocessing step in ML data pipelines:
> - **Efficient Data Lookups:** Sorted arrays allow $\mathcal{O}(\log n)$ binary search instead of $\mathcal{O}(n)$ linear search. When indexing millions of feature records, this is the difference between a 1-second lookup and a 10-minute lookup.
> - **Stability in Pandas:** `pandas.DataFrame.sort_values(by=..., kind='mergesort')` uses a **stable** sort by default. Knowing *why* stability matters (as above with students) directly applies to sorting multi-key DataFrames.

---

<div align="center">

➡️ [Next: Basic Sorting Algorithms Part 2](./BasicSortingAlgos_2.md)

</div>
