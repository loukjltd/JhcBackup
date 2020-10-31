# exercise 12-01
'''
student name: Yakira
ID: 201810701580034
class: network182
'''
student_marks = []
student_marks.append(75)
student_marks.append(87)
student_marks.append(55)
student_marks.append(63)
student_marks.append(87)
student_marks.append(71)
num = 0
for marks in student_marks:
    print(marks)
    if marks >= 70 and marks <= 80:
        num = num+1
sum = sum(student_marks)
average = sum/6
max = max(student_marks)
min = min(student_marks)
print("sum: ",sum)
print('average: ',average)
print('Largest mark: ',max)
print('Smallest mark: ',min)
print('There are {0} marks between 70 and 80'.format(num))

