f = open('my_text2.txt', 'r')
x = []
for a in f.readlines():
    x.append(int(a))
print(sum(x))
