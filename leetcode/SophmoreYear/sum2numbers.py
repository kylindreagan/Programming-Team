from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numstoindex = {}
        for i, num in enumerate(nums):
            compliment = target - num
            if compliment in numstoindex:
                return numstoindex[compliment],i
            numstoindex[num] = i
        return