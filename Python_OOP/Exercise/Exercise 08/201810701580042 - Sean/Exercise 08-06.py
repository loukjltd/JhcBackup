# Exercise 08-06
'''
Student Name: Sean
ID: 201810701580042
Class: Network 182
'''


class Person:

    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value == '':
            print('Error - name is wrong')
        else:
            self.__name = value

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if value < 0 or value > 100:
            print('Error - age is wrong')
        else:
            self.__age = value


sam = Person('Sam', 20)
print(sam.name)
sam._Person__age = 30
print(sam.age)
sam.age = 130
print(sam.age)
