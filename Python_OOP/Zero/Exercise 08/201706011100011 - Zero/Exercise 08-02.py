#Net171 ZEERO
class Person:
    name=""
    age=0
    def message(self):
        print("Hello")
    def details(self):
        print("My name is {0} and I am {1} years old.".format(self.name,self.age))

sam=Person()
sam.name="sam"
sam.age=20

James=Person()
James.name="James"
James.age=21

sam.message()
sam.details()
James.message()
James.details()