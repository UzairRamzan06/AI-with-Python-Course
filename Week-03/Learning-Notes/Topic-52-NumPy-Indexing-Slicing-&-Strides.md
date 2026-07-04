# 📘 Artificial Intelligence Using Python (DigiSkills.pk)

## Week 03 – Video Lecture 52

### **Topic: NumPy Indexing, Slicing & Strides**

This is one of the **most important NumPy lectures** because almost every AI, Machine Learning, and Data Science project involves selecting and manipulating data from arrays. If you master indexing, slicing, and strides now, many future topics will feel much easier.

---

# 🎯 Learning Objectives

After this lecture, you should be able to:

* Access a single element from a NumPy array.
* Use positive and negative indexing.
* Slice rows and columns.
* Skip rows or columns using strides (step size).
* Understand the difference between a **View** and a **Copy**.
* Know when to use `.copy()`.

---

# 🧠 Simple Explanation (Imagine It Like a Classroom)

Imagine a classroom with **3 rows** and **3 columns** of students.

```
        Column
        0    1    2
      ----------------
Row 0 | 10 | 20 | 30 |
Row 1 | 40 | 50 | 60 |
Row 2 | 70 | 80 | 90 |
```

This is exactly our NumPy array.

```python
import numpy as np

arr = np.array([
    [10,20,30],
    [40,50,60],
    [70,80,90]
])
```

Think of it as a table.

Rows go downward.

Columns go sideways.

---

# Part 1 — Indexing (Access One Element)

## Syntax

```python
array[row][column]
```

or

```python
array[row, column]
```

Both work.

---

### Example 1

```python
print(arr[0,1])
```

Question:

Which row?

```
0
```

👉 First row

Which column?

```
1
```

👉 Second column

```
10  20  30
    ↑
```

Output

```
20
```

---

### Example 2

```python
print(arr[2,2])
```

Row 2

↓

```
70 80 90
      ↑
```

Output

```
90
```

---

## ✅ Rule to Remember

> **Python indexing always starts from 0.**

| Index | Meaning |
| ----- | ------- |
| 0     | First   |
| 1     | Second  |
| 2     | Third   |

---

# Part 2 — Negative Indexing

Instead of counting from the beginning...

You can count **from the end**.

Example

```
Index

-3   -2   -1

10   20   30
```

So

```
-1 → Last

-2 → Second Last

-3 → Third Last
```

---

Example

```python
print(arr[-1,-2])
```

Last row

```
70 80 90
```

Second-last column

```
80
```

Output

```
80
```

---

Another example

```python
print(arr[-3,-3])
```

Third-last row

↓

First row

Third-last column

↓

First column

```
10
```

Output

```
10
```

---

# Easy Memory Trick 🎯

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

# Part 3 — Slicing

Sometimes we don't need just **one element**.

We need **a group of elements**.

That's called **Slicing**.

---

Syntax

```python
array[row_start:row_end,
      col_start:col_end]
```

---

Example

```python
arr[0:2,1:3]
```

Let's understand carefully.

Rows

```
0:2

includes

0
1

NOT 2
```

Columns

```
1:3

includes

1
2

NOT 3
```

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

# ⭐ Golden Rule of Slicing

```
Start → Included

End → NOT Included
```

Always remember:

```
[start:end)
```

The ending index is excluded.

---

# Memory Trick

Think of slicing like booking seats.

```
Seat 0

Seat 1

Seat 2

Seat 3
```

You say

```
0:3
```

You stop **before** seat 3.

So you get

```
0

1

2
```

---

# Part 4 — Strides (Step Size)

This is called **Stepping**.

Instead of taking every element...

You jump.

Syntax

```python
array[::step]
```

---

Example

```python
arr[::2,::2]
```

means

Take

Every

Second

Row

AND

Every

Second

Column

---

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

Selected elements

```
10     30

70     90
```

Output

```
[[10 30]
 [70 90]]
```

---

## Easy Way to Remember

Imagine climbing stairs.

```
Step = 1

Every stair

Step = 2

Skip one stair

Step = 3

Skip two stairs
```

Exactly the same idea.

---

# Part 5 — View vs Copy ⭐⭐⭐ (Very Important)

This is the most important concept in today's lecture.

Many beginners make mistakes here.

---

Suppose

```python
slice_array = arr[:2,:2]
```

Did Python create a new array?

❌ No

It created a **View**.

Think of it like a **window** into the original array.

```
Original Array

↓

View

Both point to same data
```

---

Now

```python
slice_array[0,0]=999
```

Question

Will original change?

✅ YES

Because

```
View

=

Original Memory
```

Both share the same memory.

---

Example

Original

```
10 20 30

40 50 60

70 80 90
```

After

```python
slice_array[0,0]=999
```

Original becomes

```
999 20 30

40 50 60

70 80 90
```

Even though you modified only the slice.

---

# Real-life Analogy

Imagine a mirror.

```
Original Person

↓

Mirror
```

If the original person smiles,

Mirror smiles.

They are connected.

A View behaves similarly—it reflects the original data.

---

# Part 6 — Copy

If you don't want the original array to change...

Use

```python
copy()
```

Example

```python
copy_array = arr[:2,:2].copy()
```

Now

```python
copy_array[0,0]=555
```

Original

```
10 20 30

40 50 60

70 80 90
```

Still remains

```
10 20 30

40 50 60

70 80 90
```

Because

```
Copy

=

Separate Memory
```

---

# Memory Trick

## View

```
One Memory

Original

↓

View

Both connected
```

---

## Copy

```
Original Memory

Separate Memory

No connection
```

---

# View vs Copy Comparison

| View             | Copy                     |
| ---------------- | ------------------------ |
| Shares memory    | Own memory               |
| Fast             | Slightly slower          |
| Changes original | Does not change original |
| Uses less memory | Uses more memory         |

---

# Complete Concept Map

```
NumPy Array
│
├── Indexing
│      │
│      ├── Positive
│      └── Negative
│
├── Slicing
│      │
│      └── Start : End
│
├── Strides
│      │
│      └── Step Size
│
└── Slice Result
       │
       ├── View
       └── Copy
```

---

# Practice Questions

### Q1

What is the output?

```python
arr=np.array([
[10,20,30],
[40,50,60],
[70,80,90]
])

print(arr[1,2])
```

Answer

```
60
```

---

### Q2

Output?

```python
print(arr[-1,-1])
```

Answer

```
90
```

---

### Q3

Output?

```python
print(arr[0:2,0:2])
```

Answer

```
[[10 20]
 [40 50]]
```

---

### Q4

Output?

```python
print(arr[::2,::2])
```

Answer

```
[[10 30]
 [70 90]]
```

---

### Q5

Which one changes the original array?

A)

```python
slice=arr[:2,:2]
```

B)

```python
slice=arr[:2,:2].copy()
```

Answer

✅ A

---

# Mini Practice

Create this array

```python
import numpy as np

arr=np.array([
[1,2,3],
[4,5,6],
[7,8,9]
])
```

Try these yourself:

```python
arr[0,2]

arr[2,0]

arr[-1,-2]

arr[:2,:2]

arr[1:3,1:3]

arr[::2,::2]
```

Then experiment with:

```python
slice_arr=arr[:2,:2]

slice_arr[0,0]=100
```

Observe the original array.

Next,

```python
copy_arr=arr[:2,:2].copy()

copy_arr[0,0]=500
```

Observe the difference.

---

# Flashcards

**Q:** Where does Python indexing start?
**A:** 0

**Q:** What does `-1` represent?
**A:** Last element

**Q:** Does slicing include the ending index?
**A:** No

**Q:** What is a stride?
**A:** The step size used while selecting elements.

**Q:** Does a View share memory with the original array?
**A:** Yes

**Q:** Does `.copy()` create separate memory?
**A:** Yes

---

# 30-Second Revision

* Python indexing starts from **0**.
* Negative indexing starts from the **end** (`-1` is the last element).
* Slicing uses `start:end`, where the **end is excluded**.
* Strides (`::step`) let you skip elements.
* A sliced array is a **View** by default, so changes affect the original.
* Use `.copy()` to create an independent copy that can be modified safely.

---

# 💡 Mentor's Tip

This lecture introduces concepts you'll use constantly in AI. Whenever you work with datasets, you'll frequently select specific rows, columns, or subsets of data. Make sure you're comfortable with indexing, slicing, strides, and especially the difference between **Views** and **Copies**—it will save you from subtle bugs later in the course.
