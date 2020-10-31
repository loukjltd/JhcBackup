# Exercise 08-04
'''
Student Name: Sean
ID: 201810701580042
Class: Network 182
'''


class Person:

    def __init__(self, name, age):
        self.__name = name
        self.__age = age


sam = Person('Sam', 20)
sam._Pet__name = 'Sam'
print(sam._Person__name)
print(sam.name)
