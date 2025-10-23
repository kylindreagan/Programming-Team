from queue import Queue
from copy import deepcopy

def press(x,y, keypad):
    new_keypad = deepcopy(keypad)
    for i in range(3):
        new_keypad[y][i] = (1+new_keypad[y][i])%4
        new_keypad[i][x] = (new_keypad[i][x]+1)%4
    new_keypad[y][x] = (new_keypad[y][x] - 1) % 4
    return new_keypad

def ratInASafe(init_keypad):
    min_moves = float('inf')
    Q = Queue()
    visited = set()
    Q.put((init_keypad,0))
    visited.add(tuple(tuple(row) for row in init_keypad))
    
    while not Q.empty():
        curr_keypad, moves = Q.get()
        
        if all(element == 0 for row in curr_keypad for element in row):
            min_moves = min(moves, min_moves)
        
        for i in range(3):
            for j in range(3):
                temp = press(i,j,curr_keypad)
                new_state = tuple(tuple(row) for row in temp)
                if new_state not in visited:
                    Q.put((temp, moves + 1))
                    visited.add(new_state)
    
    return min_moves if min_moves != float('inf') else -1

keypad = [[int(x) for x in input().split()] for _ in range(3)]
moves = ratInASafe(keypad)
print(moves)
