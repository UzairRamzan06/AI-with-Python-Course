# Course : Artificial Intelligence using Python
# Week   : 02
# File   : 09_getters_and_setters.py
# Lecture: 35
# Topic  : Using Getters and Setters in Python
#
# What to Practice:
#     ✔ Understand getter methods
#     ✔ Understand setter methods
#     ✔ Access private attributes safely
#     ✔ Data validation using setters
# ==========================================================
class Student:
    @property
    def grade(self):
        return self.__grade
    def __init__(self,name,grade):
        self.__grade = grade
    def get_grade(self):
        return self.__grade
    def set_grade(self, grade):
        if 0 <= grade <= 100:
            self.__grade = grade
        else:
            print("invalid grade!")

student = Student("Ali" , 90)
student.set_grade(95)
print(student.get_grade())

#OUTPUT : 95

# IF MENTION NEGATIVE " - " INSIDE " student.set_grade(-95 ) " then output will be changed

student = Student("Ali" , 90)
student.set_grade(-95)             
print(student.get_grade())

# OUTPUT : Invalid grade! 
# OUTPUT : 90
----------------------------------------------------------



# ----------------------------------------------------------
# What are Getters and Setters?
# ----------------------------------------------------------
# In Encapsulation, we make variables private:
#     self.__age
#
# But we still need controlled access.
#
# ✔ Getter → used to GET value (read data)
# ✔ Setter → used to SET value (update data)
#
# This ensures:
# ✔ Data safety
# ✔ Validation
# ✔ Controlled modification
# ----------------------------------------------------------


# ==========================================================
# Example 1: Without Getters and Setters (Problem)
# ==========================================================

class Student:

    def __init__(self, name, age):
        self.name = name
        self.__age = age  # private variable


student = Student("Ali", 20)

print("Example 1")
print("Name:", student.name)

# Direct access is not allowed:
# print(student.__age)  ❌ Error

print("\nProblem: Cannot access private data directly")


print("\n" + "=" * 50)


# ==========================================================
# Example 2: Getter Method
# ==========================================================

class Student:

    def __init__(self, name, age):
        self.name = name
        self.__age = age

    # Getter method
    def get_age(self):
        return self.__age


student = Student("Sara", 22)

print("Example 2 - Getter")
print("Age:", student.get_age())

# Output:
# Age: 22


print("\n" + "=" * 50)


# ==========================================================
# Example 3: Setter Method
# ==========================================================

class Student:

    def __init__(self, name, age):
        self.name = name
        self.__age = age

    # Getter
    def get_age(self):
        return self.__age

    # Setter
    def set_age(self, new_age):
        self.__age = new_age


student = Student("Ali", 20)

print("Example 3 - Before Update")
print("Age:", student.get_age())

student.set_age(25)

print("After Update")
print("Age:", student.get_age())

# Output:
# Age: 20
# Age: 25


print("\n" + "=" * 50)


# ==========================================================
# Example 4: Setter with Validation (IMPORTANT)
# ==========================================================

class Student:

    def __init__(self, name, age):
        self.name = name
        self.__age = age

    def get_age(self):
        return self.__age

    def set_age(self, new_age):

        # Validation rule
        if new_age > 0:
            self.__age = new_age
        else:
            print("Invalid age! Age must be positive.")


student = Student("Ahmed", 30)

print("Example 4 - Validation")

student.set_age(35)
print("Updated Age:", student.get_age())

student.set_age(-10)  # Invalid input

# Output:
# Updated Age: 35
# Invalid age! Age must be positive.


print("\n" + "=" * 50)


# ==========================================================
# Example 5: Real-World Example (Bank Account)
# ==========================================================

class BankAccount:

    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance

    # Getter
    def get_balance(self):
        return self.__balance

    # Setter (Deposit)
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
        else:
            print("Invalid deposit amount!")

    # Setter (Withdraw)
    def withdraw(self, amount):
        if amount > self.__balance:
            print("Insufficient balance!")
        elif amount <= 0:
            print("Invalid withdrawal amount!")
        else:
            self.__balance -= amount

    def show_details(self):
        print("Owner  :", self.owner)
        print("Balance:", self.__balance)


account = BankAccount("Ali", 5000)

print("Example 5 - Bank System")

account.show_details()

account.deposit(2000)
print("After Deposit:", account.get_balance())

account.withdraw(1000)
print("After Withdraw:", account.get_balance())

account.withdraw(10000)  # Invalid case


print("\n" + "=" * 50)


# ==========================================================
# Key Concepts Summary
# ==========================================================
# ✔ Getter → reads private data
# ✔ Setter → updates private data
# ✔ Used with encapsulation
# ✔ Provides validation and control
# ==========================================================

print("Getters and Setters provide controlled access to data.")


print("\n" + "=" * 50)


# ==========================================================
# Practice Examples
# ==========================================================

# Practice 1

class Car:

    def __init__(self, brand):
        self.__brand = brand

    def get_brand(self):
        return self.__brand

car = Car("Toyota")

print("Practice 1")
print(car.get_brand())

print()


# Practice 2

class Employee:

    def __init__(self, salary):
        self.__salary = salary

    def get_salary(self):
        return self.__salary

    def set_salary(self, salary):
        if salary > 0:
            self.__salary = salary

emp = Employee(50000)

print("Practice 2")
print(emp.get_salary())
emp.set_salary(60000)
print(emp.get_salary())

print()


# Practice 3

class Laptop:

    def __init__(self, price):
        self.__price = price

    def get_price(self):
        return self.__price

laptop = Laptop(1200)

print("Practice 3")
print(laptop.get_price())


print("\n" + "=" * 50)


# ==========================================================
# Challenge Exercises
# ==========================================================

# Challenge 1
# What is a getter method?

# Challenge 2
# What is a setter method?

# Challenge 3
# Why do we use getters and setters?

# Challenge 4
# Create a class Student with private marks.

# Challenge 5
# Add getter and setter with validation.


# ==========================================================
# Git Commit Message
# ==========================================================

# git add .
# git commit -m "Add lecture 35 getters and setters with examples"
