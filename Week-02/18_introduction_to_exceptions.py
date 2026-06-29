# ==========================================================
# Course : Artificial Intelligence using Python
# Week   : 02
# File   : 18_introduction_to_exceptions.py
# Lecture: 44
# Topic  : Introduction to Exceptions in Python
#
# What to Practice:
#     ✔ Understand what exceptions are
#     ✔ Learn common runtime errors
#     ✔ Understand program crashes vs handling
# ==========================================================

# ----------------------------------------------------------
# What is an Exception?
# ----------------------------------------------------------
# An exception is an error that happens during program execution.
#
# If not handled:
# ❌ Program crashes immediately
#
# If handled:
# ✔ Program continues safely
# ----------------------------------------------------------


# ==========================================================
# Example 1: Division by Zero Error
# ==========================================================

print("Example 1 - Division by zero error")

# This will cause an exception
# result = 10 / 0

print("Division by zero causes a crash if not handled")


print("\n" + "=" * 50)


# ==========================================================
# Example 2: Type Error
# ==========================================================

print("Example 2 - Type error")

# This will cause an exception
# result = "10" + 5

print("Adding string and integer causes TypeError")


print("\n" + "=" * 50)


# ==========================================================
# Example 3: Index Error
# ==========================================================

print("Example 3 - Index error")

numbers = [1, 2, 3]

# This will cause an exception
# print(numbers[5])

print("Accessing invalid index causes IndexError")


print("\n" + "=" * 50)


# ==========================================================
# Example 4: Key Error (Dictionary)
# ==========================================================

print("Example 4 - Key error")

student = {
    "name": "Ali",
    "age": 20
}

# This will cause an exception
# print(student["grade"])

print("Accessing missing dictionary key causes KeyError")


print("\n" + "=" * 50)


# ==========================================================
# Example 5: Why Exceptions Matter
# ==========================================================

print("Example 5 - Importance of exceptions")

# Without exception handling:
# Program stops immediately on error

# With exception handling:
# Program continues running safely

print("Exceptions help prevent program crashes")


print("\n" + "=" * 50)


# ==========================================================
# Example 6: Basic try-except Introduction
# ==========================================================

print("Example 6 - Basic handling preview")

try:
    result = 10 / 0
    print(result)

except ZeroDivisionError:
    print("Cannot divide by zero!")

# Output:
# Cannot divide by zero!


print("\n" + "=" * 50)


# ==========================================================
# Common Types of Exceptions
# ==========================================================
# ✔ ZeroDivisionError
# ✔ TypeError
# ✔ IndexError
# ✔ KeyError
# ✔ ValueError
# ==========================================================

print("Common Python exceptions occur during runtime errors")


print("\n" + "=" * 50)


# ==========================================================
# Real-Life Analogy
# ==========================================================
# Think of exceptions like:
#
# ✔ Car breaking down while driving
# ✔ Without control → accident (crash)
# ✔ With control → safe handling and recovery
# ==========================================================

print("Exceptions = runtime problems that must be handled")


print("\n" + "=" * 50)


# ==========================================================
# Practice Examples
# ==========================================================

# Practice 1

print("Practice 1")

# try:
#     print(10 / 0)

print("Division error example understood")

print()


# Practice 2

print("Practice 2")

numbers = [10, 20, 30]

# try:
#     print(numbers[10])

print("Index error example understood")

print()


# Practice 3

print("Practice 3")

data = {"name": "Ali"}

# try:
#     print(data["age"])

print("Key error example understood")


print("\n" + "=" * 50)


# ==========================================================
# Challenge Exercises
# ==========================================================

# Challenge 1
# What is an exception?

# Challenge 2
# What happens if exception is not handled?

# Challenge 3
# Give examples of common exceptions.

# Challenge 4
# What is ZeroDivisionError?

# Challenge 5
# Why do we use exception handling?


# ==========================================================
# Git Commit Message
# ==========================================================

# git add .
# git commit -m "Add lecture 44 introduction to exceptions in Python"
