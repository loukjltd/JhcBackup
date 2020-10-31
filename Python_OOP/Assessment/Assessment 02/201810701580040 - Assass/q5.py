'''
class:net182
name:Assass
id:201810710580040
'''
a=input('Enter a list of numbers separated by commas: ')
f=open('./some_numbers.txt','w')
f.write(a)
f.close()
f=open('./some_numbers.txt','r')
line_of_numbers = f.readline()
l=line_of_numbers.split(',')
m=0
s=0
for i in l:
    print(i)
    s+=int(i)
    if int(i)>=m:
        m=int(i)
print('Sum: '+str(s))
print('Maximum:'+str(m))