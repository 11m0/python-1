def my_func(my_list):
    return [el_2 for el_1, el_2 in zip(my_list, my_list[1:]) if el_2 > el_1]


print(my_func([300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]))
