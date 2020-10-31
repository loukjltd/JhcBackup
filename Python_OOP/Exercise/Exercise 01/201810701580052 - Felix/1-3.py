# Exercise 01-03
'''
student name: felix
#ID: 201810701580052
#class: net182
'''
print('My name'+ "'"+'s'+ ' " '+'Sam'+ ' " ' + '\ and I am 20 years old')
template = '{0:<12}{1:>5}{2:>10}'
result = template.format('welcome','to','python')
apple = 1.69234
orange = 2.1612561
template2 = '{0:<12}{1:>12}'
result2 = template2.format('Apple','Orange')
template3 = '{0:<12.2f}{1:>12.4f}'
result3 = template3.format(apple,orange)
print(result)
print(result2)
print(result3)