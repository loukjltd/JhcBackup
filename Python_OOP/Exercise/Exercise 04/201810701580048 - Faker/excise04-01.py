# Exercise 04-01
'''
Student Name: Faker
ID: 201810701580048
Class: Network 182
'''

correctPsw = 1111
pswEntered = 0

print("Program to Check Password")

while pswEntered != correctPsw:
    pswEntered = int(input("Please enter password: "))

print("Password accepted!")
