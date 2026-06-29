# 📘 Exception Handling in Python

> **Course:** Artificial Intelligence using Python
> **Week:** 02
> **Section:** Exception Handling
> **Related Lectures:** 44–47

---

# 📖 Introduction

Exception handling is a mechanism in Python that allows a program to detect and handle runtime errors without crashing.

When an error occurs during program execution, Python raises an **exception**. Instead of terminating the program immediately, exception handling provides a structured way to respond to the error and continue execution when appropriate.

Exception handling is an essential skill for developing reliable, user-friendly, and maintainable Python applications.

---

# 🎯 Learning Objectives

After completing these lectures, you should be able to:

* Understand what exceptions are.
* Differentiate between syntax errors and exceptions.
* Handle exceptions using `try` and `except`.
* Use `else` and `finally` blocks effectively.
* Raise exceptions using the `raise` keyword.
* Create custom exceptions.
* Write more reliable and robust Python programs.

---

# 📚 Lecture Roadmap

| Lecture | Topic                                     |
| ------: | ----------------------------------------- |
|      44 | Introduction to Exceptions in Python      |
|      45 | Using `try`, `except`, `else` & `finally` |
|      46 | Raising Exceptions in Python              |
|      47 | Creating Custom Exceptions in Python      |

---

# 🤔 What is an Exception?

An **exception** is an event that interrupts the normal flow of a program during execution.

Examples include:

* Dividing by zero
* Opening a file that does not exist
* Accessing an invalid list index
* Converting invalid data types
* Performing unsupported operations

If an exception is not handled, the program stops executing and displays an error message.

---

# ⚠️ Syntax Errors vs Exceptions

| Syntax Error                    | Exception                               |
| ------------------------------- | --------------------------------------- |
| Occurs before the program runs  | Occurs while the program is running     |
| Caused by invalid Python syntax | Caused by unexpected runtime conditions |
| Prevents execution              | Can be handled using exception handling |

Examples:

**Syntax Error**

* Missing colon (`:`)
* Incorrect indentation
* Misspelled keywords

**Exception**

* `ZeroDivisionError`
* `FileNotFoundError`
* `ValueError`

---

# 🔍 Common Built-in Exceptions

Python provides many built-in exception types.

Some common examples include:

| Exception           | Description                          |
| ------------------- | ------------------------------------ |
| `ZeroDivisionError` | Division by zero                     |
| `ValueError`        | Invalid value passed to a function   |
| `TypeError`         | Operation on incompatible data types |
| `NameError`         | Variable not defined                 |
| `IndexError`        | Invalid list index                   |
| `KeyError`          | Dictionary key not found             |
| `FileNotFoundError` | File does not exist                  |
| `AttributeError`    | Object has no requested attribute    |

---

# 🛡️ Why Exception Handling is Important

Exception handling helps to:

* Prevent program crashes.
* Display meaningful error messages.
* Improve user experience.
* Handle unexpected situations gracefully.
* Increase software reliability.
* Simplify debugging.

---

# 🧩 The `try` Block

The `try` block contains code that may produce an exception.

General syntax:

```python id="tsg4ri"
try:
    # Code that may raise an exception
```

If no exception occurs, the code executes normally.

---

# 🧩 The `except` Block

The `except` block handles exceptions raised in the corresponding `try` block.

General syntax:

```python id="g8c2wy"
except:
    # Handle the exception
```

Specific exceptions can also be handled individually.

Example:

```python id="bhmz5z"
except ValueError:
    ...
```

Handling specific exceptions makes debugging easier and improves code clarity.

---

# 🧩 The `else` Block

The `else` block runs only if the `try` block completes successfully without raising an exception.

Typical use cases include:

* Displaying success messages.
* Executing follow-up operations.
* Processing results after successful execution.

---

# 🧩 The `finally` Block

The `finally` block always executes, regardless of whether an exception occurs.

It is commonly used for cleanup tasks such as:

* Closing files.
* Releasing resources.
* Closing database connections.
* Cleaning temporary data.

This ensures important operations are completed before the program continues or exits.

---

# 🔄 Flow of Exception Handling

```text id="u1i2j0"
Program Starts
       │
       ▼
   try Block
       │
 ┌─────┴─────┐
 │           │
 ▼           ▼
No Error    Exception
 │           │
 ▼           ▼
else       except
 │           │
 └─────┬─────┘
       ▼
   finally
       │
       ▼
Program Ends
```

---

# 🚨 Raising Exceptions

Python allows programmers to generate exceptions manually using the `raise` keyword.

Purpose:

* Validate user input.
* Enforce business rules.
* Prevent invalid program states.
* Improve code reliability.

General syntax:

```python id="ywlgvz"
raise Exception("Error message")
```

The `raise` statement immediately stops normal execution and signals an exceptional condition.

---

# 🏗️ Custom Exceptions

Python allows developers to define their own exception classes.

Custom exceptions are useful when built-in exceptions do not clearly describe a specific problem in an application.

Examples include:

* Invalid student ID
* Insufficient account balance
* Age restriction violation
* Invalid product code
* Unauthorized access

Custom exceptions improve code readability and make applications easier to maintain.

---

# 🌍 Real-World Applications

Exception handling is used in:

* Banking software
* Hospital management systems
* Online shopping platforms
* Student management systems
* Web applications
* APIs
* AI and Machine Learning pipelines
* Data processing scripts
* File management systems

Handling exceptions ensures these applications continue operating safely even when unexpected situations occur.

---

# 📌 Best Practices

* Handle only exceptions you expect.
* Catch specific exception types whenever possible.
* Write meaningful error messages.
* Keep `try` blocks focused on code that may fail.
* Use `finally` for cleanup tasks.
* Raise exceptions when invalid conditions are detected.
* Create custom exceptions only when they improve clarity.

---

# ❌ Common Beginner Mistakes

### Using a broad `except` block for every situation

Catching every exception without identifying its type can hide programming errors and make debugging difficult.

---

### Writing too much code inside the `try` block

Only include statements that might raise an exception.

Keeping the `try` block small makes problems easier to identify.

---

### Ignoring exception messages

Error messages provide valuable information for understanding and fixing problems.

Read them carefully during development.

---

### Forgetting the `finally` block when cleanup is required

Resources such as files or database connections should always be released properly.

The `finally` block is the ideal place for cleanup operations.

---

### Using exceptions for normal program flow

Exceptions should represent unexpected situations, not replace normal decision-making using conditions.

---

# 📝 Quick Revision

| Concept          | Description                                              |
| ---------------- | -------------------------------------------------------- |
| Exception        | A runtime error that interrupts normal program execution |
| `try`            | Contains code that may raise an exception                |
| `except`         | Handles exceptions                                       |
| `else`           | Executes if no exception occurs                          |
| `finally`        | Executes regardless of whether an exception occurs       |
| `raise`          | Generates an exception manually                          |
| Custom Exception | A user-defined exception class                           |

---

# 🎤 Interview Questions

### What is an exception?

An exception is a runtime error that interrupts the normal execution of a Python program.

---

### Why is exception handling important?

It prevents programs from crashing unexpectedly, improves reliability, and provides meaningful error handling.

---

### What is the purpose of the `try` block?

The `try` block contains code that may generate an exception during execution.

---

### What is the difference between `except` and `finally`?

The `except` block executes only when an exception occurs, whereas the `finally` block always executes, regardless of whether an exception occurs.

---

### When is the `else` block executed?

The `else` block runs only if the `try` block completes successfully without raising any exceptions.

---

### Why do we use the `raise` keyword?

The `raise` keyword is used to generate exceptions intentionally when invalid conditions are detected.

---

### What is a custom exception?

A custom exception is a user-defined exception class created to represent application-specific errors more clearly than built-in exceptions.

---

### What is the difference between a syntax error and an exception?

A syntax error prevents the program from running because the code is written incorrectly. An exception occurs during program execution and can often be handled using exception handling.

---

# 📚 Summary

Exception handling enables Python programs to respond gracefully to runtime errors instead of terminating unexpectedly. During these lectures, you learned how Python raises exceptions, how to manage them using `try`, `except`, `else`, and `finally`, how to generate exceptions with the `raise` keyword, and how to create custom exceptions for application-specific scenarios. These techniques are fundamental for building reliable Python applications and will become increasingly important as you develop larger projects in Artificial Intelligence, Machine Learning, Data Science, and software development.
