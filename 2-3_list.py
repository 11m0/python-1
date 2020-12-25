month_input = int(input('Введите месяц в виде целого числа от 1 до 12: '))
season_list = ['Зима', 'Весна', 'Лето', 'Осень']
if month_input in range(1, 3):
    print(f'Месяцу номер {month_input} соответствует время года - {season_list[0]}')
elif month_input == 12:
    print(f'Месяцу номер {month_input} соответствует время года - {season_list[0]}')
elif month_input in range(3, 6):
    print(f'Месяцу номер {month_input} соответствует время года - {season_list[1]}')
elif month_input in range(6, 9):
    print(f'Месяцу номер {month_input} соответствует время года - {season_list[2]}')
elif month_input in range(9, 12):
    print(f'Месяцу номер {month_input} соответствует время года - {season_list[3]}')
