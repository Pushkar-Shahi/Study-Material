<div align="center">

# <span style="color:#D4A017">🟡 Phase 3 — Loops</span>

![Phase](https://img.shields.io/badge/Phase-3-D4A017) ![Theme](https://img.shields.io/badge/Theme-Yellow_%E2%80%94_Repetition-D4A017)

</div>

---

## 🔁 The `for` Loop

Has **three main parts**:

| Part | Role | Example |
|---|---|---|
| Initialization | Starting value | `int i = 1` |
| Condition | Checked each round | `i <= 100` |
| Increment | Updates after each round | `i++` |

```cpp
for (int i = 1; i <= 100; i++) {
    cout << i << " ";
}
```

---

## 🔄 `while` vs. `do-while`

| Loop | Best For | Checks Condition |
|---|---|---|
| `while` | Unknown number of iterations | **Before** running the code |
| `do-while` | Guarantee at least 1 run | **After** running the code |

```cpp
// while
int i = 1;
while (i <= 5) {
    cout << i;
    i++;
}

// do-while — always runs at least once
int j = 1;
do {
    cout << j;
    j++;
} while (j <= 5);
```

---

## 🎮 Loop Control Keywords

| Keyword | Effect |
|---|---|
| `break` | Immediately stops and exits the loop |
| `continue` | Skips the rest of this round, jumps to the next |

---

## 💡 Common Practice Problems

- 📋 Printing multiplication tables (e.g., table of 19)
- 🔢 Counting digits in a number
- 🔍 Checking if a number is prime

---

## 📝 Summary Table

| Concept | Purpose |
|---|---|
| `for` | Repeat a known number of times |
| `while` | Repeat while a condition holds (checked first) |
| `do-while` | Same as while, but runs at least once |
| `break` / `continue` | Control loop flow |

---

### 🛠️ MLOps Perspective: Loops in Training & Pipelines
> [!NOTE]
> Loops are the engine behind model training and data processing:
> - **Training epochs:** `for (int epoch = 1; epoch <= max_epochs; epoch++)` — every deep learning training loop is a for loop
> - **Batch processing:** Iterating over mini-batches of data is a nested loop — outer loop over epochs, inner loop over batches
> - **`break` = Early Stopping:** The most common regularization trick in ML — monitor validation loss and `break` out of the training loop when it stops improving
> - **`while` = Retry Logic:** In MLOps pipelines, `while (!success && retries < max_retries)` wraps flaky API calls to cloud services

---

<div align="center">

⬅️ [Previous: Phase 2 — Conditionals](./02_conditionals.md) &nbsp;&nbsp;|&nbsp;&nbsp; 🗺️ [Roadmap](./00_README.md) &nbsp;&nbsp;|&nbsp;&nbsp; ➡️ [Next: Phase 4 — Pattern Printing](./04_pattern_printing.md)

</div>
