#Exercise 04-05
'''
Name:Lester
ID:201810701580055
Class:Net 182
'''

studentNum = int(input("Enter the number of student grades:"))
for a in (0,studentNum):
    grade = int(input("Enter grade" + str(a) + ":"))
    if grade > 50:
        print("Student has passed")
    else:
        print("Student has failed")
    