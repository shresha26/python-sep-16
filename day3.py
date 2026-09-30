#logical operator

age = 20
citizen = True
print(age >= 18 and citizen) #true

is_weekend = False
is_holiday = True
print(is_weekend or is_holiday) #true

logged_in = False
print(not logged_in) #true


if ("hari"=="kari"):
  print("code block")
  print("this is testing")


a = True
if a:
  print("always true")
else:
   print("else")
   print("after if")

if True:
   print("a")

if (2==3):
   print("inside if condition")
   print("True")
else:
   print("else condition") 


x = 99
if x > 10:
   print(f"{x} is greater than 10 ")


if 2==2:
   print("this is true")
elif(3==3):
   print("this is elif condition")
else:
   print("else condition")


percent = 80

if percent >= 80:
   print("A+")
elif percent >= 70:
   print("B+")
elif percent >= 60:
   print("C+")
else:
   print("Fail")



percent = 60

if (percent>100 or percent<0):
  print("percent number is not valid")

elif percent >= 80 and percent <=100:
  if percent == 100:
    print("topper")
elif percent == 80:
    print("lucky distinction")
    print("Distinction")
    print("pass")

elif percent >= 60 and percent <= 79:
  print("first divison")

elif percent >= 50 and percent <= 59:
  print("second division")

else:
  print("fail")


gender = "F"
if gender == "M":
   print("Male")
else:
  print("Female")


data = "Male" if gender == "M" else "Female"
print(data)


