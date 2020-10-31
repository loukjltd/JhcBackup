#Exercise 08-07
'''
student name :Vicky
ID:201810701580032
class:Net182
'''

class Person:
    number_of_perple = 0
    def __init__(self,name,age):
        self.__name = name
        self.__age = age
        Person.number_of_perple += 1
        print("Added 1 person")



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

def message():
        print('Hello')
def count_population():
        print("There are {0} people ".format(Person.number_of_perple))

message()
tim = Person("Tim",29)
count_population()
alice = Person("Alice",25)
count_population()
