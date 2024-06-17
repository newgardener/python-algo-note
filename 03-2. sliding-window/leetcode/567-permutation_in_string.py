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
