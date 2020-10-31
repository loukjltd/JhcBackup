#Exercise 02-06
'''
student name :Vicky
ID:201810701580032
class:Net182
'''

num1 = 2
num2 = 7

print("Arithmetic operations")
print("Number 1: " + str(num1) + " and Number 2: " + str(num2))
print()

answer = num1 + num2
print("Addition: " + str(num1) + " + " + str(num2) + " = " + str(answer))


answer =num1 - num2
print("Subtraction: " + str(num1) + " - " + str(num2) + " = " + str(answer))

answer = num1 * num2
print("Multiplication:"+str(num1) +" *"+str(num2)+" = "+str(answer))


answer = num1/ num2
print("Division: " + str(num2) + " /" + str(num1) + " = " + str(answer))

answer=num2 % num1
print("Remainder of " + str(num2) + " % " + str(num1) + " = " + str(answer))

print("Division when using double data types")
num3 = 2.0
num4 = 7.0

answer2=num4 / num3

print("Division: " + str(num4) + " div " + str(num3)  + " = " + str(answer2))

answer2=num4 % num3

print("Remainder of "+str(num3)+" mod "+str(num4)+"="+str(answer2))
