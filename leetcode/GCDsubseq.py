from typing import*
import math

class Solution:
    def countDifferentSubsequenceGCDs(self, nums: List[int]) -> int:
        max_num = max(nums)
        occurance = [False for _ in range(max_num+1)]
        for num in nums:
            occurance[num] = True
        