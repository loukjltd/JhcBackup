# exercise 10-01
'''
student name: Yakira
ID: 201810701580034
class: network182
'''
class Person:

    def __init__(self, name):
        self.name = name
    def greeting(self):
        print("Hello")
    def display_info(self):
        print("Name: {0}".format(self.name))
class Customer(Person):
    def __init__(self,name,age):
        Person.__init__(self,name)
        self.age = age
    def greeting(self):
        print("Dear customers, I am {}".format(self.age),"years old")

cs1 = Customer("John Smith",20)
cs1.greeting()
cs1.display_info()