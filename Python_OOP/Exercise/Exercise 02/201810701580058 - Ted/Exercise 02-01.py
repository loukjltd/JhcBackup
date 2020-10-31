#Exercise 02-01
'''
name: Ted
#idnumber: 201810701580058
#class: net182
'''


meal=44.5
x=6.75
y='%'
tax=str(x)+y
x1=15
tip=str(x1)+y
a=float(meal)*float(x/100)
total =float(meal)*float(x1/100)+float(meal)
b=round(a+total,2)
z='$'
c=z+str(b)
print('Total cost of meal: '+str(c))
