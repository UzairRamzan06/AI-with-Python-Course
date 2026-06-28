# Course : Artificial Intelligence with Python
# Week   : 01
# File   : 07_conditionals.py
# VDO Lectures Covered : 16 & 17
# Topic  : Conditional Statement - Part I  & Conditional Statement - Part II > Conditional Statements (if, elif, else) 
# What to Practice:
#     ✔ if statement
#     ✔ if...else statement
#     ✔ if...elif...else statement
#     ✔ Grade Calculator
#     ✔ Even / Odd Number
#     ✔ Positive / Negative Number


# Also
    Grade calculator
    Even/Odd
    Positive/Negative
# ===========================================

age = 18
if age >= 18:
    print("Eligible")
else:
    print("Not Eligible")
# ==========================================================

# Quick Revision Table

| Statement | Purpose                                              |
| --------- | ---------------------------------------------------- |
| `if`      | Execute code when a condition is true                |
| `else`    | Execute code when the condition is false             |
| `elif`    | Check another condition if the previous one is false |


# ==========================================================

print("===== Python Conditional Statements =====")

# ----------------------------------------------------------
# What are Conditional Statements?
# ----------------------------------------------------------
# Conditional statements help a program make decisions.
#
# Python checks whether a condition is True or False.
#
# If the condition is True, one block of code runs.
# Otherwise, another block of code runs.
# ----------------------------------------------------------


# ==========================================================
# Example 1 : Simple if Statement
# ==========================================================

print("\n===== Example 1 : if Statement =====")

age = 20

if age >= 18:
    print("You are eligible to vote.")

# Output:
# You are eligible to vote.


# ==========================================================
# Example 2 : if...else Statement
# ==========================================================

print("\n===== Example 2 : if...else Statement =====")

age = 16

if age >= 18:
    print("Eligible to vote.")
else:
    print("Not eligible to vote.")

# Output:
# Not eligible to vote.


# ==========================================================
# Example 3 : Check Even or Odd
# ==========================================================

print("\n===== Example 3 : Even or Odd =====")

number = 8

if number % 2 == 0:
    print(number, "is an Even Number.")
else:
    print(number, "is an Odd Number.")

# Output:
# 8 is an Even Number.


# ==========================================================
# Example 4 : Check Positive or Negative
# ==========================================================

print("\n===== Example 4 : Positive or Negative =====")

number = -15

if number >= 0:
    print(number, "is Positive.")
else:
    print(number, "is Negative.")

# Output:
# -15 is Negative.


# ==========================================================
# Example 5 : if...elif...else Statement
# ==========================================================

print("\n===== Example 5 : if...elif...else =====")

marks = 75

if marks >= 80:
    print("Grade A")
elif marks >= 60:
    print("Grade B")
else:
    print("Grade C")

# Output:
# Grade B


# ==========================================================
# Example 6 : Grade Calculator
# ==========================================================

print("\n===== Example 6 : Grade Calculator =====")

marks = 92

if marks >= 90:
    print("Grade A+")
elif marks >= 80:
    print("Grade A")
elif marks >= 70:
    print("Grade B")
elif marks >= 60:
    print("Grade C")
else:
    print("Fail")

# Output:
# Grade A+


# ==========================================================
# Example 7 : Check Pass or Fail
# ==========================================================

print("\n===== Example 7 : Pass or Fail =====")

marks = 45

if marks >= 50:
    print("Pass")
else:
    print("Fail")

# Output:
# Fail


# ==========================================================
# Example 8 : Compare Two Numbers
# ==========================================================

print("\n===== Example 8 : Compare Two Numbers =====")

num1 = 30
num2 = 20

if num1 > num2:
    print(num1, "is greater than", num2)
else:
    print(num2, "is greater than", num1)

# Output:
# 30 is greater than 20


# ==========================================================
# Practice Examples
# ==========================================================

print("\n===== Practice Examples =====")

# Practice 1
temperature = 35

if temperature > 30:
    print("Weather is Hot")
else:
    print("Weather is Cool")


# Practice 2
salary = 50000

if salary >= 50000:
    print("Good Salary")
else:
    print("Needs Improvement")


# Practice 3
is_logged_in = True

if is_logged_in:
    print("Welcome User")
else:
    print("Please Login")


# ==========================================================
# Challenge Exercises
# ==========================================================

# Challenge 1
# Create a variable age.
# Check whether the person can apply for a driving license.

# Challenge 2
# Create a variable number.
# Check whether it is Even or Odd.

# Challenge 3
# Create a variable number.
# Check whether it is Positive or Negative.

# Challenge 4
# Create a Grade Calculator using marks.

# Challenge 5
# Compare two numbers and print the greater number.


print("\nEnd of Conditional Statement Examples")
