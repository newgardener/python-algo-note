class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)
        memo = {}

        def dp(i, j):
            # base case
            if i >= m and j >= n:
                return True
            if j >= n:
                return False
            if i >= m:
                # able to discard rest of pattern substring as they are wildcard pairs
                return (j - n) % 2 == 0 and all(p[k] == "*" for k in range(j + 1, n, 2))

            # pattern matching logic
            # "." matches every character
            if s[i] == p[j] or p[j] == ".":
                # if next character is a wild card
                if j < n - 1 and p[j + 1] == "*":
                    # case 1 - continue matching with the same character
                    # case 2 - skip a wild card pair (=wild card matches zero or more of the preceding element)
                    memo[(i, j)] = dp(i + 1, j) or dp(i, j + 2)
                else:
                    # match one character each
                    memo[(i, j)] = dp(i + 1, j + 1)
            else:
                # skip a wild card pair
                if j < n - 1 and p[j + 1] == "*":
                    memo[(i, j)] = dp(i, j + 2)
                else:
                    return False
            return memo[(i, j)]

        return dp(0, 0)
