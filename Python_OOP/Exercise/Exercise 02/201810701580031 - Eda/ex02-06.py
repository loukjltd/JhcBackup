# exercise 02-05
'''
student name: Eda
ID: 201810701580031
class: network182
'''

num1 = 2
num2 = 7

print("Arithmetic operations")
print("Number 1: " + str(num1) + " and Number 2: " + str(num2))
print()

answer = num1 + num2
print("Addition: " + str(num1) + " + " + str(num2) + " = " + str(answer))

answer = num1 - num2
print("Subtraction: " + str(num1) + " - " + str(num2) + " = " + str(answer))

answer = num1 * num2
print("Subtraction: " + str(num1) + " * " + str(num2) + " = " + str(answer))

num1 += 5

answer = num2 / num1
print("Division: " + str(num2) + " / " + str(num1) + " = " + str(answer))

answer = num2 % num1
print("Remainder of " + str(num2) + " % " + str(num1) + " = " + str(answer))

print("Division when using double data types")
num3 = 2.0
num4 = 7.0

answer2 = num4 / num3
print("Division: " + str(num4) + " div " + str(num3)  + " = " + str(answer2))

anser2 = num4 % num3
print("Remainder of " + str(float(num4)) + " mod " + str(float(num3))  + " = " + str(float(answer2)))