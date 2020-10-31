#Exercise 01-04
'''
name: Assass
idnumber: 201810701580040
class: network 182
'''
Max=77.234
Alice=89.325235
Bob=68
template = "{0:<10}{1:>5}"
result=template.format('\"Name\"', '\"Score\"')
print(result)

template1 = "{0:<10}{1:>5.1f}"
result2 = template1.format('Max',Max)
print(result2)

result3 = template1.format('Alice',Alice)
print(result3)

result4 = template1.format('Bob',Bob)
print(result4)