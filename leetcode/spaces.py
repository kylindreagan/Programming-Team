from typing import List
class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        space_set = set(spaces)
        result = []
        for i, char in enumerate(s):
            if i in space_set:
                result.append(" ")
            result.append(char)
        return "".join(result)