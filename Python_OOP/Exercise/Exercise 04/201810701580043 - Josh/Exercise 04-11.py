#Exercise 04-11
#Josh net182 201810701580043

print('M\tT\tW\tT\tF\tS\tSu')
for i in range(1, 31):
    print(i, end='\t')
    if i % 7 == 0:
        print()