# j - i != nums[j] - nums[i] (i < j)
# nums[i] - i != nums[j] - j is a bad pair
# math.comb(len(nums), 2) - pairs of nums[i] - i == nums[j] - j == pairs of nums[i] - i != nums[j] - j (
from collections import defaultdict
import math


def countBadPairs(nums: list[int]) -> int:
    counts = defaultdict(int)
    for i, num in enumerate(nums):
        counts[num - i] += 1

    not_bad = 0
    for v in counts.values():
        not_bad += math.comb(v, 2)
    return math.comb(len(nums), 2) - not_bad
