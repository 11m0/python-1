from math import factorial
from itertools import count


def fact():
    for n in count(1):
        yield factorial(n)


i = 0
for el in fact():
    if i < 6:
        print(el)
        i += 1
    else:
        break
