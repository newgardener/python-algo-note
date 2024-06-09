from typing import List


def threeSum(nums: List[int]) -> List[List[int]]:
    nums.sort()

    added = set()
    res = []
    for i, a in enumerate(nums):
        l, r = i + 1, len(nums) - 1
        while l < r:
            threeSum = a + nums[l] + nums[r]
            if threeSum > 0:
                r -= 1
            elif threeSum < 0:
                l += 1
            else:
                if (a, nums[l], nums[r]) not in added:
                    res.append([a, nums[l], nums[r]])
                    added.add((a, nums[l], nums[r]))
                    r -= 1
    return res
