from typing import*
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        running_total = 0
        curr_min = float('inf')
        for i in prices:
            curr_min = min(curr_min, i)
            curr_best = max(curr_best, i-curr_min)
        return curr_best