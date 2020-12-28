a = True
solve = 0
while a:
    my_str = input('Input numbers separated by space: ').split()
    result = [int(el) if el.isdigit() else el for el in my_str]
    try:
        solve += sum(result)
        print(solve)
    except TypeError:
        for el in result[0:len(result)-1]:
            solve += el
        a = False
        print(solve)
