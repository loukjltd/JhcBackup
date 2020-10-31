#Exercise 04-05
'''
name: Jax
idnumber: 201810701580041
class: net182
'''

studentNum=int(input("Enter the number of student grades:  "))

# loop for the number of students
for i in range(1,studentNum+1):
    grade=int(input('Enter grade '))
    print('Enter grade '+str(i)+':'+str(grade))
    if grade>=50:
        print("Student has passed")
    else:
        print('Student has failed')

