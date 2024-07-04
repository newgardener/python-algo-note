from typing import List


def findLongestChain(pairs: List[List[int]]) -> int:
    pairs.sort(key=lambda x: x[1])
    result = []
    for i in range(len(pairs)):
        if not result or result[-1][1] < pairs[i][0]:
            result.append(pairs[i])
    return len(result)
