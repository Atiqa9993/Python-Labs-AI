class Greet:
    def __init__(self, name):
       self.name=name

    def greeting(self):
        print(f" Good Morning {self.name}")


class Employee(Greet):
    def __init__(self, name,id):
        self.id=id
        super().__init__(name)

    def show(self):
        print(f"name is {self.name} Id is {self.id}")

# a1=Greet()
# def caller():
#     a1.greeting()


# def func():
#     print("Mym Module")

class Fact:
    def __init__(self, num):
        self.num = num

    def calculate(self):
       
        def factorial(n):
            if n == 1:
                return 1
            else:
                return n * factorial(n - 1)

        return factorial(self.num)

