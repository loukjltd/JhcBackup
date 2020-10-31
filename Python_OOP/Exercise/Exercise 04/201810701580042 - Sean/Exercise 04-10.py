# Exercise 04-10
'''
Student Name: Sean
ID: 201810701580042
Class: Network 182
'''

times = int(input('Enter the number for the times table: '))
for i in range(1, times + 1):
    for j in range(1, times + 1):
        print(i*j, end='\t')
    print()
