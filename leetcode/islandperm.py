from typing import List
from collections import deque

class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        img = [['0'] * (len(grid[0])+2)]
        for i in grid:
            img.append(['0'] + [str(x) for x in i] + ['0'])
        img.append(['0'] * (len(grid[0])+2))
        return Solution.floodFill(img,0,0,"-1")
    
    def floodFill(img, x, y, newClr):
        coast = 0
        q = deque()

        # Rows and columns of the display
        m = len(img)
        n = len(img[0])

        prevClr = img[x][y]
        if prevClr == newClr:
            return

        # Append the position of the starting pixel 
        # of the component
        q.append((x, y))
        print(img)
        img[x][y] = newClr

        # While the queue is not empty, i.e., the whole 
        # component having prevClr color
        # is not colored with newClr color
        while q:
            # Dequeue the front node
            x, y = q.popleft()

            # Check if the adjacent pixels are valid and enqueue
            if x + 1 < m and img[x + 1][y] == prevClr:
                img[x + 1][y] = newClr
                q.append((x + 1, y))
            elif x + 1 < m and img[x + 1][y] == '1':
                coast += 1
            if x - 1 >= 0 and img[x - 1][y] == prevClr:
                img[x - 1][y] = newClr
                q.append((x - 1, y))
            elif x - 1 >= 0 and img[x - 1][y] == '1':
                coast += 1
            if y + 1 < n and img[x][y + 1] == prevClr:
                img[x][y + 1] = newClr
                q.append((x, y + 1))
            elif y + 1 < n and img[x][y + 1] == '1':
                coast += 1
            if y - 1 >= 0 and img[x][y - 1] == prevClr:
                img[x][y - 1] = newClr
                q.append((x, y - 1))
            elif y - 1 >= 0 and img[x][y - 1] == '1':
                coast += 1
        
        return coast