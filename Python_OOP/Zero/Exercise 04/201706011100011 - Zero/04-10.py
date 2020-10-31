a =int(input("Enter the number for the times table: "))
count = 0
for m in range(1,a+1):
    for n in range(1,a+1):
        b = m*n
        count += 1
        print(b,end="\t")
    if count %  5 == 0:
        print()