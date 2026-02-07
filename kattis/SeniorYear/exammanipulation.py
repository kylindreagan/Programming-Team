n, k = map(int, input().split())
students = [input().strip() for _ in range(n)]

best = 0

for mask in range(1 << k):
    key = []
    for i in range(k):
        if mask & (1 << i):
            key.append('T')
        else:
            key.append('F')
    key = ''.join(key)

    lowest = k
    for s in students:
        score = sum(1 for i in range(k) if s[i] == key[i])
        lowest = min(lowest, score)

    best = max(best, lowest)

print(best)
