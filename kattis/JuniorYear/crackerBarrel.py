from queue import Queue

def crackSearch(possible, board, target):
    visited =  set()
    desired = {'_', target}
    D = Queue()
    D.put(board)
    while not D.empty():
        curr = D.get()
        currColor = [c for c in curr.values()]
        if set(currColor) == desired:
            if currColor.count(target) == 1:
                return True
        if tuple(curr.items()) not in visited and target in currColor:
            visited.add(tuple(curr.items()))
            for num, peg in curr.items():
                if peg == "_":
                    continue
                currPossible = [i for i in possible[num]]
                newBoard = CBJump(currPossible, curr, num)
                if newBoard != []:
                    for k in newBoard:
                        D.put(k)
    return False


def CBJump(possible, board, node):
    T = []
    for j, k in possible:
        if board[j] != "_" and board[k] == '_':
            tempPeg = board[j]
            newBoard = board.copy()
            newBoard[k] = newBoard[node]
            newBoard[node] = newBoard[j] = "_"
            T.append(newBoard)
    return T

while True:
    peg = input()[0]
    if peg == "*":
        break
    graph = {
    0: [(1, 3), (2, 5)],
    1: [(3, 6), (4, 8)],
    2: [(4, 7), (5, 9)],
    3: [(1, 0), (4, 5), (6, 10), (7, 12)],
    4: [(7, 11), (8, 13)],
    5: [(4, 3), (8, 12), (9, 14)],
    6: [(3, 1), (7, 8)],
    7: [(4, 2), (8, 9)],
    8: [(4, 1), (7, 6)],
    9: [(5, 2), (8, 7)],
    10: [(6, 3), (11, 12)],
    11: [(7, 4), (12, 13)],
    12: [(7, 3), (8, 5), (11, 10), (13, 14)],
    13: [(8, 4), (12, 11)],
    14: [(9, 5), (13, 12)]
}
    temp = []
    for i in range(5):
        temp = temp + [y for x, y in  enumerate([*input().strip()]) if x % 2 == 0]
    board = {i:j for i,j in enumerate(temp)}
    validity = crackSearch(graph, board, peg)
    if validity:
        print("Possible")
    else:
        print("Impossible")