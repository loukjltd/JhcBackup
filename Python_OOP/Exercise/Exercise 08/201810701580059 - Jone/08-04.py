'''
student name: jone
#ID: 201810701580059
#class: net182
'''


class Person:
    def __init__(self,name,age):
        self.__name = name
        self.__age = age




myPerson = Person("Sam",20)
#print(myPerson._Person__age)
myPerson._Person__name = "Sam"
print(myPerson._Person__name)
