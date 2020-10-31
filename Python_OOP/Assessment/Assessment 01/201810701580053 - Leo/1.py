'''
Student Name: leo
ID: 201810701580053
Class: Network 182
'''
template = "{0:<10}{1:>15}"
result = template.format("Escape sequance", "Description")
print(result)
template1 = "{0:<10}{1:>15}"
result1 = template1.format("____________________","________________")
print(result1)
template2 = "{0:<10}{1:>15}"
result2 = template.format("\\n", "New Line character")
print(result2)
template3 = "{0:<10}{1:>15}"
result3 = template.format("\\t", "Tab character")
print(result3)
template4 = "{0:<10}{1:>15}"
result4 = template.format('\\"', "Double quote character")
print(result4)
