from math import sqrt
from functools import reduce

class Solution:
    def kthFactor(n: int, k: int) -> int:
        all_factors = list(Solution.factors(n))
        all_factors.sort()
        return -1 if len(all_factors) < k else all_factors[k-1]

    def factors(n):
        step = 2 if n%2 else 1
        return set(reduce(list.__add__,
                    ([i, n//i] for i in range(1, int(sqrt(n))+1, step) if n % i == 0)))