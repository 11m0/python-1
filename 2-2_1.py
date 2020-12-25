my_list = (input('Пожалуйста введите элементы списка через пробел: ')).split()
result_list = []
print(my_list)

n = 0
while n < len(my_list) // 2:
    result_list.extend(my_list[2*n+1:2*(n+1)] + my_list[2*n:2*n+1])
    n += 1
if len(my_list) % 2 != 0:
    result_list.append(my_list[len(my_list) - 1])

print(result_list)
