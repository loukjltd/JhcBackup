'''
student name: leo
ID: 201810701580053
class: network182
'''
studentNum=int(input("Enter the number of student grades: "))
# loop for the number of students
for i in range (0,studentNum):
    grade=int(input("Enter grade"+str(i+1)+':'))
    if grade>= 50:
        print("Student has passed")
    else:
        print("Student has failed")
