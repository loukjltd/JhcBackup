# Exercise 01-04
'''
Student Name: Sean
ID: 201810701580042
Class: Network 182
'''

Max = 77.234
Alice = 89.325235
Bob = 68
template = "{0:<10}{1:>5}"
result = template.format("\"Name\"", "\"Score\"")
print(result)

template2 = "{0:<10}{1:>5.1f}"
result2 = template2.format("Max", Max)
print(result2)

template3 = "{0:<10}{1:>5.1f}"
result3 = template3.format("Alice", Alice)
print(result3)

template4 = "{0:<10}{1:>5.1f}"
result4 = template4.format("Bob", Bob)
print(result4)
