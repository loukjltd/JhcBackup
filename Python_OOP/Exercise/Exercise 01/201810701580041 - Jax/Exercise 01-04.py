#Exercise 01-04
'''
name: Jax
idnumber: 201810701580041
class: net182
'''


Max=77.234
Alice=89.325235
Bob=68

template = "{0:<10}{1:>5}"
result=template.format('\"Name\"', '\"Score\"')
print(result)

template = "{0:<10}{1:>5.1f}"
result2 = template.format('Max',Max)
print(result2)

template = "{0:<10}{1:>5.1f}"
result3 = template.format('Alice',Alice)
print(result3)

template = "{0:<10}{1:>5.1f}"
result4 = template.format('Bob',Bob)
print(result4)
