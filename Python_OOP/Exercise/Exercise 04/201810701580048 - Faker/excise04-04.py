# Exercise 04-04
'''
Student Name: Faker
ID: 201810701580048
Class: Network 182
'''
# counter for number of logins
i = 3
done = False
print("Program to Change Password")
print("Your password has expired and you have " + str(i) + " chances left to change your password")
# While password is not entered correctly AND more than 0 chances
while not done and i >0:
    newPsw = input("Please enter your new password: ")
    pasEntered = input("Please enter your new password again: ")
# change password correct
    if newPsw == pasEntered:
        done = True
    else:
        print("Error in entering password, please try again")
        i -= 1
        print("You have " + str(i) + " times left")
if i <= 0:
    print("Password not changed") # password accepted
else:
    print("Password accepted!")
