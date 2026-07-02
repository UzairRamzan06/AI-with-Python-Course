# 🎓 Topic 51: Creating Arrays in NumPy (Simple Explanation)

## Before We Start

In the previous topic, we learned that **NumPy** is a Python library used for fast numerical computations and that its core data structure is the **ndarray**.

Now the question is:

> **How do we create NumPy arrays?**

Fortunately, NumPy provides many built-in functions for creating arrays quickly.

---

# Method 1: `np.array()`

This is the **most common** way to create a NumPy array.

### Syntax

```python
import numpy as np

arr = np.array([1, 2, 3])
```

### Output

```text
[1 2 3]
```

### Explanation

* `np.array()` converts a Python list into a NumPy array.
* It is the most frequently used function when you already have data.

### Memory Trick

> **`np.array()` = Convert a Python list into a NumPy array.**

---

# Method 2: `np.zeros()`

Sometimes we need an array where **every value is 0**.

Instead of writing:

```text
0 0 0
0 0 0
```

NumPy can create it automatically.

### Example

```python
arr = np.zeros((2, 3))
```

### Output

```text
[[0. 0. 0.]
 [0. 0. 0.]]
```

### Explanation

* First value → Number of rows
* Second value → Number of columns

Here:

* 2 rows
* 3 columns

### Why use it?

Zero matrices are commonly used as placeholders or as a starting point for calculations.

### Memory Trick

> **`zeros()` → Fill everything with 0.**

---

# Method 3: `np.ones()`

Instead of zeros, suppose we need every value to be **1**.

### Example

```python
arr = np.ones((2, 3))
```

### Output

```text
[[1. 1. 1.]
 [1. 1. 1.]]
```

### Why use it?

One matrices are useful in mathematical and matrix multiplication operations because multiplying by 1 keeps values unchanged.

### Memory Trick

> **`ones()` → Fill everything with 1.**

---

# Method 4: `np.full()`

Suppose we don't want all zeros or all ones.

Instead, we want every value to be **7**.

### Example

```python
arr = np.full((2, 3), 7)
```

### Output

```text
[[7 7 7]
 [7 7 7]]
```

### Explanation

* `(2, 3)` → Shape of the array
* `7` → Fill value

### Memory Trick

> **`full()` → Fill the whole array with any value you choose.**

---

# Method 5: `np.arange()`

This function creates a sequence of numbers.

Think of it like Python's `range()`, but it returns a NumPy array.

### Example

```python
arr = np.arange(0, 10, 2)
```

### Output

```text
[0 2 4 6 8]
```

### Explanation

The arguments are:

* Start = 0
* Stop = 10
* Step = 2

Notice that **10 is not included**.

### Memory Trick

> **`arange()` → Start, Stop, Step**

---

# Method 6: `np.linspace()`

Sometimes we don't know the step size.

Instead, we know **how many values** we want.

That's where `linspace()` is useful.

### Example

```python
arr = np.linspace(0, 1, 5)
```

### Output

```text
[0.   0.25 0.5  0.75 1.  ]
```

### Explanation

We asked NumPy to:

* Start at 0
* End at 1
* Divide into 5 equal values

NumPy automatically calculates the spacing.

### Difference from `arange()`

| `arange()`         | `linspace()`          |
| ------------------ | --------------------- |
| Uses step size     | Uses number of values |
| End value excluded | End value included    |

### Memory Trick

> **`linspace()` → Equal spacing between start and end.**

---

# Method 7: `np.eye()`

Creates an **Identity Matrix**.

### Example

```python
arr = np.eye(3)
```

### Output

```text
[[1. 0. 0.]
 [0. 1. 0.]
 [0. 0. 1.]]
```

### Explanation

* Diagonal values = 1
* Everything else = 0

Identity matrices are very important in Linear Algebra.

### Memory Trick

> **`eye()` → Identity Matrix**

---

# Method 8: `np.diag()`

Suppose we want different diagonal values.

### Example

```python
arr = np.diag([1, 2, 3])
```

### Output

```text
[[1 0 0]
 [0 2 0]
 [0 0 3]]
```

### Explanation

The provided list becomes the diagonal of the matrix.

All other values remain zero.

### Memory Trick

> **`diag()` → Custom diagonal values**

---

# Method 9: Using `dtype`

Sometimes we want to control the data type.

### Example

```python
arr = np.array([1, 2, 3], dtype=float)
```

### Output

```text
[1. 2. 3.]
```

### Explanation

Although we entered integers, NumPy converted them to floating-point numbers.

### Common Data Types

| Data Type | Meaning    |
| --------- | ---------- |
| `int`     | Integer    |
| `float`   | Decimal    |
| `bool`    | True/False |

---

# Method 10: `astype()`

Suppose the array already exists.

Now we want to convert its data type.

### Example

```python
arr = np.array([1.5, 2.7, 3.9])

arr.astype(int)
```

### Output

```text
[1 2 3]
```

### Explanation

`astype()` creates a converted version of the array.

The decimal part is removed because integers cannot store decimal values.

### Memory Trick

> **`astype()` → Convert data type after the array is created.**

---

# Quick Comparison

| Function     | Purpose                       |
| ------------ | ----------------------------- |
| `array()`    | Create array from list        |
| `zeros()`    | Fill with 0                   |
| `ones()`     | Fill with 1                   |
| `full()`     | Fill with any value           |
| `arange()`   | Sequence with step size       |
| `linspace()` | Equal spacing                 |
| `eye()`      | Identity matrix               |
| `diag()`     | Custom diagonal               |
| `dtype`      | Set data type during creation |
| `astype()`   | Change data type later        |

---

# Easy Way to Remember

```text
Have a list?
      ↓
np.array()

Need all zeros?
      ↓
np.zeros()

Need all ones?
      ↓
np.ones()

Need same value?
      ↓
np.full()

Need a sequence?
      ↓
np.arange()

Need equal spacing?
      ↓
np.linspace()

Need identity matrix?
      ↓
np.eye()

Need custom diagonal?
      ↓
np.diag()

Need specific data type?
      ↓
dtype

Need to convert data type later?
      ↓
astype()
```

---

## 🌟 My Observation

The most important lesson from this lecture is that **NumPy offers multiple ways to create arrays, and each method is designed for a specific purpose**. Instead of manually filling arrays with values, NumPy provides built-in functions like `zeros()`, `ones()`, `full()`, `arange()`, and `linspace()` that make code shorter, cleaner, and more efficient. Understanding when to use each function is a foundational skill for Data Science, Machine Learning, and Artificial Intelligence.
