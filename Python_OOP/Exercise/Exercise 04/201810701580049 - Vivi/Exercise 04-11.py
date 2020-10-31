#Exercise 04-11
'''
class:net182
name:vivi
id:201810701580049
'''

print('M\tT\tW\tT\tF\tS\tSu')
for i in range(1, 31):
    print(i, end='\t')
    if i % 7 == 0:
        print()
