# Course : Artificial Intelligence using Python
# Week   : 02
# File   : 04_creating_classes_and_objects.py
# Lecture: 30
# Topic  : Defining a Class & Creating Objects
#
# What to Practice:
#     ✔ Define a class
#     ✔ Create objects
#     ✔ Access object attributes
#     ✔ Call object methods
# ==========================================================





# ----------------------------------------------------------
# What is a Class?
# ----------------------------------------------------------
# A class is a blueprint or template for creating objects.
#
# What is an Object?
# An object is an instance of a class.
#
# Think of a class as a design for a house.
# Every house built from that design is an object.
# ----------------------------------------------------------


# ==========================================================
# Example 1: Creating Your First Class
# ==========================================================

class Student:
    pass


print("Example 1")
print("Student class created successfully.")

# Expected Output:
# Student class created successfully.


print("\n" + "=" * 50)


# ==========================================================
# Example 2: Creating Objects
# ==========================================================

class Student:
    pass

student1 = Student()
student2 = Student()

print("Example 2")
print("Two Student objects created.")

# Expected Output:
# Two Student objects created.


print("\n" + "=" * 50)


# ==========================================================
# Example 3: Adding Class Attributes
# ==========================================================

class Student:
    name = "Ali"
    age = 20

student = Student()

print("Example 3")
print("Name :", student.name)
print("Age  :", student.age)

# Expected Output:
# Name : Ali
# Age  : 20


print("\n" + "=" * 50)


# ==========================================================
# Example 4: Creating a Method
# ==========================================================

class Student:

    def display(self):
        print("Welcome to Python OOP!")

student = Student()

print("Example 4")
student.display()

# Expected Output:
# Welcome to Python OOP!


print("\n" + "=" * 50)


# ==========================================================
# Example 5: Class with Attributes and Method
# ==========================================================

class Student:

    name = "Sara"
    department = "Computer Science"

    def show_information(self):
        print("Student Name :", self.name)
        print("Department   :", self.department)

student = Student()

print("Example 5")
student.show_information()

# Expected Output:
# Student Name : Sara
# Department   : Computer Science


print("\n" + "=" * 50)


# ==========================================================
# Example 6: Creating Multiple Objects
# ==========================================================

class Car:

    brand = "Toyota"

    def start(self):
        print("Car started successfully.")

car1 = Car()
car2 = Car()

print("Example 6")

print("Car 1 Brand :", car1.brand)
car1.start()

print()

print("Car 2 Brand :", car2.brand)
car2.start()

# Expected Output:
# Car 1 Brand : Toyota
# Car started successfully.
#
# Car 2 Brand : Toyota
# Car started successfully.


print("\n" + "=" * 50)


# ==========================================================
# Example 7: Another Simple Class
# ==========================================================

class Mobile:

    brand = "Samsung"
    storage = "128 GB"

    def phone_info(self):
        print("Brand   :", self.brand)
        print("Storage :", self.storage)

mobile = Mobile()

print("Example 7")
mobile.phone_info()

# Expected Output:
# Brand   : Samsung
# Storage : 128 GB


print("\n" + "=" * 50)


# ==========================================================
# Practice Examples
# ==========================================================

# Practice 1

class Book:

    title = "Python Basics"

book = Book()

print("Practice 1")
print("Book Title :", book.title)

print()


# Practice 2

class Employee:

    company = "ABC Technologies"

employee = Employee()

print("Practice 2")
print("Company :", employee.company)

print()


# Practice 3

class Laptop:

    brand = "Dell"

    def show_brand(self):
        print("Laptop Brand :", self.brand)

laptop = Laptop()

print("Practice 3")
laptop.show_brand()


print("\n" + "=" * 50)


# ==========================================================
# Challenge Exercises
# ==========================================================

# Challenge 1
# Create a class named Teacher.

# Challenge 2
# Create an object of the Teacher class.

# Challenge 3
# Add two attributes:
# subject
# experience

# Challenge 4
# Create a method named introduce()
# that prints a simple message.

# Challenge 5
# Create two objects of a Car class
# and call the same method using both objects.


# ==========================================================
# End of File
# ==========================================================
