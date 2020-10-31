#Exercise 04-12
'''
Name:Lester
ID:201810701580055
Class:Net 182
'''

for i in range(8):                # do this 8 times
    # print spaces first
    for j in range(0,7-i):        # go from 0 to 7-i
        print(" ", end="")        # print space on same line

    # print stars
    for k in range(0, (2*i + 1)): # go from 0 to (2*i + 1)
        print("*", end="")        # print star on same line
    print()                       # print a new line

# now print the bottom half of the diamond
for i in range(7,0,-1):
    # print spaces first
    for q in range(0,8-i):
        print(" ", end="")

    # print stars
    for w in range(0, 2*i-1):
        print("*", end="")
    print()
