#net171 Zero

correctPsw = 1111# set password
pswEntered=0
print("Program to Check Password")

# check password
while pswEntered != correctPsw:
    pswEntered=int(input("Please enter password: "))

print("Password accepted!")