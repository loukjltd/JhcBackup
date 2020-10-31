def get_sum(list):

    if len(list) == 0:
        return 1
    else:
        new_list = list[1:len(list)]
        return  list[0] * get_sum(new_list)

numbers = [1.2, 2.0, 3.5, 5.3]
sum = get_sum(numbers)
print(sum)
