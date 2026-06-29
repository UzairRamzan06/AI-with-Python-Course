# ==========================================================
# Course : Artificial Intelligence using Python
# Week   : 02
# File   : 19_try_except_else_finally.py
# Lecture: 45
# Topic  : try, except, else & finally Blocks
#
# What to Practice:
#     ✔ Understand full exception structure
#     ✔ Use try-except safely
#     ✔ Learn else block behavior
#     ✔ Understand finally block usage
# ==========================================================

# ----------------------------------------------------------
# Exception Handling Structure
# ----------------------------------------------------------
# try:
#     code that may cause error
# except:
#     handle error
# else:
#     runs if NO error occurs
# finally:
#     ALWAYS runs (cleanup section)
# ----------------------------------------------------------


# ==========================================================
# Example 1: Basic try and except
# ==========================================================

print("Example 1 - try and except")

try:
    result = 10 / 2
    print("Result:", result)

except ZeroDivisionError:
    print("Cannot divide by zero!")

# Output:
# Result: 5.0


print("\n" + "=" * 50)


# ==========================================================
# Example 2: try, except, else
# ==========================================================

print("Example 2 - try, except, else")

try:
    result = 20 / 4

except ZeroDivisionError:
    print("Error: division by zero")

else:
    print("Success! Result is:", result)

# Output:
# Success! Result is: 5.0


print("\n" + "=" * 50)


# ==========================================================
# Example 3: else block when error occurs
# ==========================================================

print("Example 3 - else skipped if error happens")

try:
    result = 10 / 0

except ZeroDivisionError:
    print("Error handled successfully")

else:
    print("This will NOT run because error occurred")

# Output:
# Error handled successfully


print("\n" + "=" * 50)


# ==========================================================
# Example 4: finally block (always runs)
# ==========================================================

print("Example 4 - finally block")

try:
    result = 10 / 2
    print("Result:", result)

except ZeroDivisionError:
    print("Error occurred")

finally:
    print("This always runs (cleanup section)")

# Output:
# Result: 5.0
# This always runs (cleanup section)


print("\n" + "=" * 50)


# ==========================================================
# Example 5: finally with error
# ==========================================================

print("Example 5 - finally with error")

try:
    result = 10 / 0

except ZeroDivisionError:
    print("Handled division error")

finally:
    print("Finally block always executes")

# Output:
# Handled division error
# Finally block always executes


print("\n" + "=" * 50)


# ==========================================================
# Example 6: Real-Life Analogy
# ==========================================================
# try     → Try to open door
# except  → If locked, handle situation
# else    → If opened successfully, enter room
# finally → Close door no matter what
# ==========================================================

print("Complete exception flow explained")


print("\n" + "=" * 50)


# ==========================================================
# Example 7: Real-World Usage Pattern
# ==========================================================

print("Example 7 - real-world pattern")

try:
    file = open("demo_try.txt", "w")
    file.write("Learning exception handling\n")

except Exception as e:
    print("Error occurred:", e)

else:
    print("File written successfully")

finally:
    try:
        file.close()
        print("File closed safely")
    except:
        print("File was not opened")


print("\n" + "=" * 50)


# ==========================================================
# Key Concepts Summary
# ==========================================================
# ✔ try → risky code
# ✔ except → handle errors
# ✔ else → runs only if no error
# ✔ finally → always runs
# ==========================================================

print("Full exception handling structure learned")


print("\n" + "=" * 50)


# ==========================================================
# Practice Examples
# ==========================================================

# Practice 1

print("Practice 1")

try:
    result = 5 + 5

except:
    print("Error occurred")

else:
    print("Addition successful:", result)

finally:
    print("Execution completed")

print()


# Practice 2

print("Practice 2")

try:
    result = 10 / 2

except ZeroDivisionError:
    print("Division error")

else:
    print("Result:", result)

finally:
    print("Done")

print()


# Practice 3

print("Practice 3")

try:
    result = 10 / 0

except ZeroDivisionError:
    print("Handled safely")

finally:
    print("Always executes")


print("\n" + "=" * 50)


# ==========================================================
# Challenge Exercises
# ==========================================================

# Challenge 1
# What is the purpose of else in try-except?

# Challenge 2
# When does finally execute?

# Challenge 3
# What happens if no exception occurs?

# Challenge 4
# Create a program using all four blocks.

# Challenge 5
# Explain real-life use of exception handling.


# ==========================================================
# Git Commit Message
# ==========================================================

# git add .
# git commit -m "Add lecture 45 try except else finally complete structure"
