def one_to_n(x):
    if x % 4 == 0:
        return x
    if x % 4 == 1:
        return 1
    if x % 4 == 2:
        return x + 1
    return 0

n = int(input())
a, b = map(int, input().split())
c = one_to_n(b) ^ one_to_n(a-1)
if c == 0:
    print("Enginn")
elif c > n:
    print("Gunnar")
else:
    print(c)