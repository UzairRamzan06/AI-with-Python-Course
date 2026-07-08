# 📘 Artificial Intelligence Using Python

**Platform:** DigiSkills.pk

**Week:** 03

**Lecture:** 57

# 🎓 Topic 57: Import & Export - CSV, Excel & JSON (Simple Explanation)

---

# Before We Start

In the **previous lecture (Topic 56)**, we learned how to work **inside a DataFrame**:

* Select rows using `.loc`
* Select rows using `.iloc`
* Filter data using conditions
* Modify values safely

Now we know **how to manipulate data**, but one important question remains:

> **Where does this data come from?**

In real AI projects, we don't manually type thousands of records into Python.

Instead, datasets usually come from:

* CSV files
* Excel spreadsheets
* JSON files
* Databases
* APIs

So the next logical step is learning **how to import data into Pandas and export it after cleaning or processing it**.

This is one of the first tasks performed in almost every data analysis or machine learning project.

---

# Introduction

Imagine you work as a data analyst for a retail company.

Every day, the company sends you a file named:

```text
retail_sales.csv
```

Your job is to:

1. Load the file into Python.
2. Clean the data.
3. Analyze it.
4. Save the cleaned version.
5. Send it back to your manager.

This is exactly what today's lecture teaches.

The main topics are:

* Reading CSV files
* Reading Excel files
* Reading JSON files
* Exporting DataFrames
* Saving memory while loading data
* Converting date columns correctly

These skills are essential because **AI models depend on good-quality data**, and the first step toward good data is importing it correctly.

---

# Concept 1: Why Do We Import Data?

When building AI systems, the data is rarely created inside Python.

Instead, it usually comes from external sources such as:

* Excel sheets
* Company reports
* Databases
* Government datasets
* Kaggle competitions
* APIs
* JSON files

Pandas acts like a bridge:

```text
CSV / Excel / JSON
          │
          ▼
     Pandas DataFrame
          │
          ▼
Data Cleaning & Analysis
          │
          ▼
Machine Learning Model
```

Without importing data, there is no dataset to analyze or train a model.

---

# Concept 2: Reading a CSV File

CSV stands for:

**Comma-Separated Values**

Example:

```text
Name,Age,City
Ali,20,Lahore
Sara,22,Karachi
Ahmed,21,Multan
```

Each comma separates one value from another.

CSV is one of the most common formats because it is:

* Simple
* Lightweight
* Supported by almost every software

---

## Basic Syntax

```python
df = pd.read_csv("retail_sales.csv")
```

This tells Pandas:

> "Open the CSV file and convert it into a DataFrame."

---

# Concept 3: Understanding `read_csv()` Parameters

The lecture introduced some useful parameters that make loading data more efficient.

## `parse_dates`

```python
parse_dates=["Date"]
```

### What does it do?

It converts the `Date` column into a proper **date/time** data type instead of leaving it as plain text.

### Why is this important?

If dates are stored as strings:

```text
"2024-01-15"
```

Python sees them as text.

You cannot easily calculate:

* Days between dates
* Months
* Years
* Weekly sales
* Monthly reports

When parsed as dates, Pandas understands that they are calendar values.

---

### Real-life Example

Suppose you want to answer:

> "How many sales happened in January?"

If the column is text, this is harder.

If it's a datetime column, Pandas can filter by month easily.

---

## Memory Trick

**`parse_dates` = Parse (understand) dates**

---

## `dtype`

```python
dtype={
    "Category": "category",
    "Region": "category"
}
```

### What does it do?

It tells Pandas what data type to use for specific columns.

### Why does it exist?

By default, Pandas guesses the data type.

Sometimes you already know the correct type, so you can specify it yourself.

This can reduce memory usage and improve performance.

---

### Why use the `category` type?

Imagine the `Region` column:

```text
North
South
East
West
North
South
East
...
```

Instead of storing the full words repeatedly, Pandas stores a small list of unique values and references them.

This is more memory efficient.

---

### Real-life Analogy

Think of a school attendance sheet.

Instead of writing:

```text
Present
Present
Present
Absent
Present
```

for every student, you could use:

```text
P
A
```

This saves space.

The `category` type works in a similar way for repeated values.

---

## `usecols`

The instructor also mentioned:

```python
usecols=["Date", "Sales"]
```

### What does it do?

Loads only the specified columns.

### Why is it useful?

If a dataset has 100 columns but you only need 2, loading only those 2:

* Uses less memory
* Loads faster

---

## `nrows`

```python
nrows=100
```

### What does it do?

Reads only the first 100 rows.

### Why use it?

When exploring a huge dataset, you may not need to load millions of rows immediately.

---

# Concept 4: Reading an Excel File

Pandas can also read Microsoft Excel files.

```python
df = pd.read_excel("sales.xlsx")
```

If the Excel file contains multiple sheets, you can choose one.

```python
df = pd.read_excel(
    "sales.xlsx",
    sheet_name="January"
)
```

---

## Why is this useful?

Many companies keep their data in Excel.

Instead of copying data manually, Pandas can read it directly.

---

# Concept 5: Reading a JSON File

JSON stands for:

**JavaScript Object Notation**

It stores data in a structured text format.

Example:

```json
[
  {
    "Name": "Ali",
    "Age": 20
  },
  {
    "Name": "Sara",
    "Age": 22
  }
]
```

Pandas can read JSON files with:

```python
df = pd.read_json("data.json")
```

JSON is widely used in:

* Web APIs
* Mobile apps
* Cloud services

---

# Concept 6: Exporting Data

After cleaning or analyzing data, we often need to save it.

Pandas provides several methods.

---

## Export to CSV

```python
df.to_csv("clean_data.csv")
```

---

## Export to Excel

```python
df.to_excel("clean_data.xlsx")
```

---

## Export to JSON

```python
df.to_json("clean_data.json")
```

---

## Why export data?

Different people and systems may require different formats.

* Excel → Business users
* CSV → Data analysis tools
* JSON → Web applications and APIs

---

# Concept 7: The `index` Parameter

When saving to CSV:

```python
df.to_csv("file.csv", index=False)
```

### What does `index=False` mean?

Do **not** save the row numbers.

Example:

Without `index=False`:

```text
0,Ali,20
1,Sara,22
```

With `index=False`:

```text
Ali,20
Sara,22
```

This produces a cleaner file if the index isn't needed.

---

# Concept 8: Memory-Efficient Loading

The instructor emphasized that large datasets consume memory.

Two simple ways to reduce memory usage are:

1. Use `usecols` to load only required columns.
2. Use `dtype` to choose appropriate data types.

Benefits:

* Faster loading
* Lower RAM usage
* Better performance on large datasets

---

# Concept 9: Public Dataset Sources

The lecture mentioned several places where you can find datasets.

Some popular sources are:

* **Kaggle** – One of the largest collections of datasets for machine learning competitions and practice.
* **UCI Machine Learning Repository** – A well-known academic collection of datasets.
* **Google Cloud Public Datasets** – Large-scale datasets hosted on Google Cloud.
* Pakistan-specific open datasets – Available from various organizations and government portals.

These resources are useful for practicing data analysis and machine learning on real-world data.

---

# Code Explanation

## Code 1: Installing `openpyxl`

```python
!pip install openpyxl
```

### What does `!` mean?

In Jupyter Notebook, a command starting with `!` is sent to the operating system (shell) instead of being treated as normal Python code.

### What is `pip`?

`pip` is Python's package manager. It installs external libraries.

### Why install `openpyxl`?

Pandas uses `openpyxl` to read and write **`.xlsx` Excel files**.

Without it, operations like `read_excel()` or `to_excel()` may fail.

### Output

```text
Requirement already satisfied...
```

This means the library is already installed, so nothing new needed to be downloaded.

---

## Code 2: Importing Libraries

```python
import pandas as pd
import openpyxl
```

### `import pandas as pd`

Imports the Pandas library.

### `import openpyxl`

Makes the Excel engine available for reading and writing `.xlsx` files.

---

## Code 3: Reading the CSV

```python
df = pd.read_csv(
    "retail_sales.csv",
    parse_dates=["Date"],
    dtype={
        "Category": "category",
        "Region": "category"
    }
)
```

### Line-by-Line

* `"retail_sales.csv"` → The CSV file to load.
* `parse_dates=["Date"]` → Convert the `Date` column into the `datetime64[ns]` type.
* `dtype={...}` → Store `Category` and `Region` using the efficient `category` data type.

The result is stored in the variable `df`.

---

## Code 4: Inspecting the DataFrame

```python
df.info()
```

### What does it show?

* Number of rows (`1825`)
* Number of columns (`6`)
* Non-null values in each column
* Data types
* Memory usage

### Understanding the Output

```text
Date      datetime64[ns]
```

The date column is now recognized as a true date/time column.

```text
Category  category
Region    category
```

These text columns are stored efficiently.

```text
Sales
Quantity
Profit
```

These are numeric (`float64`) because they contain decimal values or missing values.

The line:

```text
memory usage: 61.3 KB
```

shows approximately how much memory the DataFrame occupies.

---

## Code 5: Removing Invalid Rows

```python
clean_df = df[df["Sales"] > 0]
```

### What does it do?

Keeps only rows where the `Sales` value is greater than `0`.

Rows with zero or negative sales are excluded.

### Why?

In many datasets, a sales value of `0` may represent an invalid, incomplete, or irrelevant record for analysis.

---

## Code 6: Selecting Specific Columns

```python
subset = clean_df[
    ["Date", "Category", "Sales", "Region"]
]
```

### What does it do?

Creates a new DataFrame containing only these four columns.

### Why?

Suppose your client only needs these columns. Keeping unnecessary columns increases file size and complexity.

---

## Code 7: Exporting to Excel

```python
subset.to_excel(
    "subset_sales.xlsx",
    sheet_name="sales"
)
```

### Explanation

* `"subset_sales.xlsx"` → Name of the output Excel file.
* `sheet_name="sales"` → The worksheet inside the Excel file will be named **sales**.

---

## Code 8: Exporting to JSON

```python
subset.to_json(
    "subset_sales.json",
    orient="records",
    date_format="iso"
)
```

### `orient="records"`

Each row is written as a separate JSON object in a list.

Example:

```json
[
  {
    "Date": "...",
    "Category": "...",
    "Sales": ...
  }
]
```

### `date_format="iso"`

Writes dates using the standard ISO format (for example, `2024-01-15T00:00:00`), which is widely accepted by web services and APIs.

---

## Code 9: Confirmation Message

```python
print("Files exported!")
```

Simply displays a confirmation message.

---

## Code 10: Checking the Final DataFrame

```python
subset.info()
```

This verifies:

* The cleaned DataFrame now has **4 columns**.
* Only rows with `Sales > 0` remain.
* Data types are still correct after cleaning.

---

# Important Notes

* `read_csv()` loads CSV files into a DataFrame.
* `read_excel()` reads Excel spreadsheets.
* `read_json()` loads JSON data.
* `parse_dates` converts text into proper date/time values.
* `dtype` helps optimize memory usage.
* `usecols` loads only the columns you need.
* `nrows` limits how many rows are loaded.
* `to_csv()`, `to_excel()`, and `to_json()` export DataFrames into different formats.
* `index=False` prevents row indexes from being written to the output file when exporting to CSV.

---

# Common Beginner Mistakes

* Forgetting to install `openpyxl` before working with Excel files.
* Misspelling a column name in `parse_dates` or `dtype`.
* Assuming `parse_dates` changes the original CSV file—it only affects how the data is loaded into the DataFrame.
* Forgetting to assign the result of filtering to a new variable when you want a cleaned DataFrame.
* Saving files without checking whether the output path is correct.

---

# Quick Comparison

| Format          | Best For                           | Human Readable | Common Use                        |
| --------------- | ---------------------------------- | -------------- | --------------------------------- |
| CSV             | Simple tables                      | ✅ Yes          | Data analysis, spreadsheets       |
| Excel (`.xlsx`) | Reports with sheets and formatting | ✅ Yes          | Business users                    |
| JSON            | Structured data exchange           | ✅ Yes          | APIs, web and mobile applications |

---

# Easy Way to Remember

* **`read_csv()`** → Read a CSV file.
* **`read_excel()`** → Read an Excel workbook.
* **`read_json()`** → Read JSON data.
* **`to_csv()`** → Save as CSV.
* **`to_excel()`** → Save as Excel.
* **`to_json()`** → Save as JSON.
* **`parse_dates`** → Parse text into dates.
* **`dtype`** → Decide the data type.
* **`usecols`** → Use only selected columns.
* **`nrows`** → Read only the first *n* rows.

---

## 🌟 My Observation

> Today I learned that working with data is not just about analyzing it—it also involves importing it correctly and exporting it in the format others need. Before this lecture, I thought Pandas mainly worked with DataFrames created inside Python, but now I understand that most real-world projects start by reading data from external files.

> The biggest thing I understood today is that options like `parse_dates`, `dtype`, `usecols`, and `nrows` are not just extra features. They help make programs faster, use less memory, and prepare data in the right format from the beginning.

> I also realized why exporting data matters. After cleaning or processing a dataset, I can save it as CSV, Excel, or JSON depending on who will use it next. This makes Pandas a complete tool for moving data between different systems, which will be very useful in future AI and Machine Learning projects.

---

# Practice Section

## 1. Coding Exercise

Create a CSV file named `students.csv` with the following data:

| Name  | Age | City    | Marks |
| ----- | --: | ------- | ----: |
| Ali   |  20 | Lahore  |    85 |
| Sara  |  22 | Karachi |    91 |
| Ahmed |  21 | Multan  |    78 |

Then:

1. Read the file using `pd.read_csv()`.
2. Display `df.info()`.
3. Select only `Name` and `Marks`.
4. Export the result to:

   * `students.xlsx`
   * `students.json`

---

## 2. Output Prediction

What will be displayed?

```python
import pandas as pd

df = pd.read_csv(
    "sales.csv",
    nrows=5
)

print(df.shape)
```

*Hint:* Think about how many rows are loaded and how `.shape` reports dimensions.

---

## 3. Debugging Challenge

Find the mistake:

```python
df = pd.read_csv(
    "sales.csv",
    parse_dates=["SaleDate"]
)
```

**Hint:** Ensure the CSV actually contains a column named `SaleDate`. If the real column is `Date`, use:

```python
parse_dates=["Date"]
```

---

## 4. MCQs

1. Which function reads a CSV file into a DataFrame?

   * A. `read_excel()`
   * B. `read_json()`
   * C. `read_csv()`
   * D. `load_csv()`

   **Answer:** C

2. Which parameter converts a column into a date/time type while loading?

   * A. `dtype`
   * B. `parse_dates`
   * C. `sheet_name`
   * D. `index`

   **Answer:** B

3. Which parameter helps reduce memory by loading only selected columns?

   * A. `nrows`
   * B. `usecols`
   * C. `orient`
   * D. `sheet_name`

   **Answer:** B

---
