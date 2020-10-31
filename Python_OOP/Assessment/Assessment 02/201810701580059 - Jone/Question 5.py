# Qusetion 5
'''
Student Name: jone
ID: 201810701580059
Class: Network 182
'''
a=input('Enter a list of numbers separated by commas: ')
list=[]
f=open('./some_number.txt','w')
f.write(a)
f.close()
f=open('./some_number.txt','r')
line_of_numbers=f.readline()
max=0
b=0
for i in line_of_numbers.split(','):
    list.append(i)
for i in list:
    print(i)
    b+=int(i)
    if int(i)>int(max):
        max=i
print('Sum: '+str(b))
print('Maximum: '+max)

