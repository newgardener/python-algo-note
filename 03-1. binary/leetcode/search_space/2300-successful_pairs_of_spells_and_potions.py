from typing import List

"""
given N is len(potions), M is len(spells),
Time Complexity: O(NlogM + MlogM)
Space Complexity: O(M)
"""


class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        n = len(potions)
        potions.sort()

        def leftmost(spell):
            l, r = 0, n
            while l < r:
                mid = l + (r - l) // 2
                if potions[mid] * spell >= success:
                    r = mid
                else:
                    l = mid + 1
            return l

        res = []
        for spell in spells:
            if potions[0] * spell >= success:
                res.append(n)
                continue
            idx = leftmost(spell)
            res.append(n - idx)
        return res

