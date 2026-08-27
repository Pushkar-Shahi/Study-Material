<div align="center">

# <span style="color:#008B8B">🩵 Time Complexity — Part 2 (Logarithmic & Tricky Cases)</span>

![Section](https://img.shields.io/badge/Concept-Time_Complexity-008B8B) ![Language](https://img.shields.io/badge/Language-C++-00599C?logo=c%2B%2B&logoColor=white)

</div>

---

## 📊 Complexity Ranking (Revisited)

```
O(1) < O(log n) < O(√n) < O(n) < O(n log n) < O(n²) < O(2^n)
```

---

## 🔬 1. Logarithmic Loops: `i *= 2` → $\mathcal{O}(\log n)$

When `i` doubles each time (`i *= 2`), it takes only $\log_2 n$ iterations to reach `n`.

```cpp
for(int i = 1; i <= n; i *= 2) {
    cout << "Tousif";
}
// i = 1, 2, 4, 8, 16, ... , n
// i = 2^0, 2^1, 2^2, ..., 2^k where 2^k = n → k = log₂n
// TC = O(log n)
```

> [!TIP]
> **Why?** If `n = 2^k`, then after `k` iterations, `i` exceeds `n`. So `k = log₂n` iterations.

### Homework: `i += i` → $\mathcal{O}(\log n)$
```cpp
for(int i = 1; i <= n; i += i) { ... }
// Same as i *= 2! → TC = O(log n)
```

---

## 🔬 2. Square Root Loop: `i*i <= n` → $\mathcal{O}(\sqrt{n})$

```cpp
for(int i = 1; i * i <= n; i++) {
    cout << "Amit";
}
// Loop runs while i² ≤ n → i runs from 1 to √n
// TC = O(√n)
```

---

## 🔬 3. Nested Loop with Logarithmic Outer: `O(n log n)`

```cpp
for(int i = 1; i <= n; i *= 2) { // O(log n) outer iterations
    for(int j = 1; j <= n; j++) { // O(n) inner iterations each time
        cout << "Jatin";
    }
}
// TC = O(log n) × O(n) = O(n log n)
```

---

## 🔬 4. Nested Logarithmic: Sum of Powers of 2 → $\mathcal{O}(n)$

```cpp
for(int i = 1; i <= n; i *= 2) {
    for(int j = 1; j <= i; j++) {
        cout << "Dilnawaz";
    }
}
// Outer i = 1, 2, 4, 8, ... n
// Inner runs: 1 + 2 + 4 + 8 + ... + n = 2n - 1 ≈ O(n)
// (Sum of geometric series: a(r^k - 1)/(r-1) where a=1, r=2)
```

> [!NOTE]
> This is a classic tricky question! Even though it has a nested loop, the total iterations sum to $2n - 1$, making it $\mathcal{O}(n)$.

---

## 🔬 5. Doubly Logarithmic: `i *= i` → $\mathcal{O}(\log \log n)$

```cpp
for(int i = 2; i <= n; i *= i) {
    cout << "Raghav";
}
// i = 2, 4, 16, 256, 65536, ...
// i = 2^(2^0), 2^(2^1), 2^(2^2), 2^(2^3)...
// Runs about log₂(log₂n) times → TC = O(log log n)
```

---

## 🎯 6. Tricky Cases: `break` and `continue`

### Loop with `break` after one inner iteration → $\mathcal{O}(n)$
```cpp
for(int i = 0; i < n; i++) {
    for(int j = 0; j < n; j++) {
        cout << i;
        break; // Exits inner loop after just 1 iteration every time!
    }
}
// Inner loop always runs just ONCE per outer iteration
// TC = O(n × 1) = O(n)
```

### Loop with `continue` → $\mathcal{O}(n^2)$
```cpp
for(int i = 0; i < n; i++) {
    for(int j = 0; j < n; j++) {
        continue; // Just skips to next iteration, doesn't exit loop
    }
}
// continue doesn't reduce iterations! TC = O(n²)
```

> [!WARNING]
> `break` **exits** the loop early — reduces total iterations.
> `continue` **skips** the rest of the current iteration but the loop still runs the same number of times.

---

## 📝 7. Special: `while(j < n)` Outside Outer Loop → $\mathcal{O}(n)$

```cpp
int j = 0;
for(int i = 0; i < n; i++) {
    while(j < n) {
        cout << j;
        j++; // j is NEVER reset inside the outer loop
    }
}
// j only increments n times in total (across all outer iterations)
// TC = O(n), NOT O(n²)!
```

> [!IMPORTANT]
> This is a classic interview trick. Because `j` is defined **outside** the `for` loop and never reset, the `while` loop across all outer iterations only runs `n` times total.

---

## 📋 8. Summary of Common Patterns

| Loop Pattern | TC |
|---|:---:|
| `for(i=1; i<=n; i++)` | $\mathcal{O}(n)$ |
| `for(i=1; i<=n; i+=2)` | $\mathcal{O}(n)$ |
| `for(i=1; i<=10; i++)` | $\mathcal{O}(1)$ |
| `for(i=1; i*i<=n; i++)` | $\mathcal{O}(\sqrt{n})$ |
| `for(i=1; i<=n; i*=2)` | $\mathcal{O}(\log n)$ |
| Nested: outer `O(n)`, inner `O(n)` | $\mathcal{O}(n^2)$ |
| Nested: outer `O(log n)`, inner `O(n)` | $\mathcal{O}(n \log n)$ |
| Nested: outer `i*=2`, inner `j<=i` | $\mathcal{O}(n)$ |
| `for(i=2; i<=n; i*=i)` | $\mathcal{O}(\log \log n)$ |
| Nested loop with inner `break` | $\mathcal{O}(n)$ |

---

### 🛠️ MLOps Perspective: Time Complexity in Real ML Systems
> [!IMPORTANT]
> Understanding these complexity classes is how MLOps engineers design scalable systems:
> - **$\mathcal{O}(\log n)$ is the goal for search:** Vector database lookups (HNSW index in Qdrant or Weaviate) aim for $\mathcal{O}(\log n)$ retrieval so that your RAG chatbot doesn't slow down as your document store grows from 10K to 10M documents.
> - **`break` trick:** This mirrors **early stopping** logic in ML training. If a model stops improving, you `break` out of the training loop early — reducing total compute time from $\mathcal{O}(\text{epochs})$ to much less.
> - **The `j` outside loop trick:** This is how efficient **streaming data processors** work. A pointer `j` into a data stream advances monotonically — processing each record exactly once total, giving $\mathcal{O}(n)$ instead of $\mathcal{O}(n^2)$.

---

<div align="center">

⬅️ [Previous: Time Complexity Part 1](./Time_Complexity_1.md)

</div>
