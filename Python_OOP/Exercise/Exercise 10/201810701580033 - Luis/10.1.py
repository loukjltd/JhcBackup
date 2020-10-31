


# exercise 10-01
'''
student name: Luis
ID: 201810701580033
class: network182
'''

class Person:

    def __init__(self, name):
        self.name = name

    def greeting(self):
        return 2

    def greeting(self):
        print("Hello")

    def display_info(self) :
        print( "Name:" + self.name)


class Customer(Person):

    def __init__ (self,name,age):
     Person.name=name
     Person.age=age

    def greeting(self) :
        print("Dear customers, I am "+str(self.age)+"years old")


smith=Customer("John Smith",20)
smith.greeting()
smith.display_info()

