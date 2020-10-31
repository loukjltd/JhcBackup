#exercise 08-04
'''
studentname:Faker
studentid:201810701580048
class:net182
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
