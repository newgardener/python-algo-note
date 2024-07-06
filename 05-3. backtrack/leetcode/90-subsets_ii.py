from typing import List

"""
Key Points:
How to avoid duplicate paths?
=> skip the same number (do not make the same choice path)

1. sort nums list
(inside recursive function)
2. add a copy of choices to result list
3. for-loop nums list and make a choice whether to include or not to include
3-1. if a given number is the same number with the previous one, skip  
"""


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []

        def dfs(choices, idx):
            result.append(choices[:])

            for i in range(idx, len(nums)):
                if i > idx and nums[i] == nums[i - 1]:
                    continue
                choices.append(nums[i])
                dfs(choices, i + 1)
                choices.pop()

        dfs([], 0)
        return result
