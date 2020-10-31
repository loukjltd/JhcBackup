# exercise 08 04
'''
Bro
201810701580056
network 182
'''
class Person:
    def __init__(self,name,age):
        self.__name =name
        self.__age =age
    def message(self):
        print('Hello')
    def __details(self):
        print('My name is ' + str(self.name) + ' and I am ' + str(self.age) + ' years old')
sam=Person('Sam',20)
#print(sam.name)
print(sam._Person__name)