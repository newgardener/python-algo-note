from typing import List


def threeSum(nums: List[int]) -> List[List[int]]:
    nums.sort()

    res = []
    for i in range(len(nums) - 2):
        # remove duplicates (i)
        if i > 0 and nums[i - 1] == nums[i]:
            continue
        j, k = i + 1, len(nums) - 1
        while j < k:
            three = nums[i] + nums[j] + nums[k]
            if three > 0:
                k -= 1
            elif three < 0:
                j += 1
            else:
                res.append([nums[i], nums[j], nums[k]])
                j += 1
                # remove duplicates (ii)
                while j < k and nums[j - 1] == nums[j]:
                    j += 1
    return res
