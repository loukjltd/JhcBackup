#Name:Lester
#ID:201810701580055
#class:Net182

#Exercise 01-03
template = "{0:<15}{1:>5}{2:>10}"
result = template.format("Welcome","to","python")
print(result)

num1 = 1.69234
num2 = 2.1612561
template = "{0:<12}{1:>12}"
result = template.format("Apple","Orange")
print(result)
template2 = "{0:<12.2f}{1:>12.4f}"
result2 = template2.format(num1,num2)
print(result2)
