# **Topic 51: Introduction to NumPy** 

# 🎓 Simple Explanation (From Scratch)
# What is NumPy?

Imagine you have a notebook with just **10 numbers**.

You can easily add them together using Python.

Now imagine you have **10 million numbers**.

Can normal Python still do the job?

**Yes.**

Will it be fast?

**Not really.**

This is where **NumPy** comes in.

---

## Think of it Like This

Imagine two workers.

### Worker 1 (Python List)

He moves one box at a time.

📦 → 📦 → 📦 → 📦

---

### Worker 2 (NumPy)

He uses a forklift.

🚜📦📦📦📦📦

He moves many boxes together.

Obviously,

the second worker finishes much faster.

That's exactly what NumPy does.

---

# Why Was NumPy Created?

Python lists are great.

But they become slow when working with:

* Millions of numbers
* Scientific calculations
* AI
* Machine Learning
* Matrix operations

NumPy was created to solve this problem.

It provides a **much faster way** to store and manipulate numerical data.

---

# The Most Important Thing to Remember

The **heart of NumPy** is something called:

> **ndarray**

This is the most important concept in this lecture.

---

# What is ndarray?

`ndarray` stands for

> **N-Dimensional Array**

"N" means:

Any number of dimensions.

It can be

* 1D
* 2D
* 3D
* Even more

Instead of using Python lists,

NumPy stores data inside an ndarray.

---

## Example

### Python List

```python
numbers = [1,2,3,4]
```

---

### NumPy Array

```python
numbers = np.array([1,2,3,4])
```

Looks almost the same.

But internally,

NumPy stores it much more efficiently.

---

# Why is ndarray Faster?

The instructor mentions an important term:

> **Vectorization**

Sounds difficult,

but it's actually simple.

---

Imagine you have

```text
1
2
3
4
5
```

and you want to multiply every number by 2.

---

## Python List

Python does:

```
1×2

then

2×2

then

3×2

then

4×2

then

5×2
```

One by one.

---

## NumPy

NumPy says:

> Multiply the whole array together.

Everything happens in one optimized operation.

This is called

> **Vectorization**

---

## Easy Memory Trick

Vectorization means

> **One operation on the entire array**

instead of

> One operation for each element.

---

# Why is NumPy Used in AI?

Machine Learning uses

* Millions of numbers

For example,

An image

```
1920 × 1080 pixels
```

already contains

more than **2 million values**.

Imagine processing thousands of such images.

Normal Python becomes slow.

NumPy makes these calculations much faster.

That's why almost every AI library uses NumPy internally.

---

# Dimensions in NumPy

The lecture introduces dimensions.

---

## 1D Array

Looks like a normal list.

```text
[10 20 30 40]
```

Only one direction.

---

## 2D Array

Looks like a table.

```text
1 2 3

4 5 6
```

Rows and columns.

---

## 3D Array

Imagine stacking many tables together.

Like pages inside a notebook.

Each page is one 2D table.

Together,

they become a 3D array.

---

# Shape

Every ndarray has a property called

> Shape

Shape tells us

how many

Rows

and

Columns

exist.

Example

```
1 2 3

4 5 6
```

Shape is

```
(2,3)
```

Meaning

2 rows

3 columns

---

Easy memory trick

Shape answers

> "How big is my array?"

---

# Number of Dimensions

Another property is

```
ndim
```

It tells us

how many dimensions the array has.

Example

```
[1 2 3]
```

ndim

```
1
```

---

Example

```
1 2

3 4
```

ndim

```
2
```

---

Memory Trick

```
shape → size

ndim → dimensions
```

---

# Data Type (dtype)

Every value inside NumPy has a data type.

Examples

```
Integer

Float

Boolean
```

The lecture shows

```
int64
```

Meaning

64-bit Integer.

---

Why is this useful?

Because

NumPy stores all values efficiently.

Knowing the data type helps save memory and improves performance.

---

# Installing NumPy

The instructor installs NumPy using

```bash
pip install numpy
```

In Jupyter Notebook,

we write

```python
!pip install numpy
```

The exclamation mark tells Jupyter to run a terminal command.

---

# Importing NumPy

Almost every Python programmer writes

```python
import numpy as np
```

Notice

```
np
```

This is just a short nickname.

It has become an industry standard.

---

# Creating an Array

Example

```python
import numpy as np

array = np.array([
    [1,2,3],
    [4,5,6]
])
```

This creates

```
1 2 3

4 5 6
```

---

# Checking Shape

```python
array.shape
```

Output

```
(2,3)
```

Meaning

2 rows

3 columns

---

# Checking Dimensions

```python
array.ndim
```

Output

```
2
```

Meaning

2D Array.

---

# Checking Data Type

```python
array.dtype
```

Output

```
int64
```

Meaning

64-bit Integer.

---

# NumPy vs Python Lists

| Python List           | NumPy Array           |
| --------------------- | --------------------- |
| Slower                | Much Faster           |
| More Memory           | Less Memory           |
| One element at a time | Vectorized operations |
| General Purpose       | Scientific Computing  |
| Small datasets        | Large datasets        |

---

# Easy Way to Remember Everything

```
Python List
↓

Good

↓

Large Data

↓

Need Speed

↓

Use NumPy

↓

Core Object

↓

ndarray

↓

Properties

↓

shape

ndim

dtype
```

---

# Quick Revision

✅ NumPy = Fast numerical library

✅ Core object = ndarray

✅ ndarray = N-Dimensional Array

✅ shape = Rows & Columns

✅ ndim = Number of dimensions

✅ dtype = Data type

✅ Vectorization = One operation on the entire array

✅ NumPy is faster than Python lists

---
