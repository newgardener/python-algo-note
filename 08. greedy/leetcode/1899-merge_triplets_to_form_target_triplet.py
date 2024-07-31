from typing import List


def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
    filtered = [item for item in triplets if item[0] <= target[0] and item[1] <= target[1] and item[2] <= target[2]]
    if not filtered:
        return False

    good = set()
    for item in filtered:
        for i, v in enumerate(item):
            if v == target[i]:
                good.add(i)
            # early-return
            if len(good) == 3:
                return True
    return False
