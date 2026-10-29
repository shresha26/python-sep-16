class Test():
    data = "hello world"

    def __str__(self):
        return self.data



obj = Test()
print(obj)


# string method
# return method
# output method



class Person:

    def __init__(self,name, age):
        self.name = name
        self.age = age


class Employee(Person):


    def __init__(self,name, age,employee_id, salary):
        self.employee_id = employee_id
        self.salary = salary
        super().__init__(name,age)




class Manager(Employee):

    def __init__(self, **kwargs):
        self.team_size = kwargs['team_size']
        self.department = kwargs['department']
        super().__init__(kwargs['name'], kwargs['age'],kwargs['employee_id'], kwargs['salary'])

        print(kwargs)



    def display(self):
        return f"Name = {self.name} employee = {self.employee_id} department = {self.department}"

    def annual_salary(self):
        return f"Annual Salary of {self.name } is {self.salary * 12}"

    def is_supervises(self):
        return True if self.team_size >= 10 else False


obj = Manager(name = "suman",age = 22, employee_id=234, salary=40000, team_size=3, department = "IT")
obj1 = Manager(name = "Hari",age = 22, employee_id=2314, salary=400300, team_size=3, department = "IT")
obj2 = Manager(name = "Milan",age = 22, employee_id=234, salary=400300, team_size=3, department = "Science")

# print(obj.display())
# print(obj1.display())
# print(obj2.display())

print(obj.annual_salary())
print(obj1.annual_salary())
print(obj2.annual_salary())

# print(obj.is_supervises())