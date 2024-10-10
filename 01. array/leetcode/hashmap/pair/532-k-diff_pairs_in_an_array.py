from collections import defaultdict


# |nums[i] - nums[j]| == k (i < j)
# given nums[j], we can find nums[i] by either (nums[j] - k) or nums[j] + k
def findPairs(nums: list[int], k: int) -> int:
    counts = defaultdict(int)
    res = set()

    for i, num in enumerate(nums):
        if num - k in counts:
            res.add((num, num - k) if num <= num - k else (num - k, num))
        if num - k != num + k and num + k in counts:
            res.add((num, num + k) if num <= num + k else (num + k, num))
        counts[num] += 1

    return len(res)
