# Exercise 04-05
'''
student name: felix
#ID: 201810701580052
#class: net182
'''
studentNum = int(input("Enter the number of student grades: "))

for i in range(0,studentNum):
    grade=int(input( 'Enter grade'+ str(i+1) + ':'))
    if grade >= 50:
        print("Student has passed")
    else:
        print("Student has failed")
