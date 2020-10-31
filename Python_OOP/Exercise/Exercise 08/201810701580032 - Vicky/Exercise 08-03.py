#Exercise 08-03
'''
student name :Vicky
ID:201810701580032
class:Net182
'''

class Person:
    name = ""
    age= 0

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def message(self):
        print("Hello")

    def details(self):
        print("My name is {}".format(self.name)," and I am {0}".format(self.age) , "years old.")

sam = Person("Sam",20)
sam.message()
sam.details()

james = Person("Jams",21)
james.message()
james.details()
