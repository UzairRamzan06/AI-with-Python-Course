# Course : Artificial Intelligence using Python
# Week   : 02
# File   : 07_accessing_attributes_methods.py
# Lecture: 33
# Topic  : Accessing Object Attributes & Methods
#
# What to Practice:
#     ✔ Access instance variables (attributes)
#     ✔ Call instance methods
#     ✔ Understand dot notation
#     ✔ Work with multiple objects
# ==========================================================

class Car:
    def drive (self):
        print("The car is moving.")
car1 = Car()
car1.drive()

# Output : The car is moving.
# ----------------------------------------------------------
class Car:
    color = "red"
    def drive (self):
        print(f"{self.color} car is moving!")

car1 = Car()
car1.drive()

# Output: red car is moving!
# ----------------------------------------------------------
class Car:
    color = "red"
    def drive (self):
        print(f"{self.color} car is moving!")
    def setColor (self, new_color):
        self.color = new_color

car2 = Car()
car2.setColor("gree")
car2.drive()

# Output: gree car is moving!
# ----------------------------------------------------------




# What is Accessing in OOP?
# ----------------------------------------------------------
# Accessing means:
# ✔ Getting data from an object (attributes)
# ✔ Using functions of an object (methods)

# We use DOT notation:
#     object.attribute
#     object.method()
# ----------------------------------------------------------


# ==========================================================
# Example 1: Accessing Attributes
# ==========================================================

class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age


student = Student("Ali", 20)

print("Example 1")
print("Name:", student.name)
print("Age :", student.age)

# Output:
# Name: Ali
# Age : 20


print("\n" + "=" * 50)


# ==========================================================
# Example 2: Accessing Methods
# ==========================================================

class Student:

    def __init__(self, name):
        self.name = name

    def greet(self):
        print("Hello, my name is", self.name)


student = Student("Sara")

print("Example 2")
student.greet()

# Output:
# Hello, my name is Sara


print("\n" + "=" * 50)


# ==========================================================
# Example 3: Multiple Objects Accessing Data
# ==========================================================

class Student:

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def show(self):
        print(self.name, "scored", self.marks, "marks")


student1 = Student("Ali", 85)
student2 = Student("Sara", 90)

print("Example 3")

print("Accessing Attributes:")
print(student1.name, student1.marks)
print(student2.name, student2.marks)

print("\nAccessing Methods:")
student1.show()
student2.show()

# Output:
# Ali 85
# Sara 90
# Ali scored 85 marks
# Sara scored 90 marks


print("\n" + "=" * 50)


# ==========================================================
# Example 4: Updating Attributes Directly
# ==========================================================

class Student:

    def __init__(self, name):
        self.name = name

    def show(self):
        print("Student Name:", self.name)


student = Student("Ali")

print("Example 4 - Before Update")
student.show()

# Updating attribute directly
student.name = "Ahmed"

print("After Update")
student.show()

# Output:
# Student Name: Ali
# Student Name: Ahmed


print("\n" + "=" * 50)


# ==========================================================
# Example 5: Calling Multiple Methods
# ==========================================================

class Mobile:

    def __init__(self, brand):
        self.brand = brand

    def call(self):
        print(self.brand, "is making a call")

    def message(self):
        print(self.brand, "is sending a message")


phone = Mobile("Samsung")

print("Example 5")
phone.call()
phone.message()

# Output:
# Samsung is making a call
# Samsung is sending a message


print("\n" + "=" * 50)


# ==========================================================
# Example 6: Real-Life Interaction
# ==========================================================

class BankAccount:

    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def show_balance(self):
        print(self.owner, "has balance:", self.balance)


account = BankAccount("Ali", 5000)

print("Example 6")
account.show_balance()

# Accessing attribute + method together
print("Owner:", account.owner)
account.show_balance()

# Output:
# Ali has balance: 5000
# Owner: Ali
# Ali has balance: 5000


print("\n" + "=" * 50)


# ==========================================================
# Key Concept: Dot Notation
# ==========================================================
# We always use dot (.) to access:
#
# ✔ Attributes → object.attribute
# ✔ Methods    → object.method()
# ==========================================================

print("Dot notation is used to access attributes and methods.")


print("\n" + "=" * 50)


# ==========================================================
# Practice Examples
# ==========================================================

# Practice 1

class Car:

    def __init__(self, brand):
        self.brand = brand

car = Car("Toyota")

print("Practice 1")
print(car.brand)

print()


# Practice 2

class Employee:

    def __init__(self, name):
        self.name = name

    def show(self):
        print("Employee:", self.name)

emp = Employee("Sara")

print("Practice 2")
emp.show()

print()


# Practice 3

class Laptop:

    def __init__(self, brand):
        self.brand = brand

    def details(self):
        print("Laptop Brand:", self.brand)

laptop = Laptop("Dell")

print("Practice 3")
laptop.details()


print("\n" + "=" * 50)


# ==========================================================
# Challenge Exercises
# ==========================================================

# Challenge 1
# What is dot notation?

# Challenge 2
# Create a class Book with title attribute.

# Challenge 3
# Access the attribute using object.

# Challenge 4
# Create a method and call it using object.

# Challenge 5
# Create two objects and access both attributes and methods.


# ==========================================================
# Git Commit Message
# ==========================================================

# git add .
# git commit -m "Add lecture 33 accessing attributes and methods examples"
