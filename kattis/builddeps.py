global nodeToNum

def topologicalSort(adj,v):
    # Stack to store the result
    stack = []
    visited = [False for _ in range(n)]
    
    # Call the recursive helper function to store
    # Topological Sort starting from all vertices one by
    # one
    topologicalSortUtil(v, adj, visited, stack)
    return stack

def topologicalSortUtil(v, adj, visited, stack):
    # Mark the current node as visited
    visited[nodeToNum[v]] = True
    # Recur for all adjacent vertices
    for i in adj[v]:
        if not visited[nodeToNum[i]]:
            topologicalSortUtil(i, adj, visited, stack)
    # Push current vertex to stack which stores the result
    stack.append(v)
    
n = int(input())
rules = {}
nodeToNum = {}
for i in range(n):
    node, temp = map(str, input().split(":"))
    temp = temp.split()
    nodeToNum[node] = i
    for j in temp:
        if j not in rules.keys():
            rules[j] = set()
        rules[j].add(node)

Sinks = [rule for rule in nodeToNum.keys() if rule not in rules]
for sink in Sinks:
    rules[sink] = set()
changed = input()
stack = topologicalSort(rules, changed)
while len(stack) > 0:
    print(stack.pop())