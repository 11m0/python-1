with open('my_file.txt', 'w+') as my_file:
    my_file.write(input('Input data: '))
    my_file.seek(0)
    print(sum([int(el) for el in my_file.read().split()]))
