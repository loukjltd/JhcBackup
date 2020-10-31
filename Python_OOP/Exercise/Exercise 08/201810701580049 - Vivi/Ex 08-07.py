#Exercise 08-07
'''
class net182
id 2018100701580049
name vivi
'''
class Person:

    number_of_people = 0

    def __init__(self,name,age):
        self.__name = name
        self.__age = age
        Person.number_of_people += 1
        print("Added 1 person")


    @staticmethod
    def message():
        print("Hello")

    def details(self):
        print("My name is {0} and I am {1} years old".format(self.__name,self.__age))
    @classmethod
    def count_population(cls):
        print("There are {0} people".format(Person.number_of_people))
Person.message()
sam = Person("Sam",20)
Person.count_population()
james = Person("James",21)
Person.count_population()




