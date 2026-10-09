def test_func():
    a = 100
    return 100,90

print(test_func())
print(test_func())
print(test_func())
print(test_func())
print(test_func())
print(test_func())
print(test_func())
print(test_func())
print(test_func())
print(test_func())
print(test_func())


def random():
    data = 0.5
    return data

result = random()
print("------",result)


def add(a,b):
    c=a+b
    return c

print(add(1,1))
print(add(77,33))


def return_two_data():
    return "hello","testing"

print(return_two_data)
a,b = return_two_data()
print(a,b)



def student_info(name, total_marks):
    no_of_subject = 5
    percent = total_marks/no_of_subject
    return name, percent

name,percent = student_info("Ramesh",355)

print("name",name)
print("percent",percent)

def add_numbers(numbers):
    if isinstance(numbers, list):
        return "Please provide list"
    total = 0
    for i in numbers:
        total = total + i
    return total
    
result = add_numbers([1,2,3,4,5,5])
print(result)
result = add_numbers([14,25,378])
print(result)

def merge_list(list1, list2):
    list1.extend(list2)
    return list1

print(merge_list(['a','b','c','d','e'],[1,2,3]))
print(merge_list(list2=['a','b','c','d','e'],list1=[1,2,3]))

[1,2,3,'a','b','c','d']


def find_max_number(numbers):
    max_number = 0
    for i in numbers:
        if i > max_number:
            max_number = i
    return max_number
    ...

print(find_max_number([80,13,414,343,235,222]))
