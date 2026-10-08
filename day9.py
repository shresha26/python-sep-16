#tuples and set

#tuple
a = (1,2,3,4,5,6,7)
print(a)
print(len(a))
print(type(a))

print(a[0])

#print(a[-40])
print(a[-4])

#a[0]=20
#print(a)

a = list(a)

print(a)
a[0]=20
print(a)

a=tuple(a)
print(a)


#set

a = [7,1,2,1,3]
a = list(set(a))
a.remove(1)
print(a)

#sort and sorted
data = [1,234,45,67,44,77,88]
data.sort()
print(data)

result = sorted(data)
print(data)
print(result)
