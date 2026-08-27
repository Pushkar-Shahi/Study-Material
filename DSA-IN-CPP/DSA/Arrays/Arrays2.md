<div align="center">

# <span style="color:#1E6FEB">🟦 Arrays — Part 2 (Memory & Pointers)</span>

![Section](https://img.shields.io/badge/Data_Structure-Arrays-1E6FEB) ![Language](https://img.shields.io/badge/Language-C++-00599C?logo=c%2B%2B&logoColor=white)

</div>

---

## 💾 1. Memory Allocation in Arrays

Arrays are stored in **contiguous (continuous) memory locations**. 
Because the memory blocks are right next to each other, accessing any element using its index `arr[i]` takes **$\mathcal{O}(1)$ time**.

If an integer takes 4 bytes of memory, and the first element is at memory address `x500`:
- `arr[0]` is at `x500`
- `arr[1]` is at `x504`
- `arr[2]` is at `x508`
- `arr[3]` is at `x512`

---

## 🏷️ 2. Array Addresses & Pointers

In C++, the name of the array itself (e.g., `arr`) acts as a **pointer** to the first element of the array.

```cpp
int arr[] = {8, 4, 1, 3};

// Both of these print the exact same memory address:
cout << &arr[0] << endl; 
cout << arr << endl;     
```

Because `arr` is just a memory address, `arr[i]` is actually converted by the compiler into pointer arithmetic: `*(arr + i)`.

---

## 🔄 3. Passing Arrays to Functions

When you pass a standard variable to a function, C++ passes a *copy* of the value (Pass by Value). 
However, **arrays are always passed by reference (specifically, a pointer to the first element).**

### Why?
Copying a 10,000-element array into a function would be extremely slow and waste memory. Instead, C++ just hands the function the starting memory address.

### Example:
```cpp
void change(int y[]) {
    y[0] = 20; // Modifies the original array in memory!
}

int main() {
    int x[] = {6, 1, 2};
    change(x);
    cout << x[0]; // Prints 20, NOT 6!
}
```

> [!WARNING]
> Because arrays decay into pointers when passed to functions, the function **loses the size** of the array. You cannot use `sizeof(y)/sizeof(y[0])` inside the function. You must always pass the `size` as a second parameter!
> `void printArray(int arr[], int size)`

---

## 🧠 4. Concept Check (True/False)

| Statement | Answer | Explanation |
|---|:---:|---|
| `int num[26]` has 26 elements. | ✅ True | Indices `0` through `25`. |
| `num[1]` is the first element. | ❌ False | `num[0]` is the first. `num[1]` is the second. |
| You must initialize an array when declaring it. | ❌ False | `int arr[5];` is completely valid. |
| `num[27]` designates the 28th element. | ✅ True | Since it starts at `0`, index `27` is element 28. (Though it's out of bounds for `num[26]`). |

---

### 🛠️ MLOps Perspective: Pointers & Contiguous Memory
> [!IMPORTANT]
> The concepts of memory addresses and passing arrays by reference are crucial when writing custom C++/CUDA extensions for deep learning frameworks (like PyTorch or TensorFlow):
> - When PyTorch passes a tensor to a custom C++ layer, it doesn't copy the gigabytes of model weights. It passes a pointer to the contiguous block of GPU/CPU memory (exactly like `change(int y[])`).
> - Understanding that elements are stored contiguously (separated by a "stride") is how you correctly navigate matrix dimensions in low-level AI code.

---

<div align="center">

⬅️ [Previous: Arrays Part 1](./Arrays1.md) &nbsp;&nbsp;|&nbsp;&nbsp; ➡️ [Next: Arrays Part 3](./Arrays3.md)

</div>
