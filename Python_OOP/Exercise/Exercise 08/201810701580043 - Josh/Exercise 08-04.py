#Exercise 08-04
#Josh net182 201810701580043

class Person:
    def __init__(self,name,age):
        self.__name = name
        self.__age = age
    def message(self):
        print('Hello')
    def details(self):
        print('My name is '+self.__name+' and I am '+str(self.__age)+' years old.')

sam = Person('Sam', 20)

james = Person('James', 21)

print(sam._Person__name)