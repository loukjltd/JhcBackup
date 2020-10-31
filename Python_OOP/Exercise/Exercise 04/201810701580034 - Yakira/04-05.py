# exercise 04-05
'''
student name : Yakira
ID : 201810701580034
class : Net182
'''
studentNum = int(input("Enter the number of student grades: "))
for i in range(0,studentNum) :
    grade = int(input('Enter grade ' + str(i + 1) + ':'))

    if grade >= 50:
        print("Student has passed")
    else :
        print ("Student has failed")
