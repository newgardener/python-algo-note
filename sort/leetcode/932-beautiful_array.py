from typing import List

"""
Note: odd + even = odd 
so, segregate the array into two [odd array] + [even array] so that where i < k < j, nums[k] * 2 == nums[i] + nums[j] never happens
"""


def beautifulArray(n: int) -> List[int]:
    if n == 1:
        return [1]

    odd = beautifulArray((n + 1) // 2)
    even = beautifulArray(n // 2)

    return [num * 2 - 1 for num in odd] + [num * 2 for num in even]
