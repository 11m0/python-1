def my_func(arg_1, arg_2, arg_3):
    return max(arg_1, arg_2, arg_3) + min(max(arg_1, arg_2), max(arg_1, arg_3), max(arg_2, arg_3))


print(my_func(
    (input('Input first arg: ')),
    (input('Input second arg: ')),
    (input('Input third arg: '))
))
