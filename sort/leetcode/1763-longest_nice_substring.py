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
