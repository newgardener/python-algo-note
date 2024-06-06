import collections


def longestPalindrome(s: str) -> int:
    if len(s) == 1:
        return 1

    chDict = collections.defaultdict(int)
    for ch in s:
        chDict[ch] += 1

    mid, res = 0, 0
    for ch, cnt in chDict.items():
        if cnt >= 2:
            res += 2 * (cnt // 2)
        if cnt % 2 == 1:
            mid += 1
    return res + 1 if mid >= 1 else res
