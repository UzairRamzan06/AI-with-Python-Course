# ==========================================================
# Course : Artificial Intelligence with Python
# Week   : 01
# File   : mini_project_calculator.py
#
# Mini Project : Simple Calculator
#
# Concepts Used:
#     ✔ Variables
#     ✔ Type Casting
#     ✔ Operators
#     ✔ Conditional Statements
#     ✔ Functions (basic)
#
# Description:
# This is a simple calculator program that performs:
# Addition, Subtraction, Multiplication, and Division.
# ==========================================================

print("===== SIMPLE CALCULATOR =====")


# ==========================================================
# Function to add two numbers
# ==========================================================
def add(a, b):
    return a + b


# ==========================================================
# Function to subtract two numbers
# ==========================================================
def subtract(a, b):
    return a - b


# ==========================================================
# Function to multiply two numbers
# ==========================================================
def multiply(a, b):
    return a * b


# ==========================================================
# Function to divide two numbers
# ==========================================================
def divide(a, b):
    return a / b


# ==========================================================
# User Input
# ==========================================================

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print("\nSelect Operation:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

choice = input("Enter choice (1/2/3/4): ")

print("\n===== RESULT =====")


# ==========================================================
# Conditional Logic (Decision Making)
# ==========================================================

if choice == "1":
    result = add(num1, num2)
    print("Addition =", result)

elif choice == "2":
    result = subtract(num1, num2)
    print("Subtraction =", result)

elif choice == "3":
    result = multiply(num1, num2)
    print("Multiplication =", result)

elif choice == "4":
    result = divide(num1, num2)
    print("Division =", result)

else:
    print("Invalid choice! Please select 1, 2, 3, or 4.")


# ==========================================================
# Extra Practice Version (Optional)
# ==========================================================

print("\n===== QUICK TEST CALCULATION =====")

a = 10
b = 5

print("Addition:", add(a, b))
print("Subtraction:", subtract(a, b))
print("Multiplication:", multiply(a, b))
print("Division:", divide(a, b))


print("\nEnd of Calculator Program")
