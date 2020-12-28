def my_func(number_1, number_2):
    i = 1
    solve = 1 / number_1
    if number_2 == 0:
        solve = 1
    while i < abs(number_2):
        solve = solve / number_1
        i += 1
    return solve


print(my_func(float(input('Input real positive number: ')), int(input('Input negative integer: '))))
