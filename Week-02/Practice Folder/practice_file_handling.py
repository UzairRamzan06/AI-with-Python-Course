# ==========================================================
# Practice File Handling
# ==========================================================

# Write to file
with open("practice.txt", "w") as file:
    file.write("Hello AI Student\n")

# Read file
with open("practice.txt", "r") as file:
    print(file.read())

# Append data
with open("practice.txt", "a") as file:
    file.write("Learning Python is fun\n")


# ==========================================================
# Practice Tasks
# ==========================================================
# Create a file and store your name and course
# Then read and display it
