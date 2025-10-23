import sys
sys.setrecursionlimit(300000)
MOD = 10**9 + 7

def treefs(u):
    dp0 = [0] * (m+1)
    dp0[0] = 1
    dp1 = [0] * (m + 1)
    if is_red[u]:
        dp1[1] = 1
    else:
        dp1[0] = 1
    subred = is_red[u]

    for v in children[u]:
        dp0_v, dp1_v, subred_v = treefs(v)
        subred += subred_v

        max_k = min(m, subred)
        new0 = [0] * (max_k + 1)
        new1 = [0] * (max_k + 1)
        for i in range(min(len(dp0), max_k + 1)):
            if dp0[i] == 0 and dp1[i] == 0:
                continue
            for j in range(min(len(dp0_v), max_k - i + 1)):
                if dp0_v[j] == 0 and dp1_v[j] == 0:
                    continue
                t = i + j
                if t > m:
                    break
                # u not chosen: child can be chosen or not
                new0[t] = (new0[t] + dp0[i] * (dp0_v[j] + dp1_v[j])) % MOD
                # u chosen: child root cannot be chosen
                new1[t] = (new1[t] + dp1[i] * dp0_v[j]) % MOD

        dp0 = new0
        dp1 = new1
    
    return dp0, dp1, subred

n, m = map(int, input().split())
children = [[] for _ in range(n)]
is_red = [0]*n
has_parent = [False] * n

for i in range(1,n):
    parent = int(input())-1
    children[parent].append(i)
    has_parent[i] = True

for _ in range(m):
    is_red[int(input())-1] = 1

roots = [node for node in range(n) if not has_parent[node]]

dp0, dp1, _ = treefs(0)
for i in range(m+1):
    print((dp0[i]+dp1[i])%MOD)