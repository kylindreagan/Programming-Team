from math import comb

def find_num_bags(n):
    if n == 0:
        return 0
    group_size = n//4

    bags_needed = comb(group_size, 2) * 4
    return bags_needed + 4

n = int(input())
print(find_num_bags(n))
