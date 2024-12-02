from Math import sqrt
class Solution:
    def fib(self, n:int):
        return int((((1+sqrt(5))**n)-((1-sqrt(5)))**n)/(2**n*sqrt(5)))