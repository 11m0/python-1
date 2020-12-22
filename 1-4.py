number = int(input('Введите целое положительное число: '))
max_digit = number % 10
while number > 0:
    number //= 10
    if max_digit < number % 10:
        max_digit = number % 10
print(f'Самая большая цифра в числе: {max_digit}')
