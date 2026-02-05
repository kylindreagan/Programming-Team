def DFA_BFS(dfa, word, s, f):
    curr = s
    for letter in word:
        curr = dfa[curr][letter]
    return curr in f


n,c,s,f = map(int, input().split())
alphabet = list(input())
travel_dict = {p+1:{x:None for x in alphabet} for p in range(n)}
end_states = [int(x) for x in input().split()]

for i in range(n):
    next_nodes = input().split()
    for j in range(c):
        travel_dict[i+1][alphabet[j]] = int(next_nodes[j])

for _ in range(int(input())):
    word = input()
    if f == n:
        print("accept")
    elif f == 0:
        print("reject")
    elif DFA_BFS(travel_dict, word, s, end_states):
        print("accept")
    else:
        print("reject")