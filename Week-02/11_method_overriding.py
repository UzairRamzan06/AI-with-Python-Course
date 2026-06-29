# Course : Artificial Intelligence using Python
# Week   : 02
# File   : 11_method_overriding.py
# Lecture: 37
# Topic  : Method Overriding
#
# What to Practice:
#     ✔ Understand method overriding
#     ✔ Parent vs Child method behavior
#     ✔ Redefining methods in child class
#     ✔ Real-world usage of overriding
# ==========================================================

class Animal:
    def speak(self):
        print("Some sound")

class Dog(Animal):
    def speak(self):
        print("Woof! Woof!")

dog1 = Dog()

dog1.speak()
# OUTPUT : Woof! Woof!

# ----------------------------------------------------------
# What is Method Overriding?
# ----------------------------------------------------------
# Method Overriding means:
# ✔ A child class provides a new version of a method
#   that already exists in the parent class
#
# In simple words:
# 👉 Same method name, different behavior
# ----------------------------------------------------------


# ==========================================================
# Example 1: Basic Parent Class Method
# ==========================================================

class Animal:

    def sound(self):
        print("Animal makes a sound")


print("Example 1")

a = Animal()
a.sound()

# Output:
# Animal makes a sound


print("\n" + "=" * 50)


# ==========================================================
# Example 2: Overriding Method in Child Class
# ==========================================================

class Animal:

    def sound(self):
        print("Animal makes a sound")


class Dog(Animal):

    def sound(self):
        print("Dog barks")


print("Example 2")

dog = Dog()
dog.sound()

# Output:
# Dog barks


print("\n" + "=" * 50)


# ==========================================================
# Example 3: Multiple Child Classes Overriding Same Method
# ==========================================================

class Animal:

    def sound(self):
        print("Animal makes a sound")


class Dog(Animal):

    def sound(self):
        print("Dog barks")


class Cat(Animal):

    def sound(self):
        print("Cat meows")


print("Example 3")

dog = Dog()
cat = Cat()

dog.sound()
cat.sound()

# Output:
# Dog barks
# Cat meows


print("\n" + "=" * 50)


# ==========================================================
# Example 4: Real-Life Analogy
# ==========================================================
# Parent Class: Vehicle
#
# Child Classes:
#   Car → start() behaves differently
#   Bike → start() behaves differently
# ==========================================================

class Vehicle:

    def start(self):
        print("Vehicle is starting")


class Car(Vehicle):

    def start(self):
        print("Car is starting with key ignition")


class Bike(Vehicle):

    def start(self):
        print("Bike is starting with self start")


print("Example 4")

v1 = Vehicle()
c1 = Car()
b1 = Bike()

v1.start()
c1.start()
b1.start()

# Output:
# Vehicle is starting
# Car is starting with key ignition
# Bike is starting with self start


print("\n" + "=" * 50)


# ==========================================================
# Example 5: Overriding with Additional Behavior
# ==========================================================

class Person:

    def introduce(self):
        print("I am a person")


class Student(Person):

    def introduce(self):
        print("I am a student and I study Python")


print("Example 5")

p = Person()
s = Student()

p.introduce()
s.introduce()

# Output:
# I am a person
# I am a student and I study Python


print("\n" + "=" * 50)


# ==========================================================
# Example 6: Why Overriding is Important
# ==========================================================
# ✔ Same method name
# ✔ Different behavior based on object type
#
# This is very useful in:
# - AI systems
# - Frameworks
# - Game development
# - Real-world applications
# ==========================================================

print("Method Overriding allows different behavior in child classes.")


print("\n" + "=" * 50)


# ==========================================================
# Practice Examples
# ==========================================================

# Practice 1

class Animal:

    def move(self):
        print("Animal is moving")

class Fish(Animal):

    def move(self):
        print("Fish is swimming")

print("Practice 1")

f = Fish()
f.move()

print()


# Practice 2

class Employee:

    def work(self):
        print("Employee is working")

class Manager(Employee):

    def work(self):
        print("Manager is managing team")

print("Practice 2")

m = Manager()
m.work()

print()


# Practice 3

class Device:

    def start(self):
        print("Device is starting")

class Laptop(Device):

    def start(self):
        print("Laptop is starting with OS boot")

print("Practice 3")

l = Laptop()
l.start()


print("\n" + "=" * 50)


# ==========================================================
# Challenge Exercises
# ==========================================================

# Challenge 1
# What is method overriding?

# Challenge 2
# Why do we override methods?

# Challenge 3
# Create a class Shape with method draw().

# Challenge 4
# Override draw() in Circle and Rectangle classes.

# Challenge 5
# Explain real-world usage of overriding.


# ==========================================================
# Git Commit Message
# ==========================================================

# git add .
# git commit -m "Add lecture 37 method overriding examples in OOP"
