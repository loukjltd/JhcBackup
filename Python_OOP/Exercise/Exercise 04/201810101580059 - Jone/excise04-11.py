# Exercise 04-11
'''
Student Name: jone
ID: 201810101580059
Class: Network 182
'''
print('M\tT\tM\tW\tF\tS\tSu')
a=-6
b=1
for i in range(0,5):
    a+=7
    b+=7
    for j in range(a,b):
        if j <= 31:
            print(j,end='\t')
        else:
            break
    print()

