'''
Student Name: Leo
ID: 201810701580053
Class: Network 182
'''
class Person:
    def __init__(self,name,age):
        self.__name=name
        self.__age=age
    def message(self):
        print('Hello')
    def details(self):
        print('My name is ' +str(self.__name)+ ' and I am {0} years old.'.format(self.__age))
    def get_name(self):
        return self.__name
    def set_name(self,value):
        if value=='':
            print('Error - wrong name')
        else:
            self.__name=value
    def get_age(self):
        return self.__age
    def set_age(self,value):
        if value<0 or value>100:
            print('Error - wrong age')
        else:
            self.__age=value
    name=property(get_name,set_name)
    age = property(get_age, set_age)
sam=Person('Sam',20)

james=Person('James',21)
sam.name='Sam'
sam.age=20
print(sam.name)
sam.set_age(30)
print(sam.get_age())
sam.set_age(130)
print(sam.get_age())
