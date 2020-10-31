#Exercise 08-03
'''
class net182
id 2018100701580049
name vivi
'''
class Person:

    def __init__(self,name,age):
        self.name = name
        self.age = age

    def message(self):
        print("Hello")

    def details(self):
        print("My name is {0} and I am {1} years old".format(self.name,self.age))

sam = Person("Sam",20)
james = Person("James",21)

sam.message()
sam.details()

james.message()
james.details()
