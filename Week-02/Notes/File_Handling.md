# 📘 File Handling in Python

> **Course:** Artificial Intelligence using Python
> **Week:** 02
> **Section:** File Handling
> **Related Lectures:** 40–43

---

# 📖 Introduction

File handling is the process of creating, opening, reading, writing, updating, and closing files using Python.

Files allow programs to **store data permanently** so that information is not lost when the program stops running.

Python provides built-in functions that make file handling simple and efficient.

---

# 🎯 Learning Objectives

After completing these lectures, you should be able to:

* Understand the purpose of file handling.
* Open and close files.
* Read data from files.
* Write data to files.
* Append data to existing files.
* Understand different file modes.
* Use the `with` statement (Context Manager).
* Handle file-related errors safely.

---

# 📚 Lecture Roadmap

| Lecture | Topic                                         |
| ------: | --------------------------------------------- |
|      40 | Reading from & Writing to Files in Python     |
|      41 | Modes of File Handling – Read, Write & Append |
|      42 | Using Context Managers (`with` Statement)     |
|      43 | Handling Exceptions During File Operations    |

---

# 📁 What is a File?

A file is a collection of data stored permanently on a storage device.

Examples:

* Text files (`.txt`)
* CSV files (`.csv`)
* JSON files (`.json`)
* Python files (`.py`)
* Images (`.png`, `.jpg`)
* PDF documents (`.pdf`)

Python can work with many types of files.

---

# 🤔 Why Do We Use File Handling?

Without files, data exists only while a program is running.

File handling allows us to:

* Save program output.
* Store user information.
* Read existing data.
* Generate reports.
* Keep records for future use.

Many real-world applications rely on file handling.

Examples include:

* Student management systems
* Banking software
* Inventory systems
* AI datasets
* Log files

---

# 📂 Opening a File

Python uses the built-in `open()` function to open a file.

General syntax:

```python
file = open("filename.txt", "mode")
```

The `open()` function returns a file object that can be used for reading or writing.

---

# 📖 Reading Files

Reading retrieves the contents of a file.

Common methods include:

* `read()`
* `readline()`
* `readlines()`

### `read()`

Reads the entire file.

```python
content = file.read()
```

---

### `readline()`

Reads one line at a time.

```python
line = file.readline()
```

---

### `readlines()`

Reads all lines and returns them as a list.

```python
lines = file.readlines()
```

---

# ✍️ Writing Files

Writing stores new data inside a file.

Method:

```python
file.write("Hello World")
```

If the file does not exist, Python creates it when using an appropriate write mode.

---

# ➕ Appending Files

Appending adds new data to the end of an existing file without removing the existing content.

Example:

```python
file.write("New Record")
```

Append mode is useful for:

* Logs
* Reports
* Daily records
* User activity

---

# 📚 File Modes

Different modes control how a file is opened.

| Mode | Description                                              |
| ---- | -------------------------------------------------------- |
| `r`  | Read only                                                |
| `w`  | Write (creates a new file or overwrites an existing one) |
| `a`  | Append (adds data to the end of the file)                |
| `x`  | Create a new file (fails if the file already exists)     |
| `r+` | Read and write                                           |
| `w+` | Read and write (overwrites existing content)             |
| `a+` | Read and append                                          |

---

# 📖 Read Mode (`r`)

Purpose:

* Read an existing file.

Characteristics:

* File must already exist.
* Data cannot be modified using read mode alone.
* Raises an error if the file is missing.

---

# ✍️ Write Mode (`w`)

Purpose:

* Write new content.

Characteristics:

* Creates the file if it does not exist.
* Overwrites existing data if the file already exists.

Use with caution because previous data is removed.

---

# ➕ Append Mode (`a`)

Purpose:

* Add new content to the end of a file.

Characteristics:

* Existing content remains unchanged.
* Creates the file if it does not exist.

Ideal for adding new records over time.

---

# 🧹 Closing a File

Files should be closed after use.

Syntax:

```python
file.close()
```

Closing a file:

* Frees system resources.
* Saves pending changes.
* Prevents file corruption.

---

# 📦 Context Managers (`with` Statement)

Python provides the `with` statement to manage files automatically.

Example:

```python
with open("students.txt", "r") as file:
    content = file.read()
```

When the `with` block ends, the file is closed automatically.

---

# ✅ Advantages of Using `with`

* Automatically closes files.
* Cleaner code.
* Reduces mistakes.
* Prevents resource leaks.
* Recommended in modern Python programs.

---

# ⚠️ File-Related Errors

Common problems include:

* File does not exist.
* Incorrect file path.
* Missing permissions.
* Attempting to read a closed file.
* Invalid file mode.

These situations may cause exceptions.

---

# 🛡️ Handling File Exceptions

Python allows file operations to be protected using exception handling.

Benefits:

* Prevents program crashes.
* Displays meaningful error messages.
* Makes programs more reliable.
* Improves user experience.

Detailed exception handling is introduced in the next section of Week 02.

---

# 📌 Best Practices

* Use meaningful file names.
* Close files after use.
* Prefer the `with` statement over manually calling `close()`.
* Use the correct file mode.
* Avoid overwriting important files accidentally.
* Handle possible file-related exceptions.

---

# 🌍 Real-World Applications

File handling is used in:

* Saving user data
* Reading configuration files
* AI datasets
* Machine Learning training data
* Log management
* Report generation
* Student databases
* Banking systems
* Hospital management systems

---

# ❌ Common Beginner Mistakes

### Forgetting to close a file

Always close files or use the `with` statement.

---

### Using write mode accidentally

Opening a file in `w` mode removes existing content.

Always verify the mode before writing.

---

### Trying to read a file that does not exist

This raises a `FileNotFoundError`.

Check that the file exists before attempting to read it.

---

### Using the wrong file mode

Choose the mode based on the task:

* Read → `r`
* Write → `w`
* Append → `a`

---

### Reading after closing the file

Once a file is closed, it cannot be read or written until it is opened again.

---

# 📝 Quick Revision

| Concept       | Description                        |
| ------------- | ---------------------------------- |
| File          | Permanent storage for data         |
| `open()`      | Opens a file                       |
| `read()`      | Reads the entire file              |
| `readline()`  | Reads one line                     |
| `readlines()` | Reads all lines into a list        |
| `write()`     | Writes data to a file              |
| `close()`     | Closes the file                    |
| `with`        | Automatically manages file closing |
| Read Mode     | Opens a file for reading           |
| Write Mode    | Creates or overwrites a file       |
| Append Mode   | Adds data to the end of a file     |

---

# 🎤 Interview Questions

### What is file handling?

File handling is the process of reading, writing, creating, updating, and managing files in Python.

---

### Why is file handling important?

It allows data to be stored permanently and reused after the program ends.

---

### What is the purpose of the `open()` function?

It opens a file and returns a file object for performing operations such as reading or writing.

---

### What is the difference between `r`, `w`, and `a` modes?

* `r` reads an existing file.
* `w` writes to a file and overwrites existing content.
* `a` appends new content without deleting existing data.

---

### Why is the `with` statement recommended?

Because it automatically closes the file after use, making code cleaner and reducing the risk of resource leaks.

---

### What happens if you open a file in write mode?

If the file exists, its contents are overwritten. If it does not exist, Python creates a new file.

---

# 📚 Summary

File handling enables Python programs to store and retrieve data permanently. During these lectures, you learned how to open files, read and write data, use different file modes, work with the `with` statement for automatic file management, and understand common issues that can occur during file operations. These skills are essential for building real-world applications and provide the foundation for working with datasets in later Artificial Intelligence and Machine Learning topics.
