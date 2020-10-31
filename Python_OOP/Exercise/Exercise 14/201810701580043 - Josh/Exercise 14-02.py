#Exercise 14-02
#Josh net182 201810701580043

try:
    f = open('./my_text2.txt', 'r')
    sum1 = []
    for i in f.readlines():
        a = i.replace('\n', '')
        if a != '':
            sum1.append(int(a))
    print('Sum:', sum(sum1))

finally:
    if f:
        f.close()