#
'''
class:net182
name:lenny
ID:201810701580045
'''
class person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def message(self):
        print('Hello')

    def details(self):
        print('My name is {0}'.format(self.name) + ' and I am {0}'.format(self.age)  + ' years old')

Sam = person('Sam',20)
Sam.message()
Sam.details()

James = person('James',21)
James.message()
James.details()
