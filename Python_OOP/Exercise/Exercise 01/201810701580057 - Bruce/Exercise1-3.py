# exercise 01-03
'''
student name:Bruce
ID:201810701580057
class: network 182
'''
num1 = 1.69
num2 = 2.1613
print('My name\'s "Sam" \ and I am 20 years old\n')

template = '{0:<15}{1:>5}{2:>10}'
result = template.format('Weclome', 'to', 'Python\n')
print(result)

template2 = '{0:<12}{1:>12}'
result2 = template2.format('Apple', 'Orange')
print(result2)

template3 = '{0:<12}{1:>12}'
result3 = template3.format(num1, num2)
print(result3)