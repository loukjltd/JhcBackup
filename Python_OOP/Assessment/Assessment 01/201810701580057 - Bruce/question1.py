'''
student name:Bruce
ID:201810701580057
class: network 182
'''


template = '{0:<10}{1:>15}'

result1 = template.format('Escape sequence','Description')
result2 = template.format('——————','——————')
result3 = template.format('\\n','         New line character')
result4 = template.format('\\t','         Tab character')
result5 = template.format('\\"','         Double quote character')
print(result1)
print(result2)
print(result3)
print(result4)
print(result5)