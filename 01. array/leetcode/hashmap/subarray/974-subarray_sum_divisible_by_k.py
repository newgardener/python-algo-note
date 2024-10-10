from collections import defaultdict


def subarraysDivByK(nums: list[int], k: int) -> int:
    res = 0
    remainder = 0
    counts = defaultdict(int)

    for num in nums:
        remainder = (remainder + num) % k
        if remainder in counts:
            res += counts[remainder]

        counts[remainder] += 1

    return res
