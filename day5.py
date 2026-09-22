# list 
#append

a = [1,2,3,4]
a.append("test")
print(a)

data = 2
a = []
a.append(data)
print(a)

# insert
a = [1,2,3,4,5,6]

a.insert(0,100)
a.insert(4,12)

a.insert(1000,2)
print(a)

# extend

a = [1,2,3]
b = [5,6,7]
b.extend(a)
a.extend(b)
b.extend(b)

print(a)
print(b)

#concat(+)
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

data = my_list.pop(4)
print(my_list)
print(data)

#remove
my_list = [10,25.4, "python", 34,10,56.4,"Django",100,9.9,"Nepal",2026]
my_list.remove(10)
print(my_list)

# clear

my_list.clear()
print(my_list)

#count

a = [1,2,4,35,6,7,6,99,4]
print(a.count(4))

#reverse

print(a.reverse())
a.sort()
print(a)
a.sort(reverse=True)
print(a)