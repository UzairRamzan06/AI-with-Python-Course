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
