from collections import deque

q = deque(input())
new = []
while q:
    c = q.popleft()
    if c == "<":
        if new:  
            new.pop()  
    else:
        new.append(c)  
print("".join(new))