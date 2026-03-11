intervals = []
for _ in range(int(input())):
    x,y = map(int, input().split())
    intervals.append((x,y))

interSort = sorted(intervals, key=lambda x:x[1], reverse=False)

f_i = interSort.pop(0)[1]
nonover = 1
for s, f in interSort:
    if f_i <= s:
        f_i = f
        nonover += 1

print(nonover)