# Course : Artificial Intelligence using Python
# Week   : 02
# File   : 06_instance_variables_methods.py
# Lecture: 32
# Topic  : Instance Variables & Instance Methods
#
# What to Practice:
#     ✔ Understand instance variables
#     ✔ Understand instance methods
#     ✔ Difference between class and instance data
#     ✔ How objects store their own data
# ==========================================================
class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade
    def display_info(self):
        print(f"Student_Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Grade: {self.grade}")
    def is_eligible(self):
        if self.age >=15:
            print (self.name, "is eligible for admission.")
        else:
            print (self.name, " is not eligible for admission.")

# Creating objects
student1 = Student("Ali",16,"10th")
student2 = Student("Sara",14,"8th")

# Accessing attributes
print(student1.name)
print(student2.grade)

# Output : Ali
# Output : 8th

# Calling methods
student1.display_info()
student1.is_eligible()

# Output : Student_Name: Ali
# Output : Age: 16
# Output : Grade: 10th
# Output : Ali is eligible for admission.

# Calling methods
student2.display_info()
student2.is_eligible()

# Output : Student_Name: Sara
# Output : Age: 14
# Output : Grade: 8th
# Output : Sara  is not eligible for admission.



# ----------------------------------------------------------
# What are Instance Variables?
# ----------------------------------------------------------
# Instance variables are variables that belong to an object.
#
# Each object has its own copy of instance variables.
#
# Example:
# student1 → name = Ali
# student2 → name = Sara
#
# Both are separate objects with separate data.
# ----------------------------------------------------------


# ----------------------------------------------------------
# What are Instance Methods?
# ----------------------------------------------------------
# Instance methods are functions inside a class.
#
# They work with instance variables using "self".
#
# They define behavior of objects.
# ----------------------------------------------------------


# ==========================================================
# Example 1: Instance Variables using Constructor
# ==========================================================

class Student:

    def __init__(self, name, age):
        # Instance variables
        self.name = name
        self.age = age


student1 = Student("Ali", 20)
student2 = Student("Sara", 22)

print("Example 1")
print("Student 1:", student1.name, student1.age)
print("Student 2:", student2.name, student2.age)

# Output:
# Student 1: Ali 20
# Student 2: Sara 22


print("\n" + "=" * 50)


# ==========================================================
# Example 2: Each Object Has Its Own Data
# ==========================================================

student1.name = "Ahmed"

print("Example 2")
print("Student 1 Updated Name:", student1.name)
print("Student 2 Name:", student2.name)

# Output:
# Student 1 Updated Name: Ahmed
# Student 2 Name: Sara

# Each object is independent.


print("\n" + "=" * 50)


# ==========================================================
# Example 3: Instance Method
# ==========================================================

class Student:

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display(self):
        print("Name  :", self.name)
        print("Marks :", self.marks)


student = Student("Ali", 85)

print("Example 3")
student.display()

# Output:
# Name  : Ali
# Marks : 85


print("\n" + "=" * 50)


# ==========================================================
# Example 4: Multiple Objects with Methods
# ==========================================================

class Student:

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display(self):
        print(self.name, "scored", self.marks, "marks")


student1 = Student("Ali", 85)
student2 = Student("Sara", 90)

print("Example 4")
student1.display()
student2.display()

# Output:
# Ali scored 85 marks
# Sara scored 90 marks


print("\n" + "=" * 50)


# ==========================================================
# Example 5: Modifying Instance Variables
# ==========================================================

class Student:

    def __init__(self, name):
        self.name = name

    def update_name(self, new_name):
        self.name = new_name

    def show(self):
        print("Student Name:", self.name)


student = Student("Ali")

print("Example 5 - Before Update")
student.show()

student.update_name("Ahmed")

print("After Update")
student.show()

# Output:
# Student Name: Ali
# Student Name: Ahmed


print("\n" + "=" * 50)


# ==========================================================
# Example 6: Instance Method with Calculation
# ==========================================================

class Student:

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def calculate_percentage(self):
        return (self.marks / 100) * 100


student = Student("Sara", 80)

print("Example 6")
print("Percentage:", student.calculate_percentage())

# Output:
# Percentage: 80.0


print("\n" + "=" * 50)


# ==========================================================
# Real-Life Analogy
# ==========================================================
# Think of each student as a separate object:
#
# Student 1:
#   Name  → Ali
#   Marks → 85
#
# Student 2:
#   Name  → Sara
#   Marks → 90
#
# Each student has:
# ✔ Their own data (instance variables)
# ✔ Their own behavior (instance methods)
# ==========================================================


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

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def show(self):
        print(self.name, self.salary)

employee = Employee("Sara", 50000)

print("Practice 2")
employee.show()

print()


# Practice 3

class Laptop:

    def __init__(self, brand, price):
        self.brand = brand
        self.price = price

    def details(self):
        print(self.brand, self.price)

laptop = Laptop("Dell", 1200)

print("Practice 3")
laptop.details()


print("\n" + "=" * 50)


# ==========================================================
# Challenge Exercises
# ==========================================================

# Challenge 1
# What is an instance variable?

# Challenge 2
# What is an instance method?

# Challenge 3
# Create a class Book with title and author.

# Challenge 4
# Add a method to display book details.

# Challenge 5
# Create two objects and modify one object's data.


# ==========================================================
# Git Commit Message
# ==========================================================

# git add .
# git commit -m "Add lecture 32 instance variables and methods examples"
