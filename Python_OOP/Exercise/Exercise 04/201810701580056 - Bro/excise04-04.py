# exercise 04 04
'''
Bro
201810701580056
network 182
'''
i = 3
done = False
print("Program to Change Password")
print("Your password has expired and you have " + str(i) + " chances left to change your password")
while not done and i >0:
    newPsw = input("Please enter your new password: ")
    pasEntered = input("Please enter your new password again: ")
    if newPsw == pasEntered:
        done = True
    else:
        print("Error in entering password, please try again")
        i -= 1
        print("You have " + str(i) + " times left")
if i <= 0:
    print("Password not changed")
else:
    print("Password accepted!")