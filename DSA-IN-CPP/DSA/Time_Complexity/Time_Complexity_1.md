<div align="center">

# <span style="color:#008B8B">🩵 Time Complexity — Part 1 (Fundamentals)</span>

![Section](https://img.shields.io/badge/Concept-Time_Complexity-008B8B) ![Language](https://img.shields.io/badge/Language-C++-00599C?logo=c%2B%2B&logoColor=white)

</div>

---

## 🤔 1. Why Do We Need Time Complexity?

When you write a solution that works correctly, the next question is: **"Is it fast enough?"**
Time Complexity gives us a way to measure and compare the *efficiency* of algorithms — how their runtime grows as input size `n` grows.

> [!IMPORTANT]
> Time Complexity is **NOT** the actual time in seconds. It's a mathematical description of growth rate, independent of hardware.

---

## 📐 2. Big-Oh Notation O(...)

We use **Big-Oh (O)** to express the **worst-case** (upper bound) of an algorithm's runtime.

**Common Complexities (fastest → slowest):**

| Notation | Name | Example |
|---|---|---|
| $\mathcal{O}(1)$ | Constant | Accessing `arr[i]` |
| $\mathcal{O}(\log n)$ | Logarithmic | Binary Search |
| $\mathcal{O}(\sqrt{n})$ | Square Root | `for(i=1; i*i <= n; i++)` |
| $\mathcal{O}(n)$ | Linear | Single loop |
| $\mathcal{O}(n \log n)$ | Linearithmic | Merge Sort |
| $\mathcal{O}(n^2)$ | Quadratic | Nested loops |
| $\mathcal{O}(2^n)$ | Exponential | Recursive subsets |

---

## 🔍 3. Worked Examples — Single Loops

### Q: Basic Loop → $\mathcal{O}(n)$
```cpp
for(int i = 1; i <= n; i++) {
    cout << "Ishan";
}
// Runs n times → TC = O(n)
```

### Q: Increment by 2 → $\mathcal{O}(n)$
```cpp
for(int i = 1; i <= n; i += 2) {
    cout << "Sahil";
}
// Runs n/2 times → TC = O(n/2) = O(n) (constants are dropped)
```

### Q: Fixed upper limit → $\mathcal{O}(1)$
```cpp
for(int i = 1; i <= 10; i++) {
    cout << "Ansh";
}
// Runs exactly 10 times regardless of n → TC = O(10) = O(1)
```

### Q: Loop runs `n - 7` times → $\mathcal{O}(n)$
```cpp
for(int i = 1; i <= n - 7; i++) {
    cout << "Aditi";
}
// Runs n-7 times → TC = O(n-7) = O(n) (constants are subtracted/added, ignored)
```

> [!TIP]
> **Key Rules for simplification:**
> 1. Drop constants: $\mathcal{O}(n/2) = \mathcal{O}(n)$
> 2. Drop lower-order terms: $\mathcal{O}(n^2 + n) = \mathcal{O}(n^2)$

---

## 🔢 4. Two Independent Loops → Addition Rule

```cpp
for(int i = 1; i <= n; i++) { ... }  // O(n)
for(int i = 1; i <= m; i++) { ... }  // O(m)
// Total TC = O(n + m) = O(max(n, m))
```

---

## 🔲 5. Nested Loops → Multiplication Rule

### Square Matrix (m × n)
```cpp
for(int i = 1; i <= m; i++) {
    for(int j = 1; j <= n; j++) {
        cout << "Hattori";
    }
}
// TC = O(m * n). For square matrix: O(n^2)
```

### Triangular Nested Loop
```cpp
for(int i = 1; i <= n; i++) {
    for(int j = 1; j <= i; j++) {
        cout << "Bhumi";
    }
}
// Iterations = 1 + 2 + 3 + ... + n = n*(n+1)/2
// TC = O(n^2)
```

> [!NOTE]
> **Homework:** For `for(int i = 1; i <= n; i++) { for(int j = i+1; j <= n; j++) {...} }` → Answer: $\mathcal{O}(n^2)$

---

### 🛠️ MLOps Perspective: Big-Oh in Production Systems
> [!IMPORTANT]
> In ML Engineering, choosing the right algorithm's time complexity directly determines whether your pipeline is viable at scale:
> - An $\mathcal{O}(n^2)$ algorithm on $n = 1,000,000$ records performs **1 trillion operations** — roughly 11 days on a 100M ops/sec machine.
> - An $\mathcal{O}(n \log n)$ algorithm on the same data performs only **20 million operations** — under a second.
> - This is why ML engineers obsessively benchmark and profile pipeline steps and use efficient vectorized operations (NumPy, Spark, Arrow) instead of Python `for` loops.

---

<div align="center">

➡️ [Next: Time Complexity Part 2](./Time_Complexity_2.md)

</div>
