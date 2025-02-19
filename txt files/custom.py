def greet(name):
    print(f"Hello {name}. Welcome to our class")

def add(a,b):
    return a+b

class Student:
    def __init__(self, name, age, marks):
        self.name = name
        self.age = age
        self.marks = marks

    def info(self):
        print(f"Student Name: {self.name}, Age: {self.age}, Marks: {self.marks}")
