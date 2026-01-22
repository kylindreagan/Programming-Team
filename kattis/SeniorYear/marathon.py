def probability_all_above(m):
    prob = 1.0
    for a, b in all_times:
        if m <= a:
            p_i = 1.0
        elif m >= b:
            p_i = 0.0
        else:
            p_i = (b - m) / (b - a)
        prob *= p_i
    return prob

total_interval = 0
all_times = []
high, low = float('-inf'), float('inf')
for i in range(int(input())):
    start, end = map(float, input().split())
    total_interval += end - start
    all_times.append((start, end))
    if end > high:
        high = end
    if start < low:
        low = start

target = total_interval / 2
while True:
    mid = (high + low) / 2
    curr_length = 0
    prob = probability_all_above(mid)
    
    if abs(prob - .5) < 1e-10:
        break

    if prob > .5:
        low = mid
    else:
        high = mid

print((high + low) / 2)