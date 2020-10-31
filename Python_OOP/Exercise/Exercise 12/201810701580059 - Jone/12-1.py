# Exercise 12-01
'''
student name: jone
#ID: 201810701580059
#class: net182
'''
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

for j in student_marks:
    sum_marks = sum_marks + j

print('Sum: ',sum_marks)
print('Auerage: ',sum_marks/len(student_marks))
