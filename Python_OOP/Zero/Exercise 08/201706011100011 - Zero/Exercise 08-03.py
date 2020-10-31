#Net171 ZERO
class Person:

    def message(self):
        print("Hello")
    def details(self):
        print("My name is {0} and I am {1} years old.".format(self.name,self.age))

    def __init__(self,name,age):
        self.name=name
        self.age=age

sam=Person("Sam",20 )
James=Person("James",21 )

sam.message()
sam.details()
James.message()
James.details()