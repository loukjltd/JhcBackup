#Exercise 04-01
'''
name: Ted
idnumber: 201810701580058
class: net182
'''

correctPsw = 1111 # set password
pswEntered=int(0)
print("Program to Check Password")

# check password
while pswEntered!=correctPsw:
    pswEntered=int(input('Please enter password: '))

print("Password accepted!")
