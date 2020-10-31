#exercise 08-03
'''
studentname:shrek
studentid:201810101580038
class:net182
'''
class Person:
    def __init__(self,name,age):
        self.name =name
        self.age =age
    def message(self):
        print('Hello')
    def details(self):
        print('My name is ' + str(self.name) + ' and I am ' + str(self.age) + ' years old')
sam=Person('Sam',20)
sam.message()
sam.details()
james = Person('James',21)
james.message()
james.details()