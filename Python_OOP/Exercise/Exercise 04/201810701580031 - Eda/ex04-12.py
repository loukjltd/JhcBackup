# exercise 04-12
'''
student name: Eda
ID: 201810701580031
class: network182
'''

for i in range(8):
    for j in range(0,7 - i):
        print(' ',end='')

    for k in range(0,(2 * i + 1)):
        print('*',end='')
    print( )

for i in range(7):
    for j in range(0,i+1):
        print(" ", end="")
    for k in range(0, (2*(7-i) - 1)):
        print("*", end="")
    print()