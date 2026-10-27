<div align="center">

# <span style="color:#D4AC0D">🟨 Level 15: Functional Programming Basics</span>
![Level](https://img.shields.io/badge/Level-15-F1C40F) ![Theme](https://img.shields.io/badge/Theme-Functions-E74C3C) ![Python](https://img.shields.io/badge/Python-no_NumPy-3776AB)

</div>

## 🧭 1. The Big Ideas (lecture outline)

| # | Idea | Covered with code? |
|:-:|------|:------------------:|
| 1 | Functions are treated as **values** | ✅ |
| 2 | Functions can be passed as **parameters** | ✅ |
| 3 | Functions can **return** other functions | ➖ listed only |
| 4 | `lambda` (one-line functions) | ➖ listed only |
| 5 | `filter()` (keep items by a criterion) | ➖ listed only |
| 6 | `reduce()` (combine values into one) | ➖ listed only |

## 🧩 2. Functions as Values

```python
def hello():
    print("Hello")

hello       # the function object itself (not called)
hello()     # calls it -> Hello
a = hello   # another name for the same function
a()         # Hello
```

| Expression | Meaning |
|------------|---------|
| `hello` | the function (a value) |
| `hello()` | **calls** the function |
| `a = hello` | `a` now refers to that function |

## 📨 3. Passing a Function as an Argument

```python
def cube(x):   return x**3
def square(x): return x**2

def call_func(f, n):
    return f(n)

call_func(square, 4)   # 16
call_func(cube, 5)     # 125
```

## 🔝 4. Higher-Order Functions (HOF)
A HOF **accepts a function** as an argument and/or **returns** one.

```python
def add(a, b): return a + b
def mul(a, b): return a * b

def operation(f, a, b):
    return f(a, b)

operation(add, 3, 5)   # 8
operation(mul, 3, 5)   # 15
```

> 💡 Pass the function **name without parentheses** (`add`, not `add(...)`).

## 🧮 5. Classic List Problems (loops, no built-ins)

| Problem | Idea | Key code | Result |
|---------|------|----------|--------|
| Largest without `max()` | start from first item, keep bigger | `largest = numbers[0]` | `89` for `[12,45,7,89,34]` |
| Second largest, no sorting | track two values | see below | `45` for `[10,45,20,78,34]` |
| Unique, keep order | add only if not yet in result | `if num not in unique` | `[10,20,30,40]` |
| Zeros to the end | collect non-zeros, count zeros, append zeros | `zero_count += 1` | `[5,3,8,2,0,0,0]` |
| Above average (no NumPy) | total → average → filter | `total / len(numbers)` | `[40, 50]` |
| Split positives/negatives | `if num > 0 … elif num < 0` (zero ignored) | two lists | `[10,8,12]` / `[-5,-3,-7]` |
| Common elements | `if num in list2` | | `[30, 40]` |
| In first but not second | `if e not in m` | | `[10, 30]` |

### Second largest in one pass
```python
largest = float('-inf')
second_largest = float('-inf')
for num in numbers:
    if num > largest:
        second_largest = largest      # old max becomes second
        largest = num
    elif num > second_largest:
        second_largest = num
```

> ⚠️ **Initialization gotcha:** start from `numbers[0]` (or `-inf`), never `0`, or all-negative lists give wrong answers (same lesson as the NumPy min/max loops).

### Zeros to the end
```python
result, zero_count = [], 0
for num in numbers:
    if num == 0: zero_count += 1
    else:        result.append(num)
for i in range(zero_count):
    result.append(0)
```

> ⚠️ Name clash alert: if you assigned `range = ...` earlier (as in the price-change example), this `range(...)` call will fail.

## 🧭 Summary Table

| Concept | Purpose |
|---------|---------|
| Function as value | Store/rename/pass a function |
| `f(n)` inside another function | Apply caller-chosen behavior |
| HOF `operation(f, a, b)` | One routine, many operations |
| `x not in lst` / `x in lst` | Uniqueness and set-like checks |
| Track-two-values loop | Second largest without sorting |

## 📝 Practice

1. Check whether a list is sorted ascending, **without** `sort()`/`sorted()` (`[10,20,30,40]` → `Sorted`, `[10,30,20,40]` → `Not Sorted`). 
   > 💡 Hint: compare each element with the next; if any `lst[i] > lst[i+1]`, it's not sorted.
2. Write a function that **returns** another function (idea #3 above). 
   > 💡 Hint: define an inner `def` inside the outer function and `return` its name without `()`.

<span style="color:gray">*Coming Next (listed in the outline, not demonstrated in the source): `lambda`, `filter()` and `reduce()`.*</span>

---
⬅️ [Previous](14_student_placement_case_study.md) | 🏠 [Roadmap](00_README.md) | ➡️ [Next: List Comprehensions](16_list_comprehensions.md)
