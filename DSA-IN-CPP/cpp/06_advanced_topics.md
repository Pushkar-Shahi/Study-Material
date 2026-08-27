<div align="center">

# <span style="color:#8E44AD">🟣 Phase 6 — Advanced Topics</span>

![Phase](https://img.shields.io/badge/Phase-6-8E44AD) ![Theme](https://img.shields.io/badge/Theme-Purple_%E2%80%94_Power_User_Features-8E44AD)

</div>

---

## 🔀 Function Overloading

Define **multiple functions with the same name**, as long as they have different parameter lists. The compiler picks the right one based on the arguments.

### 1️⃣ Variation in Number of Arguments
```cpp
void print();              // no arguments
void print(int x);          // one argument
void print(int x, int y);    // two arguments
```

### 2️⃣ Variation in Data Types
```cpp
void display(int x);
void display(double x);
void display(char x);
```

### 3️⃣ Variation in Argument Sequence
```cpp
void fun(int x, char ch);   // int first
void fun(char ch, int x);    // char first
```

> [!TIP]
> This avoids needing separate names like `printInt()`, `printDouble()`, etc.

---

## 🧠 Double Pointers

A **double pointer** stores the address of *another pointer* — adding a second level of indirection.

### 🔗 The Hierarchy

| Level | Declaration | Stores |
|---|---|---|
| Variable | `int x = 21;` | The value `21` |
| Single Pointer | `int* ptr = &x;` | Address of `x` |
| Double Pointer | `int** p = &ptr;` | Address of `ptr` |

### 🔍 Dereferencing
```cpp
int x = 21;
int* ptr = &x;
int** p = &ptr;

cout << *p;    // → address of x (dereferences once, gives ptr's value)
cout << **p;   // → 21 (dereferences twice, follows the full chain)
```

---

## 🔺 Pascal's Triangle

A triangular pattern where each value is the **sum of the two numbers directly above it**. Every row starts and ends with `1`.

### 📐 The Math
Value at row `i`, column `j` = combinations formula:

$$_iC_j = \frac{i!}{j! \times (i-j)!}$$

### 🗺️ Visual Pattern (n = 5)
```
1
1 1
1 2 1
1 3 3 1
1 4 6 4 1
1 5 10 10 5 1
```

### ⚙️ Implementation Approach
- Outer loop → tracks the current **row**
- Inner loop → calculates and prints each `iCj` value
- Requires a **factorial function** to compute combinations

---

## 📝 Summary Table

| Concept | Purpose |
|---|---|
| Function Overloading | Same function name, different behavior based on inputs |
| Double Pointer (`**`) | Points to a pointer — two levels of memory indirection |
| Pascal's Triangle | Combines loops + combinations math for a numeric pattern |

---

### 🛠️ MLOps Perspective: Advanced Concepts & Real-World Systems
> [!IMPORTANT]
> These advanced C++ topics connect to the internals of production ML systems:
> - **Function Overloading → Polymorphism in ML:** scikit-learn's `.fit()` and `.predict()` work on many different model types through the same interface — this is polymorphism, the OOP evolution of function overloading
> - **Double Pointers → Multi-dimensional Arrays:** `int**` is a 2D array in disguise. Tensors in TensorFlow and PyTorch are N-dimensional extensions of this concept, stored as contiguous memory with computed index offsets
> - **Pascal's Triangle → Combinatorics in ML:** Combinations (nCr) appear in hyperparameter search spaces — if you have 5 features and want all pairs, that's `5C2 = 10` combinations. Understanding this helps estimate the cost of exhaustive grid search
> - **Double Pointers in Python:** Python's list-of-lists (`[[1,2],[3,4]]`) is the Python equivalent of `int**` — a pointer to pointers

---

<div align="center">

⬅️ [Previous: Phase 5 — Functions & Pointers](./05_functions_pointers.md) &nbsp;&nbsp;|&nbsp;&nbsp; 🗺️ [Roadmap](./00_README.md)

### 🎉 You've completed the full C++ Roadmap!

</div>
