from itertools import combinations

def smallestComb(nums, target_sum, combination_size):
    for indices in combinations(range(len(nums)), combination_size):
        combo_sum = sum(nums[i] for i in indices)
        if combo_sum >= target_sum:
            return indices
    return None

N, Nboxes, Sumcandy = map(int, input().split())
boxes = [int(x) for x in input().split()]
ogBox = sum(boxes[:Nboxes])

if ogBox >= Sumcandy:
    print(0)
elif N == Nboxes:
    print("NO")
elif Nboxes == 1:
    valid = [i for i, y in enumerate(boxes) if y >= Sumcandy]
    if not valid:
        print("NO")
    else:
        print(valid[0])
else:
    winning_combination = smallestComb(boxes, Sumcandy, Nboxes)
    if winning_combination is None:
        print("NO")
    else:
        # Calculate the difference between the found indices and the first Nboxes indices
        result = sum(winning_combination) - sum(range(Nboxes))
        print(result)
