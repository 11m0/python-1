from functools import reduce


def my_func(num_from, num_to):
    return [el for el in range(num_from, num_to) if el % 2 == 0]


print(reduce(lambda x, y: x * y, my_func(100, 1001)))
