"""
Time Complexity: O(26*N)
=> size of window - most frequent character <= k
each time we need to scan through the hash map to find the most frequent character
this leads to time complexity O(26*N)

Further
how to optimize the time complexity to O(N)?
=> store mostFrequent in a constant time
=> the purpose of this problem is to maximize the size of window which means we do not need to update mostFrequent when window size shrinks
"""


def characterReplacement(s: str, k: int) -> int:
    i, result = 0, 0
    count = {}
    mostFrequent = 0
    for j in range(len(s)):
        count[s[j]] = 1 + count.get(s[j], 0)
        mostFrequent = max(mostFrequent, count[s[j]])
        while (j - i + 1) - mostFrequent > k:
            count[s[i]] -= 1
            i += 1
        result = max(result, j - i + 1)
    return result
