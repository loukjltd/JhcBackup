# net171-ZhaoYinting


def get_product(my_list):
    if len(my_list) == 0:
        return 1
    else:
        new_list = my_list[1:len(my_list)]
        return my_list[0] * get_product(new_list)


numbers = [1.2, 2.0, 3.5, 5.3]
product_list = get_product(numbers)
print(product_list)
