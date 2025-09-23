import sys
from functools import reduce
from math import sqrt

def factors(n):
        step = 2 if n%2 else 1
        return set(reduce(list.__add__,
                    ([i, n//i] for i in range(1, int(sqrt(n))+1, step) if n % i == 0)))

for line in sys.stdin:
    n = int(line)
    fN = sum(factors(n)) - n
    if n == fN:
        print(n, "perfect")
    elif abs(fN - n) <= 2:
        print(n, "almost perfect")
    else:
        print(n, "not perfect")