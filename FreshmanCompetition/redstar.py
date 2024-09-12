n = int(input())
total = []
for i in range(n):
    stops = int(input())
    total.append(stops)
total.reverse()
k = 0
p = 1
time = 0
if n % 2 == 0:
    for i in range(int(n / 2)):
        secs = total[k] - total[p]
        time += secs
        k += 2
        p += 2
    print(time)
else:
    print("still running")