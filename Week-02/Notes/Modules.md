# 📘 Modules in Python

> **Course:** Artificial Intelligence using Python
> **Week:** 02
> **Section:** Modules
> **Related Lecture:** 27 – Importing & Using Python Modules

---

# 📖 What is a Module?

A **module** is a Python file (`.py`) that contains reusable code such as:

* Functions
* Variables
* Classes
* Constants

Instead of writing the same code repeatedly, Python allows us to organize reusable code into modules.

Think of a module as a **toolbox** that contains useful tools (functions and classes) which can be used whenever needed.

---

# 🎯 Why Do We Use Modules?

Modules help us:

* Reuse existing code.
* Organize programs into smaller files.
* Improve code readability.
* Reduce duplicate code.
* Make programs easier to maintain.

---

# 📦 Types of Python Modules

Python provides three main types of modules.

## 1. Built-in Modules

These modules come pre-installed with Python.

Examples:

* `math`
* `random`
* `datetime`
* `os`
* `sys`

No installation is required.

Example:

```python
import math

print(math.sqrt(25))
```

---

## 2. User-Defined Modules

These are modules created by programmers.

Example:

```text
calculator.py
```

```python
def add(a, b):
    return a + b
```

Another file can import it.

```python
import calculator

print(calculator.add(10, 5))
```

---

## 3. Third-Party Modules

These are created by the Python community.

They are installed using `pip`.

Examples:

* NumPy
* Pandas
* Matplotlib
* Seaborn
* OpenCV
* TensorFlow
* Scikit-learn

These libraries will be introduced later in the AI course.

---

# 📥 Importing Modules

Python uses the `import` keyword.

Example:

```python
import math
```

Now the functions inside the module can be used.

```python
math.sqrt(64)
```

---

# 📥 Importing Multiple Modules

Multiple modules can be imported in one program.

```python
import math
import random
import datetime
```

---

# 📥 Importing Specific Functions

Instead of importing the entire module, a specific function can be imported.

Example:

```python
from math import sqrt
```

Now it can be used directly.

```python
sqrt(81)
```

---

# 📥 Importing Multiple Functions

Example:

```python
from math import sqrt, factorial
```

---

# 📥 Importing with an Alias

A module can be imported using a shorter name.

Example:

```python
import math as m
```

Usage:

```python
m.sqrt(49)
```

Aliases make long module names easier to type.

---

# 📚 Common Built-in Modules

## math

Used for mathematical calculations.

Common functions:

* `sqrt()`
* `pow()`
* `factorial()`
* `ceil()`
* `floor()`

Useful constant:

* `pi`

---

## random

Used to generate random values.

Common functions:

* `randint()`
* `choice()`
* `random()`
* `shuffle()`

Applications:

* Games
* Simulations
* Password generators

---

## datetime

Used to work with dates and time.

Common features:

* Current date
* Current time
* Current date and time

Example:

```python
from datetime import date

print(date.today())
```

---

## os

Provides functions for interacting with the operating system.

Examples:

* Current working directory
* Creating folders
* Renaming files
* Deleting files

This module will become more useful in larger Python projects.

---

## sys

Provides information about the Python interpreter.

Examples:

* Command-line arguments
* Python version
* Program exit

---

# 📝 Import Syntax Summary

Import an entire module:

```python
import module_name
```

Import a specific function:

```python
from module_name import function_name
```

Import multiple functions:

```python
from module_name import function1, function2
```

Import using an alias:

```python
import module_name as alias
```

---

# ✅ Advantages of Modules

* Improve code organization.
* Encourage code reuse.
* Reduce programming time.
* Simplify maintenance.
* Make large projects easier to manage.
* Allow collaboration among multiple developers.

---

# ❌ Common Beginner Mistakes

### Forgetting to import a module

Incorrect:

```python
math.sqrt(16)
```

Correct:

```python
import math
```

---

### Using a function without the module name

Incorrect:

```python
sqrt(25)
```

Correct:

```python
math.sqrt(25)
```

Unless imported directly:

```python
from math import sqrt
```

---

### Misspelling the module name

Incorrect:

```python
import maths
```

Correct:

```python
import math
```

---

### Expecting the same random value every time

```python
random.randint(1, 10)
```

The result changes each time the program runs.

---

# 💡 Best Practices

* Import only the modules you need.
* Use meaningful aliases.
* Avoid importing everything using `from module import *`.
* Keep imports at the beginning of the file.
* Organize imports for better readability.

---

# 📌 Key Terms

| Term                | Description                            |
| ------------------- | -------------------------------------- |
| Module              | A Python file containing reusable code |
| Package             | A collection of related modules        |
| Library             | A collection of packages and modules   |
| Import              | Loading a module into a program        |
| Built-in Module     | Comes with Python                      |
| User-defined Module | Created by the programmer              |
| Third-party Module  | Installed using `pip`                  |

---

# 🎯 Interview Questions

### What is a Python module?

A module is a Python file containing reusable code such as functions, classes, and variables.

---

### Why are modules used?

To organize code, improve reusability, and reduce duplication.

---

### What is the difference between a module and a package?

A module is a single Python file, while a package is a directory containing multiple related modules.

---

### What is the purpose of the `import` keyword?

It loads a module so its functions, classes, and variables can be used in another program.

---

### What is the difference between:

```python
import math
```

and

```python
from math import sqrt
```

The first imports the entire module. The second imports only the specified function.

---

# 📝 Summary

In this lecture, you learned that modules help organize and reuse Python code. Python provides built-in modules such as `math`, `random`, and `datetime`, while programmers can also create their own modules or install third-party libraries. Understanding modules is essential because almost every Python application—including AI, Machine Learning, Data Science, and Web Development—relies on importing and using modules effectively.
