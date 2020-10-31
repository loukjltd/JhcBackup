#Exercise 04-012
'''
name: Jax
idnumber: 201810701580041
class: net182
'''

for i in range(8):
    for j in range(0,7-i):
        print(" ", end="")

    for k in range(0, (2*i + 1)):
        print("*", end="")
    print()
for i in range(8):
    for j in range(0,i+1):
        print(" ", end="")

    for k in range(0,13-2*i):
        print("*", end="")
    print()
