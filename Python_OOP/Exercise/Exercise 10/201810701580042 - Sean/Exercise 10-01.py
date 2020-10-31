# Exercise 10-01
'''
Student Name: Sean
ID: 201810701580042
Class: Network 182
'''


class Person:
    def __init__(self, name):
        self.name = name

    def greeting(self):
        print('Hello')

    def display_info(self):
        print('Name: ' + str(self.name))


class Customer(Person):

    def __init__(self, name, age):
        Person.__init__(self, name)
        self.age = age

    def greeting(self):
        print('Dear customers, I am ' + str(self.age) + ' years old.')


customer1 = Customer('John Smith', 20)
customer1.greeting()
customer1.display_info()
