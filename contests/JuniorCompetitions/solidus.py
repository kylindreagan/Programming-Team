from math import gcd
n, _, d = int(input()), input(), int(input())
s = gcd(n, d)
n, d = n//s, d//s
if d < 0: n, d = -n, -d
print(f"{n}" if d == 1 else f"{n}/{d}")