# exercise03-04
'''
student name: Steven
ID: 201810101580037
class: network 182
'''
age = int(input("Enter your age:"))
if age <= 0:
    print("please enter the correct age")
if age < 2:
    print("you are a baby")
elif age < 13:
    print("you are a child")
elif age < 20:
    print("you are a teenager")
else:
    print("you are an adult")
