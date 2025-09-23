import math
from functools import reduce

#n + k^2 = m^2!!
def factors(n):
        step = 2 if n%2 else 1
        return set(reduce(list.__add__,
                    ([i, n//i] for i in range(1, int(math.sqrt(n))+1, step) if n % i == 0)))

def main():
    n = int(input())
    all_fac = factors(n)