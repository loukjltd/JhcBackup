# Exercise 12-01
'''
Student Name: Sean
ID: 201810701580042
Class: Network 182
'''

student_mark = [75, 87, 74, 63, 87, 71]

for i in student_mark:
    print(str(i))

sum_mark = 0

for j in student_mark:
    sum_mark += j

print('Sum: ' + str(sum_mark))
print('Average: ' + str('%.1f' % (sum_mark / len(student_mark))))

print('Largest mark: ' + str(max(student_mark)))
print('Smallest mark: ' + str(min(student_mark)))

c = 0
for k in student_mark:
    if 70 < k < 80:
        c += 1
        print(str(k))
print('There are ' + str(c) + ' marks between 70 and 80')
