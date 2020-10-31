#Exercise 10-03
"""
class:Net182
name:vivi
id:201810701580049
"""
class Person:

    def __init__(self,name):
        self.name = name

    def greeting(self):
        print("Hello")

    def display_info(self):
        print("Name:" + self.name)

class Customer(Person):
    def __init__(self,name,age):
        Person.__init__(self,name)
        self.age = age

    def greeting(self):
        print("Dear customers,I am {0} years old".format(self.age))

customer = Customer("John Smith","20")
customer.greeting()
customer.display_info()
