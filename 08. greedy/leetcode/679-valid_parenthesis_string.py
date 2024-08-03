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


# %%
class Solution:
    def checkValidString(self, s: str) -> bool:
        dp = {(len(s), 0): True}  # (index, left parenthesis count)

        def dfs(i, left):
            # check whether left < 0
            # in order to early-return invalid case like )(*
            if i == len(s) or left < 0:
                return left == 0
            if (i, left) in dp:
                return dp[(i, left)]

            if s[i] == "(":
                dp[(i, left)] = dfs(i + 1, left + 1)
            elif s[i] == ")":
                dp[(i, left)] = dfs(i + 1, left - 1)
            else:
                # in wild card case, we have three choices - left, None, right
                dp[(i, left)] = dfs(i + 1, left + 1) or dfs(i + 1, left) or dfs(i + 1, left - 1)
            return dp[(i, left)]

        return dfs(0, 0)
