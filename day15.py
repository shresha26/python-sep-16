class Test:
    data = "hello world"

    def __str__(self):
        return self.data


obj = Test()
print(obj)


# string method
# return method
# output method


class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age


class Employee(Person):

    def __init__(self, name, age, employee_id, salary):
        self.employee_id = employee_id
        self.salary = salary
        super().__init__(name, age)


class Manager(Employee):

    def __init__(self, **kwargs):
        self.team_size = kwargs["team_size"]
        self.department = kwargs["department"]
        super().__init__(
            kwargs["name"], kwargs["age"], kwargs["employee_id"], kwargs["salary"]
        )

        print(kwargs)

    def display(self):
        return f"Name = {self.name} employee = {self.employee_id} department = {self.department}"

    def annual_salary(self):
        return f"Annual Salary of {self.name } is {self.salary * 12}"

    def is_supervises(self):
        return True if self.team_size >= 10 else False


obj = Manager(
    name="suman", age=22, employee_id=234, salary=40000, team_size=3, department="IT"
)
obj1 = Manager(
    name="Hari", age=22, employee_id=2314, salary=400300, team_size=3, department="IT"
)
obj2 = Manager(
    name="Milan",
    age=22,
    employee_id=234,
    salary=400300,
    team_size=3,
    department="Science",
)

# print(obj.display())
# print(obj1.display())
# print(obj2.display())

print(obj.annual_salary())
print(obj1.annual_salary())
print(obj2.annual_salary())

# print(obj.is_supervises())


class A:
    d = 10

    def test(self):
        return "from class A"


class B:
    d = 12

    def test(self):
        return "from class B"


class C(A, B):
    e = 100

    f = B().test()


obj = C()
print(obj.d)
print(obj.f)
print(obj.test())


# xampp


a = "Hello"
print(len(a))


a = [1, 2, 4, "hello"]
print(len(a))


a = {"name": "hari", "age": 22}

print(len(a))


# 2. Online Food Delivery
# A food delivery app has:
# - Restaurant class with restaurant name and location.
# - DeliveryPartner class with rider name and bike number.
# Create an Order class that inherits from both.

# Requirements:
# - Store order ID.
# - Show restaurant, rider, and order details together.
# - Add a method that prints complete delivery information.


class Restaurant:
    name = ""
    location = ""

    def restro_info(): ...


class DeliveryPartner:
    rider_name = ""
    bike_number = ""

    def delivery_info(): ...


class Order(Restaurant, DeliveryPartner):
    order_id = ""

    def display(self): ...


obj = Order()
print(obj.display())


class Resturant:
    def __init__(self, name, location):
        self.name = name
        self.location = location

    def restro_info(self):
        return f"name of the resturant is {self.name} and location is {self.location}"


class DeliveryPartner:
    def __init__(self, rider_name, bike_number):
        self.rider_name = rider_name
        self.bike_number = bike_number

    def display_info(self):
        return f"the name of rider is {self.rider_name} and the number of bike is {self.bike_number}"


class Order(Resturant, DeliveryPartner):
    def __init__(self, name, location, rider_name, bike_number, order_id):
        Resturant.__init__(self, name, location)
        DeliveryPartner.__init__(self, rider_name, bike_number)
        self.order_id = order_id

    def display(self,a):
        print(a)
        return f"""
       {self.restro_info()}
       {self.display_info()}
       Order ID is {self.order_id}
       """


obj = Order("ANGAN", "Kumaripati", "Shyam", 3334, 133)
print(obj.display(1))




class Bank():
    def __init__(self, bank_name, branch_name):
        self.bank_name = bank_name
        self.branch_name = branch_name

    def display_bank_info(self):
        return(f"the name of the bank is {self.bank_name}and branch is {self.branch_name}")


class Account(Bank):
    def __init__(self,bank_name, branch, account_holder_name, account_no, balance):
        super().__init__(bank_name, branch)
        self.account_holder_name = account_holder_name
        self.account_no = account_no
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return(f"Deposited amount is {amount}")
        else:
            return("invalid deposited amount")

    def withdraw(self, amount):
        if amount<0:
            return("invalid withdrawl amount")

        elif amount <= self.balance:
            self.balance -= amount
            return(f"withdrawn amount is {amount}")

        else:
            return("balance is not sufficient")

    def check(self):
        return(f"current balance is {self.balance}")

class SavingAccount(Account):
    def __init__(self, bank_name, branch_name, account_holder_name, account_no, balance, interest_rate):
       super().__init__(bank_name, branch_name, account_holder_name, account_no, balance)
       self.interest_rate = interest_rate

    def calc_interest(self):
        interest = self.balance * self.interest_rate / 100
        return interest

print("----------"*10)
obj = SavingAccount("Nabil",'Dang','Sudan',456,0,2)
print(obj.check())
obj.deposit(1000)
print(obj.check())
print(obj.withdraw(700))
print(obj.check())
obj.deposit(600)
print(obj.check())
print(obj.withdraw(1000))

print(obj.check())



class Bank:
    def __init__(self, bank_name, branch_name):
        self.bank_name = bank_name
        self.branch_name = branch_name

    def display_bank_info(self):
        print(f"Bank Name   : {self.bank_name}")
        print(f"Branch Name : {self.branch_name}")


class Account(Bank):
    def __init__(self, bank_name: str, branch_name: str, holder_name: str, account_number: str, balance: float = 0.0):
        super().__init__(bank_name, branch_name)
        self.holder_name = holder_name
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount: float):
        if amount > 0:
            self.balance += amount
            print(f"Successfully deposited ${amount:.2f}. New Balance: ${self.balance:.2f}")
        else:
            print("Error: Deposit amount cannot be negative or zero!")

    def withdraw(self, amount: float):
        if amount <= 0:
            print("Error: Withdrawal amount must be greater than zero!")
        elif amount > self.balance:
            print(f"Error: Insufficient balance! Available balance is ${self.balance:.2f}")
        else:
            self.balance -= amount
            print(f"Successfully withdrew ${amount:.2f}. New Balance: ${self.balance:.2f}")

    def check_balance(self):
        print(f"Current Balance for {self.holder_name}: ${self.balance:.2f}")


class SavingsAccount(Account):
    def __init__(self, bank_name: str, branch_name: str, holder_name: str, account_number: str, balance: float, interest_rate: float):
        super().__init__(bank_name, branch_name, holder_name, account_number, balance)
        self.interest_rate = interest_rate

    def calculate_interest(self):
        interest = self.balance * (self.interest_rate / 100)
        print(f"Yearly Interest for {self.holder_name}: ${interest:.2f} (Rate: {self.interest_rate}%)")
        return interest

    def display_account_info(self):
        print("\n" + "=" * 45)
        print("          SAVINGS ACCOUNT DETAILS          ")
        print("=" * 45)

        self.display_bank_info()
        print(f"Holder Name  : {self.holder_name}")
        print(f"Account No   : {self.account_number}")
        print(f"Balance      : ${self.balance:.2f}")
        print(f"Interest Rate: {self.interest_rate}%")
        print("=" * 45)


my_account = SavingsAccount(
    bank_name="Global IME Bank",
    branch_name="Panipokhari Branch",
    holder_name="Nitesh",
    account_number="100400100304",
    balance=5000.0,
    interest_rate=4.0
)
my_account.deposit(5000)
my_account.withdraw(1000000)
my_account.display_account_info()
