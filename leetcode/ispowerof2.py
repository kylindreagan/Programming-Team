from math import*
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:
            return False
        x = log(n,2)
        print(x)
        return 2**floor(x) == n