# ==========================================================
# Course : Artificial Intelligence using Python
# Week   : 02
# File   : 16_context_manager.py
# Lecture: 42
# Topic  : Using Context Managers (with Statement)
#
# What to Practice:
#     ✔ Understand context manager
#     ✔ Use "with" for file handling
#     ✔ Automatic file closing
#     ✔ Safer and cleaner code
# ==========================================================






# ----------------------------------------------------------
# What is a Context Manager?
# ----------------------------------------------------------
# A context manager automatically manages resources.
#
# In file handling:
# ✔ It opens the file
# ✔ It closes the file automatically
#
# We use:
#     with open(...) as file:
# ----------------------------------------------------------


# ==========================================================
# Example 1: Writing File using "with"
# ==========================================================

print("Example 1 - Writing using with")

with open("context_demo.txt", "w") as file:
    file.write("Hello from context manager\n")
    file.write("This is safe file handling\n")

# No need to use file.close()

print("Data written successfully!")

# Output:
# Data written successfully!


print("\n" + "=" * 50)


# ==========================================================
# Example 2: Reading File using "with"
# ==========================================================

print("Example 2 - Reading using with")

with open("context_demo.txt", "r") as file:
    content = file.read()
    print(content)

# File is automatically closed here

# Output:
# Hello from context manager
# This is safe file handling


print("\n" + "=" * 50)


# ==========================================================
# Example 3: Why "with" is Better
# ==========================================================

print("Example 3 - Without manual close")

file = open("demo_old.txt", "w")
file.write("This is manual file handling\n")
file.close()

print("File closed manually")

# Problem:
# ❌ If we forget file.close(), memory issues can happen


print("\n" + "=" * 50)


# ==========================================================
# Example 4: Multiple File Operations using with
# ==========================================================

print("Example 4 - Multiple operations")

with open("multi.txt", "w") as file:
    file.write("Line 1\n")
    file.write("Line 2\n")
    file.write("Line 3\n")

with open("multi.txt", "r") as file:
    print(file.read())

# Output:
# Line 1
# Line 2
# Line 3


print("\n" + "=" * 50)


# ==========================================================
# Example 5: Real-Life Analogy
# ==========================================================
# Think of "with" like:
#
# ✔ Entering a shop → system opens file
# ✔ Doing work     → read/write data
# ✔ Leaving shop    → file closes automatically
# ==========================================================

print("Context manager = automatic resource handling")


print("\n" + "=" * 50)


# ==========================================================
# Practice Examples
# ==========================================================

# Practice 1

print("Practice 1")

with open("student_with.txt", "w") as file:
    file.write("Name: Ali\n")
    file.write("Course: AI Python\n")

with open("student_with.txt", "r") as file:
    print(file.read())

print()


# Practice 2

print("Practice 2")

with open("student_with.txt", "a") as file:
    file.write("Status: Active\n")

with open("student_with.txt", "r") as file:
    print(file.read())

print()


# Practice 3

print("Practice 3")

with open("numbers.txt", "w") as file:
    file.write("1\n2\n3\n4\n5\n")

with open("numbers.txt", "r") as file:
    print(file.read())


print("\n" + "=" * 50)


# ==========================================================
# Challenge Exercises
# ==========================================================

# Challenge 1
# What is a context manager?

# Challenge 2
# Why do we use "with"?

# Challenge 3
# What problem does "with" solve?

# Challenge 4
# Create a file using with and write your name.

# Challenge 5
# Read file content using with statement.


# ==========================================================
# Git Commit Message
# ==========================================================

# git add .
# git commit -m "Add lecture 42 context manager with file handling examples"
