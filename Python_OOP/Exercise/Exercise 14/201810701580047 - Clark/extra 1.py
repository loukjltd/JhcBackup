class IntNumberClass:

    def __init__(self, n):
        self.n = n

    def get_cube(self):
        return self.n * self.n * self.n

class Wage:

    def __init__(self, wh, hr):
        self.wh = wh
        self.hr = hr

    def calc_wage(self):
        return self.wh * self.hr


def calculate_sum_integers(int_list):

    if len(int_list) == 0:
        return 0
    else:
        first_int = int_list[0]
        new_list = int_list[1:]
        total = first_int + calculate_sum_integers(new_list)
        return total


def calculate_sum_objects(obj_list):
    x = 0
    for a in obj_list:
        x += pow(IntNumberClass.get_cube(a), 1/3)
    return int(x)


def get_total_cube(obj_list):

    if len(obj_list) == 0:
        return 0
    else:
        first_int = obj_list[0]
        new_list = obj_list[1:]
        total = first_int.get_cube() + get_total_cube(new_list)
        return total


def get_total_wage(obj_list):
    y = 0
    for a in obj_list:
        y += Wage.calc_wage(a)
    return y


nums = [2, 3, 4]
total = calculate_sum_integers(nums)
print(total)

num_objects = [IntNumberClass(2), IntNumberClass(3), IntNumberClass(4)]
total_obj = calculate_sum_objects(num_objects)
print(total_obj)

total_cube = get_total_cube(num_objects)
print(total_cube)

wage_list = [Wage(15.5, 18), Wage(23.5, 19.5), Wage(35, 25)]
total_wages = get_total_wage(wage_list)
print(total_wages)
