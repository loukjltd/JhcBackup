'''
student name :Bruce
ID:201810701580057
class:network 182
'''

def get_num(my_list):

    if len(my_list) == 0:
        return  1
    else:
        new_list = my_list[1:len(my_list)]
        return my_list[0] * get_num(new_list)
numbers = [1.2,2.0,3.5,5.3]
sum_list = get_num(numbers)
print(sum_list)
