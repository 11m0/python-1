def dev_func(number_1, number_2):
    try:
        print(number_1 / number_2)
    except ZeroDivisionError:
        print('You cannot divide by zero!')


dev_func(float(input('Input first number: ')), float(input('Input second number: ')))
