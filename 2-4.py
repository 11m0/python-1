my_list = (input('Пожалуйста введите строку из нескольких слов, разделённых пробелами: ')).split()
for ind, el in enumerate(my_list):
    print(ind + 1, el[0:10])
