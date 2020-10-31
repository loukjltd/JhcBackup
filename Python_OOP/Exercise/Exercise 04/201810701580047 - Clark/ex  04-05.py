num = int(input('Enter the number of student grades:'))
for x in range(1, num+1):
    grade = int(input('Enter grade ' + str(x) + ' : '))
    if grade >= 50:
        print('Student has passed')
    else:
        print('Student has failed')
