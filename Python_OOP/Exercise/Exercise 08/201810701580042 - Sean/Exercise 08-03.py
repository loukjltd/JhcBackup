# Exercise 08-03
'''
Student Name: Sean
ID: 201810701580042
Class: Network 182
'''


class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def message(self):
        print('Hello')

    def details(self):
        print('My name is ' + str(self.name) + ' and I am ' + str(self.age) + ' years old.')


sam = Person('Sam', 20)
sam.message()
sam.details()

james = Person('James', 21)
james.message()
james.details()
