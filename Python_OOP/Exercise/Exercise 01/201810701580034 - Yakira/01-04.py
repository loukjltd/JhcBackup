# exercise 01-04
'''
student name: Yakira
ID: 201810701580034
class: network 182
'''
template = "{0:<10}{1:<5}"
result = template.format('"Name"', '"Score"')
print(result)

name1 = "Max"
name2 = "Alice"
name3 = "Bob"
score1 = 77.234
score2 = 89.325235
score3 = 68.0

template2 = "{0:<10}{1:<5.1f}"
result2 = template2.format(name1, score1)
print(result2)

template3 = "{0:<10}{1:<5.1f}"
result3 = template2.format(name2, score2)
print(result3)

template4 = "{0:<10}{1:<5.1f}"
result4 = template3.format(name3, score3)
print(result4)
