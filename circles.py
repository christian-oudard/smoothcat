import math
import itertools

for e in itertools.count(5):
    size = round(1.03 ** e)
    for y in range(-size, size+1):
        for x in range(-size, size+1):
            r = math.sqrt(x**2 + y**2)
            if size-1 <= r <= size+1:
                print('#', end='')
            else:
                print(' ', end='')
        print()
