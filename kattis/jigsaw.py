def area_from_perimeter(p, m):
    lw = p//2
    estStart = int(m ** .5)
    for i in range(estStart, lw):
        j = lw - i
        if (i - 2) * (j - 2) == m:
            return i, j
    return None, None

c,e,m = map(int, input().split())
na = "impossible"

if c != 4:
    print(na)
elif m == 0:
    if e % 2 != 0:
        print(0)
        print(na)
    else:
        print(2, (e//2)+2)
else:
    perimeter = 8 + e
    l,w = area_from_perimeter(perimeter, m)
    if l == w == None:
        print(na)
    else:
        print(l,w)