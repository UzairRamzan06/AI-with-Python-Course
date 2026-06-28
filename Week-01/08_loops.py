# Course : Artificial Intelligence with Python
# Week   : 01
# File   : 08_loops.py
# VDO Lectures Covered : 18 , 19 , 20 , 21 , 22 
# Topic  : FOR Loop , WHILE Loop , Nested Loops , Looping through Strings , Looping through Dictionaries.

          lecture vdo # 18 > FOR Loop in Python 
          lecture vdo # 19 > WHILE Loop in Python 
          lecture vdo # 20 > Nested Loops in Python 
          lecture vdo # 21 > Looping Over Data Structures - Strings 
          lecture vdo # 22 > Looping Over Data Structures - Dictionaries

# What to Practice:
#     ✔ for loop
#     ✔ while loop
#     ✔ Nested loops
#     ✔ Looping through Strings
#     ✔ Looping through Dictionaries

# ==========================================================
                    
# Quick Revision Table
                    
| Loop            | Purpose                                                     |
| --------------- | ----------------------------------------------------------- |
| `for`           | Repeat a fixed number of times or iterate over a collection |
| `while`         | Repeat while a condition remains true                       |
| Nested Loop     | A loop inside another loop                                  |
| String Loop     | Process one character at a time                             |
| Dictionary Loop | Access keys and values                                      |

# ==========================================================

print("===== Python Loops =====")

# ----------------------------------------------------------
# What are Loops?
# ----------------------------------------------------------
# Loops are used to repeat a block of code.
#
# Instead of writing the same statement many times,
# we can use loops.
# ----------------------------------------------------------


# ==========================================================
# Example 1 : for Loop
# ==========================================================

print("\n===== Example 1 : for Loop =====")

for number in range(1, 6):
    print(number)

# Output:
# 1
# 2
# 3
# 4
# 5


# ==========================================================
# Example 2 : for Loop with Step Value
# ==========================================================

print("\n===== Example 2 : for Loop with Step =====")

for number in range(2, 11, 2):
    print(number)

# Output:
# 2
# 4
# 6
# 8
# 10


# ==========================================================
# Example 3 : Print Student Names
# ==========================================================

print("\n===== Example 3 : Loop through a List =====")

students = ["Ali", "Ahmed", "Sara", "Fatima"]

for student in students:
    print(student)


# ==========================================================
# Example 4 : while Loop
# ==========================================================

print("\n===== Example 4 : while Loop =====")

count = 1

while count <= 5:
    print(count)
    count = count + 1

# Output:
# 1
# 2
# 3
# 4
# 5


# ==========================================================
# Example 5 : Countdown using while Loop
# ==========================================================

print("\n===== Example 5 : Countdown =====")

number = 5

while number >= 1:
    print(number)
    number = number - 1

print("Time's Up!")


# ==========================================================
# Example 6 : Nested Loops
# ==========================================================

print("\n===== Example 6 : Nested Loops =====")

for i in range(1, 4):
    for j in range(1, 4):
        print("i =", i, "j =", j)

# Output:
# i = 1 j = 1
# i = 1 j = 2
# ...
# i = 3 j = 3


# ==========================================================
# Example 7 : Loop through a String
# ==========================================================

print("\n===== Example 7 : Loop through a String =====")

name = "Python"

for letter in name:
    print(letter)

# Output:
# P
# y
# t
# h
# o
# n


# ==========================================================
# Example 8 : Count Characters in a String
# ==========================================================

print("\n===== Example 8 : Count Characters =====")

word = "AI"

count = 0

for letter in word:
    count = count + 1

print("Total Characters:", count)


# ==========================================================
# Example 9 : Loop through a Dictionary
# ==========================================================

print("\n===== Example 9 : Dictionary Keys =====")

student = {
    "Name": "Ali",
    "Age": 20,
    "City": "Lahore"
}

for key in student:
    print(key)

# Output:
# Name
# Age
# City


# ==========================================================
# Example 10 : Dictionary Keys and Values
# ==========================================================

print("\n===== Example 10 : Dictionary Items =====")

student = {
    "Name": "Ali",
    "Age": 20,
    "City": "Lahore"
}

for key, value in student.items():
    print(key, ":", value)

# Output:
# Name : Ali
# Age : 20
# City : Lahore


# ==========================================================
# Practice Examples
# ==========================================================

print("\n===== Practice Examples =====")

# Practice 1
print("\nNumbers from 1 to 3")

for number in range(1, 4):
    print(number)


# Practice 2
print("\nPrint Your Name 3 Times")

count = 1

while count <= 3:
    print("Ali Zafar")
    count = count + 1


# Practice 3
print("\nLoop through a String")

city = "Karachi"

for letter in city:
    print(letter)


# Practice 4
print("\nLoop through a Dictionary")

car = {
    "Brand": "Toyota",
    "Model": "Corolla",
    "Year": 2024
}

for key, value in car.items():
    print(key, ":", value)


# ==========================================================
# Challenge Exercises
# ==========================================================

# Challenge 1
# Print numbers from 1 to 20 using a for loop.

# Challenge 2
# Print numbers from 10 to 1 using a while loop.

# Challenge 3
# Print each letter of your name using a loop.

# Challenge 4
# Create a dictionary with your information.
# Print all keys and values.

# Challenge 5
# Use nested loops to print:
#
# *
# **
# ***
# ****


print("\nEnd of Python Loops Examples")
