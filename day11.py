
def test(a,*args, **kwargs):
    print(a)
    print(args)
    print(kwargs)


test(1,2,"hello","testing", name="suman", address="nepal")


'''
Question 4: Employee Salary Calculator


Topic: Python functions, *args, **kwargs, conditional logic, and calculations.

Problem statement

    Create a Python function named calculate_salary(name, *bonuses, **details) to calculate an employee's final salary.

    The function should accept the employee's name, any number of bonus amounts using *args, and additional salary information using **kwargs.

Requirements

Employee name: Accept the employee's name as a required positional argument.

Bonus amounts (*args): Accept any number of bonuses, such as festival bonus, performance bonus, and project bonus.

    Salary details (**kwargs): Accept the following keyword arguments:

    basic_salary: Employee's basic monthly salary.

    tax_percentage: Percentage of tax to deduct from the salary after adding bonuses.

    department: Employee's department.

    Calculate total bonus: Add all the bonus amounts.

    Calculate gross salary: Add the basic salary and total bonuses.

    Calculate tax: Deduct tax based on the gross salary and tax percentage.

    Calculate net salary: Subtract the tax amount from the gross salary.

Display the salary report: Show the employee's name, department, basic salary, total bonuses, gross salary, tax amount, and net salary.

'''


def calculate_salary(name, *bonuses, **details):
    basic_salary = details["basic_salary"]
    tax_percentage = details["tax_percentage"]
    department = details["department"]

    total_bonus = sum(bonuses)

    gross_salary = basic_salary + total_bonus

    tax_amount = gross_salary * tax_percentage / 100
 
    net_salary = gross_salary - tax_amount

    print("\n----- Employee Salary Report -----")
    print("Employee Name:", name)
    print("Department:", department)
    print("Basic Salary:", basic_salary)
    print("Total Bonuses:", total_bonus)
    print("Gross Salary:", gross_salary)
    print("Tax Amount:", tax_amount)
    print("Net Salary:", net_salary)


calculate_salary(
    "Ram",
    5000, 3000, 2000,
    basic_salary=50000,
    tax_percentage=10,
    department="IT"
)

