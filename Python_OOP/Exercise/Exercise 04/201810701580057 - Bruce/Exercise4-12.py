#Exercise4-12
'''
student name:Bruce
ID:201810701580057
class: network 182
'''
for i in range(8):                # do this 8 times
    # print spaces first
    for j in range(0,7-i):        # go from 0 to 7-i
        print(" ", end="")        # print space on same line

    # print stars
    for k in range(0, (2*i + 1)): # go from 0 to (2*i + 1)
        print("*", end="")        # print star on same line
    print()
for i in range(7):
    for m in range(0,i+1):
        print(" ", end="")

    for n in range(0,2 * (6 - i) + 1):
        print("*", end="")
    print()