# ==========================================================
# Week 02 Mini Project
# ==========================================================
# Student Management System (Simple Version)
# ==========================================================

class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Grade:", self.grade)


class StudentManager:

    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)
        print("Student added successfully!")

    def show_students(self):
        print("\nAll Students:")
        for student in self.students:
            student.display()
            print("-" * 20)


# Creating objects
s1 = Student("Ali", 20, "A")
s2 = Student("Sara", 22, "A+")

manager = StudentManager()
manager.add_student(s1)
manager.add_student(s2)

manager.show_students()


# ==========================================================
# Learning Outcome
# ==========================================================
# ✔ OOP structure
# ✔ Object management
# ✔ Real-world simulation
# ✔ Basic system design
