#Exercise 01-03
'''
name: LEO
#ID: 201810701580053
#class: net182
'''


print('My name\'s "Sam" \\ and I am 20 years old')

print()

template = "{0:<15}{1:>5}{2:>10}"
result=template.format("welcome", "to",'python')
print(result)

print()

apple = 1.69234
orange = 2.1612561

template = "{0:<12}{1:>12}"
result = template.format("apple", "orange")
print(result)

template2 = "{0:<12.2f}{1:>12.4f}"
result2 = template2.format(apple,orange)
print(result2)
