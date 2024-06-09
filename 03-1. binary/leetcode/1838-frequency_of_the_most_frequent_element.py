# https://leetcode.com/problems/frequency-of-the-most-frequent-element

from typing import List


# binary search
def maxFrequency(nums: List[int], k: int) -> int:
    def binarySearch(index, cumSum):
        start, end = 0, index
        target = nums[index]
        bestIndex = index
        while start <= end:
            mid = (start + end) // 2
            count = index - mid + 1
            desired = target * count
            current = cumSum[index] - (cumSum[mid - 1] if mid > 0 else 0)
            if desired - current > k:
                start = mid + 1
            else:
                bestIndex = mid
                end = mid - 1
        return index - bestIndex + 1

    nums.sort()
    n = len(nums)
    cumSum = [0] * n
    for i in range(n):
        cumSum[i] = cumSum[i - 1] + nums[i] if i > 0 else nums[i]

    maxFreq = 0
    for i in range(n):
        maxFreq = max(maxFreq, binarySearch(i, cumSum))
    return maxFreq


# sliding window
def enhancedSolution(nums: List[int], k: int) -> int:
    nums.sort()
    maxFreq = 0
    total = 0
    left = 0

    for right in range(len(nums)):
        total += nums[right]
        while (right - left + 1) * nums[right] - total > k:
            total -= nums[left]
            left += 1
        maxFreq = max(maxFreq, right - left + 1)

    return maxFreq
