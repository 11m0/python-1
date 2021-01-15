with open('my_file.txt', 'w') as my_file:
    while True:
        data = input('Input data: ')
        print(data, file=my_file)
        if data is '':
            break
