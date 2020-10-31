# Assessment 1 Question 1
'''
Student Name: Sean
ID: 201810701580042
Class: Network 182
'''

template1 = "{0:<10}{1:>15}"
template2 = "{0:<19}{1:<15}"
line1 = template1.format('Escape sequence', 'Description')
line2 = template1.format('_______________', '___________')
line3 = template2.format(r'\n', 'New line character')
line4 = template2.format(r'\t', 'Tab character')
line5 = template2.format(r'\"', 'Double quote character')
print(str(line1))
print(str(line2))
print(str(line3))
print(str(line4))
print(str(line5))
