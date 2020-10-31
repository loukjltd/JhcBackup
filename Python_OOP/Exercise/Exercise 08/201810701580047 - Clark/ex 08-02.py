# Exercise 08-02
'''
name:Clark
class:net182
I  D:201810701580047
'''
class Person:
    name = ''
    age = 0

    def message(self):
        print('Hello')

    def details(self):
        print('my name is', self.name, 'and i am', self.age, 'year old')


Sam = Person()
Sam.name = 'Sam'
Sam.age = 20
James = Person()
James.name = 'James'
James.age = 21
Sam.message()
Sam.details()
James.message()
James.details()
