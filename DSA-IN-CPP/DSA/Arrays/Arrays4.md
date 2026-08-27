<div align="center">

# <span style="color:#2E8B57">📦 Arrays — Part 4 (Algorithmic Problem Solving)</span>

![Section](https://img.shields.io/badge/Algorithm-Array_Problems-2E8B57) ![Language](https://img.shields.io/badge/Language-C++-00599C?logo=c%2B%2B&logoColor=white)

</div>

---

## 🔀 1. Segregate 0s and 1s

Given an array of `0`s and `1`s, sort it so all `0`s are on the left and `1`s on the right.

### Method 1: Counting (Two Passes)
Count the total number of zeros. In the second pass, fill the first `count` indices with `0` and the rest with `1`.

### Method 2: Two Pointers (Optimal - One Pass)
Use two pointers `i = 0` and `j = n - 1`.
```cpp
while(i < j) {
    if(arr[i] == 0) i++; // Already in correct place
    else if(arr[j] == 1) j--; // Already in correct place
    else if(arr[i] == 1 && arr[j] == 0) {
        swap(arr[i], arr[j]);
        i++;
        j--;
    }
}
```

---

## 🔍 2. Missing Number in Array (Leetcode 268)

Given an array of size `n` containing numbers from `0` to `n`, one number is missing. Find it.

### Progression of Methods:
1. **Nested Loops:** For every number $0 \to n$, search the array. Time: $\mathcal{O}(n^2)$.
2. **Sorting:** Sort the array, then check if `arr[i] == i`. Time: $\mathcal{O}(n \log n)$.
3. **Extra Space:** Use a boolean array `flag[n+1]` to mark seen numbers. Space: $\mathcal{O}(n)$, Time: $\mathcal{O}(n)$.
4. **Math (Optimal):** Calculate the expected sum of first `n` numbers using the formula $\frac{n(n+1)}{2}$. Subtract the sum of the array elements. The difference is the missing number! Time: $\mathcal{O}(n)$, Space: $\mathcal{O}(1)$.

```cpp
int expectedSum = n * (n + 1) / 2;
int actualSum = 0;
for(int x : arr) actualSum += x;
int missing = expectedSum - actualSum;
```

---

## ➕ 3. Plus One (Leetcode 66)

Given a large integer represented as an integer array `digits`, increment it by one. 
*(e.g., `[1, 2, 9, 9] + 1` → `[1, 3, 0, 0]`)*

### 💡 Core Logic
Traverse the array from right to left.
- If the digit is `< 9`, just add 1 and return.
- If the digit is `9`, it becomes `0` (and the carry moves to the left).

```cpp
for(int i = n - 1; i >= 0; i--) {
    if(digits[i] < 9) {
        digits[i]++;
        return digits;
    }
    digits[i] = 0;
}
// If we exit the loop, all digits were 9 (like [9, 9, 9])
// It becomes [1, 0, 0, 0]
digits.insert(digits.begin(), 1); 
```

---

## 🌊 4. Wave Array (GFG)

Sort the array into a wave-like array: $arr[0] \ge arr[1] \le arr[2] \ge arr[3] \ldots$
**Approach:** Sort the array first, then swap adjacent elements `(arr[0] with arr[1], arr[2] with arr[3], etc.)`.

---

### 🛠️ MLOps Perspective: Mathematical Optimization
> [!IMPORTANT]
> The "Missing Number" problem demonstrates a core engineering principle: **Replace iteration with math whenever possible.**
> - Doing $\mathcal{O}(n^2)$ iteration over large datasets takes hours. Using the Gauss formula $\frac{n(n+1)}{2}$ brings it to milliseconds. 
> - In Machine Learning, this is exactly what happens when you replace manual nested loops over datasets with **vectorized matrix operations** using Linear Algebra math. Instead of iterating over weights and inputs manually, matrix multiplication computes it all at once mathematically.

---

<div align="center">

⬅️ [Previous: Arrays Part 3](./Arrays3.md) &nbsp;&nbsp;|&nbsp;&nbsp; ➡️ [Next: Basic Sorting Algorithms](./BasicSortingAlgos_1.md)

</div>
