from collections import defaultdict

def countInterestingSubarrays(nums: list[int], modulo: int, k: int) -> int:
    counts = defaultdict(int)
    counts[0] = 1
    cnt = 0
    res = 0
    for num in nums:
        if num % modulo == k:
            cnt += 1

        target = (cnt - k + modulo) % modulo
        if target in counts:
            res += counts[target]

        counts[num % modulo] += 1

    return res