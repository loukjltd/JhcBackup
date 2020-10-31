#Exercise 03-04
'''
name: Ted
idnumber: 201810701580058
class: net182
'''


age=int(input('enter a agge :'))
if age<0:
    print('you are not human.')
elif age<2 and age>0:
    print('You are a baby.')
elif age<13:
    print('You are a child.')
elif age<20:
    print('You are a teenager.')
else:
    print('You are an adult.')