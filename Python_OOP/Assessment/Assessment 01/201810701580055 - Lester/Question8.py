a = {"Australia": 22.5, "China": 36.4, "Malaysia": 38.4, "New Zealand": 18.2}
b = 0
list = []
c = 0

for i in a:
    print(i + ":" + str(a[i]))
    b += float(a[i])
    list.append(a[i])

print("Average temperature:" + str("%.2f" % (b / len(a))))
print("Maximum temperature:" + str("%.2f" % (max(list))))

for j in list:
    if 20 <= j <= 30:
        c += 1

print("Number of temperatures between 20 and 30:" + str(c))
