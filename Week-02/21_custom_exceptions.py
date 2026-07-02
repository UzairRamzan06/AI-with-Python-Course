# Course : Artificial Intelligence using Python
# Week   : 02
# File   : 21_custom_exceptions.py
# Lecture: 47
# Topic  : Creating Custom Exceptions in Python
#
# What to Practice:
#     ✔ Create user-defined exceptions
#     ✔ Extend Exception class
#     ✔ Use custom error messages
#     ✔ Apply in real-world validation systems
# ==========================================================

class InvalidAgeError(Exception):
    pass
age = int(input("Enter age: "))
if age < 0:
    raise InvalidAgeError(f"Age cannot be negative! , {age}")
    
# If Enter age negative :  -3
# Then Python Show following error
# OUTPUT : 
"""---------------------------------------------------------------------------
InvalidAgeError                           Traceback (most recent call last)
Cell In[2], line 3
      1 age = int(input("Enter age: "))
      2 if age < 0:
----> 3     raise InvalidAgeError(f"Age cannot be negative! , {age}")

InvalidAgeError: Age cannot be negative! , -3

"""
# ----------------------------------------------------------

try:
    age = int(input("Enter age: "))
    if age < 0:
        raise InvalidAgeError(f"Age cannot be negative! , {age}")
except InvalidAgeError as e:
    print(e)
    
# If Enter age negative :  -7
# Then Python Show following error
# OUTPUT :  Age cannot be negative! , -7

# ----------------------------------------------------------



# What is a Custom Exception?
# ----------------------------------------------------------
# A custom exception is:
# ✔ A user-defined error class
#
# Why do we need it?
# ✔ To make errors more meaningful
# ✔ To handle specific business rules
# ✔ To improve code readability
# ----------------------------------------------------------


# ==========================================================
# Example 1: Simple Custom Exception
# ==========================================================

print("Example 1 - Basic custom exception")

class MyError(Exception):
    pass


try:
    raise MyError("This is a custom error")

except MyError as e:
    print("Caught error:", e)

# Output:
# Caught error: This is a custom error


print("\n" + "=" * 50)


# ==========================================================
# Example 2: Custom Exception for Age Validation
# ==========================================================

print("Example 2 - Age validation")

class AgeError(Exception):
    pass


def check_age(age):
    if age < 18:
        raise AgeError("Age must be 18 or above")
    return "Access granted"


try:
    print(check_age(15))

except AgeError as e:
    print("Error:", e)

# Output:
# Error: Age must be 18 or above


print("\n" + "=" * 50)


# ==========================================================
# Example 3: Custom Exception for Password Validation
# ==========================================================

print("Example 3 - Password validation")

class PasswordError(Exception):
    pass


def check_password(password):

    if len(password) < 6:
        raise PasswordError("Password too short")

    if password.isdigit():
        raise PasswordError("Password cannot be only numbers")

    return "Password is valid"


try:
    print(check_password("12345"))

except PasswordError as e:
    print("Validation Error:", e)

# Output:
# Validation Error: Password too short


print("\n" + "=" * 50)


# ==========================================================
# Example 4: Real-World System Simulation
# ==========================================================

print("Example 4 - Banking system example")

class InsufficientBalanceError(Exception):
    pass


class BankAccount:

    def __init__(self, balance):
        self.balance = balance

    def withdraw(self, amount):

        if amount > self.balance:
            raise InsufficientBalanceError("Not enough balance")

        self.balance -= amount
        return f"Withdraw successful. Remaining balance: {self.balance}"


account = BankAccount(1000)

try:
    print(account.withdraw(1500))

except InsufficientBalanceError as e:
    print("Transaction Failed:", e)

# Output:
# Transaction Failed: Not enough balance


print("\n" + "=" * 50)


# ==========================================================
# Example 5: Why Custom Exceptions are Important
# ==========================================================
# ✔ Makes code readable
# ✔ Improves debugging
# ✔ Represents real business rules
# ✔ Used in professional systems
# ==========================================================

print("Custom exceptions improve professional code structure")


print("\n" + "=" * 50)


# ==========================================================
# Practice Examples
# ==========================================================

# Practice 1

print("Practice 1")

class LoginError(Exception):
    pass

try:
    raise LoginError("Invalid login attempt")

except LoginError as e:
    print(e)

print()


# Practice 2

print("Practice 2")

class ScoreError(Exception):
    pass

def check_score(score):
    if score > 100:
        raise ScoreError("Score cannot exceed 100")
    return "Valid score"

try:
    print(check_score(120))

except ScoreError as e:
    print("Error:", e)

print()


# Practice 3

print("Practice 3")

class NameErrorCustom(Exception):
    pass

def check_name(name):
    if len(name) < 3:
        raise NameErrorCustom("Name too short")
    return "Valid name"

try:
    print(check_name("Al"))

except NameErrorCustom as e:
    print("Error:", e)


print("\n" + "=" * 50)


# ==========================================================
# Challenge Exercises
# ==========================================================

# Challenge 1
# What is a custom exception?

# Challenge 2
# Why do we create custom exceptions?

# Challenge 3
# Create a custom exception for email validation.

# Challenge 4
# Create a custom exception for negative numbers.

# Challenge 5
# Build a mini system using custom exceptions.


# ==========================================================
# Git Commit Message
# ==========================================================

# git add .
# git commit -m "Add lecture 47 custom exceptions with real-world examples"
