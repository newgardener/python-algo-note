# lower <= nums[i] + nums[j] <= upper (i < j)
# [lower, upper] range search => binary search
# pair is counted as r - l because unlike subarray when counting pairs, we should not consider num itself
def countFairPairs(nums: list[int], lower: int, upper: int) -> int:
    nums.sort()

    # search returns the number of valid pairs summed up to [lower, upper]
    def search(target):
        # we should set r to len(nums) - 1, otherwise it would cause range error
        l, r = 0, len(nums) - 1
        res = 0
        # leftmost search
        while l < r:
            if nums[l] + nums[r] > target:
                r -= 1
            else:
                res += r - l
                l += 1
        return res

    return search(upper) - search(lower - 1)
