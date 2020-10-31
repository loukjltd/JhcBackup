#exercise 04-01
'''
name:Lee
class:net182
'''

correctPsw = 1111
pswEntered = 0

print("Program to Check Password")

while pswEntered != correctPsw:
    pswEntered = int(input("Please enter password: "))

print("Password accepted!")
