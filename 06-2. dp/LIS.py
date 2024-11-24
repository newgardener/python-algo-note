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

# %%
"""
Maximum Subarray problem
"""


def maxSubArray(nums):
    ans = nums[0]
    cur = nums[0]

    for i in nums[1:]:
        cur = max(i, i + cur)
        ans = max(ans, cur)

    return ans


def maxSubArrayOptimized(nums):
    total = 0
    result = float("-inf")

    for num in nums:
        total += num
        if total > result:
            result = total
        if total < 0:
            total = 0

    return result
