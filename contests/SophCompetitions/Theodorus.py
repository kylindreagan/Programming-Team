def nextvertex(x, y):
    h = (x**2 + y**2)**0.5
    return (x - y/h, y + x/h)

T = int(input())

for i in range(T):
    x = (int(input()))
    ans = nextvertex(x, x)
    print(ans)