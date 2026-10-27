<div align="center">

# <span style="color:#E74C3C">🟥 Level 17: Array Algorithms and Dictionaries</span>
![Level](https://img.shields.io/badge/Level-17-E74C3C) ![Theme](https://img.shields.io/badge/Theme-Algorithms-E74C3C) ![Python](https://img.shields.io/badge/Python-dict-3776AB)

</div>

## ✅ 0. Already Covered
Second-largest distinct element and "move zeros to the end" were marked **done** in this lecture; see [Level 15](15_functional_programming_basics.md).

## 🔢 1. Find the Missing Number (1 to n)
Input `arr = [1, 2, 4, 5, 6]`, `n = 6` → `3`.

```python
# Approach 1: sum formula
def find_missing(arr, n):
    expected_sum = n * (n + 1) // 2      # 1 + 2 + ... + n
    actual_sum = sum(arr)
    return expected_sum - actual_sum

# Approach 2: check each number
def find_missing(arr, n):
    for i in range(1, n + 1):
        if i not in arr:
            return i
```

| Approach | Idea | Note |
|----------|------|------|
| Sum formula | expected total − actual total | one pass over `arr`, no inner search |
| `i not in arr` | test each of 1..n | `in` scans the list each time |

> ⚠️ Approach 2 returns `None` if nothing is missing.

## 🎯 2. Two Numbers Equal to a Target
Input `[2, 7, 11, 15]`, target `9` → `[0, 1]`.

```python
def two_sum(arr, target):
    seen = {}                              # value -> index
    for i, num in enumerate(arr):
        required = target - num            # x + y = z  ->  y = z - x
        if required in seen:
            return [seen[required], i]
        seen[num] = i
    return []
```

| Step | What happens |
|------|--------------|
| 1 | for each `num`, compute the partner `required = target - num` |
| 2 | if the partner was **already seen**, return both indexes |
| 3 | otherwise remember `num` with its index |

> 💡 The dictionary gives instant lookup (`required in seen`) instead of a second loop. `return []` covers the no-pair case.

## 🔢 3. `enumerate`

```python
fruits = {"Apple", "Banana", "Pineapple"}
for ind, f in enumerate(fruits):
    print(ind, f)
# 0 Pineapple
# 1 Banana
# 2 Apple
```

> ⚠️ `fruits` is a **set**, so its order is arbitrary and may differ from how you typed it (the output above starts with `Pineapple`). `enumerate` just numbers whatever order it receives. Use a list for a fixed order.

## 🔀 4. Merge Two Sorted Arrays (two pointers)
Input `[1, 4, 7, 9]` and `[2, 3, 8, 10]` → `[1, 2, 3, 4, 7, 8, 9, 10]`, **without** sorting the combined list.

```python
def merge_sorted_arrays(a, b):
    i = 0
    j = 0
    result = []
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            result.append(a[i]); i += 1
        else:
            result.append(b[j]); j += 1
    while i < len(a):          # leftovers from a
        result.append(a[i]); i += 1
    while j < len(b):          # leftovers from b
        result.append(b[j]); j += 1
    return result
```

| Pointer | Meaning |
|---------|---------|
| `i` | next unused position in `a` |
| `j` | next unused position in `b` |

> 💡 Each step takes the smaller front element. Using `<=` keeps equal values stable (takes from `a` first).

## 🧭 Summary Table

| Concept | Purpose |
|---------|---------|
| `n*(n+1)//2` | Expected sum of 1..n |
| `dict` as lookup (`seen`) | Remember what you've met, find partners fast |
| `enumerate(x)` | Index and value together |
| Two pointers | Merge sorted data in one pass |

## 📝 Practice

1. Second-largest **distinct** element, printing a message if it doesn't exist (`[5, 5, 5]`). 
   > 💡 Hint: reuse the two-variable loop from Level 15 and test `if second_largest == float('-inf')`. Use `elif num > second_largest and num != largest` for distinct values.

---
⬅️ [Previous](16_list_comprehensions.md) | 🏠 [Roadmap](00_README.md) | ➡️ [Next: String Algorithms](18_string_algorithms.md)
