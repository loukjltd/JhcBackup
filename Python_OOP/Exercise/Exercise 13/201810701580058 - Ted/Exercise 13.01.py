# Exercise 013-01
'''
Student Name: Ted
ID: 201810701580058
Class: Network 182
'''

def a(x):
    if x>10:
        print('Finished!')
    else:
        print(x)
        x+=1
        a(x)
a(1)