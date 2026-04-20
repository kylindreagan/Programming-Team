#https://open.kattis.com/problems/oddaevenb
MOD = 10**9 + 7
from functools import lru_cache

@lru_cache()
def A(n):
    if n == 0:
        return 1
    if n < 0:
        return 0
    total = 0
    for o in range(1, n+1, 2):
        total = (total + B(n - o)) % MOD
    return total

@lru_cache()
def B(n):
    if n == 0:
        return 1
    if n < 0:
        return 0
    total = 0
    for e in range(2, n+1, 2):
        total = (total + A(n - e)) % MOD
    return total

n = int(input())
print((A(n)+B(n)) % MOD)