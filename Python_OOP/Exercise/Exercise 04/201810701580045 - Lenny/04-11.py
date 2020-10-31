# exercise 04-11
'''
name:Lenny
class:net182
ID:201810701580045
'''

week = ('MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN')
for w in week:
    print(str(w), end='\t')
print()

for i in range(1, 8):
    if int(i) % 8 == 0:
        print()
    print(str(i), end='\t')
print()

for i in range(8, 15):
    print(str(i), end='\t')
print()

for i in range(15, 22):
    print(str(i), end='\t')
print()

for i in range(22, 29):
    print(str(i), end='\t')
print()

for i in range(29, 32):
    print(str(i), end='\t')