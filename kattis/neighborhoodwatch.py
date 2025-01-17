from typing import List
def calculate_safety_rating(n:int, k:int, watch_houses):
    if k == 0:
        return 0  # No walk is safe if there are no watch houses

    safety_rating = n*(n+1)//2
    curr_unsafe = 0
    for house in watch_houses.keys():
        if watch_houses[house] == False:
            safety_rating -= (1 + curr_unsafe)
            curr_unsafe += 1
        else:
            curr_unsafe = 0
    return safety_rating

n, k = map(int, input().split())
watch_houses = {i+1:False for i in range(n)}
for i in range(k):
    watch_houses[int(input())] = True

print(calculate_safety_rating(n, k, watch_houses))

