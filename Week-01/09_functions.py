# Course : Artificial Intelligence with Python
# Week   : 01
# File   : 09_functions.py
# VDO Lectures Covered : 23 , 24 , 25 , 26
# Topic  : Functions ,  Parameters , Return Values , Variable Scope , Lambda Functions
 
  #        lecture vdo # 23 > Defining & Calling Functions 
  #        lecture vdo # 24 > Function Parameters & Return Values
  #        lecture vdo # 25 > Variable Scope in Python - Local vs Global 
  #        lecture vdo # 26 > Lambda Functions in Python 

# What to Practice:
#     ✔ Defining Functions
#     ✔ Calling Functions
#     ✔ Parameters
#     ✔ Return Values
#     ✔ Local Variables
#     ✔ Global Variables
#     ✔ Lambda Functions

# ==========================================================

# Quick Revision Table

| Concept         | Purpose                                          |
| --------------- | ------------------------------------------------ |
| `def`           | Define a function                                |
| Function Call   | Execute the function                             |
| Parameter       | Receive input                                    |
| `return`        | Send a value back                                |
| Local Variable  | Used only inside a function                      |
| Global Variable | Accessible inside functions when defined outside |
| `lambda`        | Create a short anonymous function                |

# ==========================================================

print("===== Python Functions =====")

# ----------------------------------------------------------
# What is a Function?
# ----------------------------------------------------------
# A function is a block of code that performs a specific task.
#
# Instead of writing the same code again and again,
# we can write it once inside a function and call it whenever needed.
# ----------------------------------------------------------


# ==========================================================
# Example 1 : Defining and Calling a Function
# ==========================================================

print("\n===== Example 1 : Defining a Function =====")

def greet():
    print("Welcome to Python Programming!")

greet()

# Output:
# Welcome to Python Programming!


# ==========================================================
# Example 2 : Function Called Multiple Times
# ==========================================================

print("\n===== Example 2 : Calling Function Multiple Times =====")

def say_hello():
    print("Hello!")

say_hello()
say_hello()
say_hello()

# Output:
# Hello!
# Hello!
# Hello!


# ==========================================================
# Example 3 : Function with One Parameter
# ==========================================================

print("\n===== Example 3 : Function with Parameter =====")

def greet_student(name):
    print("Welcome", name)

greet_student("Ali")
greet_student("Sara")

# Output:
# Welcome Ali
# Welcome Sara


# ==========================================================
# Example 4 : Function with Two Parameters
# ==========================================================

print("\n===== Example 4 : Two Parameters =====")

def add_numbers(num1, num2):
    print("Sum =", num1 + num2)

add_numbers(10, 20)
add_numbers(5, 15)

# Output:
# Sum = 30
# Sum = 20


# ==========================================================
# Example 5 : Function with Return Value
# ==========================================================

print("\n===== Example 5 : Return Value =====")

def square(number):
    return number * number

result = square(5)

print("Square =", result)

# Output:
# Square = 25


# ==========================================================
# Example 6 : Return Addition
# ==========================================================

print("\n===== Example 6 : Return Addition =====")

def add(a, b):
    return a + b

total = add(12, 8)

print("Total =", total)

# Output:
# Total = 20


# ==========================================================
# Example 7 : Local Variable
# ==========================================================

print("\n===== Example 7 : Local Variable =====")

def student():
    name = "Ali"
    print(name)

student()

# The variable 'name' exists only inside the function.


# ==========================================================
# Example 8 : Global Variable
# ==========================================================

print("\n===== Example 8 : Global Variable =====")

city = "Lahore"

def show_city():
    print(city)

show_city()

# The variable 'city' is created outside the function,
# so it can be used inside the function.


# ==========================================================
# Example 9 : Lambda Function
# ==========================================================

print("\n===== Example 9 : Lambda Function =====")

square = lambda number: number * number

print(square(6))

# Output:
# 36


# ==========================================================
# Example 10 : Lambda with Two Numbers
# ==========================================================

print("\n===== Example 10 : Lambda Addition =====")

add = lambda a, b: a + b

print(add(10, 15))

# Output:
# 25


# ==========================================================
# Practice Examples
# ==========================================================

print("\n===== Practice Examples =====")

# Practice 1
def show_name():
    print("Ali Zafar")

show_name()


# Practice 2
def multiply(a, b):
    print("Multiplication =", a * b)

multiply(4, 5)


# Practice 3
def find_cube(number):
    return number ** 3

print("Cube =", find_cube(3))


# Practice 4
country = "Pakistan"

def show_country():
    print(country)

show_country()


# Practice 5
double = lambda number: number * 2

print("Double =", double(8))


# ==========================================================
# Challenge Exercises
# ==========================================================

# Challenge 1
# Create a function that prints your favorite subject.

# Challenge 2
# Create a function that takes your name as a parameter
# and prints a welcome message.

# Challenge 3
# Create a function that returns the multiplication
# of two numbers.

# Challenge 4
# Create a global variable called university.
# Print it inside a function.

# Challenge 5
# Create a lambda function that finds the square
# of a number.


print("\nEnd of Python Functions Examples")
