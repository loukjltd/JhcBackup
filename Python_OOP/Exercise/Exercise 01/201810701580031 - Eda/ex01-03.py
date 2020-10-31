# exercise 01-03
'''
student name: Eda
ID: 201810701580031
class: network182
'''


a = str('My name is \"Eda\" and I am 19 years old')
print(a)

template = "{0:<15}{1:>5}{2:>10}"
result = template.format("Welcome","to","python")
print(result)

apple = 1.69234
orange = 2.1612561
template = "{0:<12}{1:>12}"
result = template.format("apple","orange")
print(result)

template1 = "{0:<12}{1:>12}"
result1 = template.format(apple,orange)
print(result1)