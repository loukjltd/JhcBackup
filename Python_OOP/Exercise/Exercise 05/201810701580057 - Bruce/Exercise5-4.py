#Exercise5-4
'''
student name:Bruce
ID:201810701580057
class: network 182
'''

marks = {}
marks['Sam'] = 90.5
marks['Jane'] = 85.4
marks['Max'] = 92.3
marks['Alice'] = 64.5
marks['John'] = 69.4
print(marks)

sum = 0
for i in marks:
    sum += marks[i]
    Average = sum / len(marks)
print('Sum: ',sum)
print('Average: ',Average)
