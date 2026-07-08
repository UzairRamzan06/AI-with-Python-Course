# 📘 Artificial Intelligence Using Python

**Platform:** DigiSkills.pk
**Week:** 03
**Lecture:** 55
# 🎓 Topic 55: Pandas DataFrames - Creation & Inspection (Simple Explanation)

---

# Before We Start

In the **previous lecture (Topic 54)**, we learned about **Pandas Series**.

A **Series** is a **one-dimensional** data structure that stores a single column of data with an index.

For example:

| Index | Name  |
| ----: | ----- |
|     0 | Ali   |
|     1 | Ahmed |
|     2 | Sara  |

A Series is useful when we only need **one column** of data.

Now think about real-world datasets.

Suppose you have student information:

| Name  | Age | City    |
| ----- | --: | ------- |
| Ali   |  20 | Lahore  |
| Sara  |  22 | Karachi |
| Ahmed |  21 | Multan  |

This is no longer a single column.

It has **multiple columns**.

That is why the next logical step after learning **Series** is learning **DataFrames**.

A **DataFrame** is simply a collection of multiple Series arranged together like a table.

This is the most commonly used data structure in Pandas because almost every AI and Machine Learning dataset is stored in tabular form.

---

# Introduction

This lecture introduces the **Pandas DataFrame**, which is one of the most important concepts in data analysis, AI, and Machine Learning.

Almost every dataset you will use in AI looks like a spreadsheet:

* Student records
* Hospital records
* Customer information
* Weather data
* Sales reports
* Loan applications

All of these are tables.

Pandas provides the **DataFrame** to store and manipulate such data efficiently.

The lecture also teaches how to:

* Create a DataFrame
* Load data from a CSV file
* Inspect a dataset
* Understand its structure
* Perform quick statistical analysis

These are the **first things every Data Scientist does after receiving a new dataset.**

---

# Concept 1: What is a DataFrame?

A **DataFrame** is a **two-dimensional table** provided by Pandas.

Think of it as an Excel spreadsheet inside Python.

Example:

```
+----+-------+-----+----------+
|    | Name  | Age | City     |
+----+-------+-----+----------+
| 0  | Ali   | 20  | Lahore   |
| 1  | Sara  | 22  | Karachi  |
| 2  | Ahmed | 21  | Multan   |
+----+-------+-----+----------+
```

It contains:

* Rows
* Columns
* Labels (column names)
* Indexes (row numbers)

---

## Why do we need DataFrames?

Imagine storing student information using normal Python lists.

```
names = ["Ali","Sara","Ahmed"]
ages = [20,22,21]
cities = ["Lahore","Karachi","Multan"]
```

This works for very small data.

But what if you have:

* 10,000 students?
* 100 columns?
* Missing values?
* Different data types?

Managing separate lists becomes difficult.

A DataFrame keeps everything organized in one table.

---

## Real-life analogy

Think about an Excel sheet.

```
+------------------------------+
| Name | Age | City | Marks   |
+------------------------------+
| Ali  | 20  | LHR  | 85       |
| Sara | 22  | KHI  | 91       |
+------------------------------+
```

A Pandas DataFrame behaves almost exactly like this spreadsheet.

---

# Concept 2: DataFrame is Two-Dimensional

A Series has only one direction.

```
Series

Ali
Sara
Ahmed
```

A DataFrame has two directions.

```
          Columns
       Name Age City
Rows
0      Ali   20 Lahore
1      Sara  22 Karachi
2      Ahmed 21 Multan
```

Because it has rows **and** columns, it is called a **two-dimensional** data structure.

---

# Concept 3: Columns Can Have Different Data Types

One of the biggest advantages of DataFrames is that every column can store a different type of data.

Example:

| Name | Age |  Salary | Married |
| ---- | --: | ------: | ------- |
| Ali  |  20 | 50000.5 | True    |

Here,

* Name → Text (String)
* Age → Integer
* Salary → Decimal
* Married → Boolean

This is exactly how real-world datasets look.

---

## Why is this important?

AI datasets are rarely made of only numbers.

Example:

Hospital Data

| Name | Age | Disease | Weight |
| ---- | --: | ------- | -----: |

Some columns contain text.

Some contain numbers.

Some contain dates.

DataFrames handle all of them together.

---

# Concept 4: Creating a DataFrame

The instructor created a Python dictionary first.

```python
import pandas as pd

data = {
    "Name": ["Ali", "Ahmed", "Sara"],
    "Age": [20, 21, 22],
    "City": ["Lahore", "Multan", "Karachi"]
}

df = pd.DataFrame(data)

print(df)
```

---

## Line-by-Line Explanation

### Line 1

```python
import pandas as pd
```

**What it does**

Imports the Pandas library.

**Why?**

Without importing Pandas, Python doesn't know what a DataFrame is.

---

### Line 2

```python
data = {
```

Creates a Python dictionary.

A dictionary stores information as:

```
Key → Value
```

Example

```
Name → list of names
Age → list of ages
```

---

### Line 3

```python
"Name": ["Ali","Ahmed","Sara"]
```

Creates one column called **Name**.

---

### Line 4

```python
"Age": [20,21,22]
```

Creates another column.

---

### Line 5

```python
"City": ["Lahore","Multan","Karachi"]
```

Creates the third column.

---

### Line 6

```python
df = pd.DataFrame(data)
```

This is the most important line.

It converts the dictionary into a Pandas DataFrame.

You can think of it as:

```
Dictionary
      ↓
pd.DataFrame()
      ↓
Table
```

---

### Line 7

```python
print(df)
```

Displays the DataFrame.

Output

```
     Name   Age     City
0     Ali    20   Lahore
1   Ahmed    21   Multan
2    Sara    22  Karachi
```

---

## Why are the row numbers 0, 1, 2?

Because we didn't provide our own row labels.

Pandas automatically creates an **index** starting from **0**.

---

### Common Beginner Mistakes

❌ Forgetting `import pandas as pd`

❌ Writing

```python
pd.dataframe()
```

instead of

```python
pd.DataFrame()
```

(`DataFrame` starts with a capital **D** and **F**.)

❌ Making columns with different lengths.

Example:

```
Names = 3 values
Age = 2 values
```

Every column must have the same number of rows.

---

# Concept 5: Reading a CSV File

Most real datasets are stored in **CSV** files.

CSV stands for:

**Comma-Separated Values**

Example:

```
Name,Age,City
Ali,20,Lahore
Sara,22,Karachi
Ahmed,21,Multan
```

Instead of typing data manually, we load it from a file.

```python
df = pd.read_csv("retail_sales.csv")
```

---

## Line-by-Line Explanation

```python
pd.read_csv()
```

### What does it do?

Reads a CSV file.

### Why does it exist?

Real datasets can contain thousands or even millions of rows. Entering them manually is impossible.

### Parameter

```python
"retail_sales.csv"
```

The filename or path to the CSV file.

### Expected Result

Pandas reads the file and stores it in a DataFrame.

---

## Why do Data Scientists use CSV?

Because:

* Excel can save CSV files.
* Databases can export CSV files.
* Websites often provide datasets as CSV.
* It is simple and widely supported.

---------------------------------------------------------------------
## How to upload CSV file ??
# Explanations : The upload button is in a different place depending on which one you have.
# If you are using the classic Jupyter Notebook

### Step 1: Start Jupyter Notebook
Open **Anaconda Navigator** (if you installed Anaconda).

Click **Launch** under **Jupyter Notebook**.

Or open Command Prompt and type:

```bash
jupyter notebook
```

A browser window will open.

---

### Step 2: You should see a page like this

It will look something like:

```
Files

☐ Notebook1.ipynb
☐ MyProject.ipynb

[Upload]   [New ▼]
```

The **Upload** button is in the **top-right corner**, next to the **New** button.

It looks similar to this:

```
-------------------------------------
Notebook Dashboard

Notebook1.ipynb

                         Upload   New ▼
-------------------------------------
```

---

### Step 3: Click **Upload**

A file browser opens.

Navigate to where your CSV file is stored.

For example:

```
Downloads
    retail_sales.csv
```

Select the file.

Click **Open**.

---

### Step 4: Click **Upload** again

After selecting the file, you'll return to the Jupyter page.

You'll now see something like:

```
retail_sales.csv

Upload
```

Click that **Upload** button to complete the upload.

Now your notebook folder contains:

```
Notebook.ipynb
retail_sales.csv
```

---

### Step 5: Open your notebook

Open your notebook (`Notebook.ipynb`).

Run:

```python
import pandas as pd

df = pd.read_csv("retail_sales.csv")
```

It should work because the notebook and CSV are in the same folder.

---------------------------------------------------------------------

# Concept 6: Inspecting the Dataset with `.info()`

```python
df.info()
```

This is one of the first commands you should run after loading a dataset.

It gives a summary of the DataFrame.

Typical output includes:

* Number of rows
* Number of columns
* Column names
* Non-null values
* Data types
* Memory usage

---

## Why is `.info()` useful?

Imagine receiving a dataset with 100 columns.

You don't want to inspect every value manually.

`.info()` quickly answers questions like:

* How many columns are there?
* Which columns have missing values?
* What type of data does each column contain?

---

## Understanding Common Data Types

The lecture mentioned several data types:

| Data Type | Meaning                 | Example         |
| --------- | ----------------------- | --------------- |
| `object`  | Usually text or strings | "Ali", "Lahore" |
| `int64`   | Whole numbers           | 10, 25          |
| `float64` | Decimal numbers         | 12.5, 99.99     |

**Why is `object` used for text?**

In Pandas, text columns are often stored as `object` because they hold Python string objects.

---

# Concept 7: Getting the Shape with `.shape`

```python
df.shape
```

Returns:

```
(rows, columns)
```

Example:

```
(1825, 6)
```

Meaning:

* 1825 rows
* 6 columns

---

## Why is `.shape` important?

Before training an AI model, it's useful to know:

* How much data you have.
* How many features (columns) are available.

---

# Concept 8: Checking Column Data Types with `.dtypes`

```python
df.dtypes
```

Shows the data type of every column.

Example:

```
Date        object
Sales       float64
Quantity    int64
Profit      float64
Region      object
```

---

## Why does this matter?

Machine Learning algorithms usually work with **numeric data**.

Knowing the data type helps you decide whether a column needs preprocessing (for example, converting text into numbers).

---

# Concept 9: Statistical Summary with `.describe()`

```python
df.describe()
```

This command summarizes **numeric columns** by default.

It typically shows:

| Statistic | Meaning                                            |
| --------- | -------------------------------------------------- |
| Count     | Number of non-missing values                       |
| Mean      | Average value                                      |
| Std       | Standard deviation (how spread out the values are) |
| Min       | Smallest value                                     |
| 25%       | First quartile                                     |
| 50%       | Median (middle value)                              |
| 75%       | Third quartile                                     |
| Max       | Largest value                                      |

---

## Why is `.describe()` useful?

Suppose you have a sales dataset.

Instead of manually calculating averages and minimum values, one command gives you a quick overview.

This helps you spot unusual values and understand the distribution of your data before building an AI model.

---

# Important Notes

* A DataFrame is a two-dimensional data structure.
* It is the most commonly used Pandas object in AI and Machine Learning.
* Each column can store a different data type.
* If no row labels are provided, Pandas creates an index automatically.
* Most real-world datasets are loaded from CSV files.
* `.info()` provides a quick structural overview.
* `.shape` tells you the dataset dimensions.
* `.dtypes` shows the type of each column.
* `.describe()` summarizes numeric columns and is useful for an initial statistical analysis.

---

# Common Beginner Mistakes

* Forgetting to import Pandas before using `DataFrame`.
* Writing `dataframe` instead of `DataFrame`.
* Creating columns with different numbers of values.
* Assuming `.describe()` summarizes text columns by default—it mainly summarizes numeric data.
* Forgetting to assign the loaded CSV to a variable:

  ```python
  df = pd.read_csv("file.csv")
  ```
* Confusing rows with columns.

---

# Quick Comparison

| Feature         | Series                 | DataFrame        |
| --------------- | ---------------------- | ---------------- |
| Dimensions      | 1                      | 2                |
| Looks Like      | Single column          | Complete table   |
| Stores          | One sequence of values | Multiple columns |
| Index           | Yes                    | Yes              |
| Column Labels   | No                     | Yes              |
| Most Common Use | Individual column      | Entire dataset   |

---

# Easy Way to Remember

* **DataFrame** → **Data Table** (think of an Excel sheet).
* **`read_csv()`** → **Read** a CSV file.
* **`.info()`** → **Information** about the dataset.
* **`.shape`** → **Shape = (Rows, Columns)**.
* **`.dtypes`** → **Data Types** of columns.
* **`.describe()`** → **Describe** the numeric data with statistics.

---

## 🌟 My Observation

> Today I learned that a DataFrame is much more than just a table—it is the main way Pandas stores real-world datasets. Before this lecture, I thought loading data into Python meant creating lots of lists manually, but now I understand that DataFrames organize everything in one place with rows, columns, and labels.

> The biggest thing I understood today is that inspecting a dataset is just as important as loading it. Commands like `.info()`, `.shape`, `.dtypes`, and `.describe()` help me understand the dataset before I start analyzing or using it in Machine Learning.

> I also realized why DataFrames are so important for AI. Almost every dataset I will use in future projects will likely be stored as a CSV file, and Pandas provides simple tools to load, inspect, and understand that data quickly. This lecture gave me the foundation for working with real datasets.

---

# Practice Section

## 1. Coding Exercise

Create the following DataFrame:

| Name   | Age | City       |
| ------ | --: | ---------- |
| Ayesha |  23 | Lahore     |
| Bilal  |  25 | Islamabad  |
| Hamza  |  21 | Faisalabad |

Then:

* Print the DataFrame.
* Display its shape.
* Display the data types.
* Use `.describe()` on it.

---

## 2. Output Prediction

What will this return?

```python
import pandas as pd

data = {
    "A": [10, 20, 30],
    "B": [1.5, 2.5, 3.5]
}

df = pd.DataFrame(data)

print(df.shape)
```

**Think first before running the code.**

---

## 3. Debugging Challenge

Find and fix the mistake:

```python
import pandas as pd

data = {
    "Name": ["Ali", "Sara"],
    "Age": [20]
}

df = pd.DataFrame(data)
```

*Hint:* Every column must contain the same number of values.

---

## 4. MCQs

1. Which Pandas object is most commonly used to store tabular data?

   * A. List
   * B. Series
   * C. DataFrame
   * D. Tuple

   **Answer:** C

2. Which function loads a CSV file into a DataFrame?

   * A. `read_file()`
   * B. `read_csv()`
   * C. `open_csv()`
   * D. `load_csv()`

   **Answer:** B

3. Which attribute returns the number of rows and columns?

   * A. `.info()`
   * B. `.dtypes`
   * C. `.shape`
   * D. `.describe()`

   **Answer:** C

---
