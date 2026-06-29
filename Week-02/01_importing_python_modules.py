# Course : Artificial Intelligence using Python
# Week   : 02
# File   : 01_importing_python_modules.py
# Lecture: 27
# Topic  : Importing & Using Python Modules
#
# Learning Objectives:
#     ✔ Understand what a Python module is
#     ✔ Learn why modules are useful
#     ✔ Import built-in Python modules
#     ✔ Use functions from imported modules
# ==========================================================



# What is a Python Module?
# ----------------------------------------------------------
# A Python module is a file that contains Python code such as
# functions, variables, and classes.
#
# Modules help us organize code and reuse existing functionality
# instead of writing everything from scratch.
#
# Python provides many built-in modules such as:
# - math
# - random
# - datetime
#
# We can import a module using the 'import' keyword.
# ----------------------------------------------------------
import math
print(math.sqrt(16))

from math import sqrt
print(sqrt(25))

import mymodule
mymodule.greet()


# ==========================================================
# Example 1: Importing the math Module
# ==========================================================

import math

number = 25

square_root = math.sqrt(number)

print("Example 1")
print("Number:", number)
print("Square Root:", square_root)

# Expected Output:
# Example 1
# Number: 25
# Square Root: 5.0


print("\n" + "=" * 50)


# ==========================================================
# Example 2: Using Another Function from the math Module
# ==========================================================

value = 4

power = math.pow(value, 3)

print("Example 2")
print("4 raised to the power of 3 is:", power)

# Expected Output:
# Example 2
# 4 raised to the power of 3 is: 64.0


print("\n" + "=" * 50)


# ==========================================================
# Example 3: Importing the random Module
# ==========================================================

import random

random_number = random.randint(1, 10)

print("Example 3")
print("Random Number between 1 and 10:", random_number)

# Output:
# A different random number may appear each time.
# Example:
# Random Number between 1 and 10: 7


print("\n" + "=" * 50)


# ==========================================================
# Example 4: Importing the datetime Module
# ==========================================================

import datetime

current_date = datetime.date.today()

print("Example 4")
print("Today's Date:", current_date)

# Output:
# Displays the current date.
# Example:
# Today's Date: 2026-06-29


print("\n" + "=" * 50)


# ==========================================================
# Example 5: Importing Only One Function
# ==========================================================

from math import factorial

number = 5

result = factorial(number)

print("Example 5")
print("Factorial of", number, "is", result)

# Expected Output:
# Example 5
# Factorial of 5 is 120


print("\n" + "=" * 50)


# ==========================================================
# Practice Example 1
# ==========================================================

import math

radius = 7

area = math.pi * radius * radius

print("Practice Example 1")
print("Radius:", radius)
print("Area of Circle:", area)


print("\n" + "=" * 50)


# ==========================================================
# Practice Example 2
# ==========================================================

import random

dice_number = random.randint(1, 6)

print("Practice Example 2")
print("Dice Number:", dice_number)


print("\n" + "=" * 50)


# ==========================================================
# Practice Example 3
# ==========================================================

from math import ceil

number = 6.3

rounded_number = ceil(number)

print("Practice Example 3")
print("Original Number:", number)
print("Rounded Up:", rounded_number)


print("\n" + "=" * 50)


# ==========================================================
# Summary
# ==========================================================

print("Modules help us organize and reuse Python code.")
print("Built-in modules save time by providing ready-made functions.")


# ==========================================================
# Challenge Exercises
# ==========================================================

# Challenge 1
# Import the math module and find the square root of 81.

# Challenge 2
# Generate a random number between 50 and 100.

# Challenge 3
# Import the datetime module and display today's date.

# Challenge 4
# Import only the sqrt() function from the math module
# and find the square root of 144.

# Challenge 5
# Calculate the area of a circle with a radius of 10
# using the value of pi from the math module.
