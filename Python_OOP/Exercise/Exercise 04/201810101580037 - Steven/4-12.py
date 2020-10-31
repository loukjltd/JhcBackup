# exercise04-12
'''
student name: Steven
ID: 201810101580037
class: network 182
'''
for a in range(8):
    for b in range(0,7-a):
        print(" ", end="")
    for c in range(0, (2*a + 1)):
        print("*", end="")
    print()
for a in range(7):
    for b in range(0,a+1):
        print(" ", end="")
    for c in range(0,13-a*2):
        print("*", end="")
    print()
