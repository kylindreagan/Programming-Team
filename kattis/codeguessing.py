p,q = map(int, input().split())

b,d = None, None

pos = input()
init = 0
if q - p == 3 and pos == "ABBA":
    print(p + 1, q - 1)
    quit()
if pos[0] == "B":
    b = list(range(1,p))
    if pos[1] == "B":
        d = list(range(b,p))
if pos[3] == "B":
    d = list(range(q,9))
    if pos[2] == "B":
        b = list(range(q,d))

if b == None:
    if len(d) != 1:
        print(-1)
        quit()
    else:
        b = list(range(p,q))

if d == None:
    if len(d) != 1:
        print(-1)
        quit()
    else:
        b = list(range(p,q))

if len(b) == len(d) == 1:
    print(b[0],d[0])

if len(b) == 1 != len(d) == 1:
    if any(i in b for i in d):
        small, big = min([b,d], key=len), max([b,d], key=len)
        if len(small) == len(big) == 1:
            print(small[0], big[0])

else:
    print(-1)