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






