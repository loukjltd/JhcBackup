# exercise 03 04
'''
Bro
201810701580056
network 182
'''
age = int(input("Enter your age: "))
if age > 0 and age < 2:
    print ("You are a baby")
elif age >= 2 and age < 13:
    print ("You are a child")
elif age >= 13 and age < 20:
    print ("You are a teenager")
elif age < 0:
    print ("error")
else:
    print ("You are an adult")

