<div align="center">

# <span style="color:#8E44AD">🟣 Strings in C++ — Part 2 (Conversion & Advanced Problems)</span>

![Section](https://img.shields.io/badge/Data_Structure-Strings-8E44AD) ![Language](https://img.shields.io/badge/Language-C++-00599C?logo=c%2B%2B&logoColor=white)

</div>

---

## 🔢 1. Integer ↔ String Conversion

### Integer to String
```cpp
int num = 12345;
string s = to_string(num);  // s = "12345"
```

### String to Integer
```cpp
string s = "456";
int num = stoi(s);    // Converts to int   (max ~2.1 billion)
long long l = stoll(s); // Converts to long long (for very large numbers)
```

### `stoi` vs `stoll`

| Function | Return Type | Max Value |
|---|---|---|
| `stoi(s)` | `int` | ~$2.1 \times 10^9$ |
| `stoll(s)` | `long long` | ~$9.2 \times 10^{18}$ |

> [!WARNING]
> If the string represents a number larger than `INT_MAX` (like `"9999999999"`), using `stoi` will cause **integer overflow**. Use `stoll` for large numbers.

---

## 💡 2. Count Digits Without a Loop

```cpp
// Using to_string — converts int to string, then get its length
int n = 12345;
string s = to_string(n);
int digits = s.size(); // 5
```

---

## 🔤 3. Toggle Characters (Upper ↔ Lower Case)

```cpp
for(int i = 0; i < s.size(); i++) {
    if(s[i] >= 'a' && s[i] <= 'z') {
        s[i] = s[i] - 'a' + 'A'; // lowercase to uppercase
    } else {
        s[i] = s[i] - 'A' + 'a'; // uppercase to lowercase
    }
}
// Or simply using XOR: s[i] ^= 32; (toggles the 6th bit)
```

---

## 🔤 4. Sorting a String

Strings can be sorted alphabetically using the built-in sort function.

```cpp
string s = "dcba";
sort(s.begin(), s.end()); // s = "abcd"
```

---

## 🔄 5. Anagram Check (Leetcode 242)

Two strings are anagrams if they contain the same characters in any order (e.g., `"listen"` and `"silent"`).

### Approach: Sort Both and Compare
```cpp
bool isAnagram(string s, string t) {
    sort(s.begin(), s.end());
    sort(t.begin(), t.end());
    return s == t;  // If sorted strings are equal, they're anagrams
}
```
**Time:** $\mathcal{O}(n \log n)$

> [!TIP]
> **Optimal $\mathcal{O}(n)$ approach:** Use a frequency array of size 26. Increment for characters in `s`, decrement for characters in `t`. If all counts are zero at the end, they're anagrams.

---

## 🔢 6. Find String with Maximum Numeric Value (Without `stoi`)

Given `n` strings of digits (e.g., `"0123"`, `"0023"`, `"456"`, `"00182"`, `"940"`, `"2901"`), find the index of the string with the largest numeric value.

### Core Logic
You cannot simply compare strings by length, because `"0123"` (value 123) is less than `"940"` (value 940).

1. Find the max length among all strings.
2. Pad shorter strings with leading zeros to make them equal in length.
3. Now you can do a direct lexicographic (dictionary) string comparison!

```cpp
// Find max length
int maxLen = 0;
for(auto& str : strings) maxLen = max(maxLen, (int)str.size());

// Pad all strings with leading zeros
for(auto& str : strings) {
    while(str.size() < maxLen) str = "0" + str;
}

// Find the lexicographically maximum string
int maxIdx = 0;
for(int i = 1; i < n; i++) {
    if(strings[i] > strings[maxIdx]) maxIdx = i;
}
```

---

### 🛠️ MLOps Perspective: String Processing in MLOps
> [!IMPORTANT]
> String manipulation is the backbone of all data ingestion pipelines:
> - **`stoi` / `stoll` Overflow:** In an ML pipeline, when loading a CSV dataset with an ID column, if the IDs exceed `INT_MAX` (e.g., large-scale user IDs at Twitter-scale), using `stoi` instead of `stoll` would silently corrupt your data. This is a notorious real-world bug.
> - **Anagram Check / Frequency Arrays:** This is the same concept as a **Bag of Words** model in NLP. A Bag of Words represents a document as a frequency count of each word (just like the frequency array of 26 characters), ignoring order.

---

<div align="center">

⬅️ [Previous: Strings Part 1](./Strings_1.md)

</div>
