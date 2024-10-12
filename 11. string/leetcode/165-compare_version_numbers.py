# https://leetcode.com/problems/compare-version-numbers


def compareVersion(version1: str, version2: str) -> int:
    nums1, nums2 = version1.split("."), version2.split(".")
    n1, n2 = len(nums1), len(nums2)
    for i in range(max(n1, n2)):
        v1 = nums1[i] if i < n1 else 0
        v2 = nums2[i] if i < n2 else 0

        if v1 < v2:
            return -1
        if v1 > v2:
            return 1

    return 0
