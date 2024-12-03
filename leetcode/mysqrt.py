class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0 or x == 1:
            return x
        low = 2
        high = 2**31 - 1
        mid = low + (high-low) // 2
        while low <= high:
            curr = mid * mid
            if x == curr:
                return mid
            if x < curr:
                high = mid-1
                mid = low + (high-low) // 2
            if x > curr:
                low = mid+1
                mid = low + (high-low) // 2
        return mid