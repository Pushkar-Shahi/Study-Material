<div align="center">

# <span style="color:#2E8B57">🔍 Binary Search — Part 2 (Advanced Applications)</span>

![Section](https://img.shields.io/badge/Algorithm-Binary_Search-2E8B57) ![Language](https://img.shields.io/badge/Language-C++-00599C?logo=c%2B%2B&logoColor=white)

</div>

---

## 🧮 1. Square Root using Binary Search (Leetcode 69)

Instead of searching an array, you can use binary search on the **answer space**. To find the square root of $x$, the answer must lie between $0$ and $x$.

### 💡 Core Logic

- Search space: `lo = 0`, `hi = x`
- Calculate `mid = lo + (hi - lo) / 2`
- Check `mid * mid` against `x`:

```cpp
if (mid * mid > x) {
    hi = mid - 1; // Answer is smaller
} 
else if (mid * mid < x) {
    lo = mid + 1; // Answer might be mid, or larger
} 
else {
    return mid; // Exact square root found
}
```
*(Note: Use `long long` for `mid * mid` to avoid integer overflow).*

---

## ⛰️ 2. Peak Element in a Mountain Array (Leetcode 852)

A mountain array increases to a peak, then decreases. Example: `[1, 2, 3, 4, 3, 2, 1]`. The peak is `4`.

### 💡 Core Logic

You can determine which side of the mountain you are on by comparing `arr[mid]` to its neighbors:
1. **At the Peak:** `arr[mid - 1] < arr[mid] > arr[mid + 1]` (Return `mid`)
2. **On the Climbing Slope:** `arr[mid - 1] < arr[mid] < arr[mid + 1]` (The peak is to the right → `lo = mid + 1`)
3. **On the Descending Slope:** The peak is to the left → `hi = mid - 1`

---

## 🧍 3. Single Element in a Sorted Array (Leetcode 540)

Every element appears twice except for one. Example: `[-1, -1, 4, 5, 5, 7, 7]`.

### 💡 Core Logic

You use the length of the halves to determine where the single element lies.
- **Left Half Length:** Count how many elements are in the left partition (`f - l`).
- If the left half has an **odd** number of elements, the single element *must* be in that half.
- If it's **even**, the single element is in the right half.

> [!WARNING]
> Edge cases where the single element is at the very beginning `arr[0]` or the very end `arr[n-1]` must be handled separately!

---

## 🔄 4. Search in Rotated Sorted Array (Leetcode 33)

An array is sorted but pivoted (rotated) at some unknown index. Example: `[8, 9, 10, 1, 2, 3, 4, 5, 6, 7]`.

### 💡 Core Logic

At any point, **at least one half of the array will always be perfectly sorted.**
1. First, find which half is sorted.
2. Check if the target falls within the range of that sorted half.
3. If yes, search that half. If not, search the other half.

```cpp
// 1. Is the Left Half sorted?
if (arr[lo] <= arr[mid]) {
    // Does target lie in this sorted half?
    if (target >= arr[lo] && target < arr[mid]) hi = mid - 1;
    else lo = mid + 1;
} 
// 2. Otherwise, the Right Half must be sorted
else {
    // Does target lie in this sorted half?
    if (target > arr[mid] && target <= arr[hi]) lo = mid + 1;
    else hi = mid - 1;
}
```

---

### 🛠️ MLOps Perspective: Searching on Answer Spaces
> [!IMPORTANT]
> The **Square Root** problem introduces "Binary Search on Answer Space". In MLOps, this is how many threshold-tuning algorithms work:
> - **Threshold Optimization:** If you need an ML classifier to hit exactly 95% Precision, and you know Precision is monotonic with the prediction threshold (as threshold goes $0 \to 1$, Precision goes up), you don't test every threshold by increments of 0.01.
> - Instead, you Binary Search the threshold from `0.0` to `1.0`. `mid = 0.5`. If Precision at 0.5 is < 0.95, `lo = 0.5`. If > 0.95, `hi = 0.5`. This gets you the exact threshold in $\approx 10$ steps instead of $100$!

---

<div align="center">

⬅️ [Previous: Binary Search Part 1](./Binary_Search_1.md)

</div>
