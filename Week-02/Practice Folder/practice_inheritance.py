# ==========================================================
# Practice Inheritance
# ==========================================================

class Animal:
    def speak(self):
        print("Animal speaks")


class Dog(Animal):
    def bark(self):
        print("Dog barks")


d = Dog()
d.speak()
d.bark()


# ==========================================================
# Practice Tasks
# ==========================================================
# Create a class Vehicle
# Create a class Car that inherits Vehicle
# Add methods for both
