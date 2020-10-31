# Exercise 08-01
'''
name:Clark
class:net182
I  D:201810701580047
'''
class Person:
    name = ''
    age = 0


Sam = Person()
Sam.name = 'Sam'
Sam.age = 20
James = Person()
James.name = 'James'
James.age = 21
print(Sam.name, 'is', Sam.age, '\n' + James.name, 'is', James.age)
