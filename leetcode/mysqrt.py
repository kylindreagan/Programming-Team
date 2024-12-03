class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0 or x == 1:
            return x
        start = 2
        while True:
            if x < start * start:
                return start - 1
            start += 1