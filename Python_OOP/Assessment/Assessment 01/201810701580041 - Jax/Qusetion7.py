# Qusetion7
'''
Student Name: Jax
ID: 201810701580041
Class: Net 182
'''

print('separated by commas')
a=input('Enter the first line of numbers separated by commas: ')
b=input('Enter the second line of numbers separated by commas: ')
c=[]
d=[]
cout=0
for i in a.split(','):
    c.append(float(i))
for f in b.split(','):
    d.append(float(f))
for i in c:
    for f in d:
        if i==f:
            cout+=1
print('There are ' + str(cout) +' numbers that are in both lists')