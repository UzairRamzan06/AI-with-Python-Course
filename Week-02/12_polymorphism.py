# Course : Artificial Intelligence using Python
# Week   : 02
# File   : 12_polymorphism.py
# Lecture: 38
# Topic  : Polymorphism in Python
#
# What to Practice:
#     ✔ Understand polymorphism concept
#     ✔ Method overriding as polymorphism
#     ✔ Same method, different behavior
#     ✔ Real-world flexible design
# ==========================================================

class Dog:
    def speak(self):
        print("Woof!")
class Cat:
    def speak(self):
        print("Meow!")
for pet in [Dog(), Cat()]:
    pet.speak()
  
# OUTPUT : Woof!
# OUTPUT :Meow!

# ----------------------------------------------------------

class Vehicle:
    def move(self):
        print("Vehicle is moving")

class Car(Vehicle):
    def move(self):
        print("Car is driving")
      
car1 = Car()
car1.move()

# OUTPUT : Car is driving

# ----------------------------------------------------------

class Calculator:
    def add(self, a, b=0, c=0):
        return a + b + c 
      
calc1 = Calculator()
print(calc1.add(5))
print(calc1.add(5, 10))
print(calc1.add(5, 10, 15))

# OUTPUT : 5
# OUTPUT : 15
# OUTPUT : 30

# ----------------------------------------------------------
# What is Polymorphism?
# ----------------------------------------------------------
# Polymorphism means:
# ✔ "One name, many forms"
#
# In OOP:
# 👉 Same method name behaves differently in different classes
#
# This is achieved using:
# ✔ Method Overriding
# ✔ Inheritance
# ----------------------------------------------------------


# ==========================================================
# Example 1: Basic Polymorphism with Different Classes
# ==========================================================

class Dog:

    def sound(self):
        print("Dog barks")


class Cat:

    def sound(self):
        print("Cat meows")


print("Example 1")

d = Dog()
c = Cat()

d.sound()
c.sound()

# Output:
# Dog barks
# Cat meows


print("\n" + "=" * 50)


# ==========================================================
# Example 2: Same Function, Different Objects
# ==========================================================

class Bird:

    def fly(self):
        print("Bird is flying")


class Airplane:

    def fly(self):
        print("Airplane is flying in the sky")


print("Example 2")

b = Bird()
a = Airplane()

b.fly()
a.fly()

# Output:
# Bird is flying
# Airplane is flying in the sky


print("\n" + "=" * 50)


# ==========================================================
# Example 3: Polymorphism with Inheritance
# ==========================================================

class Animal:

    def speak(self):
        print("Animal makes sound")


class Dog(Animal):

    def speak(self):
        print("Dog barks")


class Cat(Animal):

    def speak(self):
        print("Cat meows")


print("Example 3")

animals = [Dog(), Cat(), Animal()]

for a in animals:
    a.speak()

# Output:
# Dog barks
# Cat meows
# Animal makes sound


print("\n" + "=" * 50)


# ==========================================================
# Example 4: Real-Life Polymorphism
# ==========================================================

class Payment:

    def pay(self):
        print("Processing payment")


class CreditCard:

    def pay(self):
        print("Payment done using Credit Card")


class PayPal:

    def pay(self):
        print("Payment done using PayPal")


print("Example 4")

methods = [CreditCard(), PayPal(), Payment()]

for m in methods:
    m.pay()

# Output:
# Payment done using Credit Card
# Payment done using PayPal
# Processing payment


print("\n" + "=" * 50)


# ==========================================================
# Example 5: Why Polymorphism is Important
# ==========================================================
# ✔ Same interface (method name)
# ✔ Different implementations
# ✔ Easy to extend system
#
# Used in:
# - AI models
# - Web frameworks
# - Payment systems
# - Game development
# ==========================================================

print("Polymorphism = Same method, different behavior")


print("\n" + "=" * 50)


# ==========================================================
# Practice Examples
# ==========================================================

# Practice 1

class Lion:

    def sound(self):
        print("Lion roars")

class Tiger:

    def sound(self):
        print("Tiger growls")

print("Practice 1")

l = Lion()
t = Tiger()

l.sound()
t.sound()

print()


# Practice 2

class Car:

    def move(self):
        print("Car is moving")

class Bike:

    def move(self):
        print("Bike is moving")

print("Practice 2")

c = Car()
b = Bike()

c.move()
b.move()

print()


# Practice 3

class Laptop:

    def start(self):
        print("Laptop is starting")

class Desktop:

    def start(self):
        print("Desktop is starting")

print("Practice 3")

l = Laptop()
d = Desktop()

l.start()
d.start()


print("\n" + "=" * 50)


# ==========================================================
# Challenge Exercises
# ==========================================================

# Challenge 1
# What is polymorphism?

# Challenge 2
# How is polymorphism different from inheritance?

# Challenge 3
# Create Shape class with draw() method.

# Challenge 4
# Override draw() in Circle and Square classes.

# Challenge 5
# Give real-life examples of polymorphism.


# ==========================================================
# Git Commit Message
# ==========================================================

# git add .
# git commit -m "Add lecture 38 polymorphism examples in Python"
