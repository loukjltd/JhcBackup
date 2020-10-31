# Qusetion5
'''
Student Name: Jax
ID: 201810701580041
Class: Net 182
'''

a=int(input('How many sensors are currently collecting data?:'))
b=list()
c=''
flag=0
cont=0
while flag<a:
    for v in range(1,a+1):
        c = float(input('Enter temperature ' + str(v) + ': '))
        b.append(c)
        flag+=1
for i in b:
    if i>10 and i<20:
        cont+=1
print('Average temperature: '+str(sum(b)))
print('Maximum temperature: '+str(max(b)))
print('Number of temperatures between 10 and 20: '+str(cont))