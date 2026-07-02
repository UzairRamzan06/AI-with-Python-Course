# Python Libraries for AI & Data Science (DigiSkills) – Simple Notes from Scratch

This lecture introduces **four very important Python libraries** used in **Artificial Intelligence (AI), Machine Learning (ML), and Data Science**.

These libraries are:

1. **NumPy** → Fast numerical calculations
2. **Pandas** → Store and manipulate data
3. **Matplotlib** → Create graphs
4. **Seaborn** → Beautiful statistical graphs

Think of them as a team where each library has a different job.

---

# Why Do We Need These Libraries?

Imagine a company gives you a file containing **50,000 customer records**.

Your job is to:

* Read the data
* Clean the data
* Analyze the data
* Find useful information
* Show results using graphs

Doing this using only basic Python would take a lot of code and time.

These libraries make the work **easy, fast, and professional**.

---

# 1. NumPy (Numerical Python)

## What is NumPy?

NumPy is a Python library specially designed for **fast mathematical calculations**.

It works mainly with:

* Numbers
* Arrays
* Matrices
* Mathematical operations

Think of NumPy as a **super-fast calculator**.

---

## What is an Array?

An array is simply a collection of values.

Example:

```python
[10, 20, 30, 40, 50]
```

Instead of storing one number,

```python
age = 20
```

You can store many numbers together.

```python
ages = [20,21,22,23]
```

NumPy makes operations on these numbers extremely fast.

---

## Why is NumPy Fast?

Normal Python lists are slower.

NumPy is written in a low-level language (mainly C), so it uses your computer's CPU much more efficiently.

Example:

Instead of adding one number at a time,

NumPy performs calculations on the entire array together.

This makes it much faster.

---

## NumPy is Used For

* Mathematical calculations
* Matrix multiplication
* Linear Algebra
* Statistics
* Scientific computing
* AI calculations

---

## Simple Example

Without NumPy

```python
numbers = [1,2,3,4]
```

With NumPy

```python
import numpy as np

numbers = np.array([1,2,3,4])
```

Now calculations become much faster.

---

# Easy Memory Tip

**NumPy = Numbers**

Remember:

> NumPy is for Numerical Computing.

---

# 2. Pandas

## What is Pandas?

Pandas is used to store and manipulate structured data.

Think of Pandas as **Microsoft Excel inside Python.**

---

## Structured Data

Structured data means data arranged in:

Rows

and

Columns

Example:

| Name  | Age | City      |
| ----- | --- | --------- |
| Ali   | 22  | Lahore    |
| Sara  | 24  | Karachi   |
| Ahmed | 21  | Islamabad |

This is structured data.

---

## Pandas Works Best With

* Excel files
* CSV files
* SQL Databases
* Tables

---

## Pandas Uses Two Main Data Structures

### 1. Series

One column

Example

| Age |
| --- |
| 22  |
| 23  |
| 24  |

Series = One-dimensional data.

---

### 2. DataFrame

Many columns

| Name | Age | City    |
| ---- | --- | ------- |
| Ali  | 22  | Lahore  |
| Sara | 23  | Karachi |

DataFrame = Two-dimensional table.

---

## What Can Pandas Do?

It can

* Read Excel files
* Read CSV files
* Read SQL data
* Remove missing values
* Sort data
* Filter data
* Merge tables
* Analyze data

---

## Example

```python
import pandas as pd

data = pd.read_csv("students.csv")
```

Now the entire CSV file is loaded into Python.

---

# Easy Memory Tip

**Pandas = Tables**

Think:

> Pandas works like Excel.

---

# Difference Between NumPy and Pandas

| NumPy                               | Pandas                     |
| ----------------------------------- | -------------------------- |
| Works mainly with numbers           | Works with complete tables |
| Uses arrays                         | Uses DataFrames            |
| Very fast mathematical calculations | Easy data analysis         |
| Numerical computing                 | Data manipulation          |

---

# 3. Matplotlib

## What is Matplotlib?

Matplotlib is used to create graphs.

Instead of reading thousands of numbers,

we can understand data by looking at graphs.

---

Imagine sales data

| Month | Sales |
| ----- | ----- |
| Jan   | 100   |
| Feb   | 150   |
| Mar   | 250   |

Looking at numbers is difficult.

A graph makes trends easy to understand.

---

## Types of Graphs

Matplotlib can create

* Line Graph
* Bar Graph
* Pie Chart
* Scatter Plot
* Histogram
* 3D Graph

---

## Example

```python
import matplotlib.pyplot as plt
```

Then

```python
plt.plot(x, y)
```

creates a line graph.

---

# Why Use Graphs?

Graphs help us

* Understand data quickly
* Find trends
* Detect patterns
* Spot mistakes
* Present results

---

## Real Example

Suppose a company wants to know

"Are sales increasing?"

Instead of reading 10,000 rows,

a line graph answers the question in seconds.

---

# Easy Memory Tip

**Matplotlib = Basic Graphs**

Think

> Matplotlib draws graphs.

---

# 4. Seaborn

## What is Seaborn?

Seaborn is another visualization library.

It is built on top of Matplotlib.

That means:

Seaborn uses Matplotlib internally but makes graph creation easier and prettier.

---

Imagine

Matplotlib is a pencil.

Seaborn is Photoshop.

Both make pictures,

but Seaborn produces more attractive results with less effort.

---

## Why Seaborn?

It provides

* Better colors
* Better themes
* Less code
* Better statistical graphs

---

## Advanced Graphs

Seaborn creates

* Heatmaps
* Pair Plots
* Violin Plots
* Regression Plots
* Distribution Plots

These are commonly used in Data Science.

---

# Easy Memory Tip

**Seaborn = Beautiful Statistical Graphs**

Think

> Seaborn makes graphs look professional.

---

# Matplotlib vs Seaborn

| Matplotlib        | Seaborn                  |
| ----------------- | ------------------------ |
| Low-level library | High-level library       |
| More code         | Less code                |
| Manual styling    | Beautiful default styles |
| General graphs    | Statistical graphs       |
| Flexible          | Easier to use            |

---

# Can We Use Both Together?

**Yes!**

In real AI projects, we often combine them.

Example:

* Matplotlib for simple charts
* Seaborn for advanced statistical charts

They work perfectly together.

---

# Pandas + NumPy Together

These two libraries are also used together.

Example:

* Pandas reads the data.
* NumPy performs fast calculations.

Workflow:

```
CSV File
     ↓
Pandas
     ↓
Clean Data
     ↓
NumPy
     ↓
Fast Calculations
```

---

# Complete AI Data Workflow

```
Client Gives Data
        ↓
Pandas
(Read & Clean Data)
        ↓
NumPy
(Mathematical Operations)
        ↓
Matplotlib
(Simple Graphs)
        ↓
Seaborn
(Advanced Statistical Graphs)
        ↓
Machine Learning Model
```

---

# Real-Life Example

Imagine a hospital gives you patient data.

### Step 1

Pandas

* Read Excel file
* Remove missing records
* Organize data

### Step 2

NumPy

* Calculate averages
* Perform mathematical operations
* Prepare data for AI

### Step 3

Matplotlib

* Show patient age distribution
* Plot recovery trends

### Step 4

Seaborn

* Find relationships between age, disease, and recovery
* Create heatmaps and statistical visualizations

---

# Easy Way to Memorize

| Library    | Remember As                      |
| ---------- | -------------------------------- |
| NumPy      | Fast Calculator                  |
| Pandas     | Excel Inside Python              |
| Matplotlib | Graph Drawing Tool               |
| Seaborn    | Beautiful Statistical Graph Tool |

---

# One-Line Summary

* **NumPy** → Fast numerical calculations using arrays and matrices.
* **Pandas** → Read, store, clean, and analyze structured data using Series and DataFrames.
* **Matplotlib** → Create basic graphs and charts for data visualization.
* **Seaborn** → Create attractive, advanced statistical visualizations built on Matplotlib.

---

# Interview & Exam Points

* **NumPy** is used for numerical computing and fast array operations.
* **Pandas** is used for data manipulation and analysis.
* **Matplotlib** is used for creating basic visualizations like line, bar, pie, scatter, and histogram charts.
* **Seaborn** is built on top of Matplotlib and is mainly used for advanced statistical visualizations with better default styling.
* **Pandas + NumPy** are commonly used together for data analysis.
* **Matplotlib + Seaborn** are commonly used together for data visualization.

---

# GitHub Learning Journey Notes

## 📚 Python Libraries for AI & Data Science

Today, I learned the four core Python libraries that form the foundation of Data Science and Machine Learning:

* **NumPy**: Performs fast numerical computations using arrays and matrices.
* **Pandas**: Reads, cleans, organizes, and analyzes structured data through Series and DataFrames.
* **Matplotlib**: Creates basic visualizations such as line charts, bar charts, scatter plots, pie charts, and histograms.
* **Seaborn**: Built on top of Matplotlib to produce beautiful, high-level statistical visualizations like heatmaps, pair plots, violin plots, and regression plots.

### Key Learning

* Pandas + NumPy are commonly used together for data preparation and numerical processing.
* Matplotlib + Seaborn are often combined to visualize data effectively.
* A typical AI workflow is: **Load Data → Clean Data → Analyze → Visualize → Train Machine Learning Model**.

**Takeaway:** These four libraries are the essential toolkit for almost every Python-based AI, Machine Learning, and Data Science project.
