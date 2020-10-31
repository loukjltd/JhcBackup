#Exercise4-5
'''
student name:Bruce
ID:201810701580057
class: network 182
'''

studentNum = int(input('Enter the number of student grades: '))

for i in range(0,studentNum):
    grade = int(input('Enter grade ' + str(i + 1) + ': '))
    i += 1
    if grade > 50:
        print('Student has passed')
    else:
        print('Student has failed')