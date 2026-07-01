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
# coach is explaining:
# You can create a file in Python using the open() function in write mode. When you write something like opening a file with "w" mode, Python creates the file if it does not already exist. 
# We create files to store data permanently so that information is not lost when the program closes. For example, you can save names, records, or results in a file and use them later. 
# In simple words, files are used to store data for future use, and Python automatically creates them when needed

# coach is explaining the difference between opening a file for reading ("r") and opening a file for writing ("w"). Here's what they mean in simpler words.
# 1. Read mode ("r")
# When you write:
file1 = open("demo.txt", "r")

# Python says: "I want to read an existing file."
# If demo.txt does not exist, Python gives this error: FileNotFoundError

2. Write mode ("w")
# When you write:
file1 = open("demo.txt", "w")

# Python says: "I want to write to this file."
# If demo.txt doesn't exist, Python creates it automatically

# Example:
file1 = open("demo.txt", "w")
file1.write("Hello World")
file1.close()

# After running this code, a new file named demo.txt will appear in your current folder, containing: Hello World
# ----------------------------------------------------------
# 3. Why do we create files?
# Normally, when a Python program ends, all the variables in memory disappear.
# For example:
name = "Muhammad Naqeeb"
# After the program finishes, name is gone.
# If you save it in a file:

file = open("student.txt", "w")
file.write("Muhammad Naqeeb")
file.close()
# Then even after closing Python, the file student.txt still exists on your computer. You can open it tomorrow, next week, or next month.

# That's what your coach means by: "Files are used to store data permanently."
# ----------------------------------------------------------
# 4. A simple analogy
# Think of your program like writing on a whiteboard:
# When the class ends, the whiteboard is erased. (Variables are lost.)
# A file is like writing in a notebook:
# The notebook keeps your notes even after you leave. (Data is saved permanently.)

# ----------------------------------------------------------
# 5. Summary
# "r" = Read → The file must already exist, or you'll get FileNotFoundError.
# "w" = Write → If the file doesn't exist, Python creates it automatically.
# Files are used to save data so it is available even after the program stops.
# Your coach is likely expecting you to understand this workflow:

# Step 1: Create the file
file = open("demo.txt", "w")
file.write("Hello World!")
file.close()

# Step 2: Read the same file
file = open("demo.txt", "r")
print(file.read())
file.close()

# The output will be: Hello World!
# ----------------------------------------------------------
# Step 3: Open file in write mode ( Write mode (`"w") → Create a new file or overwrite existing content.)
file1 = open("demo.txt", "w")
file1.write("this is another test.")
# The output will be: 21   ( when run th code output 21 means,pythong write 21 character in demo txt file )
file1.close()


# ----------------------------------------------------------
# Step 4: Append mode (`"a") → Add new data to the end of the existing file without deleting the old data.
# For append mode:
file1 = open("demo.txt", "a")
file1.write("\nNew line added!")
# The output will be: 16   ( when run th code output 16 means,pythong write 16 character in demo txt file )
file1.close()

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
