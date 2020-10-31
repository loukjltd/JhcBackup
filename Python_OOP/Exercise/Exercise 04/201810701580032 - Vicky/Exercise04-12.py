#Exercise 04-12
'''
student name :Vicky
ID:201810701580032
class:Net182
'''

for i in range(8):
    for j in range(0,7-i):
        print(" ", end="")

    for k in range(0, (2*i + 1)):
        print("*", end="")
    print()

for i in range(8):
    for j in range(0,i):
        print(" ", end="")

    for k in range(0,2*(8-i)-1):
        print("*", end="")
    print()
