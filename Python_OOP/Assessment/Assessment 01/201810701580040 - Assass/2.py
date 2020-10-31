'''
Class:Net182
Name:Assass
ID:201810701580040
'''
r=float(input('Enter a radius:'))
p=3.1416
template = '{0:12}{1:12}{2:12}'
template1 = '{0:12}{1:12}{2:12}'
r1=template.format('Radius','Area','Perimeter')
print(str(r1))
print('---------------------------------')
a= r*r*p
d= 2*r*p
r2=template1.format(str(r),str('%.2f' % a),str('%.2f' % d))
print(str(r2))
