#Exercise 04-010
'''
name: Ted
idnumber: 201810701580058
class: net182
'''

number=int(input('Enter the number for the times table: '))
for i in range(1, number):
    for j in range(1, number+1):
        print('{}\t'.format(i*j), end='\t')
    print()