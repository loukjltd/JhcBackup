#Exercise 12-01
"""
Class:Net182
name:vivi
id:201810701580049
"""

student_marks = []
student_marks.append(75)
student_marks.append(87)
student_marks.append(74)
student_marks.append(63)
student_marks.append(87)
student_marks.append(71)

student_marks[2] = 55

for i in student_marks:
    print(i)

sum_marks = 0
for i in student_marks:
    sum_marks += i
print('Sum:', sum_marks)
print('Average:',sum_marks/len(student_marks))
