# Exercise 08-03
'''
student name: felix
#ID: 201810701580052
#class: net182
'''
class person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def message(self):
        print('Hello')
    def details(self):
        print('My name is {0} and I am {1} years old'.format(self.name,self.age))

sam = person('Sam',20)
sam.message()
sam.details()

james = person('James',21)
james.message()
james.details()
