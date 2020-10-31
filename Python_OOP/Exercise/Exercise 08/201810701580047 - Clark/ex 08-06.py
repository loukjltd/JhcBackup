# Exercise 08-06
'''
name:Clark
class:net182
I  D:201810701580047
'''


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value0):
        if value0 == '':
            print('Error - wrong name')
        else:
            self.__name = value0

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if value < 0 or value > 100:
            print('Error - wrong age')
        else:
            self.__age = value


Sam = Person('Sam', 30)
print(Sam.name)
print(Sam.age)
Sam.age = 130
print(Sam.age)
