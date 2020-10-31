#Exercise 02-01to02-07
#Josh net182 201810701580043

#02-01
meal = 44.50
tax = 0.0675
tip = 0.15
meal += meal * tax
total = meal + meal * tip
print("Total cost of meal: ${0:.2f}".format(total))
#02-02
x = "23.556"
y = 6.26
z = 5
print(float(x)+y+z)
#02-03
message = "Hello, I am "
age = 20.523
print(message+str(int(age)),'years old')
#02-04
x = 10.0
y = 3.0
i = 5
j = 5

i = int(x + y)
x = j
print('i=',i,'x=',x)
#02-05
add1 = "Five "
num1 = "5"
plus = "plus "
add2 = "seven "
num2 = "7"
equals = "equals "

print(add1+plus+add2+equals+str(float(int(num1)+int(num2))))
#02-06
num1 = 2
num2 = 7
print("Arithmetic operations")
print("Number 1: " + str(num1) + " and Number 2: " + str(num2))
print()

answer = num1 + num2
print("Addition: " + str(num1) + " + " + str(num2) + " = " + str(answer))

answer = num1 - num2
print("Subtraction: " + str(num1) + " - " + str(num2) + " = " + str(answer))
#02-07
animal = input('Enter an animal: ')
print(animal)

first_number = input('Enter the first number: ')
second_number = input('Enter the second number: ')
print('Answer =', first_number + second_number)

length = float(input('Enter the length of the rectangle: '))
width = float(input('Enter the width of the rectangle: '))
print('Area =', length * width)
print('Perimeter =', 2 * (length + width))

radius = float(input('Enter the radius of the circle: '))
print('Area =', radius * radius * 3.14)