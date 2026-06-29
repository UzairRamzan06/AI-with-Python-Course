# ==========================================================
# Practice OOP Concepts
# ==========================================================

# Class and Object

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print("Name:", self.name)
        print("Age:", self.age)


s1 = Student("Ali", 20)
s1.show()


# Encapsulation Example
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

    def show_balance(self):
        print("Balance:", self.__balance)


acc = BankAccount(1000)
acc.show_balance()


# ==========================================================
# Practice Tasks
# ==========================================================
# Create a class Car with attributes brand and model
# Create method to display details
