class diagonals:
    def __init__(self, board):
        self.N = 8
        self.board = board
    
    def UR(self, rindex, cindex):
        currCol = cindex - 1
        currRow = rindex + 1
        while currRow < 7 and currCol >= 0:
            if self.board[currRow][currCol] == "*":
                return False
            currRow += 1
            currCol -= 1
        
        return True 
    
    def UL(self, rindex, cindex):
        currCol = cindex - 1
        currRow = rindex - 1
        while currRow >= 0 and currCol >= 0:
            if self.board[currRow][currCol] == "*":
                return False
            currRow -= 1
            currCol -= 1
        
        return True 
    
    def LR(self, rindex, cindex):
        currCol = cindex + 1
        currRow = rindex + 1
        while currRow < 7 and currCol < 7:
            if self.board[currRow][currCol] == "*":
                return False
            currRow += 1
            currCol += 1
        
        return True 
    
    def LL(self, rindex, cindex):
        currCol = cindex + 1
        currRow = rindex - 1
        while currRow >= 0 and currCol < 7:
            if self.board[currRow][currCol] == "*":
                return False
            currRow -= 1
            currCol += 1
        
        return True 

board = [[*input()] for _ in range(8)]
D = diagonals(board)

cols = []

for i in range(len(board)):
    queen = [x for x,y in enumerate(board[i]) if y =="*"]
    if len(queen) != 1:
        print("invalid")
        quit()
    Qidx = queen[0]
    if Qidx in cols:
        print("invalid")
        quit()
    cols.append(Qidx)
    if not D.UR(i,Qidx) or not D.UL(i,Qidx) or not D.LR(i,Qidx) or not D.LL(i,Qidx):
        print("invalid")
        quit()
    
print("valid")