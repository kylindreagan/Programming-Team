MOD = 1000000007

class Solution:
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