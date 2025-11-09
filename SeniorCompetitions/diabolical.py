# CCSC 2025 #1: Diabolical
# --> Sudoku-like logic
#Written by Kylind and Nyugen

def dia4(M, p):
    return (M[0][0] + M[0][1]) + M[1][0] + M[1][1] == p == M[0][2] + M[0][3] + M[1][3] + M[1][2] == M[2][0] + M[2][1] + \
        M[3][0] + M[3][1] == M[2][2] + M[2][3] + M[3][2] + M[3][3]

def dia8(M, p):
    q1 = 0
    q2 = 0
    q3 = 0
    q4 = 0
    for i in range(4):
        for j in range(4):
            q1 += M[i][j]
            q2 += M[i + 4][j]
            q3 += M[i][j + 4]
            q4 += M[i + 4][j + 4]
    return q1 == q2 == q3 == q4 == p

def magic(M, n):
    r, c = [None for _ in range(n)], [None for _ in range(n)]
    for i in range(n):
        r[i] = sum(M[i])
    for i in range(n):
        x = 0
        for j in range(n):
            x += M[j][i]
        c[i] = x
    d1, d2 = 0, 0
    for i in range(n):
        d1 += M[i][i]
        d2 += M[(n - i) - 1][i]
    return d1 == d2 and all(x == d1 for x in r) and all(x == d2 for x in c), d1


for i in range(int(input())):
    d = False
    n = int(input())
    M = [[int(x) for x in input().strip().split()] for _ in range(n)]
    is_magic, p = magic(M, n)
    if is_magic:
        if n == 4:
            d = dia4(M, p)
        if n == 8:
            d = dia8(M, p)
    if d:
        print(f"Matrix #{i + 1} is diabolical.")
    elif is_magic:
        print(f"Matrix #{i + 1} is magic.")
    else:
        print(f"Matrix #{i + 1} is not magic.")
    print()