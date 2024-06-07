import math
from typing import List


def minEatingSpeed(piles: List[int], h: int) -> int:
    l, r = 1, max(piles)
    while l <= r:
        mid = (l + r) // 2
        minH = sum(list(map(lambda x: math.ceil(x / mid), piles)))
        if minH <= h:
            r = mid - 1
        else:
            l = mid + 1
    return l
