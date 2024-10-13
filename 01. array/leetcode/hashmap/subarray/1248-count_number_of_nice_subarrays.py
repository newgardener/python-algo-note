from collections import defaultdict


def numberOfSubarrays(nums: list[int], k: int) -> int:
    counts = defaultdict(int)
    counts[0] = 1 # to count subarray with k odds
    odds = 0
    res = 0
    for num in nums:
        if num % 2 == 1:
            odds += 1

        if odds - k in counts:
            res += counts[odds - k]

        counts[odds] += 1
    return res
