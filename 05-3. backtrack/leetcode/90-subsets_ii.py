from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result = []

        def dfs(choices, i):
            if i >= len(nums):
                item = sorted(choices)
                if item not in result:
                    result.append(item)
                return

            choices.append(nums[i])
            dfs(choices, i + 1)
            choices.pop()
            dfs(choices, i + 1)

        dfs([], 0)
        return result
