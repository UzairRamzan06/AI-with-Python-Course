# 📘 Object-Oriented Programming (OOP) in Python

> **Course:** Artificial Intelligence using Python
> **Week:** 02
> **Section:** Object-Oriented Programming (OOP)
> **Related Lectures:** 28–39

---

# 📖 Introduction

Object-Oriented Programming (OOP) is a programming paradigm that organizes code into **classes** and **objects**.

Instead of writing programs as a collection of separate functions, OOP groups **data (attributes)** and **behavior (methods)** into a single unit called an **object**.

Python supports Object-Oriented Programming and uses it extensively in real-world applications, including Artificial Intelligence, Machine Learning, Data Science, Web Development, and Automation.

---

# 🎯 Learning Objectives

After studying these lectures, you should be able to:

* Explain the need for Object-Oriented Programming.
* Understand classes, objects, methods, and attributes.
* Create classes and objects.
* Use constructors (`__init__()`).
* Work with instance variables and instance methods.
* Access object attributes and methods.
* Understand encapsulation.
* Use public and private attributes.
* Implement getters and setters.
* Apply inheritance.
* Override methods.
* Understand polymorphism.
* Recognize common Python special methods.

---

# 📚 Lecture Roadmap

| Lecture | Topic                                 |
| ------: | ------------------------------------- |
|      28 | Understanding the Need for OOP        |
|      29 | Core OOP Concepts                     |
|      30 | Defining a Class & Creating Objects   |
|      31 | The `__init__()` Constructor Method   |
|      32 | Instance Variables & Instance Methods |
|      33 | Accessing Object Attributes & Methods |
|      34 | Encapsulation                         |
|      35 | Getters & Setters                     |
|      36 | Inheritance                           |
|      37 | Method Overriding                     |
|      38 | Polymorphism                          |
|      39 | Python Special Methods                |

---

# 1. Why Do We Need OOP?

As programs grow larger, managing code becomes more difficult.

Object-Oriented Programming helps by:

* Organizing code into logical units.
* Improving readability.
* Encouraging code reuse.
* Simplifying maintenance.
* Making programs easier to expand.

Without OOP, large programs become difficult to understand and modify.

---

# 2. What is a Class?

A **class** is a blueprint or template used to create objects.

It defines:

* Attributes (data)
* Methods (functions)

Example:

```python
class Student:
    pass
```

The class itself does not represent an actual student. It only describes what a student object should look like.

---

# 3. What is an Object?

An **object** is an instance of a class.

It contains its own data while sharing the structure defined by the class.

Example:

```python
student1 = Student()
student2 = Student()
```

Each object is created independently from the same class.

---

# 4. Attributes

Attributes store information about an object.

Examples:

* Name
* Age
* Roll Number
* Department

Each object can have different attribute values.

---

# 5. Methods

Methods define the actions an object can perform.

Examples:

* Display information
* Calculate marks
* Print details

Methods operate on an object's data.

---

# 6. Constructor (`__init__()`)

The constructor is a special method that runs automatically when an object is created.

Purpose:

* Initialize object data.
* Assign initial values.
* Reduce repetitive code.

Example:

```python
class Student:
    def __init__(self, name):
        self.name = name
```

The constructor is called automatically when an object is created.

---

# 7. The `self` Keyword

`self` represents the current object.

It allows methods to access an object's attributes and other methods.

Example:

```python
self.name
```

Every instance method includes `self` as its first parameter.

---

# 8. Instance Variables

Instance variables belong to individual objects.

Each object maintains its own copy.

Example:

```python
self.name
self.age
```

Different objects can store different values.

---

# 9. Instance Methods

Instance methods perform operations using an object's data.

Example:

```python
def display(self):
    print(self.name)
```

They can access both instance variables and other methods.

---

# 10. Accessing Attributes and Methods

Attributes are accessed using dot (`.`) notation.

Example:

```python
student.name
```

Methods are also called using dot notation.

Example:

```python
student.display()
```

---

# 11. Encapsulation

Encapsulation means combining data and methods into a single class while controlling access to the internal data.

Benefits:

* Protects object data.
* Improves security.
* Prevents accidental modification.
* Makes code easier to maintain.

---

# 12. Public Attributes

Public attributes can be accessed from anywhere.

Example:

```python
student.name
```

They have no special prefix.

---

# 13. Private Attributes

Private attributes begin with two underscores.

Example:

```python
self.__salary
```

Private attributes should not be accessed directly outside the class.

They provide a basic level of data protection.

---

# 14. Getters and Setters

Getters retrieve private data.

Setters update private data in a controlled way.

Benefits:

* Validate input.
* Protect object data.
* Control how values are modified.

---

# 15. Inheritance

Inheritance allows one class to reuse the properties and methods of another class.

Terminology:

* Parent Class (Base Class)
* Child Class (Derived Class)

Benefits:

* Code reuse.
* Easier maintenance.
* Reduced duplication.
* Better organization.

---

# 16. Parent Class

The parent class contains common functionality.

Example:

A generic `Person` class.

---

# 17. Child Class

A child class inherits features from the parent class and may add new functionality.

Example:

A `Student` class inheriting from `Person`.

---

# 18. Method Overriding

Method overriding occurs when a child class provides its own implementation of a method already defined in the parent class.

Purpose:

* Customize inherited behavior.
* Extend existing functionality.
* Implement specialized behavior.

---

# 19. Polymorphism

Polymorphism means **one interface, many implementations**.

The same method name can behave differently depending on the object.

Benefits:

* Flexible code.
* Cleaner design.
* Easier maintenance.

---

# 20. Method Overloading in Python

Unlike some programming languages, Python does not support traditional method overloading based solely on different parameter lists.

Similar behavior can be achieved using:

* Default parameter values
* Variable-length arguments (`*args`, `**kwargs`)

This topic becomes more useful as you progress to advanced Python.

---

# 21. Python Special Methods

Special methods begin and end with double underscores.

Examples:

| Method       | Purpose                  |
| ------------ | ------------------------ |
| `__init__()` | Constructor              |
| `__str__()`  | String representation    |
| `__len__()`  | Object length            |
| `__repr__()` | Developer representation |

These methods allow Python objects to interact naturally with built-in functions and operators.

---

# 📌 OOP Principles

The four fundamental principles of Object-Oriented Programming are:

1. Encapsulation
2. Inheritance
3. Polymorphism
4. Abstraction

> **Note:** Abstraction is an important OOP concept, but it is **not covered in Week 02** of this course. It is included here for general awareness.

---

# 🌍 Real-World Examples of OOP

| Real-World Object | Class       | Attributes              | Methods           |
| ----------------- | ----------- | ----------------------- | ----------------- |
| Car               | Car         | Brand, Model, Color     | Start, Stop       |
| Student           | Student     | Name, Roll Number       | Study, Display    |
| Bank Account      | BankAccount | Balance, Account Number | Deposit, Withdraw |
| Employee          | Employee    | Name, Salary            | Work, Display     |
| Mobile Phone      | Mobile      | Brand, Storage          | Call, Charge      |

---

# ✅ Advantages of OOP

* Better code organization
* Reusable code
* Easier debugging
* Improved maintainability
* Supports large projects
* Simplifies teamwork
* Reduces code duplication
* Makes applications scalable

---

# ❌ Common Beginner Mistakes

* Confusing a class with an object.
* Forgetting to use `self` in instance methods.
* Trying to access private attributes directly.
* Forgetting to create an object before calling a method.
* Assuming Python supports traditional method overloading.
* Misspelling `__init__()` (for example, using `_init_` instead of `__init__`).

---

# 📝 Quick Revision

| Concept           | Description                               |
| ----------------- | ----------------------------------------- |
| Class             | Blueprint for objects                     |
| Object            | Instance of a class                       |
| Attribute         | Data stored in an object                  |
| Method            | Function inside a class                   |
| `self`            | Reference to the current object           |
| Constructor       | Initializes an object                     |
| Instance Variable | Data unique to each object                |
| Instance Method   | Operates on object data                   |
| Encapsulation     | Protects and organizes data               |
| Getter            | Retrieves private data                    |
| Setter            | Updates private data                      |
| Inheritance       | Reuses code from another class            |
| Method Overriding | Redefines inherited behavior              |
| Polymorphism      | Same interface, different behavior        |
| Special Method    | Built-in method with a predefined purpose |

---

# 🎤 Interview Questions

### What is Object-Oriented Programming?

Object-Oriented Programming is a programming paradigm that organizes code into classes and objects, combining data and behavior into reusable units.

---

### What is the difference between a class and an object?

A class is a blueprint, while an object is an instance created from that blueprint.

---

### What is the purpose of the `__init__()` method?

It initializes an object and assigns initial values to its attributes when the object is created.

---

### What is encapsulation?

Encapsulation combines data and methods into a single class while controlling access to internal data.

---

### What is inheritance?

Inheritance allows a child class to reuse the properties and methods of a parent class.

---

### What is method overriding?

Method overriding occurs when a child class provides a new implementation of a method inherited from the parent class.

---

### What is polymorphism?

Polymorphism allows the same method or interface to behave differently depending on the object using it.

---

### What are Python special methods?

Special methods are predefined methods (such as `__init__()` and `__str__()`) that allow objects to integrate with Python's built-in behavior.

---

# 📚 Summary

Object-Oriented Programming is one of the most important concepts in Python. It enables developers to design modular, reusable, and maintainable software by organizing data and behavior into classes and objects. In Week 02, you learned how to create classes, initialize objects, use instance variables and methods, apply encapsulation, implement inheritance, override methods, understand polymorphism, and recognize commonly used Python special methods. These concepts provide the foundation for building larger Python applications and will be used extensively throughout the remaining Artificial Intelligence using Python course.
