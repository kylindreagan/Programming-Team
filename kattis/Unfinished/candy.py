import heapq

def min_swaps_to_front(boxes, F, T):
    N = len(boxes)

    indexed = [(boxes[i], i) for i in range(N)]

    indexed.sort(reverse=True)

    chosen = []
    candy_sum = 0
    index_sum = 0

    best_cost = float('inf')

    for candy, idx in indexed:
        heapq.heappush(chosen, (-idx, candy))
        candy_sum += candy
        index_sum += idx

        if len(chosen) > F:
            neg_idx, removed_candy = heapq.heappop(chosen)
            index_sum -= -neg_idx
            candy_sum -= removed_candy

        if len(chosen) == F and candy_sum >= T:
            cost = index_sum - F * (F - 1) // 2
            best_cost = min(best_cost, cost)

    return best_cost if best_cost != float('inf') else None

N, F, T = map(int, input().split())
boxes = list(map(int, input().split()))

if sum(boxes[:F]) >= T:
    print(0)
else:
    ans = min_swaps_to_front(boxes, F, T)
    if ans is None:
        print("NO")
    else:
        print(ans)
