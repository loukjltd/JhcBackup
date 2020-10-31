# exercise 08-03
'''
student name: Yakira
ID: 201810701580031
class: network182
'''
class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age



    def message(self):
        print("Hello")
    def details(self):
        print("My name is {} ".format(self.name), "and I am {0}".format(self.age), "years old.")

sam = Person("Sam",20)
sam.message()
sam.name = "Sam"
sam.age = 20
sam.details()

James = Person("James",21)
James.message()
James.name = "James"
James.age = 21
James.details()