# data access modifier / abstraction
class Test():

    a = 100 # public attrs
    __data = "hello world" # private attrs
    b = __data + " modified"


obj = Test()
print(obj.a)
print(obj.b)



class Test2():

    a = 100 # public attrs
    __data = "hello world" # private attrs
    b = __data + " modified"

    def display(self):
        return "Public attrs"

    def __display2(self):
        return "Private"

obj = Test2()
print(obj.display())
# print(obj.__display2())




class Test3():

    a = 100 # public attrs
    __data = "hello world" # private attrs
    b = __data + " modified"

    def display(self):
        return "Public attrs"

    def __display2(self):
        return "Private"


class Test4(Test3):
    def result(self):
        return self.__data
        return self.__display2(), "result"

obj = Test4()
# print(obj.result())


class Patient():
    patient_name = "Hari"
    __medical_history = "Fever"
    __blood_group = "+B"


    def patient_info(self):
        return f'Patient Name = {self.patient_name} history = {self.__medical_history} blood_group = {self.__blood_group}'



class GeneralPatient(Patient):
    room_no = 343
    addmission_days = 22



    def display(self):
        return f'{self.patient_info()} room_no = {self.room_no}'
        ...

obj = GeneralPatient()
print(obj.display())