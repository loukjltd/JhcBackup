'''
class:Computer Network 182
ID:201810701580049
chinese name:Zhu gaoxian en:vivi
Exercise 01-03
'''

print('My name\'s \"Sam" \\ and I am 20 years old')
template1 = "{0:<12} {1:<6} {2}"
result1 = template1.format("Welcome","to","Python")

num1 = 1.69
num2 = 2.1613
template2_1 = "{0:>6}  {1:>12}"
template2_2 = "{0:>5.2f}  {1:>12.3f}"
result2_1 = template2_1.format("Apple" ,"Orange")
result2_2 = template2_2.format(num1 ,num2)
print(result2_1)
print(result2_2)