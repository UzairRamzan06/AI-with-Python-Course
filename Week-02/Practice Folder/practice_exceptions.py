# ==========================================================
# Practice Exception Handling
# ==========================================================

# Example 1
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero")


# Example 2
try:
    num = int("abc")
except ValueError:
    print("Invalid conversion")


# ==========================================================
# Practice Tasks
# ==========================================================
# Handle IndexError in a list
# Handle KeyError in a dictionary
