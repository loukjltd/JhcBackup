# Exercise 04-10
'''
Student Name: shrek
ID: 201810101580038
Class: Network 182
'''
counts = int(input('enter the number for the times table: '))
for i in range(1,counts+1):
    for j in range(1,counts+1):
        print(i*j,end='\t')
    print()