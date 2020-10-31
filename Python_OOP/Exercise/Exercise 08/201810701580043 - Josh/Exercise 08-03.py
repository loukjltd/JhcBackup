#Exercise 08-03
#Josh net182 201810701580043

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def message(self):
        print('Hello')
    def details(self):
        print('My name is '+self.name+' and I am '+str(self.age)+' years old.')

sam = Person('Sam', 20)

james = Person('James', 21)

sam.message()
sam.details()
james.message()
james.details()