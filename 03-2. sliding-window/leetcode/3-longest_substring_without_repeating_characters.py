def lengthOfLongestSubstring(s: str) -> int:
    if not s:
        return 0

    maxLen = 0
    i, j = 0, 0
    subset = set([])
    while i < len(s) and j < len(s):
        if s[j] not in subset:
            subset.add(s[j])
        else:
            maxLen = max(maxLen, j - i)
            while s[i] != s[j]:
                i += 1
            i += 1
            subset = set([ch for ch in s[i : j + 1]])
        j += 1
    return max(maxLen, j - i)
