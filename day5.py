# list 
#append
print("------------------------append--------------------------")
a = [1,2,3,4]
a.append("test")
print(a)

data = 2
a = []
a.append(data)
print(a)

data = ["hello", 1,2,1.5,"testing"]
data.append(2)
data.append(3)

data = []
data.append("broadway")
print(data)


# insert
print("-------------------------insert-------------------")
a = [1,2,3,4,5,6]

a.insert(0,100)
a.insert(4,12)

a.insert(1000,2)
print(a)

# extend
print("----------------------extend---------------------")
a = [1,2,3]
b = [5,6,7]
b.extend(a)
a.extend(b)
b.extend(b)

print(a)
print(b)

#concat(+)
print("-----------------concat--------------------------")
a= [1,2,4]
b= [5,6,7]

print(a+b+a+b+a)
c = a+b+b+a
print(a,b)

print("--------"*10)
my_list = [10,25.4, "python", 34,56.4,"Django",100,9.9,"Nepal",2026]

del my_list[1]
print(my_list)

#pop
print("-----------------pop-------------------------")
data = my_list.pop(4)
print(my_list)
print(data)

data = [4,1,3,2,3,4]
pop_data = data.pop(1)
print(data)

print(pop_data)

# data = []
# data.pop() #error
# print(data)

#remove
print("-----------------remove-------------------------")
my_list = [10,25.4, "python", 34,10,56.4,"Django",100,9.9,"Nepal",2026]
my_list.remove(10)
print(my_list)

# clear
print("-----------------clear-------------------------")
my_list.clear()
print(my_list)

#count
print("----------------------count--------------------------")
a = [1,2,4,35,6,7,6,99,4]
print(a.count(4))

#reverse
print("----------------------reverse-------------------------")
print(a.reverse())

print("-------------sort----------------")
a.sort()
print(a)
a.sort(reverse=True)
print(a)


print("---------------list-------------------")
data = [1,2,3,4,5,6,[4,5,6,7,8,99,90,6]]
print(len(data))


print(data[6][4])
print(data[-1][-2])

c = data[6]
print(c[-2])

