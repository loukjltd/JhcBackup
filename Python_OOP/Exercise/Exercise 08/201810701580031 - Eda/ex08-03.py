# exercise 08-03
'''
student name: Eda
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
        print("My name is {} " .format(self.name),"and I am {} ".format(self.age),"years old")

sam = Person("Sam",20)
sam.message()
sam.details()

james = Person("James",21)
james.message()
james.details()