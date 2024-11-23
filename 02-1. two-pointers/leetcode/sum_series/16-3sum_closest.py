def threeSumClosest(nums: list[int], target: int) -> int:
    n = len(nums)
    nums.sort()
    closest = float('inf')
    for i in range(n-2):
        j, k = i+1, n-1
        while j < k:
            triplet = nums[i] + nums[j] + nums[k]
            if abs(triplet - target) < abs(closest - target):
                closest = triplet
            if triplet == target:
                return target
            elif triplet > target:
                k -= 1
            else:
                j += 1
    return closest