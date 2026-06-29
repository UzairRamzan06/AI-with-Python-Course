# Course : Artificial Intelligence using Python
# Week   : 02
# File   : 08_encapsulation.py
# Lecture: 34
# Topic  : Encapsulation in Python - Public & Private Attributes
#
# What to Practice:
#     ✔ Understand encapsulation
#     ✔ Public attributes
#     ✔ Private attributes
#     ✔ Data hiding concept
# ==========================================================



----------------------------------------------------------


----------------------------------------------------------



----------------------------------------------------------



# ----------------------------------------------------------
# What is Encapsulation?
# ----------------------------------------------------------
# Encapsulation means:
# ✔ Wrapping data (variables) and methods into one unit (class)
# ✔ Restricting direct access to some data
#
# In simple words:
# 👉 Protect data from direct modification
# ----------------------------------------------------------


# ==========================================================
# Example 1: Public Attributes (No Protection)
# ==========================================================

class Student:

    def __init__(self, name, age):
        self.name = name        # Public attribute
        self.age = age          # Public attribute


student = Student("Ali", 20)

print("Example 1")
print("Name:", student.name)
print("Age :", student.age)

# Output:
# Name: Ali
# Age : 20


print("\n" + "=" * 50)


# ==========================================================
# Problem with Public Attributes
# ==========================================================
# Anyone can change data directly.
# This may cause incorrect or unsafe values.
# ==========================================================

student.age = -10   # Invalid value (but still allowed)

print("After modification:")
print("Age:", student.age)

# Output:
# Age: -10
# (This is logically wrong, but Python allows it)


print("\n" + "=" * 50)


# ==========================================================
# Example 2: Private Attributes (Data Hiding)
# ==========================================================

class Student:

    def __init__(self, name, age):
        self.name = name
        self.__age = age   # Private attribute


student = Student("Sara", 22)

print("Example 2")
print("Name:", student.name)

# Trying to access private attribute directly
# print(student.__age)  ❌ This will cause error

# Output:
# AttributeError: 'Student' object has no attribute '__age'


print("\n" + "=" * 50)


# ==========================================================
# Example 3: Accessing Private Data Using Method
# ==========================================================

class Student:

    def __init__(self, name, age):
        self.name = name
        self.__age = age

    def show_age(self):
        print("Age:", self.__age)


student = Student("Ali", 20)

print("Example 3")
student.show_age()

# Output:
# Age: 20


print("\n" + "=" * 50)


# ==========================================================
# Example 4: Updating Private Data Safely
# ==========================================================

class Student:

    def __init__(self, name, age):
        self.name = name
        self.__age = age

    def set_age(self, new_age):
        if new_age > 0:
            self.__age = new_age
        else:
            print("Invalid age!")

    def show(self):
        print(self.name, "is", self.__age, "years old")


student = Student("Ahmed", 25)

print("Example 4 - Before Update")
student.show()

student.set_age(30)

print("After Update")
student.show()

student.set_age(-5)  # Invalid update

# Output:
# Ahmed is 25 years old
# Ahmed is 30 years old
# Invalid age!


print("\n" + "=" * 50)


# ==========================================================
# Example 5: Why Encapsulation is Important
# ==========================================================

# Without encapsulation:
# ❌ Anyone can change data incorrectly

# With encapsulation:
# ✔ Data is protected
# ✔ Controlled updates
# ✔ Better security
# ✔ Better program design


print("Encapsulation helps protect data from invalid changes.")


print("\n" + "=" * 50)


# ==========================================================
# Real-Life Analogy
# ==========================================================
# Bank Account System:
#
# Balance is PRIVATE
# You cannot directly change it
#
# You must use methods:
# ✔ deposit()
# ✔ withdraw()
#
# This ensures safety and control.
# ==========================================================


class BankAccount:

    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient balance!")

    def show_balance(self):
        print("Balance:", self.__balance)


account = BankAccount("Ali", 5000)

print("Example 6 - Bank System")

account.show_balance()
account.deposit(2000)
account.show_balance()
account.withdraw(1000)
account.show_balance()
account.withdraw(10000)

# Output:
# Balance: 5000
# Balance: 7000
# Balance: 6000
# Insufficient balance!


print("\n" + "=" * 50)


# ==========================================================
# Key Concepts Summary
# ==========================================================
# ✔ Public attributes  → accessible directly
# ✔ Private attributes → use __ (double underscore)
# ✔ Use methods to control private data
# ✔ Encapsulation = data protection
# ==========================================================

print("Encapsulation = Protecting data using private variables.")


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
        self.__name = name

    def show(self):
        print(self.__name)

emp = Employee("Sara")

print("Practice 2")
emp.show()

print()


# Practice 3

class Laptop:

    def __init__(self, brand):
        self.__brand = brand

    def get_brand(self):
        return self.__brand

laptop = Laptop("Dell")

print("Practice 3")
print(laptop.get_brand())


print("\n" + "=" * 50)


# ==========================================================
# Challenge Exercises
# ==========================================================

# Challenge 1
# What is encapsulation?

# Challenge 2
# What is a private attribute?

# Challenge 3
# Why do we use encapsulation?

# Challenge 4
# Create a class Student with private marks.

# Challenge 5
# Create methods to safely update and display marks.


# ==========================================================
# Git Commit Message
# ==========================================================

# git add .
# git commit -m "Add lecture 34 encapsulation with public and private attributes"
