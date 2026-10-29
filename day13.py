# area_of_circle_2 =  lambda r, pie:  pie*r*r

# print(area_of_circle_2(7,3.14))


# square = lambda a: a**3
# print(square(4))



# a = [1,2,3,4,5,6]
# result = []
# for i in a:
#     result.append(i**2)

# print(result)

# result = [i**2 for i in a]
# print(result)



# square = lambda *args : [i**2 for i in args]

# print(square(1,2,3,4))
# print(square(100,333,12,11))


class Test():
    a = 10
    b = 11


obj = Test()

obj1 = Test()

obj1.a = 100
obj1.c = "from obj1"
print(obj1.a)
print(obj1.c)

# print(obj, "<=====>" ,obj1)
print(obj.a)
print(obj.b)

# print(obj.c)




class Test2():
    a = 44
    b = 6

    def add(self):
        return self.a+self.b


    def sub(self):
        return self.a-self.b

obj = Test2()
print(obj.a)
print(obj.sub())




print("------"*10)
class Test3():

    def __init__(self,data):
        self.a = data-1
        print("from init function",data)
        return


obj = Test3(10)

print(obj.a)