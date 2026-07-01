# ==========================================================
# Course : Artificial Intelligence using Python
# Week   : 02
# File   : 17_file_exception_handling.py
# Lecture: 43
# Topic  : Handling Exceptions During File Operations
#
# What to Practice:
#     ✔ Handle file errors safely
#     ✔ Use try-except with file handling
#     ✔ Avoid program crashes
#     ✔ Understand real-world robustness
# ==========================================================
"""
What is an Exception?
---------------------
An exception is an error that occurs while the program is running.

Example:
If we try to open a file that does not exist:

    with open("missing.txt", "r") as file:
        print(file.read())

Python raises:
    FileNotFoundError

The program stops immediately.

Why use try and except?
-----------------------
The try block runs code that may cause an error.

The except block handles the error instead of crashing the program.

Example:

try:
    with open("missing.txt", "r") as file:
        print(file.read())
except FileNotFoundError:
        print("File not found!")

Output:
    File not found!

Key Points:
- try -> Execute code that may cause an error.
- except -> Handle the error.
- FileNotFoundError -> Raised when the file does not exist.
- Exception handling keeps the program running.
"""

# ----------------------------------------------------------
# Why do we need Exception Handling in Files?
# ----------------------------------------------------------
# File operations can fail due to:
# ✔ File not found
# ✔ Permission denied
# ✔ Wrong file path
#
# Without handling:
# ❌ Program crashes
#
# With handling:
# ✔ Program stays safe
# ----------------------------------------------------------


# ==========================================================
# Example 1: File Not Found Error (Without Handling)
# ==========================================================

print("Example 1 - Without handling (dangerous)")

# This will crash if file does not exist
# file = open("missing.txt", "r")

print("If file is missing, program will crash!")


print("\n" + "=" * 50)


# ==========================================================
# Example 2: Handling File Not Found Error
# ==========================================================

print("Example 2 - With try-except")

try:
    file = open("missing.txt", "r")
    content = file.read()
    print(content)
    file.close()

except FileNotFoundError:
    print("Error: File not found!")

# Output:
# Error: File not found!


print("\n" + "=" * 50)


# ==========================================================
# Example 3: Safe File Reading
# ==========================================================

print("Example 3 - Safe reading")

filename = "safe_file.txt"

# Create file first
with open(filename, "w") as file:
    file.write("This is a safe file\n")
    file.write("Used for testing exception handling\n")

try:
    with open(filename, "r") as file:
        print(file.read())

except FileNotFoundError:
    print("File does not exist!")

# Output:
# This is a safe file
# Used for testing exception handling


print("\n" + "=" * 50)


# ==========================================================
# Example 4: Handling Multiple Errors
# ==========================================================

print("Example 4 - Multiple error handling")

try:
    file = open("another_missing.txt", "r")
    print(file.read())
    file.close()

except FileNotFoundError:
    print("File missing error handled safely!")

except PermissionError:
    print("Permission denied error handled!")

# Output:
# File missing error handled safely!


print("\n" + "=" * 50)


# ==========================================================
# Example 5: finally Block (Always Executes)
# ==========================================================

print("Example 5 - finally block")

try:
    file = open("test_finally.txt", "w")
    file.write("Testing finally block\n")
    file.close()

except Exception as e:
    print("Error occurred:", e)

finally:
    print("This block always executes (cleanup section)")

# Output:
# This block always executes (cleanup section)


print("\n" + "=" * 50)


# ==========================================================
# Example 6: Real-World File Safety Pattern
# ==========================================================

print("Example 6 - Real-world safe file handling")

def read_file(filename):
    try:
        with open(filename, "r") as file:
            return file.read()

    except FileNotFoundError:
        return "File not found (handled safely)"


print(read_file("safe_file.txt"))
print(read_file("wrong_file.txt"))

# Output:
# File content OR error message safely handled


print("\n" + "=" * 50)


# ==========================================================
# Key Concepts Summary
# ==========================================================
# ✔ try → test code
# ✔ except → handle errors
# ✔ finally → always runs
# ✔ Prevents program crash
# ==========================================================

print("File exception handling makes programs safe and stable.")


print("\n" + "=" * 50)


# ==========================================================
# Practice Examples
# ==========================================================

# Practice 1

print("Practice 1")

try:
    file = open("practice_file.txt", "r")
    print(file.read())
    file.close()

except FileNotFoundError:
    print("File not found handled")

print()


# Practice 2

print("Practice 2")

with open("practice_file.txt", "w") as file:
    file.write("Hello AI Student\n")

try:
    with open("practice_file.txt", "r") as file:
        print(file.read())

except FileNotFoundError:
    print("Error handled")

print()


# Practice 3

print("Practice 3")

try:
    file = open("data.txt", "r")
    print(file.read())
    file.close()

except FileNotFoundError:
    print("Data file missing but handled safely")


print("\n" + "=" * 50)


# ==========================================================
# Challenge Exercises
# ==========================================================

# Challenge 1
# What is FileNotFoundError?

# Challenge 2
# Why do we use try-except in file handling?

# Challenge 3
# What does finally block do?

# Challenge 4
# Create a program that safely reads a file.

# Challenge 5
# Handle multiple file errors safely.


# ==========================================================
# Git Commit Message
# ==========================================================

# git add .
# git commit -m "Add lecture 43 file exception handling with safe practices"
