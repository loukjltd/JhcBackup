#Exercise 13-02
#Josh net182 201810701580043

list1 = [1.2, 2.0, 3.5, 5.3]
def get_sum(list1):
    le = len(list1)
    if le > 1:
        return list1[0] * get_sum(list1[1:le])
    else:
        return list1[0]

print(get_sum(list1))