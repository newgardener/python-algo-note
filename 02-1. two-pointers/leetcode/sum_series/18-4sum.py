def fourSum(nums: list[int], target: int) -> list[list[int]]:
    n = len(nums)
    nums.sort()
    res = []

    for i in range(n - 3):
        # remove duplicates (i)
        if i > 0 and nums[i - 1] == nums[i]:
            continue
        # remove duplicates (ii)
        for j in range(i + 1, n - 2):
            if j > i + 1 and nums[j - 1] == nums[j]:
                continue
            l, r = j + 1, len(nums) - 1
            while l < r:
                four = nums[i] + nums[j] + nums[l] + nums[r]
                if four > target:
                    r -= 1
                elif four < target:
                    l += 1
                else:
                    res.append([nums[i], nums[j], nums[l], nums[r]])
                    l += 1
                    # remove duplicates (iii)
                    while l < r and nums[l - 1] == nums[l]:
                        l += 1

    return res
