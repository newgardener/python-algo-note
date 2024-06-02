from typing import List


def findMedianSortedArrays(nums1: List[int], nums2: List[int]) -> float:
    total = len(nums1) + len(nums2)
    medianPos = total // 2

    result = [0] * medianPos
    i, j = 0, 0
    k = 0
    while i < len(nums1) and j < len(nums2) and k <= medianPos:
        if nums1[i] <= nums2[j]:
            result[k] = nums1[i]
            i += 1
        else:
            result[k] = nums2[j]
            j += 1
        k += 1

    return result[k] if total % 2 == 1 else (result[k - 1] + result[k]) / 2.0
