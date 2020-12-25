my_list = [7, 5, 3, 3, 2]
new_el = int(input('Пожалуйста введите новый элемент рейтинга: '))
if new_el >= my_list[0]:
    my_list.insert(0, new_el)
elif new_el <= my_list[len(my_list) - 1]:
    my_list.append(new_el)
elif new_el in my_list:
    my_list.insert(my_list.index(new_el), new_el)
for i in range(len(my_list)):
    if my_list[i] > new_el > my_list[i + 1]:
        my_list.insert(i+1, new_el)
print(my_list)
