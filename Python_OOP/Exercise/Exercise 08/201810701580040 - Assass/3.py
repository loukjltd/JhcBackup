'''
Class:Net182
Name:Assass
Id:201810701580040
'''
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def message(self):
        print('Hello')
    def details(self):
        print('My name is ' + self.name  + ' and I am ' + str(self.age) +  ' years old.')
sam=Person('Sam',20)
james=Person('James',21)
sam.message()
sam.details()
james.message()
james.details()
