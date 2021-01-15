with open('my_file_1.txt') as my_file:
    for line in my_file:
        new_line = line.split()
        for i, el in enumerate(new_line):
            if el == 'One':
                new_line[i] = 'Один'
            elif el == 'Two':
                new_line[i] = 'Два'
            elif el == 'Three':
                new_line[i] = 'Три'
            elif el == 'Four':
                new_line[i] = 'Четыре'
        with open('my_file_2.txt', 'a') as my_new_file:
            my_new_file.write(' '.join(new_line) + '\n')
