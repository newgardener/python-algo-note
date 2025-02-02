# %%
def numDecodingsRecursive(s: str) -> int:
    n = len(s)

    def dfs(i):
        if i == n:
            return 1
        if s[i] == "0":
            return 0

        res = dfs(i + 1)
        if i < n - 1 and (s[i] == "1" or s[i] == "2" and s[i + 1] in "0123456"):
            res += dfs(i + 2)
        return res

    return dfs(0)


# %%
def numDecodingsTopDown(s: str) -> int:
    dp = {len(s): 1}

    def dfs(i):
        # caching
        if i in dp:
            return dp[i]
        # base case
        if s[i] == "0":
            return 0

        # default choice
        res = dfs(i + 1)
        # possible choice if two digits are in range of 1-26
        if i + 1 < len(s) and (s[i] == "1" or s[i] == "2" and s[i + 1] in "0123456"):
            res += dfs(i + 2)
        dp[i] = res
        return res

    return dfs(0)
