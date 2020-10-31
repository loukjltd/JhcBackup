# exercise08-03
'''
student name: Steven
ID: 201810101580037
class: network 182
'''
class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def message(self):
        print("Hello")
    def details(self):
        print("My name is",self.name,"and I am",self.age,"years old.")

sam = Person("Sam",20)
sam.message()
sam.details()

james = Person("James",21)
james.message()
james.details()
