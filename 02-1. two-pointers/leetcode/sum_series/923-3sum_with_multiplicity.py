import math
from collections import Counter


def threeSumMulti(arr: list[int], target: int) -> int:
    arr.sort()
    counts = Counter(arr)
    res = 0
    for i in range(len(arr) - 2):
        # remove duplicates (i)
        if i > 0 and arr[i - 1] == arr[i]:
            continue
        j = i
        k = len(arr) - 1
        while j < k:
            three = arr[i] + arr[j] + arr[k]
            if three > target:
                k -= counts[arr[k]]
            elif three < target:
                j += counts[arr[j]]
            else:
                if arr[i] != arr[j] != arr[k]:
                    res += counts[arr[i]] * counts[arr[j]] * counts[arr[k]]
                elif arr[i] != arr[j] == arr[k]:
                    res += counts[arr[i]] * math.comb(counts[arr[j]], 2)
                elif arr[i] == arr[j] != arr[k]:
                    res += math.comb(counts[arr[i]], 2) * counts[arr[k]]
                else:
                    res += math.comb(counts[arr[i]], 3)
                # remove duplicates (ii)
                j += counts[arr[j]]
                k -= counts[arr[k]]

    return res % (10**9 + 7)
