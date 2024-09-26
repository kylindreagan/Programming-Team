from math import comb

MOD = 10**9+7
for _ in range(int(input())):
    R, C = map(int, input().split())
    
    outer_edges = R * 2 + C * 2
    inner_edges = R * (C - 1) + C * (R - 1)
    NumBoxes = R * C
    SquareComb = 18 #18 ways to arrange 3 colors per box
    print(SquareComb*NumBoxes*(3**(R-1)*(3**(C-1)))%MOD)
    