class Test2:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self):
        self.a = 100
        self.c = 2
        return self.a + self.b

    def sub(self):
        return self.a - self.b


obj = Test2(50, 10)
print(obj.add())
print(obj.a)
print(obj.sub())
print(obj.c)


# single
# multi level
# mutiple


print("----------" * 10)


class Parent:
    a = 10
    c = 2


class Child(Parent):
    b = "hello"
    c = "from b"


obj = Child()
print(obj.c)


class Parent:
    def test(self):
        return "from test parent class"


class Child(Parent):
    a = 10

    def result(self):
        return "from child class"


obj = Child()
print(obj.test())


class Math:
    a = 10
    b = 50

    def add(self):
        return self.a + self.b


class Result(Math):
    a = 20


obj = Result()
print(obj.add())


class Parent:
    def __init__(self):
        print("from Parent")


class Child(Parent):
    a = 2

    def __init__(self):
        Parent.__init__(self)
        super().__init__()
        print("from child")


obj = Child()


class Parent:
    a = 10


class Child1(Parent):
    b = 20


class Child2(Child1):
    c = 100


obj = Child2()
print(obj.a + obj.b + obj.c)


print("--------" * 10)


class Person:
    name = "Hari"
    age = 22


class Employee(Person):
    employee_id = "E902"
    salary = 20000


class Manager(Employee):
    team_size = 10
    department = "IT"

    def display(self):
        return f"Name = {self.name} employee = {self.employee_id} department = {self.department}"

    def annual_salary(self):
        return f"Annual Salary of {self.name } is {self.salary * 12}"

    def is_supervises(self):
        return True if self.team_size >= 10 else False


obj = Manager()
print(obj.display())
print(obj.annual_salary())
print(obj.is_supervises())