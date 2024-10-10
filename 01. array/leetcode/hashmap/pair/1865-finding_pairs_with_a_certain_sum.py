from collections import defaultdict


class FindSumPairs:

    def __init__(self, nums1: list[int], nums2: list[int]):
        self.nums1 = nums1
        self.nums2 = nums2
        self.freq = defaultdict(int)  # manage a frequency of each number in nums2
        for num in nums2:
            self.freq[num] += 1

    # add val to nums2[index]
    def add(self, index: int, val: int) -> None:
        self.freq[self.nums2[index]] -= 1
        self.nums2[index] += val
        self.freq[self.nums2[index]] += 1

    # count the number of pairs (i, j) such that nums1[i] + nums2[j] == tot <=> twoSum problem
    def count(self, tot: int) -> int:
        res = 0
        for num in self.nums1:
            if num >= tot:
                continue
            if tot - num in self.freq:
                res += self.freq[tot - num]
        return res


# Your FindSumPairs object will be instantiated and called as such:
# obj = FindSumPairs(nums1, nums2)
# obj.add(index,val)
# param_2 = obj.count(tot)
