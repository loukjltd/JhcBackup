# exercise 04-01
'''
name:Lenny
class:net182
ID:201810701580045
'''

correctPsw = 1111
pswEntered = 0

print("Program to Check Password")

while pswEntered != correctPsw:
    pswEntered = int(input("Please enter password: "))

print("Password accepted!")

