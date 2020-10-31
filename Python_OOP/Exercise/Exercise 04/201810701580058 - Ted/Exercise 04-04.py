#Exercise 04-04
'''
name: Ted
idnumber: 201810701580058
class: net182
'''

i = 3   # counter for number of logins
done=False

print("Program to Change Password")
print("Your password has expired and you have " + str(i) + " chances left to change your password")

# While password is not entered correctly AND more than 0 chances
while done==False and i>0:
    newPsw = int(input("Please enter your new password: "))
    pswEntered=int(input('Please enter your new password: '))
    # change password correct
    if newPsw==pswEntered:
        done=True
    else:
        print("Error in entering password, please try again")
        i-=1
        print('you have '+str(i)+' chance')

if i<=0:
    print("Password not changed") # password accepted
else:
    print("Password accepted!")
