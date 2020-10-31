#Exercise 04-04
'''
Name:Lester
ID:201810701580055
Class:Net 182
'''

i = 3
done = False
print("Program to Change Password")
print("Your password has expired and you have " + str(i) + " chances left to change your password")
while i > 0:
    newPsw = input("Please enter your new password: ")
    pswEntered = input("Please enter password again to confirm ;")
    if newPsw == pswEntered:
        done = True
    else:
     print("Error in entering password, please try again")
     i = i - 1
     print("You have" + str(i) + "chances left")
if i == 0:
    print("Password not changed")
else:
    print("Password accepted!")
