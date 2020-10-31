#Task2
"""
id : 201810701580049
class : Net182
name : vivi
"""
cut = "-------" * 5
radius = float(input(" Enter a radius: "))
area = (radius ** 2) * 3.1416
Perimeter = radius * 2 * 3.1416
templte = "{0:>7} {1:>8} {2:>18} \n {3} \n {4:<8} {5:>8.2f} {6:>12.2f}"
result = templte.format("Radius","Area","Perimeter",cut,radius,area,Perimeter)
print(result)

