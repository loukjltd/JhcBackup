# exercise 04-05
'''
name:Lenny
class:net182
ID:201810701580045
'''
studentNum = int(input("Enter the number of student grades: "))

for i in range(0, studentNum):
    g = int(input('Enter Grade ' + str(i + 1) + ': '))
    if g >= 50:
        print('Student has passed.')
    else:
        print('Students ha failed.')