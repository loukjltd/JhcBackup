#Exercise 04-05
'''
student name :Vicky
ID:201810701580032
class:Net182
'''

studentNum=int(input("Enter the number of student grades:"))
for i in range(0,studentNum):
    grade=int(input("Enter grade 1" + str(i + 1) + ':'))
    if grade>=50:
        print("Student has passed")
    else:
        print("Student has failed")
