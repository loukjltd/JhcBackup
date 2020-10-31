#Exercise 01-03
'''
name: Assass
idnumber: 201810701580040
class: network 182
'''
print('My name\'s "Sam\" \ and I am 20 years old','\n')

template = "{0:<15}{1:>5}{2:>10}"
result = template.format("Welcome", "to","Python")
print(result,'\n')

apple = 1.69234
orange = 2.1612561

template2 = "{0:<12}{1:>12}"
result2 = template2.format("Apple", "Orange")

print(result2)
template3 = "{0:<12.2f}{1:>12.4f}"
result3 = template3.format(apple, orange)
print(result3)



