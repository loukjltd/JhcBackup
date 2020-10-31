# Exercise 03-04
'''
name : vivi
class: net182
I D  : 201810701580049
'''
age = int(input('Enter your age:'))
if age > 0:
    if age < 20:
        print('You are a teenager')
        if age < 13:
            print('You are a child')
            if age < 2:
                print('You are a baby')
    else:
        print('You are an adult')
