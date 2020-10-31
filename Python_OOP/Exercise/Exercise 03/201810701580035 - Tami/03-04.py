'''student name:Tami
ID number:201810701580035
class:Net182
'''

print("welcome to programming in python")
print("this program shows if and logical operators")
print("Enter your age:")
age = int(input("Enter your age:"))
if age >=1 and age < 2:
    print("You are a baby")
elif age >= 2 and  age < 13:
    print("You are a child")
elif age >= 13 and age < 20:
    print("You are a teenager")
else:
    print("You are an adult")
