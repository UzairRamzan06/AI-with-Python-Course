# Course : Artificial Intelligence using Python
# Week   : 02
# File   : 05_constructor_init_method.py
# Lecture: 31
# Topic  : The __init__() Constructor Method
#
# What to Practice:
#     ✔ Understand constructor (__init__)
#     ✔ Initialize object data automatically
#     ✔ Difference between normal method and constructor
# ==========================================================

class Dog:
    def __init__(self):
        self.name = "Buddy"
    def bark(self):
        print(f"{self.name} says Woof!")

dog1 = Dog()
dog1.bark()

# Output  : Buddy says Woof!
# ----------------------------------------------------------
class Car:
    def __init__ (self , brand , color ):
        self.brand = brand
        self.color = color    
      
car1 = Car ("Toyota" , "Red")
print(car1.brand)
print(car1.color)    

# Output :   Toyota
# Output :   Red

# ----------------------------------------------------------
car1.color = "Blue"
car2 = Car ("Honda" , "White" )
print (car2.brand)
print (car2.color)
print (car1.color)

# Output :   Honda
# Output :   White
# Output :   Blue


# ----------------------------------------------------------
# What is a Constructor?
# ----------------------------------------------------------
# A constructor is a special method in Python.
#
# It is automatically called when an object is created.
#
# In Python, constructor is written as:
#     __init__()
#
# Purpose of constructor:
# ✔ Initialize object data
# ✔ Assign values when object is created
# ✔ Reduce repetition
# ----------------------------------------------------------


# ==========================================================
# Example 1: Without Constructor (Problem)
# ==========================================================

class Student:

    def set_data(self, name, age):
        self.name = name
        self.age = age

student1 = Student()
student1.set_data("Ali", 20)

print("Example 1")
print("Name:", student1.name)
print("Age :", student1.age)

# Output:
# Name: Ali
# Age : 20


print("\n" + "=" * 50)


# ==========================================================
# Problem in Above Approach
# ==========================================================
# We had to call set_data() separately after creating object.
# This is extra work and can be forgotten.
# ==========================================================


# ==========================================================
# Example 2: Using Constructor (__init__)
# ==========================================================

class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age

student1 = Student("Ali", 20)

print("Example 2")
print("Name:", student1.name)
print("Age :", student1.age)

# Output:
# Name: Ali
# Age : 20


print("\n" + "=" * 50)


# ==========================================================
# Example 3: Constructor Automatically Runs
# ==========================================================

class Student:

    def __init__(self):
        print("Constructor is called automatically!")

student1 = Student()

print("Example 3")
print("Object created successfully.")

# Output:
# Constructor is called automatically!
# Object created successfully.


print("\n" + "=" * 50)


# ==========================================================
# Example 4: Constructor with Multiple Objects
# ==========================================================

class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age

student1 = Student("Ali", 20)
student2 = Student("Sara", 22)

print("Example 4")

print("Student 1:", student1.name, student1.age)
print("Student 2:", student2.name, student2.age)

# Output:
# Student 1: Ali 20
# Student 2: Sara 22


print("\n" + "=" * 50)


# ==========================================================
# Example 5: Constructor with Method
# ==========================================================

class Student:

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display(self):
        print("Name  :", self.name)
        print("Marks :", self.marks)

student = Student("Ahmed", 85)

print("Example 5")
student.display()

# Output:
# Name  : Ahmed
# Marks : 85


print("\n" + "=" * 50)


# ==========================================================
# Example 6: Default Values in Constructor
# ==========================================================

class Student:

    def __init__(self, name="Unknown", age=0):
        self.name = name
        self.age = age

student1 = Student()
student2 = Student("Ali", 20)

print("Example 6")

print("Student 1:", student1.name, student1.age)
print("Student 2:", student2.name, student2.age)

# Output:
# Student 1: Unknown 0
# Student 2: Ali 20


print("\n" + "=" * 50)


# ==========================================================
# Example 7: Real-Life Analogy
# ==========================================================
# Think of a constructor like a "form filling system".
#
# When you create a student record:
# ✔ Name is filled
# ✔ Age is filled
#
# You don't need to set values later manually.
# ==========================================================

class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age

student = Student("Zara", 21)

print("Example 7")
print(student.name, student.age)


print("\n" + "=" * 50)


# ==========================================================
# Practice Examples
# ==========================================================

# Practice 1

class Book:

    def __init__(self, title):
        self.title = title

book = Book("Python Basics")

print("Practice 1")
print(book.title)

print()


# Practice 2

class Car:

    def __init__(self, brand):
        self.brand = brand

car = Car("Toyota")

print("Practice 2")
print(car.brand)

print()


# Practice 3

class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

employee = Employee("Sara", 50000)

print("Practice 3")
print(employee.name, employee.salary)


print("\n" + "=" * 50)


# ==========================================================
# Challenge Exercises
# ==========================================================

# Challenge 1
# What is the purpose of __init__() method?

# Challenge 2
# Create a class named Laptop with:
# brand, price

# Challenge 3
# Create 2 objects of Laptop class.

# Challenge 4
# Add a method display() that prints laptop details.

# Challenge 5
# What happens if we do not use a constructor?


# ==========================================================
# Git Commit Message
# ==========================================================

# git add .
# git commit -m "Add lecture 31 constructor init method examples"
