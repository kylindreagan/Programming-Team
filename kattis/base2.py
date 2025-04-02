def flog2(n):
    return n.bit_length() - 1

def binpal(n, cache={1:0, 2:1, 3:3}):
    if n in cache:
        return cache[n]

    k = flog2(n - 1)
    b = 1 << k
    a, c = b >> 1, b << 1

    if n == c:
        p, q, m = 0, 0, 1
    elif b < n < a + b:
        i = n - b
        logi = flog2(i)
        p, q, m = k - logi - 1, 2, (1 << logi) + i
    elif n == a + b:
        p, q, m = 0, 1, 1
    else:
        #a + b < n < c
        i = n - a - b
        logi = flog2(i)
        p, q, m = k - logi - 1, 1, (2 << logi) + i

    result = (1 << (2*k - q)) + 1 + (1 << p) * binpal(m)
    cache[n] = result
    return result

def palgenbase2(): 
    ''' generator of binary palindromes '''
    yield 0
    x, n, n2 = 1, 1, 2
    while True:
        for y in range(n, n2):
            s = format(y, 'b')
            yield int(s+s[-2::-1], 2)
        for y in range(n, n2):
            s = format(y, 'b')
            yield int(s+s[::-1], 2)
        x += 1
        n *= 2
        n2 *= 2

gen = palgenbase2()

n = int(input())
for i in range(n+1):
    b = next(gen)

print(b)