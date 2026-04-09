n = int(input())
prices = [int(x) for x in input().split()]
m = int(input())
orders = [int(x) for x in input().split()]

# M is the largest order value
M = max(orders)

dp = [0] * (M + 1)
dp[0] = 1

# parent[s] = last item index used to reach sum s (only valid if unique)
parent = [-1] * (M + 1)

for i in range(n):
    cost = prices[i]
    for s in range(cost, M + 1):
        if dp[s - cost] > 0:
            if dp[s] == 0:
                # first way to form sum s
                dp[s] = dp[s - cost]
                parent[s] = i
            else:
                # already had a way → now ambiguous
                dp[s] = 2

            if dp[s - cost] == 2:
                dp[s] = 2

# Process each order
for target in orders:
    if dp[target] == 0:
        print("Impossible")
    elif dp[target] == 2:
        print("Ambiguous")
    else:
        # reconstruct unique solution
        res = []
        cur = target
        while cur > 0:
            i = parent[cur]
            res.append(i + 1)  # 1-based index
            cur -= prices[i]

        res.sort()
        for i in range(len(res)):
            if i != 0:
                print(' ',end='') 
            print(res[i], end='') 
        print()