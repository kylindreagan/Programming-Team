from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        low_row = 0
        high_row = m-1
        mid_row = low_row+(high_row-low_row)//2
        #Row search
        while low_row <= high_row:
            mid = matrix[mid_row][0]
            if target == mid:
                return True
            if mid < target:
                low_row = mid_row+1
                mid_row = low_row+(high_row-low_row)//2
            if mid > target:
                high_row = mid_row-1
                mid_row = low_row+(high_row-low_row)//2
        #Col search
        low_col = 0
        high_col = n-1
        while low_col <= high_col:
            mid_col = low_col+(high_col-low_col)//2
            mid = matrix[mid_row][mid_col]
            if target == mid:
                return True
            if mid < target:
                low_col = mid_col+1
            if mid > target:
                high_col = mid_col-1
        return False