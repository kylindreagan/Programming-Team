#Kahn's Algorithm (Topological sort)

from math import*
from typing import*
from collections import deque

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        #Number of edges directed into a vertex in a directed graph
        indegree = [[0] * n for _ in range(m)]
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        for i in range(m):
            for j in range(n):
                for dx, dy in dirs:
                    #Next 'step'
                    si, sj = i+dx, j+dy
                    if 0 <= si < m and 0 <= sj < n and matrix[si][sj] < matrix[i][j]:
                        indegree[i][j] += 1
        
        # Start with cells of zero indegree
        q = deque([[x, y] for x in range(m) for y in range(n) if indegree[x][y] == 0])

        max_path = 0
        while q:
            for _ in range(len(q)):
                i,j = q.popleft()
                for dx,dy in dirs:
                    si, sj = i + dx, j + dy
                    if 0 <= si < m and 0 <= sj < n and matrix[si][sj] > matrix[i][j]:
                        indegree[si][sj] -= 1
                        if indegree[si][sj] == 0:
                            q.append((si, sj))
            max_path += 1
        return max_path