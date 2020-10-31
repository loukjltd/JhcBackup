correctPsw = 1111 # set password
pswEntered = 0

print("Program to Check Password")

# check password
while pswEntered + correctPsw == correctPsw:
    pswEntered = int(input('Please enter your password'))
    print("Please enter password: ")
print("Password accepted!")
