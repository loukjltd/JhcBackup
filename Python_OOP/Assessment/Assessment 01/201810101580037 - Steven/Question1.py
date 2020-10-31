# Question 1
'''
student name: Steven
ID: 201810101580037
class: network 182
'''
template1 = "{0:<10}{1:>15}"
template2 = "{0:<19}{1:<15}"
line1 = template1.format('Escape sequence', 'Description')
line2 = template1.format('_______________', '___________')
line3 = template2.format(r'\n', 'New line character')
line4 = template2.format(r'\t', 'Tab character')
line5 = template2.format(r'\"', 'Double quote character')
print(line1)
print(line2)
print(line3)
print(line4)
print(line5)
