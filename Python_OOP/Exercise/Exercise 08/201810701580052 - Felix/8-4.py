# Exercise 08-04
'''
student name: felix
#ID: 201810701580052
#class: net182
'''

class person:
    def __init__(self,name,age):
        self.__name = name
        self.__age = age
    def message(self):
        print('Hello')
    def details(self):
        return self.__name

sam = person('Sam',20)

print(sam._person__name)

james = person('James',21)


