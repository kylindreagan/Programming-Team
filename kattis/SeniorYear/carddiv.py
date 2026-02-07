n, m = map(int, input().split())
print(((n + m) * (m - n + 1) // 2) % 9)