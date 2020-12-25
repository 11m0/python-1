products = int(input("Введите количество новых товаров: "))
my_dict = {}
my_list = []
my_analytics_name = {}
my_analytics_name_list = []
my_analytics_price = {}
my_analytics_price_list = []
my_analytics_amount = {}
my_analytics_amount_list = []
my_analytics_measure = {}
my_analytics_measure_list = []
i = 1
while i <= products:
    my_dict = dict({
        'название': input('Введите название товара: '), 'цена': input('Введите цену товара: '),
        'количество': input('Введите количество товара: '), 'eд': input('Введите единицу измерения: ')
    })
    my_list.append((i, my_dict))
    my_analytics_name = my_analytics_name_list.append(my_dict.get('название'))
    my_analytics_price = my_analytics_price_list.append(my_dict.get('цена'))
    my_analytics_amount = my_analytics_amount_list.append(my_dict.get('количество'))
    my_analytics_measure = my_analytics_measure_list.append(my_dict.get('ед'))
    i += 1
print(my_list)
my_analytics = {
    'название': my_analytics_name_list, 'цена': my_analytics_price_list,
    'количество': my_analytics_amount_list, 'ед': my_analytics_measure_list
}
print(my_analytics)
