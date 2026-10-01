#  1. student grade and result

# marks = int(input("marks of student "))
# attendance_percent = int(input("attendance of student "))
# if (marks > 100 or marks < 0 ):
#   print("marks is not valid")
# elif (marks > 80 and marks < 100):
#   print("You got A")
# elif (marks > 70 and marks < 79):
#   print("You got B")
# elif (marks > 60 and marks < 69):
#   print("You got C")
# elif (marks > 50 and marks < 59):
#   print("You got D")
# elif (marks < 50):
#   if (attendance_percent >= 75):
#     print("eligible for reexam")
#   else:
#     print("not eligible for exam")


    
# 2. ATM withdrawal 
  # Create an ATM withdrwal program

# account_balance = int(input("Enter your total account balance "))
# withdrawal_amount = int(input("Enter amount to be withdraw "))

# if (withdrawal_amount <= 0):
#   print("Enter valid amount")
# elif (account_balance < withdrawal_amount):
#   print("Insufficent balance")
# elif (withdrawal_amount % 500 == 0):
#   print("Successful withdrawal")
#   print("Remaining balance:", account_balance - withdrawal_amount)
#   if((account_balance - withdrawal_amount) < 1000):
#     print("Your balamce is less than 1000. Please credit it.")
# else:
#   print(" Amount must be multiple of 500")


# electricity bill calculator

# electricity_unit = int(input("Enter the electricity units: "))
# customer_type = input("Is customer senior citizen? ")
# if(electricity_unit > 0 and electricity_unit <= 50):
#   rate = 5 * electricity_unit
# elif(electricity_unit > 50 and electricity_unit <= 150):
#   rate = 7 * electricity_unit
# elif(electricity_unit > 150 and electricity_unit <= 250):
#   rate = 10 * electricity_unit
# elif(electricity_unit>250):
#   rate = 15 * electricity_unit
# if (rate > 3000):
#   if(customer_type == "yes"):
#     rate = rate - (0.1 * rate)
#     print(rate)
#   else:
#     print("No Discount")
# else:
#   print(rate)

# Movie Ticket  System

# age = int (input("Age of a person: "))
# person = input("Is the person student? ")

# if (age <5):
#   ticket_price = 0
# elif(age>=5 and age<13):
#   ticket_price = 150
# elif (age >=13 and age<=59):
#   ticket_price =300
# if(age>=13 and age <=59):
#   ticket_price = 300
#   if(person == "yes"):
#     ticket_price = ticket_price - (0.2*ticket_price)
#     print(ticket_price)
# elif(age>=60):
#   ticket_price = 200

# print("ticket price Rs.", ticket_price)


# Login system
# correct_username = "admin123"
# correct_password = "pass123"

# username = input("Enter username:")
# password = input("Enter password:")

# if username == correct_username:
#   if password == correct_password:
#     print("Login successful")
  
#     role = input("Enter your role (admin/staff/customer):").lower()
#     if role == "admin":
#       print("Welcome Admin! You have full access.")
#     elif role == "staff":
#       print("Welcome Staff! You have limited access.")
#     elif role == "customer":
#       print("Welcome Customer! You have basic access.")
#     else:
#       print("Invalid role. Access denied.") 
#   else:
#     print("Incorrect password. Access denied.")
# else:
#   print("Incorrect username. Access denied.")


# Shopping dicount system

# total_purchase_amount = float(input("Enter the total purchase amount: "))

# if total_purchase_amount < 2000:
#   dicount = 0
# elif total_purchase_amount >= 2000 and total_purchase_amount < 5000:
#   dicount = 0.05 * total_purchase_amount
# elif total_purchase_amount >= 5000 and total_purchase_amount < 10000:
#   dicount = 0.1 * total_purchase_amount
# elif total_purchase_amount >= 10000:
#   dicount = 0.2 * total_purchase_amount

# final_amount = total_purchase_amount - dicount
# print("Total purchase amount: Rs.", total_purchase_amount)

# cutomer_membership = input("Is the customer a member? (yes/no): ").lower()
# if cutomer_membership == "yes":
#   final_amount = final_amount - (0.05 * final_amount)
#   print("Additional 5% discount applied for members.")
# else:
#   print("No additional discount for non-members.")


# print("original amount: Rs.", total_purchase_amount)
# print("Discount applied: Rs.", dicount)
# print("Final amount to be paid: Rs.", final_amount)


# Number Analyzer

print("Enter a number: ")
number = int(input())

if number > 0:
  print("The number is positive.")
  if number % 2 == 0:
    print("The number is even.")
  else:
    print("The number is odd.")
elif number < 0:
  print("The number is negative.") 
  if number > -100:
    print("The number is greater than -100.")
  elif number < -100:
    print("The number is less than  -100.")
  else:
      print("The number is equal to -100.")
else:
  print("The number is zero.")