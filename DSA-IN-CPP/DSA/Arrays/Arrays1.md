<div align="center">

# <span style="color:#2E8B57">📦 Arrays — Part 1 (Fundamentals)</span>

![Section](https://img.shields.io/badge/Data_Structure-Arrays-2E8B57) ![Language](https://img.shields.io/badge/Language-C++-00599C?logo=c%2B%2B&logoColor=white)

</div>

---

## 🤔 1. What is a Data Structure?

In real life, we store different items in different ways (e.g., clothes in a closet, words in a dictionary). Similarly, a Data Structure is a way of organizing and storing data in memory so that it can be accessed and modified efficiently.

An **Array** is the simplest data structure: a collection of items of the **same data type** stored at contiguous memory locations.

---

## 📝 2. Syntax, Initialization & Indexing

```cpp
// 1. Declare without initializing (contains Garbage Values initially)
int arr[4]; 

// 2. Declare and initialize
int marks[] = {74, 96, 91, 57, 62, 35};
```

### Invalid Declarations in C++
- `int a(25);` ❌ (Wrong brackets)
- `int c = {1, 2, 3};` ❌ (Missing `[]`)
- `int size = 10; int b[size];` ✅ (Valid dynamically sized array in modern C++, though standard C++ prefers constants).

### Indexing
Arrays are **0-indexed**. The first element is at index `0`, and the last is at index `n - 1`.

> [!WARNING]
> **Index out of Bound Error:** C++ does not strictly check bounds at compile-time. If you try to print `arr[21]` for a 5-element array, or `arr[-1]`, you might get garbage values or crash the program (Segmentation Fault).

---

## 🏃‍♂️ 3. Basic Traversal & Search

To perform actions on an array, you use loops.

### Sum of Elements
```cpp
int sum = 0;
for(int i = 0; i < n; i++) {
    sum += arr[i];
}
```

### Linear Search
Find if a target integer is present in an array:
```cpp
bool found = false;
for(int i = 0; i < n; i++) {
    if(arr[i] == target) {
        found = true;
        break; // Stop searching once found
    }
}
```

---

## 🏔️ 4. Max / Min Elements

### Maximum Element
```cpp
int mx = INT_MIN; // Smallest possible integer
for(int i = 0; i < n; i++) {
    if(arr[i] > mx) {
        mx = arr[i];
    }
}
```

### Second Maximum Element
A classic interview question. You need two variables.
```cpp
int max = INT_MIN;
int smax = INT_MIN;

for(int i = 0; i < n; i++) {
    if(arr[i] > max) {
        smax = max;      // Old max becomes second max
        max = arr[i];    // New max
    } 
    else if(arr[i] > smax && arr[i] != max) {
        smax = arr[i];   // Update second max only
    }
}
```

---

### 🛠️ MLOps Perspective: Memory Contiguity
> [!IMPORTANT]
> Why do we care about Arrays in Python/ML if Python has Lists?
> - Standard Python `list` is actually an array of pointers, which is terrible for cache performance and math operations.
> - **NumPy Arrays** (`np.array`) are true C-style contiguous arrays (exactly what you're learning here). Because the memory is contiguous, the CPU cache can load chunks of the array instantly, which is why NumPy vector operations are orders of magnitude faster than Python `for` loops!

---

<div align="center">

➡️ [Next: Arrays Part 2](./Arrays2.md)

</div>
