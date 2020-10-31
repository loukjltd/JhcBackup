# exercise 10-01
'''
student name: Eda
ID: 201810701580031
class: network182
'''

class Person:

    def __init__(self, name):
        self.name = name

    def greeting(self):
        print('Hello')
    def display_info(self):
        print('Name: ' + str(self.name))
class Customer(Person):
    def __init__(self,name,age):
        Person.__init__(self,name)
        self.age = age
    def greeting(self):
        print('Dear customers, I am ' + str(self.age) +' years old')
cus = Customer('John Smith',20)
cus.greeting()
cus.display_info()