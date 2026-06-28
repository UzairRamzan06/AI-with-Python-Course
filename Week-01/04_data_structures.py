# ===========================================
# Course : Artificial Intelligence with Python
# Week   : 01
# File   : 04_data_structures.py
# VDO Lectures Covered : 13
# Topic  : Python Data Structures - Lists, Tuples, Sets & Dictionaries
# What to practice
      List
      Tuple
      Set
      Dictionary
# ===========================================


# ==================================================
# LIST
# ==================================================

# A list stores multiple items in order.
# Lists are mutable (can be changed).

fruits = ["apple" , "banana" , "mango" , "banana", "grapes"]

print(fruits)
print(fruits[0])
print(fruits[1])
print(fruits[3])
print(fruits[-1])
print(fruits[-3])
print("List Example:")


# Access an item
print("First Fruit:", fruits[0])

# Add a new item ( append ) which always tacks an item onto the very end
fruits.append("Orange")
print("After Adding:", fruits)

# Insert a new item 
# inserting an item at a specific index (or a specific position)
# insert(index, item) lets you choose exactly where the new item goes. 
# In your example, "tomato" is placed at index 1 (the second position), pushing everything else one spot to the right.

fruits.insert(1, "tomato")
print(fruits)

fruits.insert(2, "lettuce" )
print(fruits)

# Remove an item
fruits.remove("banana")
print("After Removing:", fruits)

# .pop() What to call it: Removing (and returning) an item.
# What it does: By default, .pop() removes the very last item from the list and "pops" it out. 
# If you want to, you can capture that removed item in a variable (e.g., saved_fruit = fruits.pop()).
# Note: You can also pass an index to it, like fruits.pop(0), to remove a specific item.
fruits.pop()
print(fruits)

# .sort() What to call it: Sorting a list in place.
# It rearranges the items in the list. For strings (like your fruits), it sorts them alphabetically. 
# For numbers, it sorts them from lowest to highest. Because lists are mutable, this permanently changes the order of your original fruits list.
fruits.sort()
print(fruits)

# for fruit in fruits: What to call it: Iterating (or looping) through a list.
# This is a for loop. It goes through your list item by item, assigning the current item to the temporary variable fruit, and runs the indented code (print(fruit)) for each one until it reaches the end of the list.
for fruit in fruits:
    print(fruit)
  
print("-" * 40)


# ==================================================
# TUPLE
# ==================================================

# A tuple stores multiple items in order.
# Tuples are immutable (cannot be changed).

colors = ("Red", "Green", "Blue")

print("Tuple Example:")
print(colors)
print(colors[1])
print("First Color:", colors[0])
print(colors[-1])

print("-" * 40)


# ==================================================
# SET
# ==================================================

# A set stores unique values.
# Duplicate values are removed automatically.

numbers=(1,2,3,2,4,2)
print(numbers.count(2))
print(numbers.index(3))

A = {1,2,3}
B = {3,4,5}
print(A.union(B))
print(A.intersection(B))
print(A.difference(B))

my_set = {1,2,3,4,4,5,7,7,8,9}
print(my_set)
my_set.add(6)
my_set.remove(2)
print(my_set)

numbers = {10, 20, 30, 20, 10}
print("Set Example:")
print(numbers)

# Add a value
numbers.add(40)

print("After Adding:", numbers)

print("-" * 40)


# ==================================================
# DICTIONARY
# ==================================================

# A dictionary stores data as key-value pairs.

student = {"Name": "Ali",
    "Age": 22,
    "City": "Multan"}

print("Dictionary Example:")
print(student)

print("Student Name:", student["Name"])

# Add a new key-value pair
student["Course"] = "Artificial Intelligence"

print("Updated Dictionary:")
print(student)

print("-" * 40)


# ==================================================
# PRACTICE
# ==================================================

print("Practice Section")

# Create your own list
subjects = ["Python", "AI", "Machine Learning"]

print(subjects)

# Create your own tuple
months = ("January", "February", "March")

print(months)

# Create your own set
countries = {"Pakistan", "Turkey", "Pakistan"}

print(countries)

# Create your own dictionary
my_info = {
    "Name": "Your Name",
    "Age": 22,
    "Country": "Pakistan"
}

print(my_info)
