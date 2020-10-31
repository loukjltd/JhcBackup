#Exercise 04-010
'''
name: Jax
idnumber: 201810701580041
class: net182
'''

number=int(input('Enter the number for the times table: '))
for i in range(1, number):
    for j in range(1, number+1):
        print('{}\t'.format(i*j), end='\t')
    print()
