#Exercise 01-04
'''
student name :Vicky
ID:201810701580032
class:Net182
'''

Name1='Max'
Score1= 77.234
Name2='Alice'
Score2= 89.325235
Name3='Bob'
Score3=68

template = "{0:<10}{1:>5}"
result = template.format("Name", "Score")
print(result)

template2 = "{0:<10}{1:>5.1f}"
result2 = template2.format(Name1, Score1)
print(result2)

template2 = "{0:<10}{1:>5.1f}"
result2 = template2.format(Name2, Score2)
print(result2)

template2 = "{0:<10}{1:>5.1f}"
result2 = template2.format(Name3, Score3)
print(result2)

