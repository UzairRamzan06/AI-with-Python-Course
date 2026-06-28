# Course : Artificial Intelligence with Python
# Week   : 01
# File   : 06_operators.py
# VDO Lectures Covered : 15
# Topic  : Python Operators - Arithmetic, Comparison, Logical & Assignment
# What to Practice:
#     ✔ Arithmetic Operators
#     ✔ Comparison Operators
#     ✔ Logical Operators
#     ✔ Assignment Operators

# ==========================================================

print("===== Python Operators =====")

# ----------------------------------------------------------

# Quick Revision Table
| Operator Type | Examples                            |
| ------------- | ----------------------------------- |
| Arithmetic    | `+`, `-`, `*`, `/`, `//`, `%`, `**` |
| Comparison    | `==`, `!=`, `>`, `<`, `>=`, `<=`    |
| Logical       | `and`, `or`, `not`                  |
| Assignment    | `=`, `+=`, `-=`, `*=`, `/=`         |




# ----------------------------------------------------------
# What are Operators?
# ----------------------------------------------------------
# Operators are special symbols used to perform operations
# on variables and values.
#
# Example:
# +  Addition
# -  Subtraction
# *  Multiplication
# /  Division

# ==========================================================
# Arithmetic Operators
# ==========================================================

print("\n===== Arithmetic Operators =====")

num1 = 20
num2 = 5

print("Number 1 =", num1)
print("Number 2 =", num2)

print("Addition:", num1 + num2)
print("Subtraction:", num1 - num2)
print("Multiplication:", num1 * num2)
print("Division:", num1 / num2)
print("Floor Division:", num1 // num2)
print("Modulus (Remainder):", num1 % num2)
print("Exponent (Power):", num1 ** num2)


# ==========================================================
# Another Arithmetic Example
# ==========================================================

print("\n===== Arithmetic Example 2 =====")

a = 10
b = 3

print("Addition:", a + b)
print("Division:", a / b)
print("Modulus:", a % b)


# ==========================================================
# Comparison Operators
# ==========================================================

print("\n===== Comparison Operators =====")

x = 15
y = 20

print("x =", x)
print("y =", y)

print("x == y :", x == y)
print("x != y :", x != y)
print("x > y  :", x > y)
print("x < y  :", x < y)
print("x >= y :", x >= y)
print("x <= y :", x <= y)


# ==========================================================
# Another Comparison Example
# ==========================================================

print("\n===== Comparison Example 2 =====")

age = 18

print("Age =", age)

print("Is age equal to 18?", age == 18)
print("Is age greater than 18?", age > 18)


# ==========================================================
# Logical Operators
# ==========================================================

print("\n===== Logical Operators =====")

age = 22
has_id_card = True

print("Age =", age)
print("Has ID Card =", has_id_card)

print("AND Operator:", age >= 18 and has_id_card)
print("OR Operator :", age >= 18 or has_id_card)
print("NOT Operator:", not has_id_card)


# ==========================================================
# Another Logical Example
# ==========================================================

print("\n===== Logical Example 2 =====")

is_student = True
has_fee_paid = False

print("Can Attend Exam:", is_student and has_fee_paid)
print("Student OR Fee Paid:", is_student or has_fee_paid)
print("Fee Status:", not has_fee_paid)


# ==========================================================
# Assignment Operators
# ==========================================================

print("\n===== Assignment Operators =====")

number = 10

print("Initial Value:", number)

number += 5
print("After += 5 :", number)

number -= 3
print("After -= 3 :", number)

number *= 2
print("After *= 2 :", number)

number /= 4
print("After /= 4 :", number)


# ==========================================================
# Another Assignment Example
# ==========================================================

print("\n===== Assignment Example 2 =====")

marks = 50

print("Initial Marks:", marks)

marks += 10
print("Updated Marks:", marks)


# ==========================================================
# Practice Examples
# ==========================================================

print("\n===== Practice Examples =====")

a = 8
b = 2

print("Addition:", a + b)
print("Multiplication:", a * b)

print("Is a greater than b?", a > b)

print("Logical AND:", True and False)

value = 100
value += 50

print("Updated Value:", value)


# ==========================================================
# Challenge Exercises
# ==========================================================

# Challenge 1
# Create two variables and perform all arithmetic operations.

# Challenge 2
# Compare two numbers using:
# ==
# !=
# >
# <
# >=
# <=

# Challenge 3
# Create two Boolean variables.
# Use AND, OR and NOT operators.

# Challenge 4
# Create a variable with value 25.
# Increase it by 10 using +=

# Challenge 5
# Create a variable with value 100.
# Divide it by 5 using /=


print("\nEnd of Python Operators Examples")
   
