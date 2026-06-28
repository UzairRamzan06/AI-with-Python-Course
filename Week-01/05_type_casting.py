# Course : Artificial Intelligence with Python
# Week   : 01
# File   : 05_type_casting.py
# VDO Lectures Covered : 14
# Topic  : Type Conversion & Casting in Python 
# What to practice
    int()
    float()
    str()
    bool()
# ===========================================

age = "25"
age = int(age)
print(age)

# ===========================================


age = 25
score = 3.6
name = "Ali Zafar"
is_passed = True

contains these data types:
| Variable    | Value         | Data Type        |
| ----------- | ------------- | ---------------- |
| `age`       | `25`          | Integer (`int`)  |
| `score`     | `3.6`         | Float (`float`)  |
| `name`      | `"Ali Zafar"` | String (`str`)   |
| `is_passed` | `True`        | Boolean (`bool`) |

# ==========================================================
    
#  Quick Revision Table  
| Function  | Purpose            | Example     |
| --------- | ------------------ | ----------- |
| `int()`   | Convert to Integer | `int("25")` |
| `float()` | Convert to Float   | `float(25)` |
| `str()`   | Convert to String  | `str(25)`   |
| `bool()`  | Convert to Boolean | `bool(1)`   |
    
# ==========================================================
# Explanation 
    # What is Type Casting?
        # Type Casting means changing one data type into another.
        # For example:
            # Example 01:
                    age = "25"
                    # Here, 25 is a string because it is inside quotation marks.
                    # If we want to perform mathematical operations, we first convert it into an integer.

            # Example 02: 
                    age = int(age)
                    # Now age becomes an integer.

# 01: int()
# Used to convert a value into an integer.
age = "25"
age = int(age)
print(age)
# Output
# 25

# 02: float()
# Used to convert a value into a decimal number.
marks = 90
marks = float(marks)
print(marks)
# Output
# 90.0

# 03: str()
# Used to convert a value into text (string).
roll_no = 101
roll_no = str(roll_no)
print(roll_no)
# Output
# 101
#Now it is a string instead of an integer.

# 04: bool()
# Converts a value into either True or False.

print(bool(1))
# Output
# True

print(bool(0))
# Output
# False

print(bool(""))
# Output
# False

print(bool("Python"))
# Output
# True

# ==========================================================    
# Course : Artificial Intelligence with Python
# Week   : 01
# File   : 05_type_casting.py
# Lecture: 14
# Topic  : Type Conversion & Type Casting in Python
#
# What to Practice:
#   ✔ int()
#   ✔ float()
#   ✔ str()
#   ✔ bool()
# ==========================================================

print("===== Type Conversion & Type Casting =====")

# ----------------------------------------------------------
# What is Type Casting?
# ----------------------------------------------------------
# Type Casting means converting one data type into another.
#
# Example:
# String --> Integer
# Integer --> Float
# Float --> Integer
# Integer --> String
# ----------------------------------------------------------


# ==========================================================
# Example 1 : int()
# ==========================================================

print("\nExample 1 : Convert String to Integer")

age = "25"

print("Before Conversion :", age)
print("Data Type :", type(age))

age = int(age)

print("After Conversion :", age)
print("Data Type :", type(age))


# ==========================================================
# Example 2 : float()
# ==========================================================

print("\nExample 2 : Convert Integer to Float")

marks = 90

print("Before Conversion :", marks)
print("Data Type :", type(marks))

marks = float(marks)

print("After Conversion :", marks)
print("Data Type :", type(marks))


# ==========================================================
# Example 3 : str()
# ==========================================================

print("\nExample 3 : Convert Integer to String")

roll_no = 101

print("Before Conversion :", roll_no)
print("Data Type :", type(roll_no))

roll_no = str(roll_no)

print("After Conversion :", roll_no)
print("Data Type :", type(roll_no))


# ==========================================================
# Example 4 : bool()
# ==========================================================

print("\nExample 4 : Convert Number to Boolean")

number = 1

print("Before Conversion :", number)
print("Data Type :", type(number))

number = bool(number)

print("After Conversion :", number)
print("Data Type :", type(number))


# ==========================================================
# Example 5 : bool() with Zero
# ==========================================================

print("\nExample 5 : Zero becomes False")

value = 0

print(bool(value))


# ==========================================================
# Example 6 : bool() with Empty String
# ==========================================================

print("\nExample 6 : Empty String")

text = ""

print(bool(text))


# ==========================================================
# Example 7 : bool() with Text
# ==========================================================

print("\nExample 7 : Non-Empty String")

text = "Python"

print(bool(text))


# ==========================================================
# Practice Examples
# ==========================================================

print("\n===== Practice =====")

price = "150"
print(int(price))

temperature = 35
print(float(temperature))

student_id = 500
print(str(student_id))

print(bool(10))
print(bool(0))


# ==========================================================
# Challenge Exercises
# ==========================================================

# 1. Convert "100" into an integer.
# 2. Convert 45 into a float.
# 3. Convert 3.14 into an integer.
# 4. Convert 250 into a string.
# 5. Check the Boolean value of:
#       0
#       100
#       ""
#       "AI"

print("\nEnd of Type Casting Examples")
