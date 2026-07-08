# 📘 Artificial Intelligence Using Python

**Platform:** DigiSkills.pk

**Week:** 03

**Lecture:** 56

# 🎓 Topic 56: Pandas Indexing & Selection - `.loc` & `.iloc` (Simple Explanation)

---

# Before We Start

In the **previous lecture (Topic 55)**, we learned how to create a **Pandas DataFrame**, load data from a CSV file, and inspect it using methods like `.info()`, `.shape`, `.dtypes`, and `.describe()`.

At that point, we knew **how to load a dataset**, but we hadn't learned **how to access specific parts of it**.

Think of it like this:

* In the previous lecture, you learned how to **open a book** 📖.
* In today's lecture, you'll learn how to **find a specific page, paragraph, or sentence** inside that book.

This is exactly what **indexing and selection** are about.

When working with AI and Machine Learning datasets, you rarely need the entire dataset all at once. Instead, you often need to:

* Select certain rows.
* Select specific columns.
* Filter records that meet a condition.
* Modify only part of the data.

That's why learning `.loc`, `.iloc`, and boolean filtering is an essential next step.

---

# Introduction

Imagine you have an Excel sheet containing 100,000 employee records.

You don't always want to look at every employee.

Sometimes you only want:

* Employees older than 30.
* Employees from Lahore.
* Employees with salaries above 100,000.
* Only the **Name** and **Salary** columns.

Pandas provides powerful tools to do exactly this.

Today's lecture introduces four important techniques:

1. `.loc` → Select data using **labels (names)**.
2. `.iloc` → Select data using **integer positions (numbers)**.
3. Boolean filtering → Select rows that satisfy a condition.
4. Safe assignment with `.loc` → Modify only selected values.

These are among the most frequently used operations in data analysis and AI preprocessing.

---

# Concept 1: Understanding Indexing

Before learning `.loc` and `.iloc`, let's understand **indexing**.

An **index** is simply the identifier for each row.

Our DataFrame:

| Index | Name    | Age | City     | Salary |
| ----: | ------- | --: | -------- | -----: |
|     0 | Alice   |  25 | New York |  70000 |
|     1 | Bob     |  30 | Paris    |  80000 |
|     2 | Charlie |  22 | London   |  60000 |
|     3 | David   |  35 | Berlin   |  90000 |

Notice the numbers on the left:

```
0
1
2
3
```

These are the **row indexes**.

The column names are:

```
Name
Age
City
Salary
```

These are the **column labels**.

---

## Memory Trick

**Index = Row Number**

**Label = Column Name**

---

# Concept 2: Creating the DataFrame

## Code

```python
import pandas as pd

# Sample DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 30, 22, 35],
    'City': ['New York', 'Paris', 'London', 'Berlin'],
    'Salary': [70000, 80000, 60000, 90000]
}

df = pd.DataFrame(data)

print("Original DataFrame:\n", df)
```

---

## Line-by-Line Explanation

### Line 1

```python
import pandas as pd
```

### What does it do?

Imports the Pandas library.

`pd` is just a short nickname for Pandas.

---

### Creating the dictionary

```python
data = {
```

Creates a Python dictionary.

Each **key** becomes a column.

Each **list** becomes the values in that column.

Example:

```
Name
↓

Alice
Bob
Charlie
David
```

---

### Creating the DataFrame

```python
df = pd.DataFrame(data)
```

Converts the dictionary into a table.

Think of it as:

```
Dictionary
      ↓
DataFrame
      ↓
Table
```

---

### Printing

```python
print(df)
```

Displays the complete DataFrame.

Output

```
       Name  Age      City  Salary
0    Alice   25  New York   70000
1      Bob   30     Paris   80000
2  Charlie   22    London   60000
3    David   35    Berlin   90000
```

---

## Why create a DataFrame?

Because AI datasets are usually stored as tables.

Pandas makes working with those tables easy.

---

# Concept 3: Selecting Data with `.loc`

## What is `.loc`?

`.loc` means **location by labels**.

It selects data using:

* Row labels (index labels)
* Column names (labels)

### Syntax

```python
df.loc[row_selection, column_selection]
```

Notice there are **two parts**:

```
df.loc[ rows , columns ]
```

---

## Code

```python
subset_loc = df.loc[1:3, ['Name', 'Salary']]
print("Subset with .loc:\n", subset_loc)
```

---

## Line-by-Line Explanation

### Line 1

```python
subset_loc =
```

Stores the selected data in a new variable.

---

### `df.loc`

Uses label-based selection.

---

### First argument

```python
1:3
```

Means:

Select rows:

```
1
2
3
```

### Important Rule

With `.loc`, **both the starting and ending labels are included**.

```
1:3

↓

1 ✔
2 ✔
3 ✔
```

This is different from normal Python slicing.

---

### Second argument

```python
['Name', 'Salary']
```

Means:

Select only these two columns.

```
Name

Salary
```

---

### Output

```
      Name  Salary
1      Bob   80000
2  Charlie   60000
3    David   90000
```

---

## Why use `.loc`?

Suppose your dataset has 150 columns.

Instead of remembering:

```
Column 57

Column 89
```

You can simply write:

```python
df.loc[:, ['Salary', 'Age']]
```

This is much clearer and easier to maintain.

---

## Memory Trick

**loc → Labels**

Think:

**L in loc = Labels**

---

# Concept 4: Selecting Data with `.iloc`

## What is `.iloc`?

`.iloc` means **integer location**.

It selects rows and columns by **position numbers**, not names.

### Syntax

```python
df.iloc[row_position, column_position]
```

---

## Code

```python
subset_iloc = df.iloc[0:2, 1:3]

print("Subset with .iloc:\n", subset_iloc)
```

---

## Line-by-Line Explanation

### First argument

```python
0:2
```

Rows:

```
0 ✔

1 ✔

2 ✘
```

Why?

Because `.iloc` follows **Python slicing rules**.

The ending position is **not included**.

---

### Second argument

```python
1:3
```

Columns:

```
1 ✔

2 ✔

3 ✘
```

Column positions:

```
0 Name

1 Age

2 City

3 Salary
```

Therefore:

```
Age

City
```

are selected.

---

### Output

```
   Age      City
0   25  New York
1   30     Paris
```

---

## Memory Trick

**iloc → Integer Locations**

Think:

**I in iloc = Integer**

---

# Quick Comparison: `.loc` vs `.iloc`

| Feature             | `.loc`         | `.iloc`                    |
| ------------------- | -------------- | -------------------------- |
| Selects by          | Labels (names) | Integer positions          |
| Rows                | Label/index    | Position                   |
| Columns             | Names          | Position numbers           |
| End value included? | ✅ Yes          | ❌ No (Python slicing)      |
| Easier to read?     | Usually yes    | Good when positions matter |

---

# Concept 5: Boolean Filtering

Sometimes you don't know which row numbers you need.

Instead, you want rows that satisfy a condition.

Example:

"Show employees earning more than 75,000."

This is called **Boolean filtering**.

A **Boolean** value is simply:

* `True`
* `False`

---

## Code

```python
high_salary = df[df['Salary'] > 75000]

print("High Salary Filter:\n", high_salary)
```

---

## Line-by-Line Explanation

### Inner part

```python
df['Salary']
```

Selects the Salary column.

```
70000

80000

60000

90000
```

---

### Condition

```python
> 75000
```

Checks every value.

```
70000 → False

80000 → True

60000 → False

90000 → True
```

Pandas creates a Boolean mask:

```
False

True

False

True
```

---

### Outer brackets

```python
df[ condition ]
```

Keep only rows where the condition is `True`.

---

### Output

```
    Name  Age    City  Salary
1    Bob   30   Paris   80000
3  David   35  Berlin   90000
```

---

## Why is Boolean filtering important?

In real projects, you may need to find:

* Students with marks above 90.
* Patients older than 60.
* Products with low stock.
* Customers from a particular city.

Boolean filtering lets you answer these questions with a single line of code.

---

# Concept 6: Safe Assignment with `.loc`

Sometimes you want to **change** only part of the DataFrame.

Example:

Increase or decrease salaries for certain employees.

---

## Code

```python
df.loc[df['Age'] < 30, 'Salary'] = 65000

print(df.loc[df['Age'] < 30, 'Salary'])
```

---

## Line-by-Line Explanation

### Condition

```python
df['Age'] < 30
```

Checks:

```
25 ✔

30 ✘

22 ✔

35 ✘
```

Boolean mask:

```
True

False

True

False
```

---

### `.loc`

```python
df.loc[ condition , 'Salary' ]
```

Means:

```
Find rows where Age < 30

↓

Modify only the Salary column
```

---

### Assignment

```python
= 65000
```

Replaces the salaries with:

```
65000
```

Only for matching rows.

---

### Output

```
0    65000
2    65000
Name: Salary
```

Notice that only **Alice** and **Charlie** were updated because they are younger than 30.

---

## Why use `.loc` for assignment?

Using `.loc` clearly tells Pandas:

* **Which rows** to change.
* **Which column** to change.

It helps avoid ambiguous operations and makes your code easier to understand.

---

# Why Do Programmers Prefer Column Names?

The instructor recommends using **column labels** instead of numeric positions whenever possible.

Imagine this DataFrame:

```
0 Name

1 Age

2 City

3 Salary
```

Later, someone inserts a new column:

```
0 Name

1 Gender

2 Age

3 City

4 Salary
```

If your code relied on column number `3`, it may now refer to a different column.

Using:

```python
'Salary'
```

still works correctly because the column name hasn't changed.

This makes your code more readable and less prone to errors.

---

# Important Notes

* `.loc` uses labels (row labels and column names).
* `.iloc` uses integer positions.
* `.loc` includes the ending label in a range.
* `.iloc` excludes the ending position, following normal Python slicing.
* Boolean filtering returns only rows where the condition evaluates to `True`.
* `.loc` is the preferred way to update selected values because it is explicit and easier to read.

---

# Common Beginner Mistakes

* Confusing `.loc` and `.iloc`.
* Expecting `.iloc[0:2]` to include row `2` (it does not).
* Forgetting to put column names inside a list when selecting multiple columns with `.loc`.
* Using `=` instead of `==` when writing comparison conditions.
* Assuming boolean filtering changes the original DataFrame—it only returns a filtered view unless you assign the result or modify using `.loc`.

---

# Easy Way to Remember

* **`.loc`** → **L = Labels** (use names).
* **`.iloc`** → **I = Integers** (use positions).
* **Boolean filtering** → `True` rows stay, `False` rows are removed.
* **`.loc` for assignment** → Safely update selected rows and columns.

---

## 🌟 My Observation

> Today I learned that creating a DataFrame is only the beginning. The real power of Pandas comes from selecting exactly the data I need. Before this lecture, I thought I always had to work with the whole table, but now I know I can easily pick specific rows, columns, or records that meet a condition.

> The biggest thing I understood today is the difference between `.loc` and `.iloc`. `.loc` works with labels, while `.iloc` works with numeric positions. I also need to remember that `.loc` includes the ending label, but `.iloc` follows Python slicing and excludes the ending position.

> I also realized why boolean filtering is so useful. Instead of manually searching through thousands of rows, I can let Pandas find only the records that match my condition. This will be extremely helpful when cleaning and preparing datasets for Machine Learning.

---

# Practice Section

## 1. Coding Exercise

Create this DataFrame:

| Name   | Age | City      | Marks |
| ------ | --: | --------- | ----: |
| Ayesha |  21 | Lahore    |    85 |
| Bilal  |  24 | Multan    |    72 |
| Hamza  |  19 | Karachi   |    91 |
| Zara   |  23 | Islamabad |    88 |

Then:

1. Select rows 1 to 3 with only `Name` and `Marks` using `.loc`.
2. Select the first two rows and the `Age` and `City` columns using `.iloc`.
3. Show only students with marks greater than 80.
4. Change the marks of students younger than 20 to `95` using `.loc`.

---

## 2. Output Prediction

What will this print?

```python
import pandas as pd

df = pd.DataFrame({
    "A": [10, 20, 30],
    "B": [40, 50, 60]
})

print(df.iloc[0:2, 0:1])
```

Predict the output before running the code.

---

## 3. Debugging Challenge

Find the mistake:

```python
df.loc[0:2, "Name", "Age"]
```

**Hint:** To select multiple columns with `.loc`, pass the column names as a **list**:

```python
df.loc[0:2, ["Name", "Age"]]
```

---

## 4. MCQs

1. Which method selects data using **column names and row labels**?

   * A. `.iloc`
   * B. `.loc`
   * C. `.shape`
   * D. `.info()`

   **Answer:** B

2. Which method follows normal Python slicing rules?

   * A. `.loc`
   * B. `.iloc`
   * C. `.describe()`
   * D. `.dtypes`

   **Answer:** B

3. What values does a boolean condition produce?

   * A. Strings
   * B. Floats
   * C. `True` or `False`
   * D. Lists

   **Answer:** C

---
