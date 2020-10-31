# exercise 08-06
'''
student name: Eda
ID: 201810701580031
class: network182
'''

class Person:

    def __init__(self,name,age):
        self.__name = name
        self.__age = age

    def message(self):
        print('Hello')

    def details(self):
        print('My name is ' + self.__name + ' and I am ' + str(self.__age) + ' years old.')

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self,value):
        if value == "":
            print("error name")

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self,value):
        if value < 0 or value > 100:
            print("error message")
        else:
            self.__age = value

sam = Person("Sam",20)
james = Person("James",21)
sam.name = "Sam"
sam.age = 20
print((sam.name))
sam.age = 30
print(str(sam.age))
sam.age = 130
print(str(sam.age))