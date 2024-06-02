from typing import List

"""
Note: odd + even = odd 
so, segregate the array into two [odd array] + [even array] so that where i < k < j, nums[k] * 2 == nums[i] + nums[j] never happens
"""


# recursion
def beautifulArray(n: int) -> List[int]:
    if n == 1:
        return [1]

    odd = beautifulArray((n + 1) // 2)
    even = beautifulArray(n // 2)

    return [num * 2 - 1 for num in odd] + [num * 2 for num in even]


# while loop
# def beautifulArray(n: int) -> List[int]:
#     if n == 1:
#         return [1]

#     res = [1]
#     while len(res) < n:
#         res = [2 * x - 1 for x in res] + [2 * x for x in res]
#     return [num for num in res if num <= n]
