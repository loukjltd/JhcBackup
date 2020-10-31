#Exercise 01-03
'''
student name :Vicky
ID:201810701580032
class:Net182
'''

print("My name's 'Sam' \ and I am 20 years old")
template = "{0} {1} {2}"
template1 = "{1:>15} {0:<5} {2:>10}"
result = template.format("Welcome", "to","Python")
print(result)
apple = 1.69234
orange = 2.1612561
template = "{0:<12} {1:>12}"
result = template.format("apple", "orange")
print(result)

template2 = "{0:<12.2f}{1:>12.4f}"
result2 = template2.format(apple,orange)
print(result2)

print()
print()
print()
