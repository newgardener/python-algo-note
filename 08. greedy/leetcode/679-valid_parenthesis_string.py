# %%

"""
Greedy Solution
- Time Complexity: O(N)

Take-Away:
- manage left parenthesis count as a range => [leftMin, leftMax]
- if leftMin is 0 at the end, this ensures that there is a possible valid parenthesis case
"""


class Solution:
    def checkValidString(self, s: str) -> bool:
        leftMin, leftMax = 0, 0
        for ch in s:
            if ch == "(":
                leftMin, leftMax = leftMin + 1, leftMax + 1
            elif ch == ")":
                leftMin, leftMax = leftMin - 1, leftMax - 1
            else:
                leftMin, leftMax = leftMin - 1, leftMax + 1
            # early-return invalid parenthesis case
            if leftMax < 0:
                return False
            if leftMin < 0:
                leftMin = 0
        return leftMin == 0
