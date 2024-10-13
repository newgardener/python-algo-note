# count the number of subarray product of each element is less than k
def numSubarrayProductLessThanK(nums: list[int], k: int) -> int:
    cnt = 0
    subProduct = 1
    l = 0
    for r, num in enumerate(nums):
        subProduct *= num
        if subProduct < k:
            cnt += r - l + 1  # ex. [1,2,3] all possible subarray is [1], [1,2], [1,2,3]
        else:
            while l <= r and subProduct >= k:
                subProduct //= nums[l]
                l += 1

            if subProduct < k:
                cnt += r - l + 1

    return cnt
