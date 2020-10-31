# Exercise 10-01
'''
name:Clark
class:net182
I  D:201810701580047
'''
class Person:

    def __init__(self, name):
        self.name = name

    def greeting(self):
        print('Hello')

    def display_info(self):
        print('Name:', self.name)


class Customer(Person):

    def __init__(self, name , age):
        Person.__init__(self, name)
        self.age = age

    def greeting(self):
        print("Dear customers, I am %d years old" % self.age)


customer = Customer('John Smith', 20)
customer.greeting()
customer.display_info()
