#Question 2
#Josh net182 201810701580043

rad = float(input('Enter a radius: '))
pai = 3.1416
print('{0:<10}{1:<10}{2}'.format('Radius', 'Area','Perimeter'), '\n-------------------------------')
print('{0:<10}{1:<10.2f}{2:.2f}'.format(rad, rad**2*pai, rad*2*pai))