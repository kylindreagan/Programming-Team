n, m = map(int, input().split())
x = "".join(str(i) for i in range(n, m + 1))
print(sum(int(c) for c in x)%9)