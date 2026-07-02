# Topic 50: Introduction to NumPy

> **Course:** DigiSkills.pk – Artificial Intelligence Using Python  
> **Week:** 03  
> **Topic:** 50 – Why NumPy & Environment Setup ( Introduction to NumPy )  
> **Status:** ✅ Completed

---

# 📖 Overview

In this lecture, I learned about **NumPy (Numerical Python)**, one of the most important Python libraries used in Data Science, Machine Learning, and Artificial Intelligence.

NumPy provides a fast and memory-efficient way to store and manipulate numerical data using a special data structure called **ndarray (N-Dimensional Array)**.

---

# Why NumPy?

Python lists work well for small datasets, but they become slower when working with large amounts of numerical data.

NumPy is optimized for:

- Fast numerical computations
- Matrix operations
- Scientific computing
- Machine Learning
- AI applications

---

# Core Concept: ndarray

The most important data structure in NumPy is the **ndarray**.

**ndarray** stands for **N-Dimensional Array**.

It can represent:

- 1D Arrays
- 2D Arrays
- 3D Arrays
- Higher-dimensional arrays

Example:

```python
import numpy as np

numbers = np.array([1, 2, 3, 4])
```

---

# Why is NumPy Faster?

NumPy uses **vectorized operations**, meaning it performs operations on the entire array at once instead of processing each element one by one.

This makes NumPy significantly faster and more memory-efficient than standard Python lists.

---

# Important ndarray Properties

## Shape

Returns the number of rows and columns.

```python
array.shape
```

Example Output:

```python
(2, 3)
```

Meaning:

- 2 Rows
- 3 Columns

---

## ndim

Returns the number of dimensions.

```python
array.ndim
```

Example Output:

```python
2
```

Meaning:

The array is two-dimensional.

---

## dtype

Returns the data type of array elements.

```python
array.dtype
```

Example Output:

```python
int64
```

---

# Installing NumPy

```bash
pip install numpy
```

In Jupyter Notebook:

```python
!pip install numpy
```

---

# Importing NumPy

The standard convention is:

```python
import numpy as np
```

Using **np** as an alias is considered an industry standard.

---

# Creating a NumPy Array

```python
import numpy as np

array = np.array([
    [1, 2, 3],
    [4, 5, 6]
])
```

---

# NumPy vs Python Lists

| Python List | NumPy Array |
|--------------|-------------|
| Slower for large datasets | Optimized for speed |
| Higher memory usage | More memory-efficient |
| Element-by-element operations | Vectorized operations |
| General-purpose | Scientific & numerical computing |

---

# Key Takeaways

- NumPy is the foundation of scientific computing in Python.
- The core data structure is **ndarray**.
- NumPy is faster than Python lists because it uses vectorized operations.
- Important ndarray properties include:
  - `shape`
  - `ndim`
  - `dtype`
- NumPy is widely used in AI, Machine Learning, and Data Science.

---
# 💻 Hands-on Practice

The following examples demonstrate how to install NumPy, create arrays, inspect their properties, and compare the performance of Python lists with NumPy arrays.

---

## 1️⃣ Installing NumPy

If NumPy is not already installed, install it using:

```python
!pip install numpy
```

Example Output:

```text
Requirement already satisfied: numpy in c:\users\administrator\anaconda3\lib\site-packages (2.3.5)
```

**Explanation**

- `pip` is Python's package manager.
- `!` tells Jupyter Notebook to execute a terminal command.
- If NumPy is already installed, Python simply reports its installed version.

---

## 2️⃣ Import Required Libraries

```python
import numpy as np
import time
```

### Explanation

- `numpy` is imported using the alias `np` (industry standard).
- `time` is used to measure how long a program takes to execute.

---

## 3️⃣ Creating a NumPy Array

```python
arr = np.array([[1, 2, 3], [4, 5, 6]])
```

### Explanation

This creates a **2-dimensional NumPy array**.

Visual representation:

| | | |
|---|---|---|
|1|2|3|
|4|5|6|

It contains:

- **2 Rows**
- **3 Columns**

---

## 4️⃣ Checking Array Properties

```python
print(arr.shape)
print(arr.ndim)
print(arr.dtype)
```

Output:

```text
(2, 3)
2
int64
```

### Explanation

### `shape`

```python
arr.shape
```

Output:

```text
(2, 3)
```

Meaning:

- 2 Rows
- 3 Columns

---

### `ndim`

```python
arr.ndim
```

Output:

```text
2
```

Meaning:

The array has **2 dimensions**.

---

### `dtype`

```python
arr.dtype
```

Output:

```text
int64
```

Meaning:

The array stores **64-bit integers**.

> **Note:** Depending on your operating system or Python version, the data type may appear slightly different (such as `int32`).

---

# 🚀 Performance Comparison

One of NumPy's biggest advantages is speed.

Let's compare a normal Python list with a NumPy array.

---

## 5️⃣ Using a Python List

```python
py_list = list(range(1_000_000))
py_result = []

start_time = time.time()

for i in py_list:
    py_result.append(i + 5)

end_time = time.time()

print("Python List Time:", end_time - start_time)
```

Example Output:

```text
Python List Time: 0.47373199462890625
```

### Explanation

Step by step:

1. Create a list containing **1 million numbers**.
2. Create an empty list to store results.
3. Record the starting time.
4. Loop through every number.
5. Add **5** to each number.
6. Store the result.
7. Record the ending time.
8. Calculate the total execution time.

This process works correctly but is relatively slow because Python processes **one element at a time**.

---

## 6️⃣ Using a NumPy Array

```python
np_array = np.arange(1_000_000)

start_time = time.time()

np_result = np_array + 5

end_time = time.time()

print("NumPy Array Time:", end_time - start_time)
```

Example Output:

```text
NumPy Array Time: 0.006583452224731445
```

### Explanation

Step by step:

1. Create a NumPy array containing **1 million numbers**.
2. Record the starting time.
3. Add **5** to the **entire array** in one operation.
4. Record the ending time.
5. Calculate the execution time.

Unlike Python lists, NumPy performs the calculation using **vectorized operations**, making it significantly faster.

---

# 📊 Performance Comparison

| Python List | NumPy Array |
|--------------|-------------|
| Time ≈ 0.47 seconds | Time ≈ 0.006 seconds |
| Uses a loop | Uses vectorized operations |
| Slower | Much faster |
| Higher memory usage | More memory efficient |

> **Result:** In this example, the NumPy array is approximately **70× faster** than the Python list.

---

# 💡 Why is NumPy Faster?

NumPy stores data more efficiently in memory and performs calculations using **vectorized operations** instead of processing each element individually.

Instead of this:

```
1 + 5
2 + 5
3 + 5
...
```

NumPy performs:

```
Entire Array + 5
```

This allows the operation to execute much faster, especially on large datasets.

---

# 🎯 What I Learned

After completing these examples, I learned that:

- NumPy arrays are easy to create using `np.array()`.
- The `shape` property returns the number of rows and columns.
- The `ndim` property returns the number of dimensions.
- The `dtype` property shows the data type of the stored values.
- NumPy uses **vectorized operations**, making it much faster than Python lists.
- This speed is one of the main reasons why NumPy is widely used in Data Science, Machine Learning, and Artificial Intelligence.

## 🌟 My Observation

Before learning NumPy, I thought Python lists were sufficient for handling numerical data. After comparing their performance, I realized why NumPy is the foundation of almost every Data Science and Machine Learning library.

Even a simple operation like adding **5** to one million numbers took around **0.47 seconds** with a Python list, while NumPy completed the same task in about **0.006 seconds** using vectorized operations. This demonstrates why NumPy is the preferred choice for high-performance numerical computing.
---

# Quick Revision

| Concept | Summary |
|----------|---------|
| NumPy | Fast numerical computing library |
| ndarray | N-Dimensional Array |
| shape | Rows and columns |
| ndim | Number of dimensions |
| dtype | Data type of elements |
| Vectorization | Perform one operation on the entire array |

---

# Personal Learning Summary

In this lecture, I learned that NumPy is a high-performance numerical computing library that provides the **ndarray** data structure for efficiently storing and processing large datasets. Compared to Python lists, NumPy offers faster execution, lower memory usage, and vectorized operations, making it an essential foundation for Data Science, Machine Learning, and Artificial Intelligence.

## 💡 Real-World Connection

NumPy is used behind the scenes by many popular AI and Data Science libraries, including:

- Pandas
- Scikit-learn
- TensorFlow
- PyTorch
- OpenCV

Learning NumPy well makes it much easier to understand and work with these advanced libraries later.

---

## Tags

`Python` `NumPy` `Artificial Intelligence` `Machine Learning` `Data Science` `Scientific Computing` `Learning Journey`
