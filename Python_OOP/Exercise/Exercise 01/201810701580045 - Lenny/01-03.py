#
'''
student name:Lenny
ID:201810701580045
class:net182
'''

print('My name\'s "Sam" \ and I am 20 years old\n')

template = '{0:<15} {1:>5} {2:>10}'
result = template.format('Welcome','to','Python\n')
print(result)

num1 = 1.69234
num2 = 2.1612561
template2 = '{0:<12}{1:>12}'
result2 = template2.format('Apple','Orange')
print(result2)

template3 = '{0:<12.2f}{1:>12.4f}'
result3 = template3.format(num1,num2)
print(result3)
