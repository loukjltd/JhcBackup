# exercise03-04
'''
student name: jone
ID: 201810101580059
class: network 182
'''
age = int(input("Enter your age:"))
if age < 2:
    print("You are a baby")
else:
    if age < 13:
        print("You are a child")
    else:
        if age < 20:
            print("You are a teenager")
        else:
            print("You are an adult")