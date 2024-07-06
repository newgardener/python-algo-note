from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []

        def generate(choices, i):
            if i >= len(nums):
                result.append(choices[:])
                return

            # included
            choices.append(nums[i])
            generate(choices, i + 1)

            # not included
            choices.pop()
            generate(choices, i + 1)

        generate([], 0)
        return result
