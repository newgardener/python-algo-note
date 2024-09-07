# %%
# DFS + Memoization


def findMaxForm(self, strs: list[str], m: int, n: int) -> int:
    size = len(strs)
    memo = {}

    def dfs(i, _m, _n):
        if i >= size:
            return 0

        skip = dfs(i + 1, _m, _n)
        zeroes = strs[i].count("0")
        ones = strs[i].count("1")
        if zeroes <= _m and ones <= _n:
            not_skip = dfs(i + 1, _m - zeroes, _n - ones)
            memo[(i, _m, _n)] = max(skip, not_skip)
        else:
            memo[(i, _m, _n)] = skip
        return memo[(i, _m, _n)]

    return dfs(0, m, n)
