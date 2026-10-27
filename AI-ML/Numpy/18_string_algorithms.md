<div align="center">

# <span style="color:#8E44AD">🟪 Level 18: String Algorithms</span>
![Level](https://img.shields.io/badge/Level-18-8E44AD) ![Theme](https://img.shields.io/badge/Theme-Strings-8E44AD) ![Python](https://img.shields.io/badge/Python-str-3776AB)

</div>

## 🔤 1. String Tools Used

| Tool | Purpose | Example |
|------|---------|---------|
| `s[::-1]` | reverse | `"abc"` → `"cba"` |
| `.lower()` | lowercase | `"Listen"` → `"listen"` |
| `.replace(" ", "")` | remove spaces | |
| `.isalnum()` | letter or digit? | `"A"` ✅, `"3"` ✅, `"@"` ❌ |
| `.split()` | words list | `"a b c"` → `["a","b","c"]` |

## 🪞 2. Palindrome
**Case 1: plain lowercase letters:** compare the string with its reverse.

```python
s = "malayalam"
if s == s[::-1]: print("Yes")     # Yes       ("Aditya" -> No)
```

**Case 2: any characters** (ignore spaces, punctuation, case):

```python
def is_palindrome(text):
    cleaned = ""
    for char in text.lower():
        if char.isalnum():
            cleaned += char
    rev_s = cleaned[::-1]
    if cleaned == rev_s:
        print("Yes")
    else:
        print("No")

is_palindrome("A man, a plan, a canal: Panama")   # cleaned: amanaplanacanalpanama -> Yes
is_palindrome("Hello")                            # hello -> No
```

> 💡 Lowercase first, then keep only `isalnum()` characters, then compare.

## 🔠 3. Anagrams
`"Listen"` and `"Silent"` → same characters, same counts.

```python
def are_anagrams(s1, s2):
    s1 = s1.replace(" ", "").lower()
    s2 = s2.replace(" ", "").lower()
    if len(s1) != len(s2):
        return False
    frequency = {}
    for char in s1:
        frequency[char] = frequency.get(char, 0) + 1     # count
    for char in s2:
        if char not in frequency:
            return False
        frequency[char] -= 1                              # use up
        if frequency[char] < 0:
            return False
    return True

are_anagrams("Listen", "Silent")   # True
are_anagrams("Hello", "World")     # False
```

| Step | Why |
|------|-----|
| Clean spaces/case | the problem says to ignore them |
| Length check | different lengths can't be anagrams |
| Count `s1` in a dict | `get(char, 0) + 1` starts a new count at 0 |
| Subtract for `s2` | a missing key or count below 0 means a mismatch |

> ⚠️ The problem statement shows output `"Yes"`, but the code returns **`True`/`False`**. Print `"Yes" if are_anagrams(...) else "No"` for that format.

## 1️⃣ 4. First Non-Repeating Character

```python
def first_unique_character(text):
    frequency = {}
    for char in text:
        frequency[char] = frequency.get(char, 0) + 1     # pass 1: count
    for char in text:
        if frequency[char] == 1:                          # pass 2: first count of 1
            return char
    return -1

first_unique_character("aabcddee")   # 'b'
first_unique_character("aabb")       # -1
```

> 💡 **Two passes** are needed: count everything first, then scan in the **original order**. The problem's first example `"aabbcddee"` should give `'c'`.

## 📏 5. Longest Word

```python
def longest_word(sentence):
    words = sentence.split()
    if not words:
        return ""
    longest = words[0]
    for word in words[1:]:
        if len(word) > len(longest):       # strict >  -> keeps the FIRST of equals
            longest = word
    return longest

longest_word("Python makes problem solving easier")   # 'problem'
```

| Comparison | Tie behavior | Result for the sample |
|------------|--------------|-----------------------|
| `>` | first longest wins | `problem` |
| `>=` | **last** longest wins | `solving` |

> 💡 "problem" and "solving" both have 7 letters, so only the comparison operator decides the answer.

## 🧭 Summary Table

| Concept | Purpose |
|---------|---------|
| `s[::-1]` | Reverse for palindrome check |
| `isalnum()` + `lower()` | Normalize text |
| Frequency `dict` + `.get(k, 0)` | Count characters |
| Count then scan | First unique character |
| `>` vs `>=` | First vs last in ties |

## 📝 Practice

1. Make `is_palindrome` **return** `True/False` instead of printing, and remove the debug print of `cleaned`. 
   > 💡 Hint: `return cleaned == cleaned[::-1]`.
2. Check anagrams for `"Dormitory"` and `"Dirty room"`. 
   > 💡 Hint: spaces are removed and case ignored by the function.

---
⬅️ [Previous](17_array_algorithms_and_dictionaries.md) | 🏠 [Roadmap](00_README.md)
