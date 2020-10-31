for i in range(8):
    for j in range(0, 7-i):
        print(" ", end="")
    for k in range(0, (2*i + 1)):
        print("*", end="")
    print()
for a in range(6, -1, -1):
    for b in range(7-a, 0, -1):
        print(" ", end="")
    for c in range((2*a + 1), 0, -1):
        print("*", end="")
    print()
