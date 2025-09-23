from math import pow

dist, skips = int(input()), int(input())

total_dist = dist* (1-pow(2, -skips))

print(total_dist+dist)