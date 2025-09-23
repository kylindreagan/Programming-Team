import math

def binom(n, k):
    """Returns n choose k, for nonnegative integer n and k"""
    assert k >= 0
    assert n >= 0
    assert k == int(k)
    assert n == int(n)
    k = min(k, n - k)
    ans = 1
    for i in range(k):
        ans *= n - i
        ans //= i + 1
    return ans

def first_over(k, c):
    """Binary search to find smallest value of n for which n^k >= c"""
    n = 1
    while n ** k < c:
        n *= 2
    # Invariant: lo**k < c <= hi**k
    lo = 1
    hi = n
    while hi - lo > 1:
        mid = lo + (hi - lo) // 2
        if mid ** k < c:
            lo = mid
        else:
            hi = mid
    assert hi ** k >= c
    assert (hi - 1) ** k < c
    return hi

def find_n_k(x):
    """Given x, yields all n and k such that binom(n, k) = x."""
    assert x == int(x)
    assert x > 1
    k = 0
    while True:
        k += 1
        # https://math.stackexchange.com/a/103385/205
        if (2 * k + 1) * x <= 4**k:
            break
        nmin = first_over(k, math.factorial(k) * x)
        nmax = nmin + k + 1
        nmin = max(nmin, 2 * k)
        choose = binom(nmin, k)
        for n in range(nmin, nmax):
            if choose == x:
                yield (n, k)
                if k < n - k:
                    yield (n, n - k)
            choose *= (n + 1)
            choose //= (n + 1 - k)

#10000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
X = int(input())

if X == 1:
    print(0,0)
    quit()

allCombs = []

for (n, k) in find_n_k(X):
    allCombs.append((n,k))

final = min(allCombs)

print(final[0], final[1])