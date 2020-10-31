'''
student name: Charlie
ID: 201810701580044
class: network 182
'''
template = "{0:<10},{1:>10},{2:>20}"
re000t = template.format("Welcome", "to", "python")
print(re000t)
num1 = 1.69
num2 = 2.1613
template = "{0:<28}{1:>14}"
result = template.format("Apple", "Orange")
print(result)
template2 = "{0:<28.2f}{1:>14.3f}"
result2 = template2.format(num1, num2)
print(result2)