import heapq
from collections import Counter

from typing import List


def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
    counts = Counter(hand)
    minH = list(counts.keys())
    heapq.heapify(minH)  # in order to find a min num at a time

    while minH:
        start = minH[0]
        for num in range(start, start + groupSize):
            if num not in counts:
                return False
            counts[num] -= 1
            if counts[num] == 0:
                # it creates a hole in between some values
                # for example { 1: 1, 2: 0, 3: 1}
                if num != minH[0]:
                    return False
                heapq.heappop(minH)

    return True
