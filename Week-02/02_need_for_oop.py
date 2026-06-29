# Course : Artificial Intelligence using Python
# Week   : 02
# File   : 02_need_for_oop.py
# Lecture: 28
# Topic  : Understanding the Need for OOP
#
# What to Practice:
#     ✔ Why we need Object-Oriented Programming
#     ✔ Problems with procedural programming
#     ✔ Real-world thinking using objects
# ==========================================================




# ----------------------------------------------------------
# What is the Need for OOP?
# ----------------------------------------------------------
# In early programming, we used procedural programming.
# In procedural programming, code is written as functions.
#
# But as programs become large, problems start to appear:
# - Code becomes difficult to manage
# - Code is repeated again and again
# - Debugging becomes hard
# - Data and functions are separate
#
# Object-Oriented Programming (OOP) solves these problems.
# It combines data + functions into a single unit called "object".
# ----------------------------------------------------------


# ==========================================================
# Example 1: Procedural Style (Without OOP)
# ==========================================================

student_name = "Ali"
student_age = 20
student_marks = 85


def display_student(name, age, marks):
    print("Student Name:", name)
    print("Student Age:", age)
    print("Student Marks:", marks)


print("=== Procedural Approach ===")
display_student(student_name, student_age, student_marks)

# Output:
# Student Name: Ali
# Student Age: 20
# Student Marks: 85


print("\n" + "=" * 50)


# ==========================================================
# Problem with Procedural Approach
# ==========================================================
# If we want to add another student, we must create new variables
# and call the function again.
#
# This becomes messy when we have 100s of students.
# ==========================================================


# Example 2: Another student (repetition problem)

student_name2 = "Sara"
student_age2 = 22
student_marks2 = 90

print("=== Another Student (Repetition Problem) ===")
display_student(student_name2, student_age2, student_marks2)


print("\n" + "=" * 50)


# ==========================================================
# Why OOP is Better
# ==========================================================
# OOP allows us to:
# ✔ Combine data and functions
# ✔ Create reusable templates (classes)
# ✔ Create multiple objects easily
# ✔ Avoid repetition
# ✔ Organize code properly
# ==========================================================


# ==========================================================
# Real World Thinking Example
# ==========================================================
# Think about real-world objects:
#
# Car:
#   Data → color, model, price
#   Actions → start, stop
#
# Student:
#   Data → name, age, marks
#   Actions → study, display
#
# Bank Account:
#   Data → balance
#   Actions → deposit, withdraw
#
# OOP models real-world objects in programming.
# ==========================================================


# ==========================================================
# Simple Simulation (Still without OOP)
# ==========================================================

def car_info(model, color):
    print("Car Model:", model)
    print("Car Color:", color)


print("=== Car Example (Procedural) ===")
car_info("Toyota Corolla", "White")


# Output:
# Car Model: Toyota Corolla
# Car Color: White


print("\n" + "=" * 50)


# ==========================================================
# Limitation of Procedural Approach
# ==========================================================
# Imagine managing:
# - 100 students
# - 50 cars
# - 200 employees
#
# Using functions only becomes very difficult.
# That is why OOP is introduced.
# ==========================================================


# ==========================================================
# Challenge Exercises (Do not solve here)
# ==========================================================

# Challenge 1:
# Why is procedural programming difficult for large projects?

# Challenge 2:
# List 3 real-world objects that can be represented using OOP.

# Challenge 3:
# What is the main advantage of combining data and functions?

# Challenge 4:
# Rewrite student data for 3 students using variables (like above).

# Challenge 5:
# Why does repetition become a problem in procedural programming?


# ==========================================================
# Git Commit Message
# ==========================================================

# git add .
# git commit -m "Add lecture 28 need for OOP explanation with examples"
