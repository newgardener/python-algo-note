from typing import List


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

    frequency = 0
    for i in range(n):
        frequency = max(frequency, binarySearch(i, cumSum))
    return frequency
