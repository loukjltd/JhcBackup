# exercise 03-04

'''
name: shrek
student id :201810101580038
class : net 182
'''

age = int(input("Enter your age: "))
if age > 0 and age < 2:
    print("You are a baby")
elif age >= 2 and age < 13:
    print("You are a child")
elif age <20 and age >= 13:
    print("You are a teenage")
elif age < 0:
    print("You are not born")
else:
    print("You are an adult")

