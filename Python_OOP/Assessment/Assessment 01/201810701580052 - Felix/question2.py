radius =  float(input('Enter a radius: '))
u = 3.1416
area = radius*radius*u
perimeter = radius*2*u

r1 = '{0:<15}{1:<15}{2:>10}'
w1 = r1.format('Radius','Area','Perimeter ')
r2 = '{0:<15.2f}{1:<15.2f}{2:>5.2f}'
w2 = r2.format(radius,area,perimeter)

print(w1)
print('- - - - - - - - - - - - - - - - - - - -')
print(w2)