a = float(input("Enter a radius:"))
area = a * a * 3.1416
perimeter = a * 2 * 3.1416
template1 = "{0:<13}{1:<10}{2:<15}"
result1 = template1.format("Radius","Area","Perimeter")
template2 = "{0:<0}"
result2 = template2.format("---------------------------------")
template3 ="{0:<12.2f}{1:<15.2f}{2:<12.2f}"
result3 = template3.format(a, area, perimeter)
print(result1)
print(result2)
print(result3)
