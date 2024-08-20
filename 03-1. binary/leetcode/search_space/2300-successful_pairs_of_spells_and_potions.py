from typing import List

"""
Take-Away: define a target efficiently in terms of time and space complexity
ㄴ creating an array (potions * spell) degrades system performance
"""


class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        n = len(potions)
        res = []
        memo = {}

        for spell in spells:
            if spell in memo:
                res.append(memo[spell])
                continue

            # potions * spell >= success
            # potions >= (success + spell - 1) // spell
            target = (success + spell - 1) // spell
            l, r = 0, n
            # left-bounded search
            while l < r:
                mid = l + (r - l) // 2
                if potions[mid] < target:
                    l = mid + 1
                else:
                    r = mid
            memo[spell] = n - l if n > l else 0
            res.append(memo[spell])

        return res
