# Course : Artificial Intelligence using Python
# Week   : 02
# File   : 03_classes_objects_methods_attributes.py
# Lecture: 29
# Topic  : Core OOP Concepts - Classes, Objects,
#           Methods & Attributes
#
# What to Practice:
#     ✔ Understand what a Class is
#     ✔ Understand what an Object is
#     ✔ Learn about Attributes
#     ✔ Learn about Methods
# ==========================================================





# ----------------------------------------------------------
# Core Concepts of Object-Oriented Programming (OOP)
# ----------------------------------------------------------
# Before writing OOP programs, it is important to understand
# four basic concepts:
#
# 1. Class
# 2. Object
# 3. Attribute
# 4. Method
#
# These concepts help us organize code in a simple and
# structured way.
# ----------------------------------------------------------



# Concept 1: What is a Class?
# ==========================================================
#
# A class is a blueprint or template used to create objects.
#
# Think of a class as a design or plan.
#
# Real-Life Example:
#
# House Plan  -------->  Class
# Built House -------->  Object
#
# Student Template ---> Class
# Ali, Sara ----------> Objects
# ==========================================================

print("========== CLASS ==========")
print("A class is a blueprint used to create objects.")


print("\n" + "=" * 50)


# ==========================================================
# Concept 2: What is an Object?
# ==========================================================
#
# An object is a real instance of a class.
#
# A class describes something.
# An object represents the actual thing.
#
# Example:
#
# Class  : Student
#
# Objects:
#     Ali
#     Sara
#     Ahmed
#
# Each object has its own information.
# ==========================================================

print("========== OBJECT ==========")
print("An object is an instance of a class.")


print("\n" + "=" * 50)


# ==========================================================
# Concept 3: What is an Attribute?
# ==========================================================
#
# Attributes are the characteristics or properties
# of an object.
#
# Example:
#
# Student
# --------
# Name
# Age
# Marks
#
# Car
# ---
# Brand
# Color
# Model
# ==========================================================

student_name = "Ali"
student_age = 20
student_marks = 85

print("========== ATTRIBUTES ==========")
print("Name :", student_name)
print("Age  :", student_age)
print("Marks:", student_marks)

# Expected Output:
#
# Name : Ali
# Age  : 20
# Marks: 85


print("\n" + "=" * 50)


# ==========================================================
# Concept 4: What is a Method?
# ==========================================================
#
# A method is an action that an object can perform.
#
# Real-Life Examples:
#
# Student
#     Study()
#     Read()
#     Write()
#
# Car
#     Start()
#     Stop()
#
# Fan
#     Turn On()
#     Turn Off()
#
# In Python, methods are simply functions that belong
# to a class.
# ==========================================================


def study():
    print("Student is studying.")


def play():
    print("Student is playing.")


print("========== METHODS ==========")
study()
play()

# Expected Output:
#
# Student is studying.
# Student is playing.


print("\n" + "=" * 50)


# ==========================================================
# Understanding Class vs Object
# ==========================================================
#
# Imagine a Car Factory.
#
# Car Design
#      ↓
#    Class
#
# Car 1
# Car 2
# Car 3
#      ↓
#   Objects
# ==========================================================

print("Class  -> Car Design")
print("Object -> Actual Car")


print("\n" + "=" * 50)


# ==========================================================
# Understanding Attributes vs Methods
# ==========================================================
#
# Mobile Phone
#
# Attributes:
#     Brand
#     Color
#     Storage
#
# Methods:
#     Call()
#     Charge()
#     Restart()
# ==========================================================

mobile_brand = "Samsung"
mobile_color = "Black"
mobile_storage = "128 GB"

print("========== MOBILE ==========")
print("Brand   :", mobile_brand)
print("Color   :", mobile_color)
print("Storage :", mobile_storage)

print("Methods:")
print("- Call")
print("- Charge")
print("- Restart")


print("\n" + "=" * 50)


# ==========================================================
# Everyday Examples of OOP
# ==========================================================

print("========== REAL-WORLD OBJECTS ==========")

print("Student")
print("  Attributes -> Name, Age, Marks")
print("  Methods    -> Study(), Read()")

print()

print("Car")
print("  Attributes -> Brand, Model, Color")
print("  Methods    -> Start(), Stop()")

print()

print("Bank Account")
print("  Attributes -> Account Number, Balance")
print("  Methods    -> Deposit(), Withdraw()")


print("\n" + "=" * 50)


# ==========================================================
# Quick Revision
# ==========================================================

print("Class      -> Blueprint")
print("Object     -> Instance of a class")
print("Attribute  -> Property or Data")
print("Method     -> Action or Function")


print("\n" + "=" * 50)


# ==========================================================
# Practice Examples
# ==========================================================

# Practice 1

book_title = "Python Programming"
book_pages = 350

print("Practice 1")
print("Book Title :", book_title)
print("Pages      :", book_pages)

print()

# Practice 2

employee_name = "Sara"
employee_salary = 80000

print("Practice 2")
print("Employee Name   :", employee_name)
print("Employee Salary :", employee_salary)

print()

# Practice 3

print("Practice 3")
print("Think of a Laptop.")
print("Write its three attributes.")
print("Write its three methods.")


print("\n" + "=" * 50)


# ==========================================================
# Challenge Exercises
# ==========================================================

# Challenge 1
# Explain the difference between a class and an object.

# Challenge 2
# Write four attributes of a car.

# Challenge 3
# Write four methods of a mobile phone.

# Challenge 4
# Think of a bank account.
# List its attributes and methods.

# Challenge 5
# Explain why methods are important in OOP.


# ==========================================================
# End of File
# ==========================================================
