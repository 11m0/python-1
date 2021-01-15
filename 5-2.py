with open('my_file.txt', 'r') as my_file:
    lines_count = 0
    words_count = 0
    for line in my_file:
        words_count += len(line.split(' '))
        lines_count += 1
print(f'Number of lines in my file: {lines_count}')
print(f'Number of words in my file: {words_count}')
