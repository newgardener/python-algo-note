from collections import Counter

"""
Point: we don't need to consider about s1 permutation string order
maintain the window size as a length of s1 and make sure all characters required are included

Time Complexity: O(26*N)
"""


def checkInclusion(s1: str, s2: str) -> bool:
    if len(s1) > len(s2):
        return False

    required = Counter(s1)
    i, j = 0, len(s1) - 1
    while j < len(s2):
        window = s2[i : j + 1]
        if Counter(window) == required:
            return True
        i += 1
        j += 1
    return False


"""
Enhanced Solution
Time Complexity: O(N)
"""


def enhancedCheckInclusion(s1: str, s2: str) -> bool:
    len1, len2 = len(s1), len(s2)
    if len1 > len2:
        return False

    # character a to z
    counts1 = [0] * 26
    counts2 = [0] * 26

    for ch in s1:
        counts1[ord(ch) - ord("a")] += 1

    for i in range(len2):
        counts2[ord(s2[i]) - ord("a")] += 1
        if i >= len1:
            counts2[ord(s2[i]) - ord("a")] -= 1
        if counts1 == counts2:
            return True
    return False
