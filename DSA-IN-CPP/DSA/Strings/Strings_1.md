<div align="center">

# <span style="color:#8E44AD">🟣 Strings in C++ — Part 1 (Fundamentals)</span>

![Section](https://img.shields.io/badge/Data_Structure-Strings-8E44AD) ![Language](https://img.shields.io/badge/Language-C++-00599C?logo=c%2B%2B&logoColor=white)

</div>

---

## 🧵 1. What Are Strings?

In C++, a **string is essentially a character array** (`char arr[]`). The `<string>` library provides a more powerful `string` class that handles memory automatically.

```cpp
// C-style (char array)
char arr[] = {'R', 'a', 'v', 'i', 't', 'g'};

// C++ style (preferred)
string s = "Manit Kamau";
```

### CRUD on Strings
| Operation | How |
|---|---|
| **Create** | `string s = "hello";` |
| **Read** | `s[i]` or `s.at(i)` |
| **Update** | `s[i] = 'a';` |
| **Delete** | `s.pop_back();` |

---

## 📝 2. Declaration & Input

```cpp
string name;

// Read a single word (stops at whitespace)
cin >> name;

// Read an entire line (including spaces)
getline(cin, name);
```

> [!WARNING]
> If you use `cin >>` before `getline()`, the leftover newline `\n` in the buffer will cause `getline` to read an empty string. Always use `cin.ignore()` before `getline()` to clear the buffer.

---

## 📏 3. Indexing & Size

- Strings are **0-indexed**, just like arrays.
- Access character at index `i`: `s[i]` or safer: `s.at(i)`.
- Get total length: `s.size()` or `s.length()`. Both are equivalent.

```cpp
string s = "hello";
cout << s[0];      // 'h'
cout << s.size();  // 5
```

---

## 💡 4. Classic Problems

### Count Vowels in a String
```cpp
string s;
cin >> s;
int count = 0;
for(int i = 0; i < s.size(); i++) {
    char c = s[i];
    if(c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u') {
        count++;
    }
}
```

### Update Even-Position Characters (0-based index)
```cpp
for(int i = 0; i < s.size(); i++) {
    if(i % 2 == 0) s[i] = 'a';
}
```

---

## 🛠️ 5. Built-in String Functions

| Function | Description | Example |
|---|---|---|
| `s.size()` / `s.length()` | Length of the string | `s.size()` → `5` |
| `s.push_back('x')` | Append character to end | `"hello" → "hellox"` |
| `s.pop_back()` | Remove last character | `"hello" → "hell"` |
| `s1 + s2` | Concatenate two strings | `"hello" + " world"` |
| `reverse(s.begin(), s.end())` | Reverse the string in-place | `"hello" → "olleh"` |

---

## 🔁 6. Reverse First Half of String

```cpp
string s = "navhav"; // even-length string
int n = s.size();
// Reverse only from index 0 to n/2 - 1
reverse(s.begin(), s.begin() + n / 2);
```

---

## 🪞 7. Palindrome Check (Leetcode 125)

A string that reads the same forwards and backwards (e.g., `"mom"`, `"dad"`, `"malayalam"`).

```cpp
int i = 0, j = s.size() - 1;
bool isPalin = true;
while(i < j) {
    if(s[i] != s[j]) {
        isPalin = false;
        break;
    }
    i++;
    j--;
}
```

> [!TIP]
> You can also use the built-in: compare `s` with `string(s.rbegin(), s.rend())`.

---

### 🛠️ MLOps Perspective: Strings in NLP Pipelines
> [!IMPORTANT]
> Strings are the raw input format for all NLP (Natural Language Processing) tasks. Understanding C++ strings builds the intuition needed for:
> - **Tokenization:** Every NLP pipeline starts by splitting a string into words/tokens. `push_back`, `pop_back`, and indexing are the operations tokenizers use under the hood.
> - **Palindrome & Anagram checks** are simplified versions of the **similarity metrics** used in text: edit distance (Levenshtein), Jaccard similarity, etc.

---

<div align="center">

➡️ [Next: Strings Part 2](./Strings_2.md)

</div>
