#exercise 08-01
'''
studentname:shrek
studentid:201810101580038
class:net182
'''


class person:
    name =''
    age=0
sam=person()
sam.name='Sam'
sam.age=20

james=person
james.name='James'
james.age=21
print(str(sam.name) + ' is ' + str(sam.age))
print(str(james.name) + ' is ' + str(james.age))