# 📘 Artificial Intelligence Using Python

**Platform:** DigiSkills.pk

**Week:** 03

**Lecture:** 58

# 🎓 Topic 58: Handling Data Types & Type Conversion (Simple Explanation)

---

# Before We Start

In the **previous lecture (Topic 57)**, we learned how to:

* Import data from **CSV, Excel, and JSON** files.
* Export cleaned data back into different file formats.
* Use parameters like `parse_dates`, `dtype`, `usecols`, and `nrows` to make data loading more efficient.

Now that we know **how to load data into a DataFrame**, the next important step is making sure **each column has the correct data type**.

Imagine you receive a dataset where the **Age** column is stored as text instead of numbers.

If Python thinks ages are text, it becomes difficult (or impossible) to calculate:

* Average age
* Maximum age
* Minimum age
* Age comparisons

So today's lecture teaches us how to **check, convert, and optimize data types**, making the data easier to analyze and more memory-efficient.

---

# Introduction

Every value stored in Python has a **data type**.

For example:

| Value   | Data Type        |
| ------- | ---------------- |
| `25`    | Integer (`int`)  |
| `25.5`  | Float (`float`)  |
| `"Ali"` | String (`str`)   |
| `True`  | Boolean (`bool`) |

The same idea applies to Pandas DataFrames.

Each column has a data type.

For example:

| Column   | Data Type       |
| -------- | --------------- |
| Date     | `datetime64`    |
| Sales    | `float64`       |
| Quantity | `float64`       |
| Category | `category`      |
| Region   | `object` (text) |

Choosing the correct data type is important because it affects:

* Memory usage
* Speed
* Data analysis
* Machine Learning preprocessing

---

# Concept 1: Why Do Data Types Matter?

Imagine two columns:

### Correct

| Age |
| --: |
|  20 |
|  25 |
|  30 |

Python knows these are numbers.

You can easily calculate:

```text
Average Age

Maximum Age

Minimum Age
```

---

### Incorrect

| Age  |
| ---- |
| "20" |
| "25" |
| "30" |

Now Python thinks these are **text**.

Instead of mathematics, it treats them as words.

This creates problems during analysis.

---

## Why does this happen?

Data often comes from:

* Excel
* CSV
* Databases

Sometimes numeric values are accidentally stored as text.

Pandas allows us to fix that.

---

# Concept 2: Reading Data with Correct Data Types

## Code

```python
import pandas as pd

df = pd.read_csv(
    "retail_sales.csv",
    parse_dates=["Date"],
    dtype={
        "Category": "category"
    }
)

df.info()
```

---

# Line-by-Line Explanation

## Line 1

```python
import pandas as pd
```

Imports the Pandas library.

---

## Reading the CSV

```python
df = pd.read_csv(
```

Creates a DataFrame by reading the CSV file.

---

### Parameter 1

```python
"retail_sales.csv"
```

The filename to load.

---

### Parameter 2

```python
parse_dates=["Date"]
```

### What does it do?

Converts the **Date** column into a real date/time type.

Instead of:

```text
"2024-01-05"
```

being treated as text,

it becomes

```text
datetime
```

---

## Why is this useful?

Now Pandas understands dates.

You can ask questions like:

* Sales this month
* Sales this year
* Difference between two dates

Without conversion, these operations are much harder.

---

### Parameter 3

```python
dtype={
    "Category": "category"
}
```

This tells Pandas:

> Store the **Category** column as a **category** data type.

---

## Why?

Suppose Category contains only:

```text
Electronics

Clothing

Furniture

Food
```

These values repeat many times.

Instead of storing the complete words thousands of times,

Pandas stores:

```text
1

2

3

4
```

internally.

This saves memory.

---

## Output

```text
Date      datetime64[ns]

Category  category

Sales     float64

Quantity  float64

Profit    float64

Region    object
```

---

## Understanding Each Data Type

### datetime64[ns]

Used for dates and time.

Example:

```text
2024-05-12
```

---

### float64

Decimal numbers.

Example:

```text
500.75
```

---

### category

Stores repeated text efficiently.

Example:

```text
North

South

East

West
```

---

### object

Usually means text (strings).

Example:

```text
Lahore

Karachi

Multan
```

---

# Concept 3: `pd.to_numeric()`

Sometimes a numeric column is mistakenly stored as text.

Example:

| Profit |
| ------ |
| "500"  |
| "700"  |
| "300"  |

Although these look like numbers,

Python may treat them as strings.

---

## Code

```python
df["Profit"] = pd.to_numeric(df["Profit"])
```

---

# Line-by-Line Explanation

### Left side

```python
df["Profit"]
```

This is the column we want to update.

---

### Right side

```python
pd.to_numeric()
```

Converts values into numeric format.

---

### Parameter

```python
df["Profit"]
```

The column to convert.

---

### Assignment

```python
=
```

Stores the converted values back into the same column.

---

## Why use `to_numeric()`?

Imagine this data:

```text
"100"

"250"

"300"
```

These are strings.

After conversion:

```text
100

250

300
```

They become real numbers.

---

## Why didn't the output change?

The lecture's dataset already had:

```text
Profit → float64
```

So converting it again did not change anything.

That is why:

```text
df.info()
```

looked exactly the same before and after.

---

## Real-life Example

Suppose a CSV contains:

```text
Age

"20"

"21"

"22"
```

After:

```python
pd.to_numeric(df["Age"])
```

you can calculate:

```python
df["Age"].mean()
```

---

## Common Beginner Mistake

Many beginners expect:

```python
pd.to_numeric(df["Profit"])
```

to permanently change the column.

It **does not** unless you assign it back:

```python
df["Profit"] = pd.to_numeric(df["Profit"])
```

---

# Concept 4: `astype()`

`astype()` changes the data type of a column.

---

## Code

```python
df["Region"] = df["Region"].astype("category")
```

---

# Line-by-Line Explanation

### Step 1

```python
df["Region"]
```

Selects the Region column.

---

### Step 2

```python
.astype()
```

Means:

> Change the data type.

---

### Parameter

```python
"category"
```

Convert the column into category format.

---

### Assignment

```python
=
```

Store the converted column back.

---

## Why convert Region?

Suppose the Region column contains:

```text
North

South

East

West
```

These four words appear hundreds of times.

Instead of storing:

```text
North

North

North

North
```

again and again,

Pandas stores

```text
1

1

1

1
```

internally.

---

## Result

Before:

```text
Region → object
```

After:

```text
Region → category
```

---

# Concept 5: Memory Usage

The lecture compares memory before and after conversion.

---

## Before Conversion

```text
Memory Usage

73.6 KB
```

---

## After Conversion

```text
Memory Usage

61.3 KB
```

---

## Why did memory decrease?

Because category columns store repeated values more efficiently.

Imagine writing:

```text
Pakistan

Pakistan

Pakistan

Pakistan
```

1000 times.

Instead,

you could store:

```text
1

1

1

1
```

and keep one dictionary:

```text
1 → Pakistan
```

This requires much less memory.

---

# Concept 6: `memory_usage()`

## Code

```python
print(df["Region"].memory_usage(deep=True))
```

---

## What does it do?

Shows how much memory the Region column occupies.

---

### Parameter

```python
deep=True
```

Means:

Calculate the **actual** memory used by the objects inside the column, not just the basic container.

For text columns, `deep=True` provides a more accurate measurement.

---

## Output

```text
2395
```

This value represents the approximate memory (in bytes) used by the `Region` column after conversion.

---

# Why Do Programmers Convert Data Types?

Because correct data types help them:

* Save memory.
* Speed up processing.
* Perform mathematical operations correctly.
* Analyze dates properly.
* Prepare data for Machine Learning.

Data type conversion is an important part of **data preprocessing**, which is usually done before training an AI model.

---

# Important Notes

* Every DataFrame column has a data type.
* `parse_dates` converts text into date/time values while reading a file.
* `pd.to_numeric()` converts values into numeric types.
* `astype()` changes the data type of a column.
* `category` is ideal for columns with a small set of repeated values.
* Converting repeated text columns to `category` often reduces memory usage.
* Use `df.info()` to inspect data types and memory usage.

---

# Common Beginner Mistakes

* Assuming numbers stored as text can be used directly in calculations.
* Forgetting to assign the result of `pd.to_numeric()` or `astype()` back to the DataFrame.
* Converting every text column to `category` without checking whether the values actually repeat a lot.
* Confusing `object` (usually text) with `category` (optimized storage for repeated text).

---

# Quick Comparison

| Function          | Purpose                                    | Example                           |
| ----------------- | ------------------------------------------ | --------------------------------- |
| `astype()`        | Convert a column to another data type      | `df["Region"].astype("category")` |
| `pd.to_numeric()` | Convert values to numeric                  | `pd.to_numeric(df["Profit"])`     |
| `parse_dates`     | Convert text to dates while reading a file | `parse_dates=["Date"]`            |
| `df.info()`       | Show data types and memory usage           | `df.info()`                       |

---

# Easy Way to Remember

* **`astype()`** → "**As this type**" (change the type).
* **`to_numeric()`** → Convert **to numbers**.
* **`parse_dates`** → Parse text into **dates**.
* **`category`** → Best for **repeated text values**.
* **`df.info()`** → Information about the DataFrame.

---

## 🌟 My Observation

> Today I learned that loading a dataset is not enough—I also need to make sure each column has the correct data type. Before this lecture, I didn't realize that a column containing numbers could still be treated as text, which would make calculations difficult.

> The biggest thing I understood today is that choosing the right data type is not only about correctness but also about efficiency. Converting repeated text columns like `Category` or `Region` to the `category` type can significantly reduce memory usage, which becomes very important when working with large datasets.

> I also learned that functions like `pd.to_numeric()`, `astype()`, and `parse_dates` are part of data preprocessing. They help prepare the dataset so it can be analyzed accurately and later used for Machine Learning models.

---

# Practice Section

## 1. Coding Exercise

Create this DataFrame:

```python
import pandas as pd

df = pd.DataFrame({
    "Name": ["Ali", "Sara", "Ahmed"],
    "Age": ["20", "22", "21"],
    "City": ["Lahore", "Karachi", "Lahore"]
})
```

Now:

1. Check the data types using `df.info()`.
2. Convert the `Age` column to numeric using `pd.to_numeric()`.
3. Convert the `City` column to the `category` type using `astype()`.
4. Display `df.info()` again and compare the changes.

---

## 2. Output Prediction

Predict the output:

```python
import pandas as pd

df = pd.DataFrame({
    "Marks": ["80", "90", "100"]
})

df["Marks"] = pd.to_numeric(df["Marks"])

print(df.dtypes)
```

**Think before running it.**

---

## 3. Debugging Challenge

Find and fix the mistake:

```python
df["Age"].astype("int")
```

**Hint:** This creates a converted Series but doesn't save it back.

Correct version:

```python
df["Age"] = df["Age"].astype("int")
```

---

## 4. MCQs

1. Which function converts a column to numeric values?

   * A. `astype()`
   * B. `to_numeric()`
   * C. `parse_dates`
   * D. `read_csv()`

   **Answer:** B

2. Which data type is best for columns with many repeated text values?

   * A. `float64`
   * B. `object`
   * C. `category`
   * D. `datetime64`

   **Answer:** C

3. Which method displays data types and memory usage?

   * A. `df.shape`
   * B. `df.describe()`
   * C. `df.info()`
   * D. `df.head()`

   **Answer:** C

---
