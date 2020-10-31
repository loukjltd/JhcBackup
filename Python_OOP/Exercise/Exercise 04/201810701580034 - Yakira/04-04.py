# exercise 04-04
'''
student name : Yakira
ID : 201810701580034
class : Net182
'''
i = 3
done = False
print("Program to Change Password")
print("Your password has expired and you have " + str(i) + " chances left to change your password")
while not done and i > 0 :
    newPsw = input("Please enter your new password: ")
    pswEntered = input("Please enter password again to confirm: ")
    if newPsw == pswEntered :
        done = True
    else :
        print("Error in entering password, please try again")
        i -= 1
        print("you have ",i, "chances left")

if i <= 0 :
    print("Password not changed")  # password accepted
else:
    print("Password accepted!")
