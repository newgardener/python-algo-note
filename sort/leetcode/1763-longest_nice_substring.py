# %%
"""
Brute-Force Solution
Time Complexity: O(N^2)
go through every possible substring and check if it's nice substring
"""


def longestNiceSubstring(s: str) -> str:
    N = len(s)
    start = 0
    maxLen = 0

    for i in range(N):
        seen = set()
        missing = 0
        for j in range(i, N):
            if s[j] not in seen:
                seen.add(s[j])
                if s[j].lower() not in seen or s[j].upper() not in seen:
                    missing += 1
                else:
                    missing -= 1

            if missing == 0 and (j - i + 1) > maxLen:
                start = i
                maxLen = j - i + 1

    return s[start : start + maxLen]


# %%
"""
Divide and Conquer Solution
Time Complexity: O(NlogN)
- create two subproblems whose size are reduced to N/2 => O(NlogN)
- in worst case scenario, O(N^2)
"""


def longestNiceSubstring(s: str) -> str:
    def divideAndConquer(s: str) -> str:
        if not s or len(s) < 2:
            return ""

        for i in range(len(s)):
            if s[i].lower() not in s or s[i].upper() not in s:
                left = divideAndConquer(s[:i])
                right = divideAndConquer(s[i + 1 :])
                if len(left) >= len(right):
                    return left
                else:
                    return right
        # nice str
        return s

    return divideAndConquer(s)


# %%
"""
Ideal Divide and Conquer Solution
Important Take-Away: the depth of recursion tree is bounded by the number of unique characters in the string
Time Complexity: O(26*N) -> O(N) linear time comparative to length of s
- identify "not nice" characters at each recursion tree
- at most 26 levels of recursion and each level involves O(n) work => O(26*N), which simplifies to O(N)
"""


def longestNiceSubstring(s: str) -> str:
    def divideAndConquer(i: int, j: int):
        if j - i + 1 < 2:
            return (0, -1)

        # find all unpaired characters in O(N)
        hashSet = set()
        for k in range(i, j + 1):
            hashSet.add(s[k])

        parts = [i - 1]
        for k in range(i, j + 1):
            if s[k].lower() not in hashSet or s[k].upper() not in hashSet:
                parts.append(k)
        parts.append(j + 1)

        maxLenPair = (0, -1)
        # nice substr
        if len(parts) == 2:
            return (i, j)
        for i in range(len(parts) - 1):
            ni, nj = divideAndConquer(parts[i] + 1, parts[i + 1] - 1)
            if nj - ni + 1 > maxLenPair[1] - maxLenPair[0] + 1:
                maxLenPair = (ni, nj)
        return maxLenPair

    l, r = divideAndConquer(0, len(s) - 1)
    return s[l : r + 1]
