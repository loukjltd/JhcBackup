# exercise 05-04
'''
student name : Yakira
ID : 201810701580034
class : Net182
'''
marks = {"Sam" : 90.5, "Jane" : 85.4, "Max" : 92.3, "Alice" : 64.5, "John" : 69.4}
sum = 0
for key in marks :
    sum += marks[key]
print('Sum: ',sum)
average = sum/len(marks)
print('Average: ',average)


