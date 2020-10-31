'''
Class:Net182
Name:Assass
ID:201810701580040
'''
template = "{0:<20}{1:<50}"
result = template.format("Escape sequence", "Description",END='\n')
result1 = template.format("__________________", "______________",'\n')
result2 = template.format("\\n", "New line character",'\n')
result3 = template.format("\\t", "Tab character",'\n')
result4 = template.format("\\\"", "Double quote character",'\n')
print(result)
print(result1)
print(result2)
print(result3)
print(result4)