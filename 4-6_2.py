from itertools import cycle
import time


timeout_start = time.time()
timeout = 5
for i in cycle([1, 2, 3, 4, 5]):
    print(i)
    if time.time() > timeout_start + timeout:
        break
