# Exercise 04-04
'''
student name: felix
#ID: 201810701580052
#class: net182
'''
i = 3
done = False

print("Program to Change Password");
print("Your password has expired and you have " + str(i) + " chances left to change your password")

while not done  and i > 0:
    newPsw = input("Please enter your new password: ")
    pswEntered = input()
    if newPsw == pswEntered:
        done  = True
    else:
        print("Error in entering password, please try again")
        i -= 1
        print('you have '+ str(i) +' chances left')
if i <= 0:
    print("Password not changed")
else:
    print("Password accepted!")
