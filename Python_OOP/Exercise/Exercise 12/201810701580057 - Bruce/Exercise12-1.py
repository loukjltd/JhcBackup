'''
student name :Bruce
ID:201810701580057
class:network 182
'''

student_marks = []
student_marks.append(75)
student_marks.append(87)
student_marks.append(55)
student_marks.append(63)
student_marks.append(87)
student_marks.append(71)

for marks in student_marks:
    print(marks)

sum_marks = 0
for sum in student_marks:
    sum_marks += sum
print('Sum: ' + str(sum_marks))
print('Average: ' + str(sum_marks/len(student_marks)))
