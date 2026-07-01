# 📘 Topic 43: Handling Exceptions During File Operations

## What is an Exception?

An **exception** is an error that happens while a program is running.

For example, if you try to open a file that doesn't exist, Python cannot find it, so it raises an exception.

Example:

```python
with open("missing.txt", "r") as file:
    print(file.read())
```

### What happens?

Python looks for a file named `missing.txt`.

If the file does not exist, the program stops immediately and shows an error like:

```text
FileNotFoundError: [Errno 2] No such file or directory: 'missing.txt'
```

### Visual Explanation

```
Program starts
      │
      ▼
Open "missing.txt"
      │
      ▼
File exists?
   ┌───────┐
   │  No   │
   └───────┘
      │
      ▼
Program crashes ❌
```

---

# What is `try` and `except`?

Python gives us a way to **catch errors** so the program doesn't crash.

We use:

* `try` → Try running this code.
* `except` → If an error happens, run this code instead.

Example:

```python
try:
    with open("missing.txt", "r") as file:
        print(file.read())
except FileNotFoundError:
    print("File not found!")
```

### Step-by-step

Python does this:

```
Try opening the file.
```

If the file exists

```
Open file
Read file
Print contents
```

If the file does NOT exist

```
Don't crash
Go to except block
Print:
File not found!
```

Output

```
File not found!
```

---

# Why use `try` and `except`?

Without them

```
Program starts
↓

Error occurs
↓

Program stops ❌
```

With them

```
Program starts
↓

Error occurs
↓

Handle the error

↓

Program continues ✅
```

This makes your programs much more user-friendly.

---

# Understanding the Third Example

The tutor wrote:

```python
filename = "my_info.txt"
name = "GitHub Copilot"
age = 1
```

These are just variables.

```
filename → my_info.txt

name → GitHub Copilot

age → 1
```

Nothing special happens yet.

---

Now comes the interesting part.

```python
try:
    with open(filename, "r") as fin:
        print(fin.read())
```

Python tries to read the file.

Question:

Does `my_info.txt` exist?

### Case 1: Yes ✅

```
Open file

↓

Read data

↓

Print data
```

Done.

---

### Case 2: No ❌

Python cannot find the file.

Instead of crashing,

it goes here:

```python
except FileNotFoundError:
```

This means

> "If the file is missing, do the following."

---

Now Python executes

```python
with open(filename, "w") as fout:
```

Remember:

`"w"` means

* Create the file if it doesn't exist.
* Open it for writing.

Now Python creates

```
my_info.txt
```

Then

```python
fout.write(f"{name}\n{age}\n")
```

writes

```
GitHub Copilot
1
```

inside the file.

Now the file looks like

```
GitHub Copilot
1
```

---

After creating the file,

Python reads it again.

```python
with open(filename, "r") as fin:
    print(fin.read())
```

Output

```
GitHub Copilot
1
```

---

# Complete Flow

```
Start Program
       │
       ▼
Try opening my_info.txt
       │
       ▼
Does file exist?
      / \
     /   \
   Yes    No
    │      │
    ▼      ▼
Read     Create file
File     Write data
    │      │
    ▼      ▼
 Print    Read file
    │      │
    └──► Print
```

---

# Why did the tutor write this program?

The goal is:

> "If the file already exists, read it."

Otherwise

> "Create the file, save the data, then read it."

So the program **always works**, whether the file exists or not.

---

# Easy Way to Remember

### Without Exception Handling

```
Problem occurs

↓

Program crashes ❌
```

---

### With Exception Handling

```
Problem occurs

↓

Python catches the error

↓

Runs another block of code

↓

Program continues ✅
```

---

# Beginner Notes for GitHub

## Handling Exceptions During File Operations

When working with files, sometimes a file may not exist. If we try to open a missing file in read mode (`"r"`), Python raises a `FileNotFoundError` and the program stops.

To prevent the program from crashing, we use `try` and `except`.

* `try` → Runs the code that might cause an error.
* `except` → Runs only if an error occurs.

Example:

```python
try:
    with open("missing.txt", "r") as file:
        print(file.read())
except FileNotFoundError:
    print("File not found!")
```

If the file exists, Python reads and prints its contents.

If the file does not exist, instead of crashing, Python prints:

```
File not found!
```

This makes programs more reliable and user-friendly.

### Key Points

* `try` → Try to execute the code.
* `except` → Handle the error if one occurs.
* `FileNotFoundError` → Happens when Python cannot find the file.
* Exception handling prevents the program from crashing and allows it to continue running.
