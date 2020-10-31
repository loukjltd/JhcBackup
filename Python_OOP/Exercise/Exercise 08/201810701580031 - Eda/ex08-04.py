# exercise 08-04
'''
student name: Eda
ID: 201810701580031
class: network182
'''

class Person:

    def __init__(self,name,age):
        self.__name = name
        self.__age = age

    def message(self):
        print('Hello')

    def details(self):
        print('My name is ' + self.__name + ' and I am ' + str(self.__age) + ' years old.')



sam = Person("Sam",20)
james = Person("james",21)
#print(sam.name)
print(sam._Person_name)

