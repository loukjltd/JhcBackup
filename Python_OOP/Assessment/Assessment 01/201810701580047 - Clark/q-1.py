# Question 1
'''
name:Clark
class:net182
I  D:201810701580047
'''
template = "{0:<10}{1:>20}"
template2 = "{0:<10}{1:>32}"
template3 = "{0:<10}{1:>27}"
template4 = "{0:<10}{1:>36}"
result0 = template.format("Escape sequence", "Description\n")
result1 = template.format("_______________", "___________\n")
result2 = template2.format("\\n", "New line character\n")
result3 = template3.format("\\t", "Tab character\n")
result4 = template4.format("\\\"", "Double quote character\n")
print(result0 + result1 + result2 + result3 + result4)
