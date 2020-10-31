#Question 2
'''
student name :Vicky
ID:201810701580032
class:Net182
'''

a=float(input("Enter a radius:"))

template = "{0:<10}{1:>10}{2:>15}"
result = template.format("Radius","Area","Perimeter")
print(result)

print("------------------------------------")

template = "{0:<10}{1:>10.6}{2:>15.6}"
result = template.format(str(a),str(a *a*3.1416),str(2 * 3.1416*a))
print(result)

