#Exercise 13-02
'''
class:net182
name:vivi
id:201810701580049
'''

list1 = [1.2, 2.0, 3.5, 5.3]
def get_sum(list1):
    lens = len(list1)
    if lens> 1:
        return list1[0] * get_sum(list1[1:lens])
    else:
        return list1[0]

print(get_sum(list1))
