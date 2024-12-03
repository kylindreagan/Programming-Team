class Solution:
    def partitionString(self, s: str) -> int:
        substring = ""
        total = 0
        for i in s:
            if i not in substring:
                substring += i
            else:
                substring = i
                total += 1
        return total + 1