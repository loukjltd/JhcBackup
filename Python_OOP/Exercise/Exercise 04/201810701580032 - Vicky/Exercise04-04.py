#Exercise 04-04
'''
student name :Vicky
ID:201810701580032
class:Net182
'''

i = 3
done=False

print("Program to Change Password")
print("Your password has expired and you have " + str(i) + " chances left to change your password")

while i >0 and not done :
    newPsw = int(input("Please enter your new password: "))
    pswEntered=int(input("Please enter your new password: "))
    if newPsw==pswEntered:
       done=True
    else:
        print("Error in entering password, please try again")
        i=i-1
        print(i)
if i<=0:
    print("Password not changed")
else:
    print("Password accepted!")