# Course : Artificial Intelligence using Python
# Week   : 02
# File   : 13_special_methods.py
# Lecture: 39
# Topic  : Python Special Methods (Magic / Dunder Methods)
#
# What to Practice:
#     ✔ Understand special methods (__init__, __str__, etc.)
#     ✔ Make objects behave like built-in types
#     ✔ Improve readability of objects
# ==========================================================
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
    def __str__(self):
        return f"'{self.title}' by {self.author}"

b = Book("1984", "George Orwell")

print(b)
# OUTPUT : '1984' by George Orwell

----------------------------------------------------------

class Playlist:
    def __init__(self, songs):
        self.songs = songs
    def __len__(self):
        return len(self.songs)
    def __add__(self, other):
        return Playlist(self.songs + other.songs)

p1 = Playlist(["Song1", "Song2"])
p2 = Playlist(["Song3"])

print(len(p1)) #2
# OUTPUT : 2

print(len(p1 + p2)) #3
# OUTPUT : 3

----------------------------------------------------------

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __str__(self):
        return f"({self.x}, {self.y})"
    def __add__(self, other):
        if not isinstance(other, Point):
            return NotImplemented
        return Point(self.x + other.x, self.y + other.y)

p1 = Point(2, 3)
p2 = Point(4, 1)
print ( p1 + p2 )

# OUTPUT : (6, 4)

# ----------------------------------------------------------



# What are Special Methods?
# ----------------------------------------------------------
# Special methods are predefined methods in Python
# that start and end with double underscores (__).
#
# They are also called:
# ✔ Dunder methods (Double UNDERscore)
# ✔ Magic methods
#
# Examples:
#   __init__   → constructor
#   __str__    → string representation
#   __len__    → length of object
# ----------------------------------------------------------


# ==========================================================
# Example 1: __init__ Method (Constructor)
# ==========================================================

class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age


print("Example 1")

s = Student("Ali", 20)
print(s.name, s.age)

# Output:
# Ali 20


print("\n" + "=" * 50)


# ==========================================================
# Example 2: __str__ Method (Readable Output)
# ==========================================================

class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Student Name: {self.name}, Age: {self.age}"


print("Example 2")

s = Student("Sara", 22)

print(s)

# Output:
# Student Name: Sara, Age: 22


print("\n" + "=" * 50)


# ==========================================================
# Example 3: Without __str__ vs With __str__
# ==========================================================

class Book:

    def __init__(self, title):
        self.title = title


print("Example 3 - Without __str__")

b1 = Book("Python Basics")
print(b1)

# Output:
# <__main__.Book object at 0x...>


print("\nExample 3 - With __str__")


class Book:

    def __init__(self, title):
        self.title = title

    def __str__(self):
        return f"Book Title: {self.title}"


b2 = Book("Python Basics")
print(b2)

# Output:
# Book Title: Python Basics


print("\n" + "=" * 50)


# ==========================================================
# Example 4: __len__ Method
# ==========================================================

class Team:

    def __init__(self, members):
        self.members = members

    def __len__(self):
        return len(self.members)


print("Example 4")

team = Team(["Ali", "Sara", "Ahmed"])

print(len(team))

# Output:
# 3


print("\n" + "=" * 50)


# ==========================================================
# Example 5: Real-Life Usage
# ==========================================================

class Product:

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.name} costs {self.price} PKR"


print("Example 5")

p = Product("Laptop", 120000)

print(p)

# Output:
# Laptop costs 120000 PKR


print("\n" + "=" * 50)


# ==========================================================
# Example 6: Why Special Methods are Important
# ==========================================================
# ✔ Makes objects readable
# ✔ Makes objects behave like built-in types
# ✔ Used in professional Python libraries
#
# Example:
# print(), len(), str() all use special methods internally
# ==========================================================

print("Special methods make Python objects powerful and readable.")


print("\n" + "=" * 50)


# ==========================================================
# Practice Examples
# ==========================================================

# Practice 1

class Car:

    def __init__(self, brand):
        self.brand = brand

    def __str__(self):
        return f"Car Brand: {self.brand}"

print("Practice 1")

c = Car("Toyota")
print(c)

print()


# Practice 2

class Student:

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Student: {self.name}"

print("Practice 2")

s = Student("Ali")
print(s)

print()


# Practice 3

class Group:

    def __init__(self, members):
        self.members = members

    def __len__(self):
        return len(self.members)

print("Practice 3")

g = Group(["A", "B", "C", "D"])
print(len(g))


print("\n" + "=" * 50)


# ==========================================================
# Challenge Exercises
# ==========================================================

# Challenge 1
# What are special methods?

# Challenge 2
# What is __str__ used for?

# Challenge 3
# What is __len__ used for?

# Challenge 4
# Create a class Employee with readable output using __str__.

# Challenge 5
# Create a class Library and return number of books using __len__.


# ==========================================================
# Git Commit Message
# ==========================================================

# git add .
# git commit -m "Add lecture 39 special methods (dunder methods) examples"
