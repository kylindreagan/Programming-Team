def neighborhood_paths(n, valid, distances):
    all_possible = (n*(n+1))//2 + len(valid)

    for distance in distances:
        all_possible -= (distance*(distance-1))//2

    return all_possible

total_houses, num_safe = map(int, input().split())
safe_houses = set()
distance = []

for i in range(num_safe):
    watch = int(input())
    safe_houses.add(watch)
    if i == 0:
        prev = watch
    else:
        distance.append(watch-prev)
        prev = watch

print(neighborhood_paths(total_houses, safe_houses,distance))
