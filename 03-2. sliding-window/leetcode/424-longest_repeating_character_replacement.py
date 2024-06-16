"""
Time Complexity: O(26*N)
=> size of window - most frequent character <= k
each time we need to scan through the hash map to find the most frequent character
this leads to time complexity O(26*N)

Further
how to optimize the time complexity to O(N)?
"""


def characterReplacement(s: str, k: int) -> int:
    i, result = 0, 0
    count = {}
    for j in range(len(s)):
        count[s[j]] = 1 + count.get(s[j], 0)
        while (j - i + 1) - max(count.values()) > k:
            count[s[i]] -= 1
            i += 1
        result = max(result, j - i + 1)
    return result
