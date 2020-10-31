# Exercise 04-01
'''
Student Name: Charlie
ID: 201810101580044
Class: Network 182
'''

correctPsw = 1111
pswEntered = 0

print("Program to Check Password")

while pswEntered != correctPsw:
    pswEntered = int(input("Please enter password: "))

print("Password accepted!")