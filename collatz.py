import random

def collatz(n):
    x = n
    while True:
        yield x
        if x == 1:
            break
        if x % 2 == 0:
            x = x // 2
        else:
            x = 3*x + 1


while True:
    n = random.randrange(10**100, 10**101)
    for x in collatz(n):
        print(x, end=' ' if x > 1 else '')
    print()
