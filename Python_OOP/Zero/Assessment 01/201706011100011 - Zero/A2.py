#201706011100011 ZERO
radius = 8.5
π = 3.1416
area = radius * radius * π
perimeter = radius * 2 * π

template = "{0:<6}{1:<2}{2:<8}{3:<3}"
result = template.format("Enter","a","radius:","8.5")
print(result)

template2 = "{0:<14}{1:<12}{2:<9}"
result2 = template2.format("Radius","Area","Perimeter")
print(result2)

print("___________________________________")#___________________________________

template3 = "{0:<14}{1:<12.2f}{2:<9.2f}"
result3= template3.format(radius,area,perimeter)
print(result3)