from typing import List


def numberOfSubarrays(nums: List[int], k: int) -> int:
    odd, result = 0, 0
    l, m = 0, 0

    for r in range(len(nums)):
        if nums[r] % 2:
            odd += 1

        while odd > k:
            if nums[l] % 2:
                odd -= 1
            l += 1
            m = l

        if odd == k:
            while not nums[m] % 2:
                m += 1
            result += m - l + 1

    return result
