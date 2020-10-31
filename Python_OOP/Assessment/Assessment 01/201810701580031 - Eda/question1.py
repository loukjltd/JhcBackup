#question1
'''
student name:Eda xiang
student ID:201810701580031
Pledge of Honour: I pledge by honour that this program is solely my own work.
'''

template = "{0:<25}{1:>17}"
result = template.format("Escape sequence","Description")
print(result)

template1 = "{0:<25}{1:>20}"
result1 = template1.format("__________________","______________")
print(result1)

template2 = "{0:<25}{1:>24}"
result2 = template2.format("\\n","New line character")
print(result2)

template3 = "{0:<25}{1:>19}"
result3 = template3.format("\\t","Tab character")
print(result3)

template4 = "{0:<25}{1:>28}"
result4 = template4.format("\\\"" , "Double quote character")
print(result4)