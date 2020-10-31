# Exercise 04-10
'''
Student Name: Faker
ID: 201810701580048
Class: Network 182
'''
counts = int(input('enter the number for the times table: '))
for i in range(1,counts+1):
    for j in range(1,counts+1):
        print(i*j,end='\t')
    print()
