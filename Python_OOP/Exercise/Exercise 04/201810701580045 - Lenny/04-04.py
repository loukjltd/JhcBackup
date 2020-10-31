# exercise 04-04
'''
name:Lenny
class:net182
ID:201810701580045
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