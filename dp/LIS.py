# %%
"""
1D problem
O(n^2) solution
"""


def _lengthOfLIS(nums):
    dp = [1 for _ in range(len(nums))]

    for i in range(len(nums)):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j] + 1)

    res = 0
    for i in range(len(dp)):
        res = max(res, dp[i])
    return res


print(_lengthOfLIS([1, 4, 3, 4, 2, 3]))


# %%
"""
1D problem
O(nlogn) solution
apply binary search
"""


def lengthOfLIS(nums):
    top = [0] * len(nums)

    piles = 0
    for i in range(len(nums)):
        # card to handle
        poker = nums[i]

        left, right = 0, piles
        # leftmost binary search
        while left < right:
            mid = (left + right) // 2
            if top[mid] >= poker:
                right = mid
            else:
                left: int = mid + 1

        # if there's no pile to fit in, create new pile
        if left == piles:
            piles += 1
        top[left] = poker

    return piles


# %%
"""
2D problem
time complexity: O(nlogn)
space complexity: O(n)
"""


def maxEnvelops(envelops):
    envelops.sort(key=lambda x: x[0])
    height = list(map(lambda x: x[1], envelops))
    return lengthOfLIS(height)


envelops = [[5, 4], [6, 4], [6, 7], [2, 3]]
print(maxEnvelops(envelops))
