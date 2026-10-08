for i in [1,2,3]:
  for j in [4,5,6]:
    print(i,j)



print("-----------"*4)

for i in range(1,15,2):
  print(i)

print("-----------"*4)

for i in range(1,15,2):
  if (i%2==0):
    print(i)

print("------"*4)
for i in range(10,1,-1):
  print(i)

print("--------------")

num = 2
for i in range (1,11,1):
  print(f'{num}x{i}={num*i}')

print("--------------")

for i in [44,47,99,77]:
  for j in range(1,11,1):
    print(f'{i}x{j} = {i*j} ')
  print()

print("---------------")

total = 0
for i in [1,20,1]:
  total = total + i
print(total)

print("--------------")

a = [1,2,3,4,55,5,3,2]
print(sum(a))


print("------while loop-----------")

i = 0
while(i<10):
  print(i)
  i=i+1



number = 77
attempt = 0

while True:
  user_input = int(input("Enter number: "))
  attempt = attempt + 1
  if user_input == number:
    print("Number matched in", attempt)
    break
  else:
    print("Try again")


