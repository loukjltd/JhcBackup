# Exercise 08-04
'''
name: King
idnumber: 201810701580054
class: net182
'''
class Person:
    def __init__(self,name,age):
        self.__name=name
        self.__age=age
    def message(self):
        print('Hello')
    def details(self):
        print('My name is ' +str(self.__name)+ ' and I am {0} years old.'.format(self.__age))
sam=Person('Sam',20)
#print(sam.name)
print(sam._Person__name)
james=Person('James',21)
