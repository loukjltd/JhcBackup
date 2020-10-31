'''
student name:Lenny
ID:201810701580045
class:net182
'''

num1 = 77.234
num2 = 89.325235
num3 = 68
name1 = 'Max'
name2 = 'Alice'
name3 = 'Bob'
template = '{0:<10}{1:<10}'
result = template.format("\"Name\"", "\"Score\"")
print(result)

template2 = '{0:<10}{1:<5.1f}'
result2 = template2.format(name1, num1)
print(result2)

template3 = '{0:<10}{1:<5.1f}'
result3 = template3.format(name2, num2)
print(result3)

template4 = '{0:<10}{1:<5.1f}'
result4 = template4.format(name3, num3)
print(result4)


