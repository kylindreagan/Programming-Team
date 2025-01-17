from typing import List
def calculate_safety_rating(n:int, k:int, watch_houses: List[bool]) -> int:
    if k == 0:
        return 0  # No walk is safe if there are no watch houses

    safety_rating = n*(n+1)//2
    curr_unsafe = 0

    for house in range(n):
        if not watch_houses[house]:
            curr_unsafe += 1
            safety_rating -= curr_unsafe
        else:
            curr_unsafe = 0
    return safety_rating

n, k = map(int, input().split())
watch_houses = [False for _ in range(n)]
for i in range(k):
    watch_houses[int(input())-1] = True

print(calculate_safety_rating(n, k, watch_houses))

