# exercise 01-04
'''
student name: Eda
ID: 201810701580031
class: network182
'''


template = "{0:<10}{1:<5}"
result = template.format("\"name\"","\"score\"")
print(result)

name1 = str("Max")
name2 = str("Alice")
name3 = str("Bob")
score1 = 77.234
score2 = 89.325235
score3 = 68
template1 = "{0:<10}{1:<5.1f}"
result1 = template1.format(name1,score1)
result2 = template1.format(name2,score2)
result3 = template1.format(name3,score3)
print(result1)
print(result2)
print(result3)