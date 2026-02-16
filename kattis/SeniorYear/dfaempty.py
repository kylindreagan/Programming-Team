from queue import Queue

def DFA_empty(dfa, symbols, s, f, n):
    visited = [False for _ in range(n)]
    q = Queue()
    q.put(s)
    visited[s-1] = True
    while not q.empty():
        curr = q.get()
        for symb in symbols:
            temp = dfa[curr][symb]
            if temp in f:
                return False
            if not visited[temp-1]:
                q.put(temp)
                visited[temp-1] = True
    return True

n, c, s, f = map(int, input().split())

alphabet = list(input())
travel_dict = {p+1:{x:None for x in alphabet} for p in range(n)}
final = set(int(x) for x in input().split())

for i in range(n):
    next_nodes = input().split()
    for j in range(c):
        travel_dict[i+1][alphabet[j]] = int(next_nodes[j])

if DFA_empty(travel_dict, alphabet, s, final, n):
    print("empty")

else:
    print("non-empty")