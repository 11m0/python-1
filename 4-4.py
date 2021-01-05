def my_func(my_list):
    return [el for el in my_list if my_list.count(el) == 1]


print(my_func([2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]))
