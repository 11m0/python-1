with open('my_file.txt', 'r') as my_file:
    my_dict = {}
    for line in my_file:
        my_dict[line.rstrip().split(' ')[0]] = line.rstrip().split(' ')[1]

my_sum = 0
for key in my_dict:
    my_sum += float(my_dict.get(key))
    if float(my_dict.get(key)) < 20000:
        print(key)
print(my_sum / len(my_dict.values()))
