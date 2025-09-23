import itertools

for i in range(int(input())):
    n, A, B, C, D, x0, y0, M = map(int, input().split())
    points = []
    X, Y = x0, y0
    points.append((x0, y0))
    for j in range(n-1):
        X = (A*X+B) % M
        Y = (C*Y+D) % M
        points.append((X, Y))
    total = set()
    triangles = itertools.combinations(points, 3)

    total = 0
    for triangle in triangles:
        p1, p2, p3 = triangle
        midpoint_x = (p1[0]+p2[0]+p3[0])/3
        midpoint_y = (p1[1]+p2[1]+p3[1])/3
        if midpoint_x == int(midpoint_x) and midpoint_y == int(midpoint_y):
            total += 1
    
    print(f"CASE #{i+1}: {total}")