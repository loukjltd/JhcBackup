#exercise 01
'''
studentname:shrek
student id:201810101580038
class:net182
'''

template1 = "{0:<10}{1:>15}"
template2 = "{0:<19}{1:>10}"
result1 = template1.format('Escape sequence', 'Description')
result2 = template1.format('_______________', '___________')
result3 = template2.format(r'\n', 'New line character')
result4 = template2.format(r'\t', 'Tab character')
result5 = template2.format(r'\"', 'Double quote character')
print(str(result1))
print(str(result2))
print(str(result3))
print(str(result4))
print(str(result5))