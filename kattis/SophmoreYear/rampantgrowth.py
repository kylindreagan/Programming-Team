r, c = map(int, input().split())
n = r; r -= 1
for i in range(c-1):
    n *= r
    n = n % 998244353
print(n)
