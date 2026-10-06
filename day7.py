# for loop

for data in [1,233,244,43,645,458]:
  print("hello world",data)

for i in ['hello','hi','bye']:
  print(i)

for i in [1,2,3]:
  print(i+1)

for i in [1,2,3,4,4,3,2,2,2,2,2]:
  if i==2:
    print(i)




for i in [299,333,444,554,556]:
  if (i % 2 == 0):
    print(i)




data = [10, "Python", 25, "Django", "Hello", 7]

for i in data:

  if isinstance(i, str):
    print(i)



result = []
for i in data:
  if isinstance(i, str):
    result.append(i)
print(result)


data = "Hello World"

for i in data:
  print(i)

data = {
  "name": "ram",
  "age": 10,
  "phone": 293
}

for i in data:
  print(f'{i}={data[i]}')

for i in data.values():
  print(i)

for i in data.items():
  print(i)


print('------------------------------------------------------------------')

for i in [1,2,3,4,5,6,7]:
  if i==3:
    break
  print(i)


print('------------------------------------------------------------------')

for i in [1,2,3,4,5,6,7]:
  if i==3 or i==6:
    continue
  print(i)


