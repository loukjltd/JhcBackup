# exercise08-04
'''
student name: Steven
ID: 201810101580037
class: network 182
'''
class Person:
    def __init__(self,name,age):
        self.__name = name
        self.__age = age

myPerson = Person("Sam",20)
myPerson._Person__name = "Sam"
print(myPerson._Person__name)
