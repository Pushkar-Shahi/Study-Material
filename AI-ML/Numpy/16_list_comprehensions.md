<div align="center">

# <span style="color:#E67E22">🟧 Level 16: List Comprehensions</span>
![Level](https://img.shields.io/badge/Level-16-E67E22) ![Theme](https://img.shields.io/badge/Theme-Comprehensions-8E44AD) ![Python](https://img.shields.io/badge/Python-lists-3776AB)

</div>

## 🧱 1. Basic Form: `[expression for item in iterable]`

| Loop version | Comprehension |
|--------------|---------------|
| `sq = []`<br>`for e in numbers: sq.append(e**2)` | `[e**2 for e in numbers]` |

| Task | Code | Result |
|------|------|--------|
| Squares | `[e**2 for e in [1,2,3,4,5]]` | `[1, 4, 9, 16, 25]` |
| ×5 | `[n*5 for n in numbers]` | `[5, 10, 15, 20, 25]` |
| +5 bonus | `[n+5 for n in marks]` | `[6, 7, 8, 9, 10]` |
| °C → °F | `[(9/5)*c + 32 for c in celsius]` | `[32.0, 50.0, 68.0, 86.0, 104.0]` |
| Uppercase | `[name.upper() for name in names]` | `['AMIT','NEHA','RAHUL','PRIYA']` |
| Drop decimals | `[int(p) for p in [100.50, 250.75, 399.99, 120.25]]` | `[100, 250, 399, 120]` |
| Sum per cart | `[sum(c) for c in carts]` | `[400, 700, 600]` |

> 💡 `int()` **truncates** toward zero (same as floor for positive prices).

## 🔍 2. Filtering: `[expr for x in it if condition]`

```python
[n for n in numbers if n % 2 == 0]                    # [2, 4, 6, 8]
[n for n in [15,60,45,90,35,75] if n > 50]            # [60, 90, 75]
[w for w in words if len(w) >= 5]                     # ['elephant', 'giraffe']
[n**2 for n in numbers if n % 2 == 0]                 # squares of evens: [4, 16, 36, 64]
[n[0] for n in names if len(n) >= 4]                  # ['A','N','C','P']
[e for e in list1 if e in list2]                      # common: [30, 40]
[emp["name"] for emp in employees if emp["sales"] >= 50000]   # ['Aman','Karan','Neha']
```

> 📌 The `if` at the **end** *filters* (drops items). The employees example loops over a **list of dictionaries**.

## 🔀 3. If-Else Inside: `[a if cond else b for x in it]`

| Rule | Position of `if` |
|------|------------------|
| Filter (drop items) | **after** `for` |
| Choose between two values | **before** `for`, with `else` (mandatory) |

```python
["Even" if n % 2 == 0 else "Odd" for n in numbers]       # ['Odd','Even',…]
[n if n >= 0 else 0 for n in [-5,10,-3,8,-1,15]]         # [0, 10, 0, 8, 0, 15]
["Hot" if t >= 35 else "Normal" for t in temperatures]   # [22,36,30,40,28,35] -> Normal,Hot,Normal,Hot,Normal,Hot
[p*0.9 if p >= 1000 else p for p in [500,1200,800,2500,1500]]   # [500, 1080.0, 800, 2250.0, 1350.0]
[p*1.18 if p > 1000 else p*1.05 for p in prices]         # tax 18% / 5%
```

> ⚠️ Mixed results are normal: unchanged items stay `int` (`500`), changed items become `float` (`1080.0`).

### Three or more categories (chain `else if`)

```python
grades = ["Distinction" if m >= 80
          else "Pass" if m >= 40
          else "Fail"
          for m in marks]          # [95,72,38,81,45,29] -> Distinction,Pass,Fail,Distinction,Pass,Fail

bonuses = [s*0.20 if s >= 80000
           else s*0.10 if s >= 50000
           else s*0.05
           for s in salaries]      # [90000,65000,40000,100000,50000] -> [18000.0, 6500.0, 2000.0, 20000.0, 5000.0]

category = ["Free Express Shipping" if v >= 2000
            else "Free Standard Shipping" if v >= 1000
            else "Shipping Fee Applicable"
            for v in orders]
```

> 💡 Same logic as nested `np.where`, but for plain Python lists.

## 🔁 4. Nested Loops: `[expr for a in A for b in B]`
The **first** `for` is the outer loop.

```python
[(n1, n2) for n1 in [1,2,3] for n2 in [10,20]]
# [(1,10),(1,20),(2,10),(2,20),(3,10),(3,20)]

[[c, s] for c in colors for s in sizes]                 # 3x3 = 9 colour/size combos
[(a,b,c) for a in digits for b in digits for c in digits]   # 27 triples
[(a,b,c) for a in digits for b in digits for c in digits
 if a != b and b != c and a != c]                       # 6 all-different triples
```

| Task | Code | Result |
|------|------|--------|
| Pairs with sum > 12 | `[(n1,n2) for n1 in nums1 for n2 in nums2 if n1+n2 > 12]` | `[(1,20),(2,20),(3,10),(3,20)]` |
| Different numbers 1–5 with even product | `if n1 != n2 and n1*n2 % 2 == 0` | 14 pairs |
| Vowels from words | `[c for w in words for c in w if c in "aeiou"]` | `['e','u','a','i','o','o','a','a','i']` |

### Flattening a 2D list

```python
marks = [[75,80,90],[60,85,70],[95,88,92]]
[e for r in marks for e in r]                # [75,80,90,60,85,70,95,88,92]
[e for r in marks for e in r if e >= 75]     # [75,80,90,85,95,88,92]
[e + 5 for r in marks for e in r]            # [80,85,95,65,90,75,100,93,97]
```

> ⚠️ **Result is flat:** "replace negatives with zero in a matrix" using `[e if e>=0 else 0 for r in data for e in r]` returns a **1D list** `[10,0,20,0,15,0,25,0,12]`, not a 3×3 matrix. To keep rows you'd need an inner comprehension per row (not shown in the source).

> 💡 Read nested comprehensions **left to right** as the equivalent nested `for` loops. The nested-loop print version of the 3-digit example confirms the order.

## 🧭 Summary Table

| Syntax | Purpose |
|--------|---------|
| `[f(x) for x in L]` | Transform every item |
| `[x for x in L if c]` | Filter items |
| `[a if c else b for x in L]` | Per-item choice (keeps all items) |
| `a if c1 else b if c2 else d` | 3+ categories |
| `[… for a in A for b in B]` | Combinations / flattening |

## 📝 Practice (HW, no solution in source)

1. Convert full names into lowercase usernames joined by a dot: `["Aman Sharma","Riya Verma","Karan Patel"]` → `aman.sharma`, … 
   > 💡 Hint: lowercase the name, then replace the space with a dot (string methods).
2. Unique values keeping first-appearance order for `[4, 2, 4, 7, 2, 9, 7, 10]` (loop version appears in [Level 15](15_functional_programming_basics.md)). 
   > 💡 Hint: expected `[4, 2, 7, 9, 10]`; a comprehension needs a way to check what's been seen so far, so the loop version is simpler.

---
⬅️ [Previous](15_functional_programming_basics.md) | 🏠 [Roadmap](00_README.md) | ➡️ [Next: Array Algorithms and Dictionaries](17_array_algorithms_and_dictionaries.md)
