# Exercise 04-05
''''
student name:Luis
ID:201810701580033
class:network 182
'''



studentNum=int(input("Enter the number of student grades: "))

# loop for the number of students
for i in range (0,studentNum):
    grade=int(input( "Enter grade "))

    if grade >= 50:
      print ("Student has passed")
    else:
        print ("Student has failed")

