# Exercise 04-12
'''
student name: felix
#ID: 201810701580052
#class: net182
'''
for i in range(8):
    for j in range(0,7-i):
        print(" ", end="")
    for k in range(0, (2*i + 1)):
        print("*", end="")
    print()
for z in range(0,7):
    for x in range(0,z+1):
        print(" ", end="")
    for c in range(0,(7-z)*2-1):
        print("*", end="")
    print()


