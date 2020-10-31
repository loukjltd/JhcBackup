#exercise 13-02
'''
studentname:shrek
studentid:201810101580038
class:net182
'''

def get_sum(my_list):

    if len(my_list) == 0:
        return 1
    else:
        new_list = my_list[1:len(my_list)]
        return my_list[0] * get_sum(new_list)


numbers = [1.2, 2.0, 3.5 ,5.3]
multiply_list = get_sum(numbers)
print(multiply_list)

