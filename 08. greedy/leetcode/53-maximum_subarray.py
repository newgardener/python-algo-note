from typing import List

# %%
"""
Brute Force Solution: O(N^2)
"""


class Solution:
    def bruteforce(self, nums: List[int]) -> int:
        n = len(nums)
        maxSum = nums[0]
        for i in range(n):
            curSum = 0
            for j in range(i, n):
                curSum += nums[j]
                maxSum = max(maxSum, curSum)
        return maxSum


# %%
"""
*Kadane's algorithm is a greedy/dynamic algorithm that can be used on array problems to bring the complexity down to O(N)
Kadane Solution: O(N)
"""


def kadane(self, nums: List[int]) -> int:
    n = len(nums)
    maxSum = nums[0]
    curSum = 0
    for n in nums:
        curSum = max(curSum, 0)
        curSum += n
        maxSum = max(maxSum, curSum)
    return maxSum


# %%

"""
Sliding Window to get L, R index of a maximum subarray
"""


class Solution:
    def slidingwindow(self, nums: List[int]) -> int:
        pass
