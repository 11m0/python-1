def my_func(my_range):
    return [el for el in my_range if el % 20 == 0 or el % 21 == 0]


print(my_func(range(20, 241)))
