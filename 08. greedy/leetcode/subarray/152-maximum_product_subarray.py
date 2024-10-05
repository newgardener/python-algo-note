"""
we don't know what will come up next negative or positive value
ㄴ so we keep [curMin, curMax] and constantly update the maxProduct value
"""

def maxProduct(nums: list[int]) -> int:
    res = nums[0]
    curMin = curMax = 1

    for num in nums:
        val = (num, num * curMin, num * curMax)
        curMin = min(val)
        curMax = max(val)
        res = max(res, curMax)
    return res