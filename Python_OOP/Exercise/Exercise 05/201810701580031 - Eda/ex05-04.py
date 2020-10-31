# exercise 05-04
'''
student name: Eda
ID: 201810701580031
class: network182
'''

marks = {'Sam': 90.5,'Jane': 85.4,'Max': 92.3,'Alice': 64.5,'John': 69.4}
sum = 0
for i in marks:
    sum += marks[i]
print('Sum: '+ str(sum))
print('Average: ' + str(sum/len(marks)))