# Exercise 08-05
'''
name:Clark
class:net182
I  D:201810701580047
'''


class Person:
    def __init__(self, name, age):
        self.set_name(name)
        self.set_age(age)

    def get_name(self):
        return self.__name

    def set_name(self, value0):
        if value0 == '':
            print('Error - wrong name')
        else:
            self.__name = value0

    def get_age(self):
        return self.__age

    def set_age(self, value):
        if value < 0 or value > 100:
            print('Error - wrong age')
        else:
            self.__age = value

    age = property(get_age, set_age)
    name = property(get_name, set_name)


Sam = Person('Sam', 30)
print(Sam.name)
print(Sam.age)
Sam.age = 130
print(Sam.age)
