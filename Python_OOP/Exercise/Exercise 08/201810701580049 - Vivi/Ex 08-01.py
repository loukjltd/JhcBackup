#Exercise 08-01
'''
class net182
id 2018100701580049
name vivi
'''
class Person:
    name = ""
    age = 0

sam = Person()
sam.name = "Sam"
sam.age = 20

james = Person()
james.name = "James"
james.age = 21

print(sam.name + " is " + str(sam.age))
print(james.name + " is " + str(james.age))