def lengthOfLongestSubstring(s: str) -> int:
    result = 0
    i, j = 0, 0
    subset = set([])

    while j < len(s):
        while s[j] in subset:
            subset.remove(s[i])
            i += 1
        result = max(result, j - i + 1)
        subset.add(s[j])
        j += 1

    return result
