def minimizeMax(nums: list[int], p: int) -> int:
    nums.sort()

    if not p:
        return 0

    def can_form_pairs(diff):
        cnt = i = 0
        while i < len(nums) - 1:
            if nums[i + 1] - nums[i] <= diff:
                cnt += 1
                i += 2
            else:
                i += 1
            if cnt >= p:
                return True
        return False

    l, r = 0, nums[-1] - nums[0]
    while l < r:
        mid = l + (r - l) // 2
        # leftmost search to find a minimum diff of pairs
        if can_form_pairs(mid):
            r = mid
        else:
            l = mid + 1
    return l
