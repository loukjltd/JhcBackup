#Exercise 08-05
'''
student name :Vicky
ID:201810701580032
class:Net182
'''

class Person:

    def __init__(self,name,age):
        self.__name = name
        self.__age = age

    def message(self):
        print('Hello')

    def details(self):
        print('My name is ' + self.__name + ' and I am ' + str(self.__age) + ' years old.')

    def get_name(self):
        return self.__name
    def set_name(self,value):
        if value == "":
            print("error name")



    def get_age(self):
        return self.__age
    def set_age(self,value):
        if value < 0 or value > 100:
            print("error message")
        else:
            self.__age = value

    name = property(get_name, set_name)
    age = property(get_age,set_age)

sam = Person("Sam",20)
james = Person("James",21)
sam.name = "Sam"
sam.age = 20
print(sam.get_name())
sam.set_age = (30)
print(str(sam.get_age()))
sam.set_age = (130)
print(str(sam.get_age()))
