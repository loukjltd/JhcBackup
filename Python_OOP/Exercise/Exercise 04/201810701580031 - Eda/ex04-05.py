# exercise 04-05
'''
student name: Eda
ID: 201810701580031
class: network182
'''


studentNum = int(input("Enter the number of student grades:"))
for a in range(0,studentNum):
    grade = int(input("Enter grade 1: " or " Enter grade 2:"))
    if grade >= 50:
        print("student has passed")
    else:
        print("student has failed")