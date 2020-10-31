#question2
'''
student name:Eda xiang
student ID:201810701580031
Pledge of Honour: I pledge by honour that this program is solely my own work.
'''

radius = int(input("Enter a radius: "))
π = 3.1416
area = radius * radius * π
perimeter = radius * 2 * π

template = "{0:<10}{1:<12}{2:<9}"
result = template.format("Radius","Area","Perimeter")
print(result)

print("-------------------------------")

template1 = "{0:<10}{1:<12.2f}{2:<5.2f}"
result1 = template1.format(radius,area,perimeter)
print(result1)