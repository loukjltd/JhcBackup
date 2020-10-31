'''
Student name: Luis Zhou
Student ID: 2018100701580033
Pledge of Honour: I pledge by honour that this program is solely my own work.
'''
d={}
r=float(input('please enter the radius:'))

d['Radius'] = str(r)
d['Area'] = r**2*3.1416
d['Perimeter'] =str(2*r*3.1416)
print('Enter a radius: '+str(r))
print("{0:<5}{1:>10}{2:>15}".format('Radius','Area','Perimeter'))
print("--------------------------------------")
print("{0:<5}{1:>10}{2:>15}".format(d['Radius'],d['Area'],d['Perimeter']))

