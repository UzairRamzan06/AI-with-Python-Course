# Topic 51: Creating Arrays in NumPy

> **Course:** DigiSkills.pk – Artificial Intelligence Using Python  
> **Week:** 03  
> **Topic:** 51 – Creating Arrays in NumPy  
> **Status:** ✅ Completed

---

# 📖 Overview

In the previous topic, I learned that **NumPy** is a fast numerical computing library and that its core data structure is the **ndarray**.

In this topic, I learned the different ways to create NumPy arrays. NumPy provides several built-in functions that make array creation simple and efficient. Each function is designed for a specific purpose, such as creating arrays filled with zeros, ones, custom values, sequences, or identity matrices.

---

# Why Are There Multiple Ways to Create Arrays?

Imagine you are writing a program.

Sometimes you need:

- An array filled with **0**
- An array filled with **1**
- A sequence like **0, 2, 4, 6, 8**
- An identity matrix
- A matrix filled with the same value

Instead of manually typing these values, NumPy provides built-in functions to generate them instantly.

---

# 1. Creating an Array using `np.array()`

This is the most common way to create a NumPy array.

### Code

```python
import numpy as np

arr = np.array([1, 2, 3])

print(arr)
```

### Output

```text
[1 2 3]
```

### Explanation

- `np.array()` converts a Python list into a NumPy array.
- This method is used when you already have data available.

### Memory Tip

> **`np.array()` = Convert a Python list into a NumPy array.**

---

# 2. Creating an Array of Zeros

### Code

```python
print(np.zeros((2,3)))
```

### Output

```text
[[0. 0. 0.]
 [0. 0. 0.]]
```

### Explanation

- Creates an array containing only zeros.
- `(2,3)` means:
  - 2 Rows
  - 3 Columns

### Common Uses

- Placeholder arrays
- Initialization before calculations

### Memory Tip

> **`zeros()` → Fill everything with 0**

---

# 3. Creating an Array of Ones

### Code

```python
print(np.ones((2,3)))
```

### Output

```text
[[1. 1. 1.]
 [1. 1. 1.]]
```

### Explanation

Creates an array where every element is **1**.

### Common Uses

- Matrix multiplication
- Mathematical computations
- Initializing weights (in some ML algorithms)

### Memory Tip

> **`ones()` → Fill everything with 1**

---

# 4. Creating an Array with Any Value using `np.full()`

### Code

```python
print(np.full((2,3), 7))
```

### Output

```text
[[7 7 7]
 [7 7 7]]
```

### Explanation

Arguments:

- `(2,3)` → Shape of the array
- `7` → Fill value

Every element becomes **7**.

### Memory Tip

> **`full()` → Fill the entire array with any value you choose.**

---

# 5. Creating a Sequence using `np.arange()`

### Code

```python
print(np.arange(0, 10, 2))
```

### Output

```text
[0 2 4 6 8]
```

### Explanation

Arguments:

- Start = 0
- Stop = 10 (not included)
- Step = 2

Generated values:

```
0 → 2 → 4 → 6 → 8
```

Notice that **10 is excluded**.

### Memory Tip

> **`arange()` = Start, Stop, Step**

---

# 6. Creating Evenly Spaced Values using `np.linspace()`

### Code

```python
print(np.linspace(0, 1, 5))
```

### Output

```text
[0.   0.25 0.50 0.75 1.00]
```

### Explanation

Arguments:

- Start = 0
- End = 1
- Total Values = 5

NumPy automatically calculates equal spacing.

### Difference Between `arange()` and `linspace()`

| `arange()` | `linspace()` |
|------------|--------------|
| Uses step size | Uses number of values |
| End value excluded | End value included |

### Memory Tip

> **`linspace()` = Divide an interval into equal parts.**

---

# 7. Creating an Identity Matrix using `np.eye()`

### Code

```python
print(np.eye(3))
```

### Output

```text
[[1. 0. 0.]
 [0. 1. 0.]
 [0. 0. 1.]]
```

### Explanation

Creates a **3 × 3 Identity Matrix**.

Characteristics:

- Diagonal values = 1
- All other values = 0

Identity matrices are widely used in Linear Algebra and Machine Learning.

### Memory Tip

> **`eye()` = Identity Matrix**

---

# 8. Creating a Diagonal Matrix using `np.diag()`

### Code

```python
print(np.diag([1,2,3]))
```

### Output

```text
[[1 0 0]
 [0 2 0]
 [0 0 3]]
```

### Explanation

The provided list becomes the diagonal values.

All remaining elements are filled with zero.

### Memory Tip

> **`diag()` = Custom Diagonal Values**

---

# 9. Specifying the Data Type using `dtype`

### Code

```python
np.array([1, 2, 3], dtype=float)
```

### Output

```text
array([1., 2., 3.])
```

### Explanation

Although the values are integers, NumPy converts them into floating-point numbers because we specified:

```python
dtype=float
```

### Common Data Types

| Data Type | Description |
|-----------|-------------|
| `int` | Integer |
| `float` | Decimal Number |
| `bool` | True / False |

### Memory Tip

> **`dtype` = Decide the data type while creating the array.**

---

# 💻 Hands-on Practice

The following code combines all the examples covered in this lecture.

```python
import numpy as np

arr = np.array([1, 2, 3])
print(arr)

print(np.zeros((2,3)))

print(np.ones((2,3)))

print(np.full((2,3), 7))

print(np.arange(0, 10, 2))

print(np.linspace(0, 1, 5))

print(np.eye(3))

print(np.diag([1,2,3]))

print(np.array([1, 2, 3], dtype=float))
```

### What I Learned from This Practice

- `np.array()` creates an array from an existing list.
- `np.zeros()` creates arrays filled with zeros.
- `np.ones()` creates arrays filled with ones.
- `np.full()` fills an array with a custom value.
- `np.arange()` generates a sequence using a step size.
- `np.linspace()` generates evenly spaced values.
- `np.eye()` creates an identity matrix.
- `np.diag()` creates a diagonal matrix.
- `dtype` controls the data type during array creation.

---

# Quick Comparison Table

| Function | Purpose |
|----------|---------|
| `np.array()` | Convert list to NumPy array |
| `np.zeros()` | Array filled with 0 |
| `np.ones()` | Array filled with 1 |
| `np.full()` | Array filled with any value |
| `np.arange()` | Generate sequence using step size |
| `np.linspace()` | Generate equally spaced values |
| `np.eye()` | Identity Matrix |
| `np.diag()` | Custom Diagonal Matrix |
| `dtype` | Specify data type |

---

# Key Takeaways

- NumPy provides multiple ways to create arrays depending on the problem.
- `np.array()` is the standard method when data already exists.
- `np.zeros()`, `np.ones()`, and `np.full()` quickly create initialized arrays.
- `np.arange()` and `np.linspace()` generate numerical sequences.
- `np.eye()` and `np.diag()` are useful for matrix operations.
- `dtype` allows explicit control over the data type of array elements.

---

# Quick Revision

| Concept | Summary |
|----------|---------|
| `array()` | Create array from list |
| `zeros()` | Fill with 0 |
| `ones()` | Fill with 1 |
| `full()` | Fill with any value |
| `arange()` | Sequence with step size |
| `linspace()` | Equal spacing |
| `eye()` | Identity Matrix |
| `diag()` | Diagonal Matrix |
| `dtype` | Specify data type |

---

# 🌟 My Observation

This lecture helped me understand that NumPy provides different functions for creating arrays based on different situations. Instead of manually writing values, I can generate arrays instantly using built-in functions. This makes code shorter, cleaner, and much more efficient, especially when working with Data Science, Machine Learning, and Artificial Intelligence projects.

---

## Tags

`Python` `NumPy` `Arrays` `Machine Learning` `Artificial Intelligence` `Data Science` `Learning Journey`
