# exercise 04-04
'''
student name: Eda
ID: 201810701580031
class: network182
'''


i = 3
done = False
print("Program to Change Password");
print("Your password has expired and you have " + str(i) + " chances left to change your password")
while i > 0 and not done:
    newPsw = input("Please enter your new password: ")
    pswEntered = input("Please enter password to confirm:")
    if newPsw == pswEntered:
        done = True
    else:
        print("Error in entering password, please try again")
        i -= 1
        print("You have "+ str(i) + " changes left")
if i <= 0:
    print("Password not changed")
else:
    print("Password accepted!")