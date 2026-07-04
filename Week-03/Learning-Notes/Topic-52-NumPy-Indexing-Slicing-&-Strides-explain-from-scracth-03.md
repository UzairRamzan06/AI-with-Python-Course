Perfect! We'll build Lecture 52 exactly like a **GitHub learning journal**, not like textbook notes.

---

# 📘 Artificial Intelligence Using Python

### Platform: DigiSkills.pk

**Week:** 03
**Lecture:** 52

# 🎓 Topic 52: NumPy Indexing, Slicing & Strides (Simple Explanation)

---

## 🔄 Before We Start

In the **previous lecture (Topic 51)**, I learned different ways to **create NumPy arrays** using functions like:

* `np.array()`
* `np.zeros()`
* `np.ones()`
* `np.full()`
* `np.arange()`
* `np.linspace()`
* `np.eye()`
* `np.diag()`

At that time, we only learned **how to create arrays**.

But after creating an array, a new question comes into my mind:

> **"How can I access a specific value or a specific part of that array?"**

That's exactly what today's lecture is about.

Today, I learned how to:

* Access a single value.
* Access multiple values.
* Skip rows and columns.
* Understand why changing a sliced array sometimes changes the original array too.

This lecture is one of the most important NumPy lectures because almost every Machine Learning and AI project involves selecting specific data from large datasets.

---

# Introduction

Imagine you have a classroom with 100 students.

Sometimes you want:

* only Student #15
* only the first row
* only the last column
* every second student
* only the top-left portion

Instead of creating new arrays every time, NumPy gives us powerful techniques to access exactly the data we need.

Those techniques are:

* Indexing
* Slicing
* Strides

These are used everywhere in AI because datasets are usually stored as NumPy arrays.

---

# Concept 1: Understanding Our Array

Throughout this lecture, the instructor used the following 3×3 array.

```python
import numpy as np

arr = np.array([
    [10,20,30],
    [40,50,60],
    [70,80,90]
])
```

Instead of looking at it like code, I understand it better as a table.

```
        Column

        0    1    2
      ----------------
Row 0 | 10 | 20 | 30 |
Row 1 | 40 | 50 | 60 |
Row 2 | 70 | 80 | 90 |
```

Every value has two positions:

```
(Row Number, Column Number)
```

For example,

```
20

↓

(Row 0, Column 1)
```

and

```
90

↓

(Row 2, Column 2)
```

---

### 💻 Code Explanation

```python
arr = np.array([
    [10,20,30],
    [40,50,60],
    [70,80,90]
])
```

### What does this code do?

* Creates a **2-dimensional NumPy array**.
* It has:

  * **3 rows**
  * **3 columns**
* Every value can be accessed using its row and column number.

---

## 🧠 Memory Trick

Think of a NumPy array like an **Excel sheet**.

Rows go downward.

Columns go sideways.

Every cell has an address.

---

# Concept 2: What is Indexing?

Indexing simply means:

> **Accessing one specific element from an array.**

Instead of printing the whole array,

we can print only the value we need.

---

### Example

```python
print(arr[0,1])
```

Let's understand this carefully.

```
Row 0

↓

10 20 30
```

Now,

```
Column 1

↓

10 20 30
   ↑
```

The selected value becomes

```
20
```

Output

```
20
```

---

### Another Example

```python
print(arr[2,2])
```

```
Row 2

↓

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

### What I Learned

Python always starts counting from **0**.

Not from 1.

This rule applies everywhere in Python.

Whether it is:

* Lists
* Strings
* Tuples
* NumPy Arrays

everything starts from **0**.

---

## 🧠 Memory Trick

```
Python never says:

1 2 3

It always says

0 1 2
```

Whenever I create an array,

my first element is always at index **0**.

---

# Concept 3: Negative Indexing

Until now,

I was accessing elements from the beginning.

But Python also allows me to access elements from the end.

This is called **Negative Indexing**.

Instead of counting like this

```
0

1

2
```

I can count backwards.

```
-3

-2

-1
```

Here,

```
-1

↓

Last element
```

```
-2

↓

Second last
```

```
-3

↓

Third last
```

---

### Example

```python
print(arr[-1,-2])
```

Let's understand it.

```
Last Row

↓

70 80 90
```

Second last column

```
70 80 90
   ↑
```

Output

```
80
```

---

### Another Example

```python
print(arr[-3,-3])
```

Third last row means

```
First Row
```

Third last column means

```
First Column
```

Output

```
10
```

---

## 🧠 Memory Trick

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

# 📌 Important Notes

✅ Python indexing starts from **0**.

✅ Every element in a 2D array has:

* Row Number
* Column Number

✅ Negative indexing starts from the end of the array.

---

# ⚠️ Common Beginner Mistakes

❌ Thinking indexing starts from **1**.

Correct:

It always starts from **0**.

---

❌ Confusing rows with columns.

Remember:

```
Rows

↓

Vertical

Columns

→

Horizontal
```

---

❌ Thinking `-1` means the first element.

Actually,

```
-1

↓

Last Element
```

---

# 📊 Quick Comparison

| Positive Indexing       | Negative Indexing                |
| ----------------------- | -------------------------------- |
| Starts from beginning   | Starts from end                  |
| First index = 0         | Last index = -1                  |
| Easy for forward access | Useful for accessing last values |

---

# 📝 Easy Way to Remember

Imagine reading a book.

Positive indexing means

```
Read

Page 1

↓

Page 2

↓

Page 3
```

Negative indexing means

```
Start from

Last Page

↓

Second Last

↓

Third Last
```

Exactly the same idea.

---

## 🌟 My Observation

Today I realized that creating a NumPy array is only the first step. The real power comes from knowing **how to access the data inside it**. Before this lecture, I only knew that arrays store values, but I didn't know how to retrieve a specific value using row and column positions. I also found negative indexing very useful because it lets me access elements from the end without calculating the last index manually. One important thing I'll always remember is that **Python starts counting from 0**, not 1. I believe this understanding will help me a lot when working with datasets in Machine Learning and Artificial Intelligence.

---

> ✅ **End of Part 1**

In **Part 2**, we'll continue with:

* ✂️ What is Slicing?
* 📏 Slicing Rules (`start:end`)
* ⏭️ Strides (Step Size)
* 💻 Code Examples
* 🧠 Memory Tricks
* 📊 Comparisons
* 🌟 My Learning Journey continues...

---

## 🔄 Before We Start

In **Part 1**, I learned:

* How to access single elements using **indexing**
* How positive indexing works (0, 1, 2...)
* How negative indexing works (-1, -2, -3...)
* How NumPy arrays behave like tables with rows and columns

Now in this part, I will learn something more powerful:

> 👉 How to access **multiple values at once** using **Slicing**
> 👉 How to skip elements using **Strides**

These concepts are very important in AI because we rarely work with single values — we usually work with **chunks of data**.

---

# ✂️ Concept 1: What is Slicing?

Slicing means:

> **Selecting a portion (subset) of an array instead of a single element**

Instead of taking one value, we take a **range of values**.

Think of it like:

📖 Cutting a slice of cake
You don’t take the whole cake — only a portion.

---

## 📌 Slicing Syntax

```python
array[row_start:row_end, column_start:column_end]
```

---

## 💻 Example from Lecture

```python id="slice1"
arr[0:2, 1:3]
```

Now let’s break it slowly.

---

### 🔹 Step 1: Rows (0:2)

```text
0:2 means:

Start = 0
End = 2 (NOT included)
```

So rows selected are:

```text
Row 0
Row 1
```

❗ Important Rule:

> The end index is ALWAYS excluded in Python slicing.

---

### 🔹 Step 2: Columns (1:3)

```text
1:3 means:

Start = 1
End = 3 (NOT included)
```

So columns selected are:

```text
Column 1
Column 2
```

---

### 🧠 Final Selection

From the array:

```text
10  20  30
40  50  60
70  80  90
```

We select:

```text
20  30
50  60
```

---

### 📤 Output

```python
[[20 30]
 [50 60]]
```

---

## 🧠 Memory Trick (Slicing Rule)

> **Start is included, End is excluded**

Think of it like:

```text
Start → Step inside
End → Stop before reaching
```

---

## ⚠️ Common Mistake

❌ Beginners think `0:2` means rows 0, 1, 2
✅ Correct: It means only 0 and 1

---

# ⏭️ Concept 2: What are Strides?

Now we move to a very powerful concept.

Strides means:

> **Skipping elements using step size**

Instead of taking every value, we take every 2nd, 3rd, etc.

---

## 📌 Syntax

```python
array[::step]
```

or for 2D:

```python
array[::step_row, ::step_column]
```

---

## 💻 Example from Lecture

```python id="stride1"
arr[::2, ::2]
```

---

### 🔹 Step 1: Row stride `::2`

This means:

```text
Take every 2nd row
```

So rows selected:

```text
Row 0
Row 2
```

(Row 1 is skipped)

---

### 🔹 Step 2: Column stride `::2`

This means:

```text
Take every 2nd column
```

So columns selected:

```text
Column 0
Column 2
```

(Column 1 is skipped)

---

### 🧠 Final Selection

From:

```text
10  20  30
40  50  60
70  80  90
```

We get:

```text
10  30
70  90
```

---

### 📤 Output

```python
[[10 30]
 [70 90]]
```

---

## 🧠 Memory Trick (Strides)

> **Stride = Step Jump**

Think:

* step = 1 → take everything
* step = 2 → skip 1
* step = 3 → skip 2

Like climbing stairs:

```text
Step 1 → normal walking
Step 2 → skipping one stair
Step 3 → skipping two stairs
```

---

## 📊 Comparison: Slicing vs Strides

| Feature | Slicing          | Strides                 |
| ------- | ---------------- | ----------------------- |
| Purpose | Select range     | Skip elements           |
| Syntax  | start:end        | ::step                  |
| Control | Boundaries       | Jump size               |
| Output  | Continuous block | Pattern-based selection |

---

## ⚠️ Common Mistakes

❌ Thinking `::2` means take only 2 elements
✅ It means take every 2nd element

---

❌ Confusing slicing and strides
Remember:

* slicing → range
* stride → skipping

---

# 🔗 Connection with Previous Lecture

In Part 1, I learned how to select:

* single values (indexing)
* last values (negative indexing)

Now I learned:

* multiple values (slicing)
* skipping values (strides)

So now I can access **any part of an array**, not just one element.

This is very important because real-world datasets are large, and we rarely work with single values.

---

## 🌟 My Observation

In this part of the lecture, I realized that NumPy is not just about storing numbers — it is about **controlling data efficiently**. Slicing helped me understand how we can select a specific portion of an array, while strides showed me how powerful it is to skip unnecessary data and focus only on what we need. Before this lecture, I thought selecting data would always require loops, but now I understand that NumPy provides built-in ways to do this in a much cleaner and faster way. I believe this concept will be very useful when we start working with real datasets in Machine Learning, where selecting features and samples is a very common task.

---

> 🚀 **End of Part 2**

In **Part 3**, we will cover:

* 🧠 View vs Copy (MOST IMPORTANT CONCEPT)
* 💻 `.copy()` method
* ⚠️ Common beginner mistakes
* 📌 Important notes from lecture
* 🔥 Why changes sometimes affect original array

---


## 🔄 Before We Start

In **Part 1**, I learned how to access single elements using indexing.

In **Part 2**, I learned how to:

* Select multiple elements using **slicing**
* Skip elements using **strides**

Now in this part, I will learn something VERY IMPORTANT:

> 👉 Why sometimes changing a sliced array also changes the original array

This is one of the most confusing concepts for beginners in NumPy.

It is called:

> **View vs Copy**

---

# 🧠 Concept 1: View vs Copy in NumPy

When I create a slice like this:

```python id="view1"
slice_array = arr[0:2, 0:2]
```

I might think:

> “NumPy created a new array for me.”

But actually, NumPy does something smarter.

👉 It creates a **VIEW**, not a new array.

---

## 📌 What is a View?

A **View** means:

> Both variables (original array and slice) point to the SAME memory.

So:

```text id="mem1"
Original Array  ───┐
                   ├── Same Memory
Slice (View)    ───┘
```

---

## 💻 Example from Lecture

```python id="view2"
slice_array = arr[:2, :2]
```

Now we modify the slice:

```python id="view3"
slice_array[0, 0] = 999
```

---

## ⚠️ What happens?

Even though we changed only `slice_array`…

👉 The ORIGINAL array also changes.

---

### 🧾 Example Result

Original array becomes:

```text id="result1"
999  20  30
40   50  60
70   80  90
```

---

## 🧠 Why does this happen?

Because:

> Slice is not a new array — it is just a **window** into the original array.

So when we change the window, the original data also changes.

---

## 🧠 Memory Trick (View)

> **View = Same Memory, Different Access**

Think like this:

```text id="mirror1"
Mirror image example:

You = Original array
Mirror = Slice (View)

If you move → mirror moves too
```

---

## ⚠️ Common Mistake

❌ Thinking slicing creates a new independent array
✅ Actually, it creates a VIEW (shared memory)

---

# 🧠 Concept 2: How to Create a Copy

If I want to avoid changing the original array…

I must explicitly create a **COPY**.

---

## 💻 Example

```python id="copy1"
copy_array = arr[:2, :2].copy()
```

---

## 📌 What does `.copy()` do?

It tells NumPy:

> “Create a completely new array in memory.”

So now:

```text id="mem2"
Original Array  ─── Memory A
Copy Array      ─── Memory B (separate)
```

---

## 💻 Modifying Copy

```python id="copy2"
copy_array[0, 0] = 555
```

---

## 🧾 Result

### Original array (unchanged):

```text id="orig1"
10  20  30
40  50  60
70  80  90
```

### Copy array (changed):

```text id="copyout1"
555 20
40  50
```

---

## 🧠 Memory Trick (Copy)

> **Copy = Separate Memory**

Think:

* View → mirror reflection
* Copy → photocopy paper

---

# 📊 Quick Comparison: View vs Copy

| Feature            | View                       | Copy               |
| ------------------ | -------------------------- | ------------------ |
| Memory             | Shared                     | Separate           |
| Performance        | Faster                     | Slightly slower    |
| Effect on original | Yes                        | No                 |
| Use case           | Large datasets, efficiency | Safe modifications |

---

# ⚠️ Important Notes from Lecture

✔ Slicing in NumPy does NOT create a new array by default
✔ It creates a VIEW of the original array
✔ Any change in view affects original array
✔ Use `.copy()` when independent data is needed

---

# ⚠️ Common Beginner Mistakes

❌ Assuming slice is independent
❌ Forgetting `.copy()` when modifying data
❌ Not realizing original array changed unexpectedly

---

# 🔗 Connection with Previous Lectures

Now I understand the full workflow of NumPy arrays:

* **Lecture 51:** How to create arrays
* **Lecture 52 Part 1:** How to access single values (indexing)
* **Lecture 52 Part 2:** How to access multiple values (slicing + strides)
* **Lecture 52 Part 3:** How memory works (view vs copy)

So now I can:

> Create data → Access data → Select data → Control memory behavior

This is exactly how real AI datasets are handled.

---

## 🌟 My Observation

In this part of the lecture, I realized something very important: NumPy is not just about selecting data, it is also about how data is stored in memory. Before this lecture, I assumed that whenever we slice an array, Python creates a completely new copy. But now I understand that NumPy is optimized for performance, so it creates a **view instead of a copy** to save memory and increase speed.

This also helped me understand why sometimes my original data changes unexpectedly. The biggest takeaway for me is that if I want safe and independent data, I must explicitly use `.copy()`.

I believe this concept is extremely important for Machine Learning and Data Science because datasets are large, and memory efficiency matters a lot.

---

> 🚀 **End of Part 3**

In **Part 4 (Final Part)**, we will cover:

* 🧠 Easy revision tricks
* 📌 Practice questions
* 🎯 Quick summary
* 🌟 Final "My Observation" reflection (complete lecture understanding)

---


## 🔄 Before We Start

In the previous parts, I learned:

* How to access single elements (**Indexing**)
* How to access multiple elements (**Slicing**)
* How to skip elements (**Strides**)
* How memory works in NumPy (**View vs Copy**)

Now I will:

> 🎯 Revise everything in a simple way
> 🎯 Practice important questions
> 🎯 Understand the full concept in one flow

This part is all about **revision + clarity + confidence**.

---

# 🧠 Easy Way to Remember Everything

## 📌 1. Indexing (Single Value)

👉 Used to access ONE element

```text id="idx1"
arr[0,1]
```

🧠 Memory Trick:

> Indexing = “Exact Location”

Like finding a seat in a classroom:

* Row number + Column number

---

## 📌 2. Slicing (Range of Values)

👉 Used to access MULTIPLE elements

```text id="slc1"
arr[0:2, 1:3]
```

🧠 Memory Trick:

> Slicing = “Cut a portion”

Important rule:

```text id="rule1"
Start → included  
End → NOT included
```

---

## 📌 3. Strides (Skipping Values)

👉 Used to SKIP elements

```text id="str1"
arr[::2, ::2]
```

🧠 Memory Trick:

> Stride = Step Jump

* step 1 → normal
* step 2 → skip 1
* step 3 → skip 2

---

## 📌 4. View vs Copy (Memory Behavior)

| Concept | Meaning         |
| ------- | --------------- |
| View    | Same memory     |
| Copy    | Separate memory |

🧠 Memory Trick:

* View → Mirror reflection
* Copy → Photocopy

---

# ⚠️ Final Important Notes

✔ Python indexing starts from **0**
✔ Negative indexing starts from the **end (-1)**
✔ Slicing does NOT include end index
✔ Strides skip elements using step size
✔ NumPy slicing creates a **VIEW by default**
✔ `.copy()` creates independent data

---

# ⚠️ Common Beginner Mistakes (Final Review)

❌ Thinking indexing starts from 1
❌ Forgetting that end index is excluded
❌ Confusing slicing with strides
❌ Forgetting `.copy()` and accidentally modifying original data

---

# 📊 Quick Revision Table

| Concept  | Purpose         | Example                |
| -------- | --------------- | ---------------------- |
| Indexing | Single value    | `arr[0,1]`             |
| Slicing  | Range           | `arr[0:2,1:3]`         |
| Strides  | Skipping        | `arr[::2,::2]`         |
| View     | Shared memory   | slice changes original |
| Copy     | Separate memory | `.copy()`              |

---

# 🎯 Practice Questions

## 🧪 Q1: Indexing

What is the output?

```python id="q1"
arr[2,2]
```

✔ Answer:

```text
90
```

---

## 🧪 Q2: Negative Indexing

```python id="q2"
arr[-1,-1]
```

✔ Answer:

```text
90
```

---

## 🧪 Q3: Slicing

```python id="q3"
arr[0:2, 0:2]
```

✔ Answer:

```text
[[10 20]
 [40 50]]
```

---

## 🧪 Q4: Strides

```python id="q4"
arr[::2, ::2]
```

✔ Answer:

```text
[[10 30]
 [70 90]]
```

---

## 🧪 Q5: View vs Copy

If I do:

```python id="q5"
slice = arr[:2,:2]
slice[0,0] = 999
```

What happens?

✔ Answer:

👉 Original array ALSO changes

---

# 🧠 Final Easy Summary

If I simplify everything I learned:

* Indexing → one value
* Slicing → group of values
* Strides → skipping values
* View → shared memory
* Copy → independent memory

---

# 🔗 Full Connection of Lecture 52

Today I learned the complete way to access NumPy arrays:

* First, I learned how to pick a single value (Indexing)
* Then I learned how to pick multiple values (Slicing)
* Then I learned how to skip values (Strides)
* Finally, I learned how NumPy handles memory (View vs Copy)

So now I can confidently say:

> I know how to **create, access, and control data inside NumPy arrays**

This is a foundational skill for all AI and Machine Learning work.

---

## 🌟 My Observation (Final Reflection)

After completing this lecture, I feel that my understanding of NumPy has become much stronger. Earlier, I only knew that arrays store numbers, but now I understand how powerful they are for accessing and manipulating data efficiently.

The most important thing I learned is the difference between a **View and a Copy**. This changed my understanding completely because I used to think slicing always creates a new array, but now I know it only creates a reference to the original data. This can easily cause unexpected changes if I am not careful.

Another important takeaway for me is that NumPy is designed for performance. That is why it avoids unnecessary copying and uses views instead.

I believe this lecture is very important for my journey in Artificial Intelligence and Machine Learning because almost every dataset operation depends on these concepts.

---

# 🚀 End of Lecture 52

✔ Now I can confidently move to the next topic in NumPy with a strong foundation.

---


