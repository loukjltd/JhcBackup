#Exercise 04-01
'''
class:net182
name:vivi
id:201810701580049
'''

correctPsw = 1111 # set password
pswEntered = 0

print("Program to Check Password")

# check password
while pswEntered != correctPsw:
    try:
        pswEntered = int(input("Please enter password: "))
    except:
        print("Please enter a integer nunber!")

print("Password accepted!")
