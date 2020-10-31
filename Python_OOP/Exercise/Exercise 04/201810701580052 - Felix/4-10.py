# Exercise 04-10
'''
student name: felix
#ID: 201810701580052
#class: net182
'''
num = int(input('please enter a number:'))
for i in range(1,num+1):
    for j in range(1,num+1):
        print(i*j,end = '\t')
    print()