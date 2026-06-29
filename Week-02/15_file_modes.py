# ==========================================================
# Course : Artificial Intelligence using Python
# Week   : 02
# File   : 15_file_modes.py
# Lecture: 41
# Topic  : Modes of File Handling (r, w, a)
#
# What to Practice:
#     ✔ Understand file modes deeply
#     ✔ Difference between r, w, a
#     ✔ Real behavior of each mode
#     ✔ When to use each mode
# ==========================================================









# ----------------------------------------------------------
# What are File Modes?
# ----------------------------------------------------------
# File modes define how a file is opened.
#
# Each mode controls:
# ✔ Reading
# ✔ Writing
# ✔ Appending
# ✔ File creation or deletion
# ----------------------------------------------------------


# ==========================================================
# Example 1: Read Mode ("r")
# ==========================================================

print("Example 1 - Read Mode")

file = open("mode_demo.txt", "w")
file.write("Line 1: Python is fun\n")
file.write("Line 2: File handling is useful\n")
file.close()

file = open("mode_demo.txt", "r")

content = file.read()
print(content)

file.close()

# Output:
# Line 1: Python is fun
# Line 2: File handling is useful


print("\n" + "=" * 50)


# ==========================================================
# Example 2: Write Mode ("w") - Overwrites Data
# ==========================================================

print("Example 2 - Write Mode")

file = open("mode_demo.txt", "w")

file.write("New content replaces old data\n")
file.write("Previous data is deleted\n")

file.close()

file = open("mode_demo.txt", "r")
print(file.read())
file.close()

# Output:
# New content replaces old data
# Previous data is deleted


print("\n" + "=" * 50)


# ==========================================================
# Example 3: Append Mode ("a") - Adds Data
# ==========================================================

print("Example 3 - Append Mode")

file = open("mode_demo.txt", "a")

file.write("This line is appended\n")
file.write("Old content remains safe\n")

file.close()

file = open("mode_demo.txt", "r")
print(file.read())

file.close()

# Output:
# New content replaces old data
# Previous data is deleted
# This line is appended
# Old content remains safe


print("\n" + "=" * 50)


# ==========================================================
# Example 4: Difference Between w and a
# ==========================================================

print("Example 4 - Difference between w and a")

# Write mode (w)
file = open("compare.txt", "w")
file.write("First line\n")
file.close()

# Append mode (a)
file = open("compare.txt", "a")
file.write("Second line added\n")
file.close()

file = open("compare.txt", "r")
print(file.read())
file.close()

# Output:
# First line
# Second line added


print("\n" + "=" * 50)


# ==========================================================
# Example 5: When to Use Each Mode
# ==========================================================
# ✔ "r" → When you only want to read data
# ✔ "w" → When you want to create new file or overwrite
# ✔ "a" → When you want to add new data safely
# ==========================================================

print("Use r for reading, w for overwrite, a for adding data")


print("\n" + "=" * 50)


# ==========================================================
# Real-Life Analogy
# ==========================================================
# Think of a file like a notebook:
#
# r → Read notebook only
# w → Erase everything and write new notes
# a → Add new notes at the end
# ==========================================================


# ==========================================================
# Practice Examples
# ==========================================================

# Practice 1

print("Practice 1 - Create and read file")

file = open("student_info.txt", "w")
file.write("Name: Ali\n")
file.write("Age: 20\n")
file.close()

file = open("student_info.txt", "r")
print(file.read())
file.close()

print()


# Practice 2

print("Practice 2 - Append data")

file = open("student_info.txt", "a")
file.write("Course: AI with Python\n")
file.close()

file = open("student_info.txt", "r")
print(file.read())
file.close()

print()


# Practice 3

print("Practice 3 - Overwrite file")

file = open("student_info.txt", "w")
file.write("New Student Data\n")
file.close()

file = open("student_info.txt", "r")
print(file.read())
file.close()


print("\n" + "=" * 50)


# ==========================================================
# Challenge Exercises
# ==========================================================

# Challenge 1
# What does "r" mode do?

# Challenge 2
# What happens in "w" mode?

# Challenge 3
# What is the use of "a" mode?

# Challenge 4
# Create a file and test all three modes.

# Challenge 5
# Explain real-life difference between w and a.


# ==========================================================
# Git Commit Message
# ==========================================================

# git add .
# git commit -m "Add lecture 41 file modes explanation with examples"
