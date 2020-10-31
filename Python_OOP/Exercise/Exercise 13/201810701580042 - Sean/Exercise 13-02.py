# Exercise 13-02
'''
Student Name: Sean
ID: 201810701580042
Class: Network 182
'''


def get_multiply(my_list):

    if len(my_list) == 0:
        return 1
    else:
        new_list = my_list[1:len(my_list)]
        return my_list[0] * get_multiply(new_list)


numbers = [1.2, 2.0, 3.5, 5.3]
product_list = get_multiply(numbers)
print(product_list)
