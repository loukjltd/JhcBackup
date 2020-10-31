'''
student name: Yakira
ID: 201810701580034
Pledge of Honour: I pledge by honour that this program is solely my own work.
'''

num = input("Enter a radius: ")
template = "{0:<6}  {1:>8}  {2:>13}"
result = template.format("Radius" , "Area" ,"Perimeter")
print(result)
print("-------------------------------")
π = 3.1416
radius = float(num)
area = radius * radius * float(π)
perimeter = radius * 2 * float(π)

template2 = "{0:<5}  {1:>9.2f}  {2:>13.2f}"
result2 = template2.format(radius , area ,perimeter)
print(result2)
