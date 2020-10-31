# Exercise 04-04
'''
Student Name: Sean
ID: 201810701580042
Class: Network 182
'''

i = 3
done = False

print("Program to Change Password.")
print("Your password has expired and you have " + str(i) + " chances left to change your password.")


while done != True and i > 0:
    newPsw = input("Please enter your new password: ")
    pswEntered = str(input('Please enter your password again: '))
    if newPsw == pswEntered:
        done = True
    else:
        print("Error in entering password, please try again.")
        i -= 1
        print('You have ' + str(i) + ' times left.')

if i <= 0:
    print("Password not changed.")
else:
    print("Password accepted!")
