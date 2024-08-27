import math

def sumOfDigitsFrom1ToN(x, n):
    if (n < 10):
        return (n * (n + 1)) // 2 - (x * (x + 1)) // 2
    d = int(math.log(n, 10))
    a = [0]*(d + 2)
    a[0] = 0
    a[1] = 45
    for i in range(2, d + 1):
        a[i] = a[i - 1] * 10 + 45 * int(math.ceil(pow(10, i - 1)))
    return sumOfDigitsFrom1ToNUtil(x, n, a)
 
def sumOfDigitsFrom1ToNUtil(x, n, a):
    total = 0
    count = 0
    tx = 0
    while True:
        if (n < 10):
            total += (n * (n + 1)) // 2
            return total
        d = int(math.log(n,10))
        p = int(math.ceil(pow(10, d)))
        msd = n // p 
        total += int(msd * a[d] + (msd * (msd - 1) // 2) * p + msd * (1 + n % p)) 
        n %= p
        print(x, count)
        if count == x - 1 and x > 1:
            print(count)
            total = 0
        count += 1

for i in range(int(input())):
    whole = False
    x, y = map(int, input().split())
    if x == y:
        print(y)
        continue
    if x == 0:
        x += 1
    totalA = sumOfDigitsFrom1ToN(x,y)
    print(totalA)