#Exercise 08-01
#Josh net182 201810701580043

class Person:
    name = ''
    age = 0

sam = Person()
sam.name = 'Sam'
sam.age = 20

james = Person()
james.name = 'James'
james.age = 21

print(sam.name + ' is '+ str(sam.age))
print(james.name + ' is '+ str(james.age))