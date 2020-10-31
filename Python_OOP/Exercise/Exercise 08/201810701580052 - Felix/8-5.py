# Exercise 08-05
'''
student name: felix
#ID: 201810701580052
#class: net182
'''


class person:
    def __init__(self,name,age):
        self.__name = name
        self.__age = age
    def get_name(self):
        return self.__name


    def set_name(self,value):
        if value == '':
            print('Error - name is wrong')
        else:
            self.__name = value

    def get_age(self):
        return self.__age
    def set_age(self,value):
        if value < 0 or value > 100:
            print("Error - age is wrong")
        else :
            self.__age = value

    def message(self):
        print('Hello')
    def details(self):
        return self.__name

    name = property(get_name, set_name)
    age = property(get_age, set_age)

sam = person('Sam',20)
print(sam.name)

sam.age = 30
print(sam.age)

sam.age = 130
print(sam.age)



james = person('James',21)