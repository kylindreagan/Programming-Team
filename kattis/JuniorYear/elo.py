import heapq

def max_score_dfs(score, array, memory, biggest):
    max_score = score
    priority_queue = [-score]

    while priority_queue:
        local_score = -heapq.heappop(priority_queue)
        memory.add(local_score)
        for p in array:
            li, ri, ai = p
            if li <= local_score <= ri:
                new_score = local_score + ai
                if new_score in memory:
                    continue
                max_score = max(new_score, max_score)
                if new_score <= biggest:
                    heapq.heappush(priority_queue, -new_score)

    return max_score

players, elo = map(int, input().split())

elo_array= [tuple(map(int, input().split())) for _ in range(players)]

smallest = min(li for li,ri,ai in elo_array)
biggest = max(ri for li,ri,ai in elo_array)

if elo < smallest or elo > biggest:
    print(elo)
else:
    print(max_score_dfs(elo, elo_array, set(), biggest))