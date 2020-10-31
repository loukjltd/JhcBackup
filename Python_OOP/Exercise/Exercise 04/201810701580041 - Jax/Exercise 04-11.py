#Exercise 04-011
'''
name: Jax
idnumber: 201810701580041
class: net182
'''

for i in ('M','T','W','T','F','S','Su'):
    print(i,end='\t')
print()
a=-6
b=1
for i in range(0,5):
    a+=7
    b+=7
    for j in range(a,b):
        if j<=31:
            print(j,end='\t')
        else:
            break
    print()
