with open('my_file.txt') as my_file:
    my_list = []
    my_list_subject = []
    my_list_hours = []
    i = 0
    for line in my_file:
        my_list.append([el[:el.find('(')] for el in line.split()[1:]])
        my_list_subject.append(line.split()[0])

    while i < len(my_list):
        my_list_hours.append(sum([int(el) for el in [' '.join(el).split() for el in my_list][i]]))
        i += 1

print(dict(zip(my_list_subject, my_list_hours)))
