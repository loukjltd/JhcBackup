# Exercise 08-05
'''
Student Name: Sean
ID: 201810701580042
Class: Network 182
'''


class Person:

    def __init__(self, name, age):
        self.__name = name
        self.set_age(age)

    def get_name(self):
        return self.__name

    def set_name(self, value):
        if value == '':
            print('Error - name is wrong')
        else:
            self.__name = value

    def get_age(self):
        return self.__age

    def set_age(self, value):
        if value < 0 or value > 100:
            print('Error - age is wrong')
        else:
            self.__age = value

    name = property(get_name, set_name)
    age = property(get_age, set_age)


sam = Person('Sam', 20)
print(sam.name)
sam.set_age(30)
print(sam.age)
sam.set_age(130)
print(sam.age)
