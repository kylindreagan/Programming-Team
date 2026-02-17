from queue import Queue

def DFA_finite(dfa, symbols, start, final_states, n):
    can_reach_final = [False for _ in range(n+1)]  # 1-indexed
    # Reverse the DFA to find what can reach final states
    reverse_dfa = {i+1: {symb: [] for symb in symbols} for i in range(n)}
    for state in range(1, n+1):
        for symb in symbols:
            next_state = dfa[state][symb]
            reverse_dfa[next_state][symb].append(state)
    
    q = Queue()
    for final in final_states:
        can_reach_final[final] = True
        q.put(final)
    
    while not q.empty():
        curr = q.get()
        for symb in symbols:
            for prev_state in reverse_dfa[curr][symb]:
                if not can_reach_final[prev_state]:
                    can_reach_final[prev_state] = True
                    q.put(prev_state)
    
    visited = [False for _ in range(n+1)]
    in_stack = [False for _ in range(n+1)]
    
    def has_cycle_with_final(state):
        visited[state] = True
        in_stack[state] = True
        
        for symb in symbols:
            next_state = dfa[state][symb]
            if can_reach_final[next_state]:  # Only care if next state can reach final
                if not visited[next_state]:
                    if has_cycle_with_final(next_state):
                        return True
                elif in_stack[next_state]:
                    # Found a cycle that can reach final states
                    return True
        
        in_stack[state] = False
        return False
    
    if has_cycle_with_final(start):
        return False  #infinite
    else:
        return True   #finite

n, c, s, f = map(int, input().split())

alphabet = list(input())
travel_dict = {p+1:{x:None for x in alphabet} for p in range(n)}
final = set(int(x) for x in input().split())

for i in range(n):
    next_nodes = input().split()
    for j in range(c):
        travel_dict[i+1][alphabet[j]] = int(next_nodes[j])

if DFA_finite(travel_dict, alphabet, s, final, n):
    print("finite")

else:
    print("infinite")