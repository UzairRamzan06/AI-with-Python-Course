# Artificial Intelligence Using Python

## Offered by DigiSkills.pk

---

# Week 03 – Lecture 52

# Topic 52: NumPy Indexing, Slicing & Strides

---

# Course Objective

In this lecture, we learn how to access and manipulate data inside NumPy arrays using **Indexing**, **Slicing**, and **Strides**. We also learn an important concept about **Views** and **Copies**, which helps us understand how NumPy stores data in memory and how modifications affect the original array.

These concepts are used extensively in Artificial Intelligence, Machine Learning, Data Science, and Deep Learning because datasets are usually stored as NumPy arrays.

---

# Learning Outcomes

After completing this lecture, you should be able to:

* Understand what indexing is.
* Access any element inside a NumPy array.
* Use positive and negative indexing.
* Select multiple elements using slicing.
* Use strides (step values) to skip rows or columns.
* Understand the difference between a View and a Copy.
* Know when to use the `.copy()` method.
* Avoid common mistakes when modifying sliced arrays.

---

# Introduction

In previous lectures, we learned how to create NumPy arrays.

Creating an array is only the first step.

The next question is:

> **How do we access the data stored inside the array?**

Suppose we have a dataset containing thousands of students.

Sometimes we only need:

* one student's record,
* one column,
* a few rows,
* or every second record.

Instead of creating a new array every time, NumPy provides powerful tools like:

* Indexing
* Slicing
* Strides

These allow us to access exactly the data we need.

---

# Creating a NumPy Array

The instructor first creates a 3 × 3 NumPy array.

```python
import numpy as np

arr = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])
```

## Understanding the Code

### Line 1

```python
import numpy as np
```

Imports the NumPy library.

Instead of writing `numpy` every time, we use the shorter name `np`.

---

### Line 2

```python
arr = np.array(...)
```

Creates a NumPy array.

The variable `arr` now stores a **two-dimensional array (matrix).**

---

### What does a 2D Array look like?

```
        Column

        0    1    2
      ----------------
Row 0 | 10 | 20 | 30 |
Row 1 | 40 | 50 | 60 |
Row 2 | 70 | 80 | 90 |
```

Notice that:

* Rows go vertically.
* Columns go horizontally.

Every element has two positions:

```
(Row Number, Column Number)
```

---

# What is Indexing?

Indexing means accessing **one specific element** from an array.

Think of it like finding a student's seat in a classroom.

You need:

* Row Number
* Column Number

to find the student.

The same idea applies to NumPy arrays.

---

# Positive Indexing

Python always starts counting from **0**, not 1.

```
Column

0   1   2
```

Similarly,

```
Rows

0
1
2
```

This is called **Zero-Based Indexing**.

---

## Example

```python
print(arr[0,1])
```

### Step-by-Step Explanation

```
Row 0
```

means the first row.

```
10 20 30
```

```
Column 1
```

means the second column.

```
10 20 30
   ↑
```

Therefore,

Output

```
20
```

---

## Another Example

```python
print(arr[2,2])
```

Row 2

```
70 80 90
```

Column 2

```
70 80 90
      ↑
```

Output

```
90
```

---

# Important Note

Python indexing always starts from **0**.

| Index | Position |
| ----- | -------- |
| 0     | First    |
| 1     | Second   |
| 2     | Third    |

This rule applies to lists, tuples, strings, and NumPy arrays.

---

# Negative Indexing

Sometimes we want to access elements from the **end** instead of the beginning.

Python allows this using **negative indexing**.

```
-3   -2   -1

10   20   30
```

Meaning:

```
-1 → Last element

-2 → Second last

-3 → Third last
```

---

## Example

```python
print(arr[-1,-2])
```

### Explanation

Last row

```
70 80 90
```

Second-last column

```
70 80 90
   ↑
```

Output

```
80
```

---

## Another Example

```python
print(arr[-3,-3])
```

Third-last row

↓

First row

Third-last column

↓

First column

Output

```
10
```

---

# Memory Trick

Positive indexing

```
0 → 1 → 2
```

Negative indexing

```
-3 ← -2 ← -1
```

Positive starts from the front.

Negative starts from the back.

---

# What is Slicing?

Indexing gives us **one element**.

Slicing gives us **multiple elements**.

Imagine cutting a slice of a cake.

You don't take the whole cake.

You only take the required portion.

Similarly, slicing selects only the required part of an array.

---

# Slicing Syntax

```python
array[row_start:row_end,
      column_start:column_end]
```

---

## Example

```python
arr[0:2,1:3]
```

Let's understand this carefully.

### Rows

```
0:2
```

means

Start at row 0.

Stop before row 2.

Rows selected:

```
0

1
```

---

### Columns

```
1:3
```

means

Start at column 1.

Stop before column 3.

Columns selected

```
1

2
```

---

Selected area

```
10 [20 30]

40 [50 60]

70 80 90
```

Output

```
[[20 30]
 [50 60]]
```

---

# Very Important Rule

Python slicing follows this rule:

```
Start Index → Included

Ending Index → NOT Included
```

This is one of the most important rules in Python.

---

# What are Strides?

Sometimes we don't want every row or every column.

We want to skip some of them.

This skipping is called a **Stride** or **Step Size**.

---

## Syntax

```python
array[::step]
```

---

## Example

```python
arr[::2,::2]
```

means

Take every **second row**.

Take every **second column**.

Rows selected

```
0

2
```

Columns selected

```
0

2
```

Selected values

```
10    30

70    90
```

Output

```
[[10 30]
 [70 90]]
```

---

# Real-Life Example of Strides

Imagine climbing stairs.

If you climb:

```
Step = 1
```

You use every stair.

If you climb:

```
Step = 2
```

You skip one stair each time.

This is exactly how NumPy strides work.

---

# View vs Copy (Most Important Part of This Lecture)

This is the concept that confuses many beginners.

The instructor explains that when we create a slice, NumPy **does not create a new array**.

Instead, it creates a **View**.

---

## What is a View?

A View is simply another way of looking at the **same data**.

Example

```python
slice_array = arr[:2,:2]
```

Many beginners think this creates a new array.

It does **not**.

Both variables point to the same memory.

```
Original Array

        │

        ▼

     Memory

     ▲     ▲

     │     │

arr   slice_array
```

---

## Modifying a View

```python
slice_array[0,0] = 999
```

Since both variables share the same memory,

the original array also changes.

Original array becomes

```
999 20 30

40 50 60

70 80 90
```

Although we changed only `slice_array`, the original array was modified because a View shares memory with its parent array.

---

# Why Does NumPy Use Views?

Creating copies of large datasets would consume a lot of memory.

Views are much faster and more memory-efficient because they reuse the same data instead of duplicating it.

---

# Creating a Copy

If you do **not** want changes to affect the original array, create a copy.

```python
copy_array = arr[:2,:2].copy()
```

Now `copy_array` has its own memory.

```
Original Memory

Separate Memory
```

Changing

```python
copy_array[0,0] = 555
```

does **not** change the original array.

---

# View vs Copy Comparison

| View                    | Copy                       |
| ----------------------- | -------------------------- |
| Shares memory           | Own memory                 |
| Faster                  | Slightly slower            |
| Less memory             | More memory                |
| Changes affect original | Original remains unchanged |

---

# Common Beginner Mistakes

❌ Thinking Python indexing starts from 1.

✅ Python indexing starts from 0.

---

❌ Forgetting that the ending index is excluded in slicing.

✅ The ending index is never included.

---

❌ Assuming slices are independent arrays.

✅ Slices are Views unless `.copy()` is used.

---

# Practice Questions

### Question 1

What is the output?

```python
print(arr[0,2])
```

Answer

```
30
```

---

### Question 2

What is the output?

```python
print(arr[-1,-1])
```

Answer

```
90
```

---

### Question 3

What is the output?

```python
print(arr[1:3,0:2])
```

Try it yourself before checking the answer.

---

### Question 4

What will happen if you modify a View?

Answer:

The original array will also change.

---

### Question 5

How can you prevent changes from affecting the original array?

Answer:

Use the `.copy()` method.

---

# Key Takeaways

* Python uses zero-based indexing.
* Negative indexing starts from the end of the array.
* Slicing selects a portion of an array.
* The ending index is excluded in slicing.
* Strides allow you to skip rows or columns.
* Slices create Views by default.
* Views share memory with the original array.
* Use `.copy()` to create an independent array.

---

# Lecture Summary

This lecture introduced the fundamental techniques for accessing and manipulating NumPy arrays.

We learned how to access individual elements using indexing, retrieve groups of elements using slicing, skip rows and columns using strides, and understand the critical difference between Views and Copies.

These concepts are foundational for Machine Learning and Artificial Intelligence because almost every AI dataset is processed using NumPy arrays.

Mastering these concepts will make future topics like data preprocessing, feature selection, and dataset manipulation much easier.

---

# Quick Revision (30 Seconds)

✔ Indexing accesses a single element.

✔ Python indexing starts from **0**.

✔ Negative indexing starts from the end.

✔ Slicing selects multiple elements.

✔ Ending index is excluded.

✔ Strides skip rows or columns.

✔ A slice is a View by default.

✔ Use `.copy()` to create an independent array.

---
