# Exercise 08-01
'''
name: King
idnumber: 201810701580054
class: net182
'''
class Person:
    name=''
    age=0
sam=Person()
sam.name='Sam'
sam.age=20
james=Person()
james.name='James'
james.age=21
print('Sam is '+str(sam.age))
print('James is '+str(james.age))