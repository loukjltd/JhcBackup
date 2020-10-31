#Exercise 03-01
'''
name: Assass
idnumber: 201810701580040
class: network 182
'''
print("Program to show high and low numbers")

# Get input and calculate number
num1=int(input("Enter a number:"))

if num1 > 50:
    print(str(num1) + " is a high number")

if num1 < 50:
    print(str(num1) + " is a low number")

if num1 == 50:
    print(str(num1)," is in the middle")
