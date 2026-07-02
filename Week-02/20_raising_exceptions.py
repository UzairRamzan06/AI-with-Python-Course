# Course : Artificial Intelligence using Python
# Week   : 02
# File   : 20_raising_exceptions.py
# Lecture: 46
# Topic  : Raising Exceptions in Python
#
# What to Practice:
#     ✔ Understand raise keyword
#     ✔ Manually trigger exceptions
#     ✔ Validate user input
#     ✔ Build rule-based error systems
# ==========================================================
age = -3
if age < 0:
    raise ValueError("Age cannot be Negative!")

#OUTPUT : 

"""
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)
Cell In[2], line 2
      1 if age < 0:
----> 2     raise ValueError("Age cannot be Negative!")

ValueError: Age cannot be Negative!

"""





# ----------------------------------------------------------
# What does "raise" mean?
# ----------------------------------------------------------
# raise is used to:
# ✔ Manually generate an exception
#
# Why?
# ✔ To enforce rules
# ✔ To stop invalid data
# ✔ To control program flow
# ----------------------------------------------------------


# ==========================================================
# Example 1: Simple raise statement
# ==========================================================

print("Example 1 - Basic raise")

age = 15

if age < 18:
    raise Exception("Age must be 18 or above")

print("You are allowed")

# Output:
# Exception: Age must be 18 or above


print("\n" + "=" * 50)


# ==========================================================
# Example 2: Raising ValueError
# ==========================================================

print("Example 2 - ValueError")

number = -5

if number < 0:
    raise ValueError("Number cannot be negative")

print("Valid number")

# Output:
# ValueError: Number cannot be negative


print("\n" + "=" * 50)


# ==========================================================
# Example 3: Input Validation Example
# ==========================================================

print("Example 3 - Input validation")

password = "123"

if len(password) < 6:
    raise ValueError("Password must be at least 6 characters long")

print("Password accepted")

# Output:
# ValueError: Password must be at least 6 characters long


print("\n" + "=" * 50)


# ==========================================================
# Example 4: Raising with try-except
# ==========================================================

print("Example 4 - raise with handling")

try:
    marks = 150

    if marks > 100:
        raise ValueError("Marks cannot exceed 100")

except ValueError as e:
    print("Error caught:", e)

print("Program continues safely")

# Output:
# Error caught: Marks cannot exceed 100
# Program continues safely


print("\n" + "=" * 50)


# ==========================================================
# Example 5: Real-World Use Case
# ==========================================================

print("Example 5 - Real-world validation")

def check_username(username):

    if len(username) < 3:
        raise ValueError("Username too short")

    if username.isdigit():
        raise ValueError("Username cannot be only numbers")

    return "Valid username"


try:
    print(check_username("12"))

except ValueError as e:
    print("Validation error:", e)

# Output:
# Validation error: Username too short


print("\n" + "=" * 50)


# ==========================================================
# Example 6: Why raise is important
# ==========================================================
# ✔ Ensures data correctness
# ✔ Stops invalid operations
# ✔ Used in APIs and AI pipelines
# ✔ Helps enforce business rules
# ==========================================================

print("raise helps enforce rules in programs")


print("\n" + "=" * 50)


# ==========================================================
# Practice Examples
# ==========================================================

# Practice 1

print("Practice 1")

age = 10

if age < 18:
    raise ValueError("Must be 18+")

print()


# Practice 2

print("Practice 2")

score = 120

if score > 100:
    raise Exception("Invalid score")

print()


# Practice 3

print("Practice 3")

password = "abc"

if len(password) < 6:
    raise ValueError("Weak password")


print("\n" + "=" * 50)


# ==========================================================
# Challenge Exercises
# ==========================================================

# Challenge 1
# What is the purpose of raise?

# Challenge 2
# When should we use raise?

# Challenge 3
# Create a function that raises error for invalid input.

# Challenge 4
# Raise exception for negative numbers.

# Challenge 5
# Explain real-world use of raise in APIs.


# ==========================================================
# Git Commit Message
# ==========================================================

# git add .
# git commit -m "Add lecture 46 raising exceptions with validation examples"
