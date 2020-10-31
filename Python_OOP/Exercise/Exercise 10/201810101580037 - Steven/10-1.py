# exercise10-01
'''
student name: Steven
ID: 201810101580037
class: network 182
'''
class Person:

    def __init__(self, name):
        self.name = name
    def greeting(self):
        print("Hello")
    def display_info(self):
        print("Name:",self.name)

class Customer(Person):

    def __init__(self,name,age):
        Person.__init__(self,name)
        self.age = age
    def greeting(self):
        print("Dear customers, I am ",self.age,"years old")

cs1 = Customer("John Smith",20)
cs1.greeting()
cs1.display_info()
