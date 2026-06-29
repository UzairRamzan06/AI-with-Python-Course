# ==========================================================
# Course : Artificial Intelligence using Python
# Week   : 02
# File   : 14_file_read_write.py
# Lecture: 40
# Topic  : Reading from & Writing to Files in Python
#
# What to Practice:
#     ✔ Open files in Python
#     ✔ Write data to files
#     ✔ Read data from files
#     ✔ Understand file modes (basic intro)
# ==========================================================











# ----------------------------------------------------------
# What is File Handling?
# ----------------------------------------------------------
# File handling means:
# ✔ Storing data permanently in a file
# ✔ Reading data from a file later
#
# Why it is important?
# ✔ AI datasets are stored in files
# ✔ Logs and reports are saved in files
# ----------------------------------------------------------


# ==========================================================
# Example 1: Writing to a File
# ==========================================================

print("Example 1 - Writing to file")

file = open("demo.txt", "w")  # "w" mode = write mode

file.write("Hello, this is my first file.\n")
file.write("I am learning Python file handling.\n")

file.close()

print("Data written successfully!")

# Output:
# Data written successfully!


print("\n" + "=" * 50)


# ==========================================================
# Example 2: Reading from a File
# ==========================================================

print("Example 2 - Reading from file")

file = open("demo.txt", "r")  # "r" mode = read mode

content = file.read()

print(content)

file.close()

# Output:
# Hello, this is my first file.
# I am learning Python file handling.


print("\n" + "=" * 50)


# ==========================================================
# Example 3: Writing (Overwriting Existing File)
# ==========================================================

print("Example 3 - Overwriting file")

file = open("demo.txt", "w")

file.write("This is new content.\n")
file.write("Old content will be removed.\n")

file.close()

print("File updated successfully!")

# Output:
# File updated successfully!


print("\n" + "=" * 50)


# ==========================================================
# Example 4: Reading Line by Line
# ==========================================================

print("Example 4 - Reading line by line")

file = open("demo.txt", "r")

for line in file:
    print(line.strip())

file.close()

# Output:
# This is new content.
# Old content will be removed.


print("\n" + "=" * 50)


# ==========================================================
# Example 5: Appending Data to File
# ==========================================================

print("Example 5 - Appending data")

file = open("demo.txt", "a")  # "a" = append mode

file.write("Adding more data without deleting old content.\n")

file.close()

print("Data appended successfully!")

# Output:
# Data appended successfully!


print("\n" + "=" * 50)


# ==========================================================
# Real-Life Analogy
# ==========================================================
# Think of a file like a notebook:
#
# ✔ write mode → erase and write new notes
# ✔ read mode  → read existing notes
# ✔ append     → add new notes at the end
# ==========================================================


# ==========================================================
# Important File Modes
# ==========================================================
# "r" → read
# "w" → write (overwrite)
# "a" → append
# ==========================================================

print("File handling modes: r, w, a")


print("\n" + "=" * 50)


# ==========================================================
# Practice Examples
# ==========================================================

# Practice 1

print("Practice 1 - Write file")

file = open("student.txt", "w")
file.write("Student Name: Ali\n")
file.write("Course: AI with Python\n")
file.close()

print("File created")


print()


# Practice 2

print("Practice 2 - Read file")

file = open("student.txt", "r")

print(file.read())

file.close()


print()


# Practice 3

print("Practice 3 - Append file")

file = open("student.txt", "a")
file.write("Status: Active Student\n")
file.close()

print("Data appended")


print("\n" + "=" * 50)


# ==========================================================
# Challenge Exercises
# ==========================================================

# Challenge 1
# What is file handling?

# Challenge 2
# What does "r" mode do?

# Challenge 3
# What is the difference between "w" and "a"?

# Challenge 4
# Create a file and write 3 lines of your bio.

# Challenge 5
# Read and print the file content line by line.


# ==========================================================
# Git Commit Message
# ==========================================================

# git add .
# git commit -m "Add lecture 40 file read and write operations in Python"
