# exercise 02-04
'''
student name: Eda
ID: 201810701580031
class: network182
'''

animal = input("Enter an animal: ")
print(animal)
print()

num1 = input("Enter the first number: ")
num2 = input("Enter the second number:")
Answer = int(num1) + int(num2)
print(Answer)

length = input('Enter the length of the rectangle: ')
width = input('Enter the width of the rectangle: ')
Area =  float(length) * float(width)
Perimeter = 2*(float(length) + float(width))
print('Arae = '+ str(Area))
print('Perimeter = '+ str(Perimeter))
print()

r = input('Enter the radius of the circle: ')
Area = float(r) * float(r) * 3.14
print('Area = '+str(Area))