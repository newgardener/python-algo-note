from typing import List

# %%
"""
Time Complexity: O(M+N) where M=len(nums1) and N=len(num2)
"""


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


# %%
"""
Time Complexity: O(log(M+N)) where M=len(nums1) and N=len(num2)
ㄴ apply binary search method
"""


def findMedianSortedArray(nums1: List[int], nums2: List[int]) -> float:
    A, B = nums1, nums2
    total = len(nums1) + len(nums2)
    half = total // 2

    if len(B) < len(A):
        A, B = B, A

    l, r = 0, len(A) - 1
    while True:
        i = (l + r) // 2  # A
        j = half - i - 2  # B

        Aleft = A[i] if i >= 0 else float("-infinity")
        Aright = A[i + 1] if (i + 1) < len(A) else float("infinity")
        Bleft = B[j] if j >= 0 else float("-infinity")
        Bright = B[j + 1] if (j + 1) < len(B) else float("infinity")

        # if partition is correct
        if Aleft <= Bright and Bleft <= Aright:
            # odd case
            if total % 2:
                return min(Aright, Bright)
            return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
        elif Aleft > Bright:
            r = i - 1
        else:
            l = i + 1
