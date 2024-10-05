"""
Houses are in a circular form and no two adjacent houses should be broken
ㄴ run dp on (i, i-2) and (i+1, i-1) twice to calculate the max profit
"""


def rob(nums: list[int]) -> int:
    n = len(nums)
    case1 = nums[: n - 1]
    dp1 = [0] * n
    for i in range(1, n):
        # rob or skip
        dp1[i] = max(dp1[i - 1], case1[i - 1] + (dp1[i - 2] if i >= 2 else 0))

    case2 = nums[1:]
    dp2 = [0] * n
    for i in range(1, n):
        # rob or skip
        dp2[i] = max(dp2[i - 1], case2[i - 1] + (dp2[i - 2] if i >= 2 else 0))

    return max(dp1[n - 1], dp2[n - 1])
