# net171-ZhaoYinTing

student_marks = []
student_marks.append(75)
student_marks.append(87)
student_marks.append(74)
student_marks.append(63)
student_marks.append(87)
student_marks.append(71)

student_marks[2] = 55

for mark in student_marks:
    print(mark)

sum_marks = 0
a = 0
for mark in student_marks:
    sum_marks = sum_marks+mark
    a += 1
avg_marks = sum_marks/a
print("Sum:", sum_marks)
print("Average:", avg_marks)

Largest = student_marks[0]
for mark in student_marks:
    if Largest < mark:
        Largest = mark
print("Largest mark:", Largest)

Smallest = student_marks[0]
for mark in student_marks:
    if Smallest > mark:
        Smallest = mark
print("Smallest mark:", Smallest)

b = 0
for mark in student_marks:
    if mark >= 70 and mark <= 80:
        b += 1
print("There are %s marks between 70 and 80" % b)
