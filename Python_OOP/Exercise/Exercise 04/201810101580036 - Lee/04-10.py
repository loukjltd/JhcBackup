#exercise 04-10
'''
name:Lee
class:net182
'''

times = int(input('Enter the number for the times table: '))
for i in range(1, times + 1):
    for j in range(1, times + 1):
        print(i*j, end='\t')
    print()