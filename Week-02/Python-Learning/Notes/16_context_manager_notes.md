# Course : Artificial Intelligence using Python
# Week   : 02
# File   : 16_context_manager.py
# Lecture: 42
# Topic  : Using Context Managers (with Statement)

# What to Practice:
    ✔ Understand context manager
    ✔ Use "with" for file handling
    ✔ Automatic file closing
    ✔ Safer and cleaner code



# Using `with open()` in Python

The `with open()` statement is the **recommended way** to open a file in Python because it **automatically closes the file** after you're done using it.

### Example

```python
with open("demo.txt", "r") as file:
    data = file.read()
    print(data)

# File is closed automatically here!
```

### Output

```text
This is another test.
New line added!
```

### Explanation

* `open("demo.txt", "r")` opens the file in **read mode**.
* `as file` stores the file object in the variable `file`.
* `file.read()` reads the **entire content** of the file.
* `print(data)` displays the file's content on the screen.
* When the `with` block ends, Python **automatically closes the file**. You don't need to write `file.close()`.

### Why use `with open()`?

Without `with`:

```python
file = open("demo.txt", "r")
data = file.read()
print(data)
file.close()    # You must remember to close the file
```

With `with`:

```python
with open("demo.txt", "r") as file:
    data = file.read()
    print(data)

# File closes automatically
```

### Simple way to remember

* **`open()`** → You must close the file yourself using `file.close()`.
* **`with open()`** → Python closes the file automatically.

### Real-life example

Think of borrowing a library book.

* **Without `with`:** You borrow the book, but you must remember to return it yourself.
* **With `with`:** The librarian automatically takes the book back when you're finished reading.

That's why most Python programmers prefer `with open()`. It's shorter, cleaner, and helps prevent mistakes like forgetting to close the file.
