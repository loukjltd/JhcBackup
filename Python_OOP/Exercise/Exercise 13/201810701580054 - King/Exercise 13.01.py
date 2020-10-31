# Exercise 013-01
'''
name: King
idnumber: 201810701580054
class: net182
'''

def a(x):
    if x>10:
        print('Finished!')
    else:
        print(x)
        x+=1
        a(x)
a(1)