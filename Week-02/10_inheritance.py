# Course : Artificial Intelligence using Python
# Week   : 02
# File   : 10_inheritance.py
# Lecture: 36
# Topic  : Inheritance in Python - Parent & Child Classes
#
# What to Practice:
#     ✔ Understand inheritance concept
#     ✔ Parent (Base) class
#     ✔ Child (Derived) class
#     ✔ Code reuse
# ==========================================================
class Animal:
    def speak(self):
        print("Some sound")
      
class Dog(Animal):
    pass
  
dog1 = Dog()

dog1.speak()
#OUTPUT : Some sound

class Dog(Animal):
    def bark(self):
        print("Woof!")

childdog = Dog()
childdog.bark()
#OUTPUT : Woof!

childdog.speak()
#OUTPUT : Some sound
# ----------------------------------------------------------




# ----------------------------------------------------------
# What is Inheritance?
# ----------------------------------------------------------
# Inheritance means:
# ✔ One class can use properties and methods of another class
#
# Real meaning:
# 👉 Reuse existing code instead of writing again
#
# Parent Class → Base class
# Child Class  → Derived class
# ----------------------------------------------------------


# ==========================================================
# Example 1: Simple Parent Class
# ==========================================================

class Animal:

    def eat(self):
        print("Animal is eating")


print("Example 1")

a = Animal()
a.eat()

# Output:
# Animal is eating


print("\n" + "=" * 50)


# ==========================================================
# Example 2: Child Class Inheriting Parent Class
# ==========================================================

class Animal:

    def eat(self):
        print("Animal is eating")


class Dog(Animal):
    pass


print("Example 2")

dog = Dog()
dog.eat()

# Output:
# Animal is eating


print("\n" + "=" * 50)


# ==========================================================
# Example 3: Adding Child-Specific Method
# ==========================================================

class Animal:

    def eat(self):
        print("Animal is eating")


class Dog(Animal):

    def bark(self):
        print("Dog is barking")


print("Example 3")

dog = Dog()
dog.eat()
dog.bark()

# Output:
# Animal is eating
# Dog is barking


print("\n" + "=" * 50)


# ==========================================================
# Example 4: Parent + Child Attributes
# ==========================================================

class Animal:

    def __init__(self, name):
        self.name = name

    def eat(self):
        print(self.name, "is eating")


class Dog(Animal):

    def bark(self):
        print(self.name, "is barking")


print("Example 4")

dog = Dog("Tommy")

dog.eat()
dog.bark()

# Output:
# Tommy is eating
# Tommy is barking


print("\n" + "=" * 50)


# ==========================================================
# Example 5: Overriding Parent Method (Basic Idea)
# ==========================================================

class Animal:

    def sound(self):
        print("Animal makes a sound")


class Dog(Animal):

    def sound(self):
        print("Dog barks")


print("Example 5")

dog = Dog()
dog.sound()

# Output:
# Dog barks


print("\n" + "=" * 50)


# ==========================================================
# Example 6: Multiple Child Classes
# ==========================================================

class Animal:

    def eat(self):
        print("Animal is eating")


class Dog(Animal):
    def bark(self):
        print("Dog barks")


class Cat(Animal):
    def meow(self):
        print("Cat meows")


print("Example 6")

dog = Dog()
cat = Cat()

dog.eat()
dog.bark()

cat.eat()
cat.meow()

# Output:
# Animal is eating
# Dog barks
# Animal is eating
# Cat meows


print("\n" + "=" * 50)


# ==========================================================
# Real-Life Analogy
# ==========================================================
# Parent Class:
#   Vehicle
#
# Child Classes:
#   Car → inherits Vehicle
#   Bike → inherits Vehicle
#
# All vehicles share common features,
# but each has its own behavior.
# ==========================================================


class Vehicle:

    def start(self):
        print("Vehicle is starting")


class Car(Vehicle):
    def drive(self):
        print("Car is driving")


class Bike(Vehicle):
    def ride(self):
        print("Bike is riding")


print("Real-Life Example")

car = Car()
bike = Bike()

car.start()
car.drive()

bike.start()
bike.ride()


print("\n" + "=" * 50)


# ==========================================================
# Key Concepts Summary
# ==========================================================
# ✔ Parent class → Base class
# ✔ Child class → Inherits parent class
# ✔ Code reuse → No repetition
# ✔ Extensibility → Easy to add new features
# ==========================================================

print("Inheritance = Reusing code from parent class")


print("\n" + "=" * 50)


# ==========================================================
# Practice Examples
# ==========================================================

# Practice 1

class Person:

    def speak(self):
        print("Person is speaking")

class Student(Person):
    pass

print("Practice 1")
s = Student()
s.speak()

print()


# Practice 2

class Animal:

    def eat(self):
        print("Eating food")

class Cat(Animal):

    def meow(self):
        print("Meowing")

print("Practice 2")
c = Cat()
c.eat()
c.meow()

print()


# Practice 3

class Device:

    def power_on(self):
        print("Device is ON")

class Laptop(Device):

    def work(self):
        print("Laptop is working")

print("Practice 3")
l = Laptop()
l.power_on()
l.work()


print("\n" + "=" * 50)


# ==========================================================
# Challenge Exercises
# ==========================================================

# Challenge 1
# What is inheritance?

# Challenge 2
# What is a parent class?

# Challenge 3
# What is a child class?

# Challenge 4
# Create a class Vehicle and inherit it in Bike class.

# Challenge 5
# Add methods in both parent and child classes.


# ==========================================================
# Git Commit Message
# ==========================================================

# git add .
# git commit -m "Add lecture 36 inheritance with parent and child class examples"
