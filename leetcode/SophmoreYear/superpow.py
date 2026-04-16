from typing import List
MOD = 1337

class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        expo = int("".join(map(str, b)))
        return self.myPow(a, expo)

    def myPow(self, x: float, n: int) -> float:
        result = 1
        if n == 0:
            return 1
        if n < 0:
            power = n * -1
        else:
            power = n
        
        if x == 0:
            return 0
        elif x < 0:
            base = x * -1
        else:
            base = x
        while power > 0:
            # If power is odd
            if power % 2 == 1:
                result = (result * base) % MOD

            # Divide the power by 2
            power = power // 2
            # Multiply base to itself
            base = (base * base) % MOD
        if x < 0 and n % 2 != 0:
            result *= -1
        return result if n > 0 else 1/result