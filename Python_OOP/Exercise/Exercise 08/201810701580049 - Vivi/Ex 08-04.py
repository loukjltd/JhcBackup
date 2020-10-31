#Exercise 08-04
'''
class net182
id 2018100701580049
name vivi
'''
class Person:

    def __init__(self,name,age):
        self.__name = name
        self.__age = age

    def message(self):
        print("Hello")

    def details(self):
        print("My name is {0} and I am {1} years old".format(self.__name,self.__age))

sam = Person("Sam",20)
james = Person("James",21)

# print(sam.name)

sam._Person__name = "Sam" #use _<class_name> to hack variable__name  notice:"__" need to use _ hack!!

print(sam._Person__name)