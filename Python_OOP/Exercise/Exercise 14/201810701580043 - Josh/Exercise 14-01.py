#Exercise 14-01
#Josh net182 201810701580043

try:
    f = open('./my_text.txt', 'r')
    print(f.read())

finally:
    if f:
        f.close()