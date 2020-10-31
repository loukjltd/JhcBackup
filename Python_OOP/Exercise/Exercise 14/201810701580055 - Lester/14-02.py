f = open("./my2.txt", "r")
numbers = []

for i in f.readlines():
    numbers.append(int(i))
    a = sum(numbers)

print(numbers)
print("Sum:", a)
