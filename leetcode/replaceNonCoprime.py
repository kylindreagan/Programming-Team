from typing import*
import math

class Solution:
    def replaceNonCoprimes(self, nums: List[int]) -> List[int]: 
        stack = []
        for num in nums:
            while stack:
                g = math.gcd(stack[-1], num)
                if g != 1:
                    num = stack[-1] * num // g
                    stack.pop()
                else:
                    break
            stack.append(num)
        
        return stack