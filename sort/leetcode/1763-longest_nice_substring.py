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
