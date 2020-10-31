#Exercise 03-01
'''
name: King
idnumber: 201810701580054
class: net182
'''

print("Program to show high and low numbers")

# Get input and calculate number
num1=float(input('please enter a number:'))

if num1 > 50:
    print(str(num1) + " is a high number")

elif num1<50:
    print(str(num1) + " is a low number")

else:
    print(str(num1)+" is in the middle")