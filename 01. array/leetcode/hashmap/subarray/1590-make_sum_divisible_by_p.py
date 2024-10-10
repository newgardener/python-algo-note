# remove minimum length of subarray to make sum of nums divisible by p
from collections import defaultdict


def minSubarray(nums: list[int], p: int) -> int:
    target = sum(nums) % p
    # if sum(nums) is already divisible by p
    if target == 0:
        return 0

    seen = defaultdict(int)
    seen[0] = -1  # to calculate the length of array
    curSum = 0
    minLen = len(nums)
    for i, num in enumerate(nums):
        curSum = (curSum + num) % p
        # we should find a subarray (curSum - target) % p == 0
        complement = (curSum - target) % p
        if complement in seen:
            minLen = min(minLen, i - seen[complement])

        seen[curSum] = i

    return minLen if minLen < len(nums) else -1
