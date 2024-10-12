from collections import defaultdict


# ex. nums1 = [1,2], nums2 = [-2,-1], nums3 = [-1,2], nums4 = [0,2]
# count the number of valid pairs (i, j, k, l) satisfying nums1[i] + nums2[j] + nums3[k] + nums4[l] == 0
def fourSumCount(
    nums1: list[int], nums2: list[int], nums3: list[int], nums4: list[int]
) -> int:
    n = len(nums1)
    hashmap = defaultdict(int)
    res = 0

    for i in range(n):
        for j in range(n):
            hashmap[nums1[i] + nums2[j]] += 1

    for i in range(n):
        for j in range(n):
            res += hashmap[-(nums3[i] + nums4[j])]

    return res
