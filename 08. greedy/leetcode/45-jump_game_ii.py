from typing import List

"""
Take-Away:
- find the shortest path from src to dst => apply BFS (level-by-level traversal)

Time Complexity: O(N) 
"""


def jump(nums: List[int]) -> int:
    res = 0
    l = r = 0
    while r < len(nums) - 1:
        farthest = 0
        # traverse [l, r] to find the next farthest index
        for i in range(l, r + 1):
            farthest = max(farthest, i + nums[i])
        # move [l, r] window
        l = r + 1
        r = farthest
        # record minimum jump
        res += 1
    return res
