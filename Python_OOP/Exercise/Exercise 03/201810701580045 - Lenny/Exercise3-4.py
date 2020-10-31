#Exercise3-4
'''
student name:Lenny
ID:201810701580045
class: network 182
'''

age = int(input('Enter your age: '))

if age < 2 and age > 0:
    print('You are a baby')

elif age >= 2 and age < 13:
    print('You are a child')

elif age >= 13 and age < 20:
    print('You are a teenager')

elif age <= 0:
    print('The age is wrong')

else:
    print('You are an adult')