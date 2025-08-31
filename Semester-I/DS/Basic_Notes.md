# 🧮 Bitwise Operators in C++

Bitwise operators work **directly on binary representation** of integers.

## 🔹 Operators

| Operator | Meaning | Example (a=5, b=3) | Binary Operation | Result |
|----------|---------|--------------------|------------------|--------|
| `&`  | AND  | `a & b` | `0101 & 0011 = 0001` | **1** |
| `|`  | OR   | `a | b` | `0101 \| 0011 = 0111` | **7** |
| `^`  | XOR  | `a ^ b` | `0101 ^ 0011 = 0110` | **6** |
| `~`  | NOT  | `~a`    | `~0101 = ...1010`   | **-6** (2’s complement) |
| `<<` | Left Shift  | `a << 1` | `0101 → 1010` | **10** |
| `>>` | Right Shift | `a >> 1` | `0101 → 0010` | **2** |

## 🔹 Quick Notes
- `&` → 1 only if **both bits** are 1.  
- `|` → 1 if **at least one bit** is 1.  
- `^` → 1 if bits are **different**.  
- `~` → Flips all bits (**two’s complement** for negatives).  
- `<<` → Shifts bits **left** (multiply by 2 each shift).  
- `>>` → Shifts bits **right** (divide by 2 each shift).  






---

# 🔡 String Mutability

## 🔹 C++

* **`std::string` is mutable** → characters can be changed, appended, erased.

```cpp
#include <iostream>
#include <string>
using namespace std;

int main() {
    string s = "Hello";
    s[0] = 'Y';          // modify
    s.append(" World");  // append
    cout << s;           // Output: Yello World
}
```

✅ Works fine.

* But **string literals** are immutable when used as `char*`.

```cpp
char* s = "Hello";   // stored in read-only memory
s[0] = 'Y';          // ❌ undefined behavior
```

Use `char s[] = "Hello";` if you need a mutable C-style string.

---

## 🔹 C

* `char s[] = "Hello";` → **mutable**
* `char* s = "Hello";` → **immutable (undefined if modified)**

---

## 🔹 Other Languages

* **Python** → Strings are immutable (must create a new string).
* **Java** → `String` is immutable, but `StringBuilder` and `StringBuffer` are mutable.

---

✅ **Summary:**

* C++ → `std::string` is **mutable**.
* C string literals (`char*`) → **immutable**.
* Many modern languages (Java, Python) → immutable by default for safety/performance.

---







---

# 🔢 Multi-Dimensional Arrays

A **multi-dimensional array** is an array of arrays.
General form:

```cpp
data_type array_name[size1][size2]...[sizeN];
```

---

## 🔹 Example: 3D Array

```cpp
int arr[2][3][4];
```

* `2` → number of **blocks**
* `3` → number of **rows** in each block
* `4` → number of **columns** in each row

👉 Total elements = `2 × 3 × 4 = 24`

---

## 🔹 Memory Layout

Multi-dimensional arrays in C++ use **row-major order** → last index changes fastest.

Stored sequence:

```
arr[0][0][0], arr[0][0][1], arr[0][0][2], arr[0][0][3],
arr[0][1][0], arr[0][1][1], ...
...
arr[1][2][3]
```

---

## 🔹 Visualization of `arr[2][3][4]`

```
Block 0:
Row 0 → [ arr[0][0][0] arr[0][0][1] arr[0][0][2] arr[0][0][3] ]
Row 1 → [ arr[0][1][0] arr[0][1][1] arr[0][1][2] arr[0][1][3] ]
Row 2 → [ arr[0][2][0] arr[0][2][1] arr[0][2][2] arr[0][2][3] ]

Block 1:
Row 0 → [ arr[1][0][0] arr[1][0][1] arr[1][0][2] arr[1][0][3] ]
Row 1 → [ arr[1][1][0] arr[1][1][1] arr[1][1][2] arr[1][1][3] ]
Row 2 → [ arr[1][2][0] arr[1][2][1] arr[1][2][2] arr[1][2][3] ]
```

---

## 🔹 Initialization

```cpp
int arr[2][3][4] = {
    { {1,2,3,4}, {5,6,7,8}, {9,10,11,12} },
    { {13,14,15,16}, {17,18,19,20}, {21,22,23,24} }
};
```

---

## 🔹 Accessing Elements

```cpp
cout << arr[1][2][3];  // Output: 24
```

---

✅ **Summary**:

* Multi-dimensional arrays = arrays inside arrays.
* Total elements = product of all dimensions.
* Stored in **row-major order** in memory.
* Useful for matrices, tables, 3D grids, etc.

---






# 🏗️ Structures in C/C++

* **Definition:** User-defined data type that groups different variables of different types into one unit.
* **Analogy:** Like a **student record card** → Roll (int), Name (string), Marks (float).

---

## 🔹 Syntax

```cpp
struct Student {
    int roll;
    string name;
    float marks;
};
```

---

## 🔹 Usage

```cpp
Student s1 = {1, "Aman", 92.5};
s1.marks = 95;              // access via dot operator
cout << s1.name;            // Output: Aman
```

---

## 🔹 Arrays of Structures

```cpp
Student students[2] = {
    {1, "Aman", 92.5},
    {2, "Riya", 88.5}
};
```

---

## 🔹 Structures vs Classes (C++)

* **C** → struct holds only variables.
* **C++** → struct ≈ class, but **default access is public**.

---

✅ **Summary:** Structures are useful for storing **records** (student, employee, book).

---




---

# 🔢 Enum in C/C++

* **Definition:** `enum` (enumeration) is a user-defined type consisting of a set of **named integral constants**.
* Purpose → Improves **readability** (no need to use raw numbers).

---

## 🔹 Syntax

```cpp
enum Color { RED, YELLOW, GREEN };
```

* By default: `RED = 0, YELLOW = 1, GREEN = 2`.

---

## 🔹 Usage

```cpp
Color signal = GREEN;
if (signal == GREEN) {
    cout << "Go!" << endl;
}
```

**Output:**

```
Go!
```

---

## 🔹 Real-Life Analogy

Think of **traffic lights 🚦**:

* `RED` = Stop
* `YELLOW` = Wait
* `GREEN` = Go

Instead of remembering numbers (`0,1,2`), we use **meaningful names**.

---

## 🔹 Custom Values

```cpp
enum Week { MON=1, TUE, WED, THU=10, FRI, SAT, SUN };
// MON=1, TUE=2, WED=3, THU=10, FRI=11 ...
```

---

## 🔹 Key Points

* Default underlying type = `int`.
* Values auto-increment unless explicitly set.
* Helps write **clean, maintainable, and readable code**.

---

✅ **Summary:**
`enum` = a way to map **names → integers** (like traffic signals), making programs more understandable.

---



Great topic 👍 Here’s a **clear and exam-ready note** for your `notes.md` on **References and Memory Address in C++**:

---

# 🔗 References & Memory Address in C++

## 🔹 Reference

* A **reference** is an **alias (another name)** for an existing variable.
* Declared using `&` (ampersand) after the type.
* Must be initialized at the time of declaration.
* Changing reference = changes the original variable.

### Example:

```cpp
int x = 10;
int &ref = x;    // ref is another name for x

ref = 20;        // modifies x
cout << x;       // Output: 20
```

---

## 🔹 Memory Address

* Every variable in C++ is stored in a unique **memory location**.
* The **address-of operator (`&`)** gives the memory address.

### Example:

```cpp
int x = 10;
cout << &x;  // prints address of x (e.g. 0x7ffeefbff4ac)
```

---

## 🔹 References + Memory Address

```cpp
int x = 10;
int &ref = x;

cout << "x = " << x << endl;        // 10
cout << "ref = " << ref << endl;    // 10
cout << "&x = " << &x << endl;      // memory address
cout << "&ref = " << &ref << endl;  // same address as x
```

**Output (example):**

```
x = 10
ref = 10
&x = 0x7ffee1d5b8ac
&ref = 0x7ffee1d5b8ac
```

👉 Both `x` and `ref` point to the **same memory address**.

---

## 🔹 Key Points

* Reference = just another name (alias) for a variable.
* Both variable and reference share the **same memory address**.
* Used for:

  * Function parameters (pass by reference).
  * Avoiding copies of large objects.
  * Cleaner, safer alternative to pointers (in many cases).

---

✅ **Summary:**

* `&` before type → create a reference (alias).
* `&` before variable → get memory address.
* Reference shares the **same memory address** as the original variable.

---


 ## **short comparison table: Reference vs Pointer**

---

# 🔗 Reference vs Pointer in C++

| Feature           | Reference (`&`)                                                    | Pointer (`*`)                                              |
| ----------------- | ------------------------------------------------------------------ | ---------------------------------------------------------- |
| **Definition**    | Alias (another name) for a variable                                | Variable that stores memory address                        |
| **Declaration**   | `int &ref = x;`                                                    | `int *ptr = &x;`                                           |
| **Null value?**   | ❌ Cannot be null                                                   | ✅ Can be null (`nullptr`)                                  |
| **Reassignment**  | ❌ Must be initialized, cannot be changed to refer another variable | ✅ Can point to different variables                         |
| **Dereferencing** | Not needed (`ref` directly accesses value)                         | Must use `*ptr` to access value                            |
| **Address**       | `&ref` is same as `&x`                                             | `ptr` stores `&x`                                          |
| **Memory Safety** | Safer, simpler                                                     | More flexible but error-prone                              |
| **Use cases**     | Pass by reference, operator overloading, cleaner syntax            | Dynamic memory, data structures (linked list, trees, etc.) |

---

## 🔹 Example

```cpp
#include <iostream>
using namespace std;

int main() {
    int x = 10;

    int &ref = x;      // Reference
    int *ptr = &x;     // Pointer

    ref = 20;          // changes x
    *ptr = 30;         // also changes x

    cout << "x = " << x << endl;       // 30
    cout << "ref = " << ref << endl;   // 30
    cout << "*ptr = " << *ptr << endl; // 30
}
```

---

✅ **Summary:**

* **Reference** = alias, safer, cannot be null, fixed after initialization.
* **Pointer** = stores address, more flexible, can be null, supports arithmetic.

---

