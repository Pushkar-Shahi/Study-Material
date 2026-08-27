<div align="center">

# <span style="color:#1E6FEB">🟦 Arrays — Part 3 (Vectors & Two Pointers)</span>

![Section](https://img.shields.io/badge/Data_Structure-Vectors-1E6FEB) ![Language](https://img.shields.io/badge/Language-C++-00599C?logo=c%2B%2B&logoColor=white)

</div>

---

## 📈 1. Introduction to Vectors (Dynamic Arrays)

Standard C++ arrays have a fixed size. If you declare `int arr[5]`, you cannot add a 6th element.
**Vectors** are dynamic arrays that can grow or shrink in size automatically.

### Internal Working (Size vs Capacity)
When a vector runs out of space, it creates a new array in memory with **double the capacity**, copies the old elements over, and adds the new one.
- **Size:** How many elements are currently in the vector.
- **Capacity:** How much total space is currently allocated in memory.

> [!NOTE]
> Because it doubles in size, the *amortized* Time Complexity of `push_back()` is $\mathcal{O}(1)$.

---

## 🛠️ 2. Vector Operations

```cpp
#include <vector>

vector<int> v;
v.push_back(5);    // Adds 5 to the end
v.push_back(9);
v.pop_back();      // Removes the last element (9)
v.size();          // Returns current number of elements
v.capacity();      // Returns total allocated space
v.at(0);           // Safer way to access v[0]
```

### Passing Vectors to Functions
Unlike arrays (which pass by reference automatically), **vectors are passed by value by default**. 
To avoid copying the entire vector and to modify the original, pass by reference using `&`:
```cpp
void modifyVector(vector<int>& v) { ... }
```

---

## 🏃‍♂️ 3. The Two-Pointer Technique

Using two pointers (`i` and `j`) starting at opposite ends of the array to solve problems in $\mathcal{O}(n)$ time without extra space.

### Reverse an Array
```cpp
int i = 0, j = n - 1;
while(i < j) {
    int temp = arr[i];
    arr[i] = arr[j];
    arr[j] = temp;
    i++;
    j--;
}
```

### Segregate 0s and 1s
Given `[0, 1, 0, 1, 1, 0]`, sort it so 0s are on the left and 1s on the right.
- **Method 1:** Count the number of 0s. Loop again and fill the first `count` indices with 0, rest with 1.
- **Method 2 (Two Pointers):** `i` starts at 0, `j` starts at end. If `arr[i] == 1` and `arr[j] == 0`, swap them. Move `i` right and `j` left.

---

## 🔄 4. Rotate Array (Leetcode 189)

Rotate an array to the right by `k` steps.
Example: `[1, 2, 3, 4, 5, 6, 7]`, `k = 3` → Output: `[5, 6, 7, 1, 2, 3, 4]`

> [!TIP]
> If $k > n$, rotating by $k$ is the same as rotating by $k \% n$.

**Optimal $\mathcal{O}(n)$ Approach (No Extra Space):**
1. Reverse the first $n - k$ elements.
2. Reverse the last $k$ elements.
3. Reverse the entire array.

---

## 💡 5. Homework Problems

| Problem | Leetcode | Concept |
|---|---|---|
| **Two Sum** | Leetcode 1 | Find two numbers that add up to target. (Use hash map or sort + two pointers). |
| **Missing Number** | Leetcode 268 | Array has numbers 0 to $n$. Sum of first $n$ natural numbers minus array sum. |
| **Wave Array** | GFG | Sort and swap adjacent elements to form a wave: $a_1 \ge a_2 \le a_3 \ge a_4$. |

---

### 🛠️ MLOps Perspective: Vectors & Preallocation
> [!IMPORTANT]
> The dynamic resizing of C++ Vectors (`push_back`) is identical to Python Lists (`append`). 
> - While doubling the capacity gives an *amortized* $\mathcal{O}(1)$ time, the actual doubling step requires reallocating memory and copying everything.
> - **ML Data Pipelines:** If you are loading 1,000,000 image paths into a list, doing 1,000,000 `appends()` will trigger dozens of memory reallocations, slowing down your script. 
> - Always preallocate space if you know the final size: `vector<int> v(1000000);` (in C++) or `paths = [None] * 1000000` (in Python) to prevent performance bottlenecks during data loading.

---

<div align="center">

⬅️ [Previous: Arrays Part 2](./Arrays2.md) &nbsp;&nbsp;|&nbsp;&nbsp; ➡️ [Next: Arrays Part 4](./Arrays4.md)

</div>
