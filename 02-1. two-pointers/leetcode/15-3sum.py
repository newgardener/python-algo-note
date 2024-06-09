from typing import List


def threeSum(nums: List[int]) -> List[List[int]]:
    nums.sort()

    res = []
    for i, a in enumerate(nums):
        # condition for avoiding duplicates
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        l, r = i + 1, len(nums) - 1
        while l < r:
            threeSum = a + nums[l] + nums[r]
            if threeSum > 0:
                r -= 1
            elif threeSum < 0:
                l += 1
            else:
                res.append([a, nums[l], nums[r]])
                l += 1
                # pass through the same element by moving l pointer
                while nums[l] == nums[l - 1] and l < r:
                    l += 1
    return res
